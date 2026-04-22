calc.l
%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }

[+\-*/()]   { return yytext[0]; }

[ \t\n]     { /* ignore spaces */ }

.           { printf("Invalid character\n"); }

%%

int yywrap() {
    return 1;
}

calc.y
%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(char *s);
int yylex();
%}

%token NUMBER

%%

expr:
    expr '+' expr   { $$ = $1 + $3; }
  | expr '-' expr   { $$ = $1 - $3; }
  | expr '*' expr   { $$ = $1 * $3; }
  | expr '/' expr   { 
                        if ($3 == 0) {
                            printf("Division by zero error\n");
                            exit(0);
                        }
                        $$ = $1 / $3; 
                    }
  | '(' expr ')'    { $$ = $2; }
  | NUMBER          { $$ = $1; }
  ;

%%

void yyerror(char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Enter expression:\n");
    yyparse();
    return 0;
}



yacc -d calc.y
lex calc.l
gcc y.tab.c lex.yy.c -o calc
./calc