DEBUG = False


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

# Fails when:
# (1) there are brackets surrounding an expression only containing multiplication
#     - check if lowest inner operation is a multiplication
# (2) there are brackets surrounding brackets
#     - check there are no operators on either side of brackets upon stack exit
# (3) there are brackets surrounding an addition next to other additions
#     - check the lowest inner operation and the outer operations are additions
# (4) there are brackets surrounding the whole expression

def good_expression(expression):
    stack = Stack()

    most_recent = "."
    lowest_priority = "."
    inner_lowest_priority = "."
    was_in_brackets = False
    for character in expression:
        if character not in ("(", ")", "+", "*"): continue
        if DEBUG: print(character, most_recent, lowest_priority, inner_lowest_priority, was_in_brackets, stack)

        if character == "(":
            stack.push((most_recent, lowest_priority))
            most_recent = "."
            lowest_priority = "."
            
        if character == ")":
            inner_most_recent = most_recent
            inner_lowest_priority = lowest_priority
            most_recent, lowest_priority = stack.pop()
            # Check for failure condition (2)
            if was_in_brackets and inner_most_recent == "." and most_recent == ".":
                return False
            was_in_brackets = True

        if character in ("+", "*"):
            if was_in_brackets:
                if inner_lowest_priority == "*":
                    return False
                if character in ("+", ".") and most_recent in ("+", ".") and inner_lowest_priority == "+":
                    return False
                inner_lowest_priority = "."
                was_in_brackets = False
            if lowest_priority == ".":
                lowest_priority = character
            elif lowest_priority == "*" and character == "+":
                lowest_priority = "+"
            most_recent = character
        if DEBUG: print(">", most_recent, lowest_priority, inner_lowest_priority, was_in_brackets, stack)

    if was_in_brackets:
        if most_recent == ".":
            return False
        if was_in_brackets and most_recent in ("+", ".") and inner_lowest_priority == "+":
            return False

    return True


if __name__ == '__main__':
    print(good_expression("(1*2*3+4*5*(6*7+4*(3*2+1))*(8+9))*2"))
