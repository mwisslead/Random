grammar expr;

expr
 : '(' expr ')' #sub
 | expr (MUL='*' | DIV='/') expr #muldiv
 | expr (ADD='+' | MINUS='-') expr #addsub
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
