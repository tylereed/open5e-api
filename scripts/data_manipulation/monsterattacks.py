from django.template.defaultfilters import slugify
from django.db.models import Q

import re

from api.models import Monster as v1_model
from api_v2.models import Creature as v2_model, CreatureAction as v2_creatureaction, CreatureActionAttack as v2_creatureattack, DamageType
from .antlr4.parsers import parseAttack, parseSavingThrow, parseDice

AllDamageTypes = dict((dt.key, dt) for dt in DamageType.objects.all())

def main():
    #load_2024()

    v2_creatureaction.objects.filter(~Q(pk_istartWith='srd2024')).delete()

    # .filter(slug='accursed-guardian-naga-a5e')
    # .all()
    for v1_monster in v1_model.objects.all():

        computed_v2_key = get_v2_key_from_v1_obj(v1_monster)
        v2_creature = v2_model.objects.filter(key=computed_v2_key).first()
        
        
        if v2_creature is not None:
            #update_v2_attack(v1_monster, v2_creature)
            add_v2_attacks(v1_monster, v2_creature)

def load_2024():
    for v2_creature in v2_model.objects.filter(key__istartswith='srd2024'):
        #foo = v2_creature.actions()
        for v2_action in v2_creatureaction.objects.filter(parent=v2_creature.key):
            v2_creatureaction.objects.filter(key=v2_action.key).delete()
            add_v2_attack_type(v2_action.name, v2_action.desc, v2_action.action_type, v2_creature, v2_action.order)
        

def add_v2_attacks(v1_monster: v1_model, v2_creature: v2_model):
    actions = v1_monster.actions()
    add_list_v2_attack_type(actions, 'ACTION', v2_creature)
    
    bonus_actions = v1_monster.bonus_actions()
    add_list_v2_attack_type(bonus_actions, 'BONUS_ACTION', v2_creature)
    
    reactions = v1_monster.reactions()
    add_list_v2_attack_type(reactions, 'REACTION', v2_creature)
    
    legenday_actions = v1_monster.legendary_actions()
    add_list_v2_attack_type(legenday_actions, 'LEGENDARY_ACTION', v2_creature)

def add_list_v2_attack_type(actions: list[dict[str, str]], attack_type: str, v2_creature: v2_model):
    if actions is not None:
        order=0
        for v1_action in actions:
            add_v2_attack_type(v1_action['name'], v1_action['desc'], attack_type, v2_creature, order)
            order=order+1

def add_v2_attack_type(param_action_name: str, param_action_desc: str, attack_type: str, v2_creature: v2_model, order: int):
    # if actions is not None:
    #     order=0
    #     for v1_action in actions:
            # try:
                display_name = None
                v1_action_name = param_action_name
                v1_action_cleaned_name = re.sub(' \(.*?\)?$', '', v1_action_name)
                re_v1_additional_info = re.search('\((.*?)\)?$', v1_action_name)
                v1_additional_info = re_v1_additional_info.group(1) if re_v1_additional_info else None
                
                v1_action_desc = param_action_desc
                
                parsed_uses_type = None
                parsed_uses_param = None
                
                parsed_form_condition = None
                
                legendary_cost = 1 if attack_type == 'LEGENDARY_ACTION' else None

                if v1_additional_info:
                    handled = False
                    infos = re.split('(?<!V|S|M),', v1_additional_info)
                    for info in infos:
                        if re.search('Recharges? (after|on) (a )?((Short|Long) or )?(Short|Long) rest|1/Rest|Recharges?: Short/Long Rest', info, flags=re.IGNORECASE):
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
                        elif per_round := re.search('(\d+)/Round', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'PER_ROUND'
                            parsed_uses_param = int(per_round.group(1))
                        elif recharge_minutes := re.search('recharges after (\d+) minutes', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'RECHARGE_MINUTES'
                            parsed_uses_param = int(recharge_minutes.group(1))
                        elif recharge_rest := re.search('(\d+)/rest', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'RECHARGE_AFTER_REST'
                            parsed_uses_param = int(recharge_rest.group(1))
                        elif per_hour := re.search('(\d+)/hour', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'PER_HOUR'
                            parsed_uses_param = int(per_hour.group(1))
                        elif per_week := re.search('(\d+)/week', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_uses_type = 'PER_WEEK'
                            parsed_uses_param = int(per_week.group(1))
                        
                        elif info == 'Requires Magic Rope':
                            handled = True
                            parsed_form_condition = info.strip()
                        elif re.search('(\d(st|nd|rd|th)-Level)|(Cantrip)', info, flags=re.IGNORECASE):
                            handled = True
                            v1_action_desc = '(' + info + ') ' + v1_action_desc
                        elif re.search('Form|Only|Gaze|Bloodied|Mounted|Ablaze|wielded|Plane|(?:\d+|Temporary) HP|Fewer', info, flags=re.IGNORECASE):
                            handled = True
                            parsed_form_condition = info.strip()
                        elif (re.search('Heads?|Shapeshifted', info, flags=re.IGNORECASE)):
                            handled = True
                            if info == "Snake Head" or info == "Canine Head":
                                v1_action_cleaned_name = v1_action_name
                        elif attack_type == 'LEGENDARY_ACTION' and (legendary := re.search('^(?:Costs )?(\d+)(?: Actions)?$', info, flags=re.IGNORECASE)):
                            handled = True
                            legendary_cost = int(legendary.group(1))
                        elif re.match('Psionics', info, flags=re.IGNORECASE):
                            handled = True
                            v1_action_cleaned_name = v1_action_name
                    # have the extra text in the name so I know to handle it
                    if not handled:
                        print("Didn't handle ", v2_creature.name, param_action_name)
                        v1_action_cleaned_name = v1_action_name

                display_name = v1_action_name
                v2_action_key = get_v2_action_key(v2_creature.key, v1_action_cleaned_name + " " + attack_type.replace("_", " "))
                
                #print(v1_action_name, v1_action_cleaned_name, v1_additional_info, parsed_uses_type, parsed_uses_param, sep=",")

                v2_action = v2_creatureaction(name=display_name,
                    desc=v1_action_desc,
                    key = v2_action_key,
                    parent=v2_creature,
                    uses_type=parsed_uses_type,
                    uses_param=parsed_uses_param,
                    action_type=attack_type,
                    form_condition=parsed_form_condition,
                    legendary_cost=legendary_cost,
                    order=order
                )
                v2_action.save()
                #order = order + 1

                v2_attack_key = get_v2_attack_key(v2_action_key, "")
                
                if re.search("Multiattack|Spellcasting", v1_action_name):
                    pass
                elif re.match("_?(Melee|Ranged)", param_action_desc):
                    parsedAction = parseAttack(param_action_desc)
                    if parsedAction is not None:
                        saveParsed(parsedAction, v1_action_cleaned_name, v2_attack_key, v2_action)
                    else:
                        print("unable to parse ", v2_action_key, v2_creature.name, param_action_name, param_action_desc)

                elif re.search(
                    'DC \d+ \S+ sav(?:e|ing throw)(?:(?:(?:[, ]| or)? tak(?:e|ing) \d+)|(?:.*?\. +On a fail(?:ure|ed save)[, ] (?:it|(?:a|the|each) (?:creature|target)) takes \d+))|(?:or half damage with a successful DC \d+ \S+ sav(?:e|ing throw))|(?:\S+ Saving Throw: DC \d+)'
                    , param_action_desc):
                    #TODO: handle different styles of saving throws, grab shape and size and range, targets creatures, DC and save type
                    savingThrow = parseSavingThrow(param_action_desc)
                    if savingThrow is not None:
                        saveParsed(savingThrow, v1_action_cleaned_name, v2_attack_key, v2_action)
                    else:
                        print("unable to parse ", v2_action_key, v2_creature.name, param_action_name, param_action_desc)
                else:
                    pass
                    # try:
                    #     print("Did not match any parse types ", v2_creature.name, param_action_name, param_action_desc)
                    # except:
                    #     print("Error printing out error message")

                #TODO add new attack for weapons that are melee or ranged, and versatile

            # except:
            #     pass

def saveParsed(parsedAction, v1_action_name, v2_attack_key, v2_action):
    damage_dice_text = parsedAction['damageDice']
    damage_dice = None if damage_dice_text is None else parseDice(damage_dice_text)
    damage_average = parsedAction['damageAverage']
    
    bonus_dice_text = parsedAction['plusDamageDice']
    bonus_dice = None if bonus_dice_text is None else parseDice(bonus_dice_text)

    #TODO: for forced saving throws, include shape, range, DC, and save type
    #TODO: don't include ' Attack' if name already ends with 'Attack'
    v2_attack = v2_creatureattack(
        name=v1_action_name + " Attack",
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
        
        damage_type_keys: list[str] = parsedAction['damageType']
        if damage_type_keys is not None:
            for damage_type_key in damage_type_keys:
                v2_attack.damage_type.add(AllDamageTypes.get(damage_type_key.lower()))
                
        extra_damage_type_keys = parsedAction['plusDamageType']
        if extra_damage_type_keys is not None:
            for damage_type_key in extra_damage_type_keys:
                v2_attack.extra_damage_type.add(AllDamageTypes.get(damage_type_key.lower()))
    except Exception as e:
        print(e)

def get_v2_action_key(v2_creature_key: str, v1_action_name: str):
    v2_key = "{}_{}".format(v2_creature_key, slugify(v1_action_name))
    return v2_key

def get_v2_attack_key(v2_action_key: str, v1_action_name: str):
    v2_key = "{}_{}".format(v2_action_key, slugify(v1_action_name + " Attack"))
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
    load_2024()