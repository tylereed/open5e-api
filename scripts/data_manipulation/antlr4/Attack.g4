grammar Attack;

attack:
	attackType ':' ' ' toHit ', ' distance ', ' targets ','? '.'? ' ' hit extraText EOF;

attackType: meleeRanged ' ' weaponSpell ' Attack';

meleeRanged: MELEE | RANGED | MELEE_OR_RANGED;

weaponSpell: WEAPON | SPELL;

toHit: '+' NUMBER ' to hit';

distance: reach | range | reach OR range;

reach: 'reach '? NUMBER ' ' DISTANCE;

range: 'range ' NUMBER ('/' NUMBER)? ' ' DISTANCE;

targets:
	NUMBER_TEXT ' ' (SIZE ' or smaller ')? TARGET_TYPE grappled;

hit: damage plusDamage? versatileDamage?;

grappled: (' ' (GRAPPLED | 'This attack'))? (' ' | OR | 'three' | TEXT+)+;

damage: 'Hit:' ' ' NUMBER ' (' DICE ') ' DAMAGE_TYPE ' damage';

plusDamage:
	' plus' ' ' NUMBER ' (' DICE ') ' DAMAGE_TYPE ' damage';

versatileDamage: (OR | ',' OR) NUMBER ' (' DICE ') ' DAMAGE_TYPE ' damage' (
		plusDamage
	)? ' if used with two hands' ' to make a melee attack'?;

extraText: TEXT*? '.';

MARKUP: '_'+ -> skip;

MELEE_OR_RANGED: MELEE OR RANGED;

MELEE: 'Melee';

RANGED: 'Ranged';

WEAPON: 'Weapon';

SPELL: 'Spell';

DISTANCE: 'ft.' | 'feet';

SIZE:
	'Tiny'
	| 'Small'
	| 'Medium'
	| 'Large'
	| 'Huge'
	| 'Gargantuan'
	| 'Titanic';

TARGET_TYPE: 'target' | 'targets' | 'creature' | 'creatures';

DICE: NUMBER? 'd' NUMBER (' '? ('+' | '-') ' '? NUMBER)?;

GRAPPLED: 'grappled';

DAMAGE_TYPE:
	'acid'
	| 'bludgeoning'
	| 'cold'
	| 'fire'
	| 'force'
	| 'lightning'
	| 'necrotic'
	| 'piercing'
	| 'poison'
	| 'psychic'
	| 'radiant'
	| 'slashing'
	| 'thunder';

NUMBER: [0-9]+;

NUMBER_TEXT:
	'one'
	| 'two'
	| 'three'
	| 'four'
	| 'five'
	| 'six'
	| 'seven'
	| 'eight'
	| 'nine';

OR: ' ' 'or' ' ';

TEXT:
	.
	| NUMBER
	| NUMBER_TEXT
	| DAMAGE_TYPE
	| DICE
	| SPELL
	| WEAPON
	| RANGED
	| MELEE
	| TARGET_TYPE
	| SIZE
	| DISTANCE
	| OR
	| ' '
	| ' damage'
	| ' plus';