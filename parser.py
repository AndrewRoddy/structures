from tokenizer import tokenize
from pprint import pprint

# EBNF

# expression = term { ("+" | "-") term }
# term = factor { ("*" | "/") factor }
# factor = <number> | "(" expression ")"

def parse_factor(tokens):
    # factor = <number> | "(" expression ")"
    token = tokens[0]

    if token["tag"] == "number":
        node = {"tag": "number", "value": token["value"]}
        return node, tokens[1:]

    if token["tag"] == "(":
        # Array slice
        # implicitly throws away the first token
        tokens = tokens[1:]

        # Parses the expression in between the parenthesis
        node, tokens = parse_expression(tokens)

        # Makes sure we have hit the closing parenthesis
        if tokens[0]["tag"] != ")":
            raise SyntaxError(f"Expected ')', got {tokens[0]}")
        return node, tokens[1:]

    # Raises error if there is no # or (
    raise SyntaxError(
        f"Expected expression, got {tokens[0]}"
    )




