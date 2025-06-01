grammar SavingThrow;

forcedSavingThrow: forcedSavingThrow2024;

forcedSavingThrow2024:
	preAbility ABILITY ' Saving Throw: DC ' NUMBER preFailure2024 ' Failure: ' damage2024 (
		'.'
		| ','
		| (' plus ' plusDamage2024)
	) postText EOF;

preFailure2024: ~' Failure: '*?;

damage2024: NUMBER ' (' DICE ') ' damageType ' damage';

plusDamage2024: NUMBER ' (' DICE ') ' damageType ' damage';

preAbility: ~ABILITY*?;

forcedSavingThrow2014:
	preText (damageThenSave | savingThrow) postText EOF;

damageThenSave:
	('take ' | 'takes ' | 'deals ') NUMBER ' '? ('(' DICE ') ')? damageType ' damage' preHalfSuccess
		* ', or half damage with a successful DC ' NUMBER ' ' ABILITY (
		' save'
		| ' saving throw'
	);

savingThrow:
	'DC ' NUMBER ' ' ABILITY (' save' | ' saving throw') (
		(
			(' or ' | ',' | ' ') (
				(' '? 'taking ')
				| (' '? 'take ')
			)
		)
		| (
			preFailure* ON_A_FAILURE (',' | ' ') (
				' a '
				| ' the '
				| ' '
			) TARGET_TYPE ' ' 'takes '
		)
	) NUMBER ' '? ('(' DICE ') ')? damageType? ' damage'? (
		' and ' NUMBER ' '? ('(' DICE ') ')? damageType ' damage'
	)?;

damageType:
	'points of '? DAMAGE_TYPE (
		((',' | ' ') ' ' DAMAGE_TYPE)* (',' | ' ')? ' or ' DAMAGE_TYPE
	)?;

preText:
	~'takes damage'+? ~('DC ' | 'take ' | 'takes ' | 'deals ')+?;

preHalfSuccess: ~', or half damage with a successful DC ';

preFailure: ~(' or ' | ON_A_FAILURE)+?;

postText: .+?;

ON_A_FAILURE: '. On a fail' ('ure' | 'ed save');

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