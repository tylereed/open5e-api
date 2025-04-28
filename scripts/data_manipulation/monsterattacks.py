from api.models import Monster as v1_model
from .antlr4.parsers import parseAttack, buildCsvHeader

def main():
    print(','.join(['MonsterName', 'AttackName', buildCsvHeader()]))
    for v1_monster in v1_model.objects.all():
        for v1_actions in v1_monster.actions():
            csv_data = parseAttack(v1_actions['desc'])
            print(','.join([v1_monster.name, v1_actions['name'], csv_data]))

if __name__ == '__main__':
    main()