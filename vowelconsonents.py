%{
#include <stdio.h>

int vowels = 0;
int consonants = 0;
%}

%%

[aAeEiIoOuU]    { vowels++; }

[a-zA-Z]        { consonants++; }

\n              { 
                    printf("\nVowels = %d\n", vowels);
                    printf("Consonants = %d\n", consonants);
                }

.               { /* ignore other characters */ }

%%

int main() {
    printf("Enter a string:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}