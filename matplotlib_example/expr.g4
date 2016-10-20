grammar expr;

expr
 : '(' expr ')' #sub
 | expr op=('/' | '*') expr #muldiv
 | expr op=('+' | '-') expr #addsub
 | expr '^' expr #expo
 | expr '%' expr #mod
 | '-' expr #negate
 | funcname=ID '(' expr ')' #func
 | NUM #num
 | ID #id
 ;

ID
 : [A-Za-z][A-Za-z0-9]*
 ;

NUM
 : [0-9]* '.' [0-9]+
 | [0-9]+
 ;

WS
 : [ \t] -> skip
 ;
