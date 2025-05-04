from django.template.defaultfilters import slugify

import re

from api.models import Monster as v1_model
from api_v2.models import Creature as v2_model, CreatureAction as v2_creatureaction, CreatureActionAttack as v2_creatureattack
from .antlr4.parsers import parseAttack, parseDice, buildCsvHeader

def main():
    #print(','.join(['MonsterName', 'AttackName', buildCsvHeader()]))

    v2_creatureaction.objects.filter(action_type='ACTION').delete()

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
                v1_additional_info = re_v1_additional_info.group(0) if re_v1_additional_info else None
                
                parsed_uses_type = None
                parsed_uses_param = None
                
                if v1_additional_info:
                    if re.search('Recharge after a Short or Long rest', v1_additional_info, flags=re.IGNORECASE):
                        parsed_uses_type = 'RECHARGE_AFTER_REST'
                        parsed_uses_param = None
                    elif recharge := re.search('Recharge ((\d+)-)?(\d+)', v1_additional_info):
                            parsed_uses_type = 'RECHARGE_ON_ROLL'
                            parsed_uses_param = int(recharge.group(2) or recharge.group(3))
                    elif per_day := re.search('(\d+)/Day', v1_additional_info, flags=re.IGNORECASE):
                            parsed_uses_type = 'PER_DAY'
                            parsed_uses_param = int(per_day.group(1))

                v2_action_key = get_v2_action_key(v2_creature.key, v1_action_cleaned_name)
                
                #print(v1_action_name, v1_action_cleaned_name, v1_additional_info, parsed_uses_type, parsed_uses_param, sep=",")

                # TODO parse out form from name and set, also recharge
                v2_action = v2_creatureaction(name=v1_action_cleaned_name,
                    desc=v1_action['desc'],
                    key = v2_action_key,
                    parent=v2_creature,
                    uses_type=parsed_uses_type,
                    uses_param=parsed_uses_param,
                    action_type='ACTION',
                    form_condition=None,
                    legendary_cost=None,
                    order=order
                )
                v2_action.save()
                order = order + 1

                v2_attack_key = get_v2_attack_key(v2_action_key, v1_action['name'])
                parsedAction = parseAttack(v1_action['desc'])
                
                if parsedAction:
                    damage_dice_text = parsedAction['damageDice']
                    damage_dice = None if damage_dice_text is None else parseDice(damage_dice_text)
                    
                    bonus_dice_text = parsedAction['plusDamageDice']
                    bonus_dice = None if bonus_dice_text is None else parseDice(bonus_dice_text)

                    v2_attack = v2_creatureattack(
                        name=v1_action['name'] + ' attack',
                        key=v2_attack_key,
                        parent=v2_action,
                        attack_type='WEAPON' if parsedAction['isWeapon'] else 'SPELL',
                        to_hit_mod=parsedAction['toHitBonus'],
                        range=parsedAction['range'],
                        long_range=parsedAction['rangeMax'],
                        target_creature_only=False, #TODO, parse this out
                        
                        damage_die_count=None if damage_dice is None else damage_dice['count'],
                        damage_die_type=None if damage_dice is None else 'D' + str(damage_dice['sides']),
                        damage_bonus=None if damage_dice is None else damage_dice['modifier'],
                        
                        extra_damage_die_count=None if bonus_dice is None else bonus_dice['count'],
                        extra_damage_die_type=None if bonus_dice is None else 'D' + str(bonus_dice['sides']),
                        extra_damage_bonus=None if bonus_dice is None else bonus_dice['modifier'],
                        
                        damage_type_id=parsedAction['damageType'],
                        extra_damage_type_id=parsedAction['plusDamageType'],
                        reach=parsedAction['reach']
                    )

                    v2_attack.save()

                #TODO add new attack for weapons that are melee or ranged, and versatile

            # except:
            #     pass

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