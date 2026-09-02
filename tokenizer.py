import re

token_map = [
    (r"\s+", "whitespace"),
    (r"\d*\.\d+|\d+\.\d*|\d+", "number"),
    (r"\+"  , "+"         ),
    (r"\-"  , "-"         ),
    (r"\/"  , "/"         ),
    (r"\*"  , "*"         ),
    (r"\("  , "("         ),
    (r"\)"  , ")"         ),
    (r"."   , "error"     )
]

# Compiles the regular expressions
# original solution:
# patterns = [(re.compile(p), tag) for p, tag in token_map]
patterns = []
for pattern, tag in token_map:
    compiled = re.compile(pattern)
    patterns.append((compiled, tag))

def tokenize(text):
    index = 0
    row = column = 1
    length = len(text)
    selected_tag = None

    tokens = []
    while (index < length):

        # Iterates through all patterns
        # Checks each character in the text in order for matching with patterns list
        for pattern, tag in patterns:
            match = pattern.match(text, index)
            if match:
                selected_tag = tag
                break

        data  = match.group(0) # Gets data at tag position
        index = match.end() # Resume matching at the next token

        # Raises exception if error found
        if selected_tag == "error":
            raise Exception(f"Unexpected character: {data!r}")

        if selected_tag != "whitespace":
            token = {
                "tag"   : selected_tag,
                "line"  : row,
                "column": column
            }

            # Adds value if token is a number
            # Supports integers and floats
            if selected_tag == "number":
                if "." in value:
                    token["value"] = float(data)
                else:
                    token["value"] = int(value)

            tokens.append(token)

        # Moves row/column
        for character in data:
            column += 1

            # If the character is a newline
            # Increases row and sets column back to 1
            if character == "\n":
                row    += 1
                column  = 1

    # Adds in final token
    tokens.append({
        "tag":    None,
        "line":   row,
        "column": column
    })

    return tokens

def test_digits():
    print("test tokenize digits")
    t = tokenize("123")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 123
    assert t[1]["tag"] is None
    t = tokenize("1")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 1
    assert t[1]["tag"] is None


def test_operators():
    print("test tokenize operators")
    t = tokenize("+ - * / ( )")
    tags = [token["tag"] for token in t]
    assert tags == ["+", "-", "*", "/", "(", ")", None]


def test_expressions():
    print("test tokenize expressions")
    t = tokenize("1+222*3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 222
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None


def test_whitespace():
    print("test tokenize whitespace")
    t = tokenize("1 +\t2  \n*    3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 2
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None


def test_error():
    print("test tokenize error")
    try:
        tokenize("1@@@ +\t2  \n*    3")
    except Exception as e:
        assert str(e) == "Unexpected character: '@'"
        return
    raise Exception("Error did not happen.")


if __name__ == "__main__":
    test_digits()
    test_operators()
    test_expressions()
    test_whitespace()
    test_error()
