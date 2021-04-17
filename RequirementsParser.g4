
grammar RequirementsParser;

/* Examples:
CS 345 [Min Grade: D] or DIGM 345 [Min Grade: D]
CS 260 [Min Grade: D] and CS 270 [Min Grade: D] and (MATH 221 [Min Grade: D] or MATH 222 [Min Grade: D])
ECON 201 [Min Grade: D] (Can be taken Concurrently)(INFO 110 [Min Grade: D] or INFO 310 [Min Grade: D]) and PSY 101 [Min Grade: D]
*/

/*
    Parser Rules
*/

requirement: '(' requirement ')'
           | requirement 'and' requirement
           | requirement ',' requirement
           | requirement 'or'  requirement
           | requirement requirement
           | course min_grade? CONCURRENCY?;

course: subject number;
subject: LETTER LETTER+;
number: SPECIAL_DIGIT? DIGIT DIGIT DIGIT;
min_grade: '[Min Grade:' LETTER+ ']';

/*
    Lexer Rules
*/

LETTER: [A-Z];
DIGIT: [0-9];
SPECIAL_DIGIT: 'T'|'I';
CONCURRENCY: '(Can be taken Concurrently)';

WHITESPACE: [ \t\r\n]+ -> skip;
END_OF_FILE: EOF -> skip;
