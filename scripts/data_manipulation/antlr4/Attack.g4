grammar Attack;

attack: attack2014 | attack2024;

attack2014:
	attackType ':' ' ' toHit (',' | ' ') ' ' (
		distance (',' | ' ')? ' '
	)? targets ','? '.'? ' ' hit extraText EOF;

attack2024:
	meleeRanged ' Attack Roll: ' toHit ', ' distance '.'? ' ' damageGroup extraText EOF;

attackType: meleeRanged ' ' weaponSpell ' Attack';

meleeRanged: MELEE | RANGED | MELEE_OR_RANGED;

weaponSpell: WEAPON | SPELL;

toHit: '+' NUMBER ' to hit'?;

distance: reach | range | reach (OR | ((',' | ' ') ' ')) range;

reach: 'reach '? NUMBER ' ' DISTANCE;

range:
	'range ' NUMBER ('/' NUMBER)? ' ' DISTANCE ' (see Poor Depth Perception)'?;

targets:
	'up to '? (NUMBER | NUMBER_TEXT) (OR (NUMBER | NUMBER_TEXT))? (
		' ' (GRAPPLED | 'incapacitated')
	)? ' ' (SIZE (' or smaller ' | ' or larger '))? TARGET_TYPE grappled?;

hit: 'Hit:' (savingThrow | (damageGroup extraDamage?));

damageGroup:
	damage plusDamage? versatileDamage? savingThrow?;

savingThrow: ('. If the ' (' ' | TEXT)+? ','? ' ')? SAVING_THROW_START NUMBER ' ' ABILITY
		' saving throw' (',' | ' ')? ' taking ' NUMBER ' '? '(' DICE ') ' DAMAGE_TYPE ' damage';

extraDamage: ('. If the target' TEXT+?)? (
		'additional '
		| 'extra '
		| 'magically aged '
	) (NUMBER ' ')? '(' DICE ') damage';

grappled: (
		'.'? ' ' (
			GRAPPLED
			| 'This attack'
			| 'that'
			| 'within'
			| 'directly'
		)
	)? (
		' '
		| GRAPPLED
		| 'incapacitated'
		| 'restrained'
		| OR
		| NUMBER_TEXT
		| NUMBER
		| DISTANCE
		| 'within'
		| 'that'
		| 'directly'
		| TEXT+
	)+;

damage: ' '? NUMBER (' '? '(' DICE ') ')? damageType ' damage';

plusDamage:
	' plus' ' ' NUMBER ' '? '(' DICE ') ' damageType ' damage';

versatileDamage: (OR | ',' OR) NUMBER ' '? '(' DICE ') ' damageType ' damage' (
		plusDamage
	)? ' if used with two hands' ' to make a melee attack'?;

damageType:
	DAMAGE_TYPE (
		((',' | ' ') ' ' DAMAGE_TYPE)* (',' | ' ')? OR DAMAGE_TYPE
	)?;

extraText: .*? '.';

MARKUP: '_'+ -> skip;

MELEE_OR_RANGED: MELEE OR RANGED;

MELEE: 'Melee';

RANGED: 'Ranged';

WEAPON: 'Weapon';

SPELL: 'Spell' | 'Magical';

DISTANCE: 'ft' '.'? | 'feet';

SIZE:
	'Tiny'
	| 'Small'
	| 'Medium'
	| 'Large'
	| 'Huge'
	| 'Gargantuan'
	| 'Titanic';

TARGET_TYPE: 'target' | 'targets' | 'creature' | 'creatures';

SAVING_THROW_START: (', ' | '. ')? ((' '? T) | (' '? 'and t')) 'he target ' (
		'must make'
		| 'makes'
	) ' a DC ';

DICE: NUMBER? 'd' NUMBER (' '? ('+' | '-') ' '? NUMBER)?;

GRAPPLED: 'grappled';

DAMAGE_TYPE:
	(A 'cid')
	| (B 'ludgeoning')
	| (C 'old')
	| (F 'ire')
	| (F 'orce')
	| (L 'ightning')
	| (N 'ecrotic')
	| (P 'iercing')
	| (P 'oison')
	| (P 'sychic')
	| (R 'adiant')
	| (S 'lashing')
	| (T 'hunder');

NUMBER: [0-9]+;

NUMBER_TEXT:
	'all'
	| 'one'
	| 'two'
	| 'three'
	| 'four'
	| 'five'
	| 'six'
	| 'seven'
	| 'eight'
	| 'nine';

OR: ' or ';

ABILITY: (S 'trength')
	| (C 'onstitution')
	| (D 'exterity')
	| (I 'ntelligence')
	| (W 'isdom')
	| (C 'harisma')
	| (S T R)
	| (C O N)
	| (D E X)
	| (I N T)
	| (W I S)
	| (C H A);

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
	| ' plus'
	| 'within'
	| 'that'
	| 'directly'
	| 'incapacitated'
	| 'restrained';

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];