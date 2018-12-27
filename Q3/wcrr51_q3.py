class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data
    def __str__(self):
        text = "Stack("
        if self.isEmpty():
            return text + ")"
        current = self.head
        while current != None:
            text += "%s, " % str(current.data)
            current = current.before
        text = text[:-2] + ")"
        return text

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after
    def __str__(self):
        text = "Queue("
        if self.isEmpty():
            return text + ")"
        current = self.front
        while current != None:
            text += "%s, " % str(current.data)
            current = current.after
        text = text[:-2] + ")"
        return text

# Fails when:
# 1) there are brackets surrounding a single multiplication
#   check if operation is a multiplication
# 2) there are brackets surrounding brackets
#   check there are no operators upon stack exit
# 3) there are brackets surrounding an addition next to other additions
# 4) there are brackets surrounding the whole expression

def good_expression(expression):
    stack = Stack()

    most_recent = "."
    lowest_priority = "."
    was_in_brackets = False
    for character in expression:
        if character not in ("(", ")", "+", "*"): continue
        print(character, stack)

        if character == "(":
            stack.push(most_recent)
            most_recent = "."
            lowest_priority = "."
            
        if character == ")":
            most_recent = stack.pop()
            was_in_brackets = True

        if character in ("+", "*"):
            if was_in_brackets:
                was_in_brackets = False
            if lowest_priority == ".":
                lowest_priority = character
            elif lowest_priority == "*" and character == "+":
                lowest_priority = "+"
            most_recent = character
    
    if was_in_brackets:
        if check_priorities(
            get_priority(lowest_priority),
            get_priority(most_recent),
            get_priority(".")):
            return False

    return True


if __name__ == '__main__':
    print(good_expression("a * b + c * (e + f) * (*)"))
