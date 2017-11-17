# Mini Power Lexer

This is a lexical analyzer built for the fictional language Mini-Power.
Mini-Power is a language comprised of assign and print statements. Number literals can be assigned to variables, and manipulated with basic arithmetic operators. For more information about the language take a look at the EBNF section below

## Running The Lexer

Clone the project and navigate to the project directory from the command line. Then invoke the lexer with the following command:

```sh
python lexer.py <path_to_mini_power_program>
```

A list of tokens will be written to the `input.out` file in the project directory

NOTE: There are two sample programs included in this repository. Do not be supprised if test02.txt raises an error, it is meant to test the Lexer's error handling.
## Mini Power EBNF

For info on how to read EBNF go [here.](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)

```
Mini – Power

<stmts> ->  <stmt> {; <stmt>}
<stmt> -> (<print-stmt> | <assgmt-stmt>)
<print-stmt> -> PRINT(<id> | <const>)
<assgmt-stmt> ->  <id> = (<expr> | <string>)
<id> ->  <letter>{(<letter> | <digit>)}($|#|%)
<expr> ->  <expr> (+ | -) <term> | <term>
<term> ->  <term> (* | /) <factor> | <factor>
<factor> ->  <expr> ^ <factor> | ( <expr> ) | <num-const> | <id>
<const> ->  <num-const> | <string>
<num-const> ->  <int-const> | <real-const>
<int-const> ->  [(+|-)] <digit>{<digit>}
<real-const> ->  [(+|-)] <digit>{<digit>}.{<digit>}
<string> -> ʺ{(<letter> | <digit>)}ʺ
<digit> ->  (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)
<letter> ->  (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)
```
