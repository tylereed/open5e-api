from django.template.defaultfilters import slugify

import re

from api.models import Monster as v1_model
from api_v2.models import Creature as v2_model, CreatureAction as v2_creatureaction, CreatureActionAttack as v2_creatureattack, DamageType
from .antlr4.parsers import parseAttack, parseSavingThrow, parseDice

AllDamageTypes = dict((dt.key, dt) for dt in DamageType.objects.all())

def main():
    #print(','.join(['MonsterName', 'AttackName', buildCsvHeader()]))

    v2_creatureaction.objects.filter(action_type='ACTION').delete()

    # .filter(slug='ghost-a5e')
    # .all()
    for v1_monster in v1_model.objects.all():

        computed_v2_key = get_v2_key_from_v1_obj(v1_monster)
        v2_creature = v2_model.objects.filter(key=computed_v2_key).first()
        
        
        if v2_creature is not None:
            #update_v2_attack(v1_monster, v2_creature)
            add_v2_attack(v1_monster, v2_creature)

def add_v2_attack(v1_monster: v1_model, v2_creature: v2_model):
    actions = v1_monster.actions()
    if actions is not None:
        order=0
        for v1_action in actions:
            # try:
                v1_action_name = v1_action['name']
                v1_action_cleaned_name = re.sub(' \(.*\)', '', v1_action_name)
                re_v1_additional_info = re.search('\((.*)\)', v1_action_name)
                v1_additional_info = re_v1_additional_info.group(1) if re_v1_additional_info else None
                
                v1_action_desc = v1_action['desc']
                
                parsed_uses_type = None
                parsed_uses_param = None
                
                parsed_form_condition = None
                
                # clean up “ and ” (maybe?)
                #TODO: trim condition
                if v1_additional_info:
                    handled = False
                    infos = v1_additional_info.split(',') #TODO don't split spell stuff (V, S, etc)
                    for info in infos:
                        if re.search('Recharges? after a Short or Long rest', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'RECHARGE_AFTER_REST'
                            parsed_uses_param = None
                        elif recharge := re.search('Recharges? ((\d+)-)?(\d+)', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'RECHARGE_ON_ROLL'
                            parsed_uses_param = int(recharge.group(2) or recharge.group(3))
                        elif re.search('Recharges? Special', info):
                            handled = True
                            parsed_uses_type = 'RECHARGE_SPECIAL'
                            parsed_uses_param = None
                        elif per_day := re.search('(\d+)/Day', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'PER_DAY'
                            parsed_uses_param = int(per_day.group(1))
                        if re.search('(\d(st|nd|rd|th)-Level)|(Cantrip)', info, flags=re.IGNORECASE):
                            handled = True
                            v1_action_desc = '(' + info + ') ' + v1_action_desc
                        if re.search('Form|Only|Gaze|Bloodied|Mounted|Ablaze|wielded|Plane', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_form_condition = info
                    # have the extra text in the name so I know to handle it
                    if not handled:
                        v1_action_cleaned_name = v1_action_name

                v2_action_key = get_v2_action_key(v2_creature.key, v1_action_cleaned_name)
                
                #print(v1_action_name, v1_action_cleaned_name, v1_additional_info, parsed_uses_type, parsed_uses_param, sep=",")

                v2_action = v2_creatureaction(name=v1_action_cleaned_name,
                    desc=v1_action_desc,
                    key = v2_action_key,
                    parent=v2_creature,
                    uses_type=parsed_uses_type,
                    uses_param=parsed_uses_param,
                    action_type='ACTION',
                    form_condition=parsed_form_condition,
                    legendary_cost=None,
                    order=order
                )
                v2_action.save()
                order = order + 1

                #TODO: skip parsing multi-attack, better handle saving throws, check if starts with Melee or Ranged and skip parsing
                v2_attack_key = get_v2_attack_key(v2_action_key, v1_action_cleaned_name)
                
                if v1_action_name == 'Multiattack' or v1_action_name == 'Spellcasting':
                    pass
                elif re.match("_?(Melee|Ranged)", v1_action['desc']):
                    parsedAction = parseAttack(v1_action['desc'])
                    saveParsed(parsedAction, v1_action_cleaned_name + " attack", v2_attack_key, v2_action)

                elif re.search(
                    '(DC \d+ ((\S{3} save)|(\S+ saving throw))(([, ] taking \d+)|(\. +On a failure[, ] (it|a (creature|target)) takes \d+)))|(or half damage with a successful DC \d+ \S+ saving throw)'
                    , v1_action['desc']):
                    
                    savingThrow = parseSavingThrow(v1_action['desc'])
                    saveParsed(savingThrow, v1_action_cleaned_name + " attack", v2_attack_key, v2_action)
                else:
                    pass

                #TODO add new attack for weapons that are melee or ranged, and versatile

            # except:
            #     pass

def saveParsed(parsedAction, v1_action_name, v2_attack_key, v2_action):
    if parsedAction:
        damage_dice_text = parsedAction['damageDice']
        damage_dice = None if damage_dice_text is None else parseDice(damage_dice_text)
        damage_average = parsedAction['damageAverage']
        
        bonus_dice_text = parsedAction['plusDamageDice']
        bonus_dice = None if bonus_dice_text is None else parseDice(bonus_dice_text)

        v2_attack = v2_creatureattack(
            name=v1_action_name,
            key=v2_attack_key,
            parent=v2_action,
            attack_type='WEAPON' if parsedAction['isWeapon'] else 'SPELL' if parsedAction['isSpell'] else 'SAVING_THROW',
            to_hit_mod=parsedAction['toHitBonus'],
            reach=parsedAction['reach'],
            range=parsedAction['range'],
            long_range=parsedAction['rangeMax'],
            distance_unit='feet' if (parsedAction['reach'] or parsedAction['range']) is not None else None,
            target_creature_only=re.match('creature', parsedAction['targetType']) is not None if parsedAction['targetType'] is not None else False,

            damage_die_count=None if damage_dice is None else damage_dice['count'],
            damage_die_type=None if damage_dice is None else 'D' + str(damage_dice['sides']),
            # If no dice are thrown, but damage is done (typically 1), then put damage done in damage_bonus
            damage_bonus=damage_average if damage_dice is None else damage_dice['modifier'],
            
            extra_damage_die_count=None if bonus_dice is None else bonus_dice['count'],
            extra_damage_die_type=None if bonus_dice is None else 'D' + str(bonus_dice['sides']),
            extra_damage_bonus=None if bonus_dice is None else bonus_dice['modifier']
        )

        try:
            v2_attack.save()
            
            damage_type_keys = parsedAction['damageType']
            if damage_type_keys is not None:
                for damage_type_key in damage_type_keys:
                    v2_attack.damage_type.add(AllDamageTypes.get(damage_type_key))
                    
            extra_damage_type_keys = parsedAction['plusDamageType']
            if extra_damage_type_keys is not None:
                for damage_type_key in extra_damage_type_keys:
                    v2_attack.extra_damage_type.add(AllDamageTypes.get(damage_type_key))
        except Exception as e:
            print(e)

# def update_v2_attack(v1_monster: v1_model, v2_creature: v2_model):

#     actions = v1_monster.actions()
#     if actions is not None:
#         for v1_action in actions:
#             # try:
#                 computed_v2_action_key = get_v2_action_key(v2_creature.key, v1_action['name'])
#                 v2_action = v2_creatureaction.objects.filter(key=computed_v2_action_key,parent_id=v2_creature.key).first()

#                 parsedAction = parseAttack(v1_action['desc'])

#             # except:
#             #     pass

def get_v2_action_key(v2_creature_key: str, v1_action_name: str):
    v2_key = "{}_{}".format(v2_creature_key, slugify(v1_action_name))
    return v2_key

def get_v2_attack_key(v2_action_key: str, v1_action_name: str):
    v2_key = "{}_{}".format(v2_action_key, slugify(v1_action_name + " attack"))
    return v2_key

def get_v2_key_from_v1_obj(v1_obj):
    v2_doc = get_v2_doc_from_v1_obj(v1_obj)
    v2_key = "{}_{}".format(slugify(v2_doc),slugify(v1_obj.name))
    return v2_key

def get_v2_doc_from_v1_obj(v1_obj):
    doc_lookup = {
        'a5e':'a5e-ag',
        'cc':'ccdx',
        'blackflag':'blkflg',
        'dmag':'deepm',
        'dmag-e':'deepmx',
        'kp':'kp',
        'menagerie':'a5e-mm',
        'o5e':'open5e',
        'taldorei':'tdcs',
        'tob':'tob',
        'tob-2023':'tob-2023',
        'tob2':'tob2',
        'tob3':'tob3',
        'toh':'toh',
        'vom':'vom',
        'warlock':'wz',
        'wotc-srd':'srd',
        'blackflag':'bfrd'
    }
    return doc_lookup[v1_obj.document.slug]

if __name__ == '__main__':
    main()