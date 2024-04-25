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

print(check_brackets("([1 + 2] {3{3sdf}f})"))
print(check_brackets("([{}][)"))