def check_brackets(string):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for i in string:
        if i in dict.values():
            stack.append(i)
        elif i in dict.keys():
            if stack == [] or dict[i] != stack.pop():
                return False
                
    return len(stack) == 0
