%{
#include <stdio.h>
%}

/* Define keyword pattern */
KEYWORD    int|float|if|else|while|return

%%

{KEYWORD}      { printf("Keyword: %s\n", yytext); }

[0-9]+         { printf("Number: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*   { printf("Word (Identifier): %s\n", yytext); }

[ \t\n]+       { /* Ignore whitespace */ }

.              { /* Ignore other characters */ }

%%

int main() {
    printf("Enter a statement:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}