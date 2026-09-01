
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

def tokenize(text):
    index = 1
    length = len(text)
    line = 1
    tokens = []

    while (index < length):
        index += 1

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
