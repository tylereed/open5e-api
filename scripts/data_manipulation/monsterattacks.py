from api.models import Monster as v1_model
from .antlr4.parsers import parseAttack, buildCsvHeader

def main():
    print(','.join(['MonsterName', 'AttackName', buildCsvHeader()]))
    for v1_monster in v1_model.objects.all():
        actions = v1_monster.actions()
        if actions is not None:
            for v1_actions in actions:
                # try:
                    csv_data = parseAttack(v1_actions['desc'])
                    if csv_data is not None:
                        print('"' + v1_monster.name + '"', '"' + v1_actions['name'] + '"', csv_data, sep=',')
                    else:
                        print('"' + v1_monster.name + '"', '"' + v1_actions['name'] + '"', sep=',')
                # except:
                #     pass

if __name__ == '__main__':
    main()