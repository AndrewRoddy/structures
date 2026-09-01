# structures
Structure of Programming Languages course materials

### Evaluator.py
`evaluate(ast)`
Passes in abstract syntax tree.

### Parser.py
Contains: 
1. `parse_factor(tokens)`
2. `parse_term(tokens)`
3. `parse_expressions(tokens)`
4. `parse(tokens)`. 

##### `parse_factor(tokens)`
Recursive funtion that takes in list of tokens are returns an abstract syntax tree.

Formatted in the end like below:
```
#"left": {
    "left": {"tag": "number", "value": 3},
    "right": {"tag": "number", "value": 4},
    "tag": "/",
},
"right": {"tag": "number", "value": 5},
"tag": "*",
```

##### `parse_term(tokens)`
Runs `parse_factor(tokens)` on the tokens and returns the left side and the rest of the tokens. Iterates while "\*" or "/" is tokens[0]["tag"]. Then sets left to tag as op, left as left, and right as right.
After this, returns left and tokens

##### `parse_expression(tokens)`
Does the same thing as `parse_term` but while it is + or - instead. Also runs `parse_term` where the original runs `parse_factor`

##### `parse(tokens)`
Runs `parse_expressions(tokens)` and applies them to the ast variable and the tokens variable. Checks that the first element in the tokens list afterwards is not none. Then returns the AST.

### Runner.py
Takes in two command line arguments with the second argument being the file passed in`.
If the second command line argument ends with `.t`, then read it, if it does not assume that this is the argument.

Run `tokenize(expression)`, `parse(tokens)`, `evaluate(ast)`, then print the result.
### Tokenizer.py

Includes a token map
token_map = [
    (r"\+"  , "+"         ),
    (r"\-"  , "-"         ),
    (r"\/"  , "/"         ),
    (r"\*"  , "*"         ),
    (r"\("  , "("         ),
    (r"\)"  , ")"         ),
    (r"\d+" , "number"    ),
    (r"\s+" , "whitespace"),
    (r"."   , "error"     )
]

Compiles this list of patterns into a tag and pattern combo using `re.compile`.
Then the `tokenize(characters)` function turns it into tokens.
Iterates through all of the characters. 

Tokenizer outputs list with this structure: [{"tag": None, "line": line, "value", value (optional), "column": column}]


