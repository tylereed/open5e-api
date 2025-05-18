grammar SavingThrow;

forcedSavingThrow: preText savingThrow postText EOF;

savingThrow:
	'DC ' NUMBER ' ' ABILITY ('save' | 'saving throw') (
		( ' taking ')
		| (
			'. On a failure' COMMA_SPACE (' a ' | ' ') TARGET_TYPE ' takes '
		)
	) NUMBER ' '? '(' DICE ') ' damageType ' damage';

damageType:
	DAMAGE_TYPE (
		(COMMA_SPACE ' ' DAMAGE_TYPE)* COMMA_SPACE? ' or ' DAMAGE_TYPE
	)?;

preText: ~'DC '+?;

postText: .+?;

NUMBER: [0-9]+;

DICE: NUMBER? 'd' NUMBER (' '? ('+' | '-') ' '? NUMBER)?;

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

COMMA_SPACE: (',' | ' ');

TARGET_TYPE: ('creature' | 'target' | 'it');

TEXT: .;

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