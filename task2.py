from collections import deque

def is_palindrome(str):
    str = str.lower().replace(" ", "")
    deq = deque(str)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True

print(is_palindrome('This is palindrome Emor dnil Ap si sih t'))
print(is_palindrome('This is not palindrome'))