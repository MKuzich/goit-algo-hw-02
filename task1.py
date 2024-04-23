from queue import Queue
import random

queue = Queue()

def generate_request():
    request = random.randint(1, 10000)
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Request {request} processed")
    else:
        print("Queue is empty")

while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    generate_request()
    process_request()
