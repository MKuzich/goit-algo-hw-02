from collections import deque

def is_palindrome(str):
    str = str.lower().replace(" ", "")
    deq = deque(str)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True