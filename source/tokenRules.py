import string

class String:
    acceptedChar = list(string.printable)[:-5]
    acceptedChar.remove("\"")

    tokenRule = [(["\""], [1, 2, 3]), (acceptedChar, [1, 2, 3]), (["\\", "\'", "\n", "\t"], [1, 2, 3]), (["\""], [])]

class Function:
    tokenRule = [(["$"], [1, 4]), ([String.tokenRule], [2]), (["."], [3]), ([String.tokenRule], [2, 4]), (["$"], [])]

class Number:
    tokenRule = [(["#"], [1, 2, 5]), (["-"], [2]), (list(string.digits), [2, 3, 5]), (["."], [4]), (list(string.digits), [4, 5]), (["#"], [])]

class subObject:
    tokenRule = [(["["], [1, 5]), ([String.tokenRule], [2]), ([":"], [3]), ([String.tokenRule, Number.tokenRule, Function.tokenRule], [4, 5]), ([","], [1, 5]), (["]"], [])]

class Object:
    tokenRule = [(["("], [1, 5]), ([String.tokenRule], [2]), ([":"], [3]), ([String.tokenRule, Number.tokenRule, Function.tokenRule, subObject.tokenRule], [4, 5]), ([","], [1, 5]), ([")"], [])]

class Program:
    tokenRule = [(["{"], [1, 3]), ([">"], [2]), ([Object.tokenRule, subObject.tokenRule], [1, 3]), (["}"], [])]


