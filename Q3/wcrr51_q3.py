DEBUG = True


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


def good_expression(expression):
    stack = Stack()

    # Initialise the program state variables
    most_recent = "."
    lowest_priority = "."
    inner_lowest_priority = "."
    was_in_brackets = False
    # Loop through each character in the expression
    for character in expression:
        # If the character is not a bracket, plus or times symbol, skip to the next character
        if character not in ("(", ")", "+", "*"): continue
        if DEBUG: print(character, most_recent, lowest_priority, inner_lowest_priority, was_in_brackets, stack)

        # If the character is an open bracket
        if character == "(":
            # Push the most recent operator and the current lowest priority operator to the stack
            stack.push((most_recent, lowest_priority))
            # Reset these variables as a new layer has been entered
            most_recent = "."
            lowest_priority = "."

        # If the character is a close bracket
        if character == ")":
            # Store the value for the most recent inner operator
            inner_most_recent = most_recent
            # Store the value for the lowest priority inner operator
            inner_lowest_priority = lowest_priority
            # Pop the most recent and lowest priority operators from the stack
            # (returning to the state the program was in before entering the brackets)
            most_recent, lowest_priority = stack.pop()
            # Check to make sure the program was not previously in a set of brackets
            # (preventing a double bracket situation e.g. '((1+2))*3')
            if was_in_brackets and inner_most_recent == "." and most_recent == ".":
                return False
            # Mark the program has having just been in brackets
            was_in_brackets = True

        # If the character is a plus or a times operator
        if character in ("+", "*"):
            # If the program was previously in brackets
            if was_in_brackets:
                # If lowest priority operator within the brackets was a times, return false as the brackets were redundant
                # e.g. '1+(2*3)' or '(1*2)+3' or '1+(2*3)*4'
                if inner_lowest_priority == "*":
                    return False
                # If the character is a plus or a dot (null operator) and the most recent operator was a plus or a dot
                # and the lowest inner priority operator was a plus, return false as the brackets were redundant
                # e.g. '1+(2+3)' or '(1+2)+3'
                if character in ("+", ".") and most_recent in ("+", ".") and inner_lowest_priority == "+":
                    return False
                # Re-set program state variables as the backets have been handled
                inner_lowest_priority = "."
                was_in_brackets = False
            # If the current lowest priority operator is a dot (null operator)
            if lowest_priority == ".":
                # Set the current lowest priority operator to the current operator (current charachter)
                lowest_priority = character
            # Else if the current lowest priority operator is a times and the current operator (character) is a plus,
            # set the current lowst priority operator to a plus
            elif lowest_priority == "*" and character == "+":
                lowest_priority = "+"
            # Set the most recent operator to the current operator (character)
            most_recent = character
        if DEBUG: print(">", most_recent, lowest_priority, inner_lowest_priority, was_in_brackets, stack)

    # After the loop is finished, it may be that the program was just in a bracket,
    # so run the code to verify the brackets again
    if was_in_brackets:
        # This time check if the most recent was a dot (indicating there are brackets surrounding the whole expression)
        if most_recent == ".":
            return False
        if most_recent in ("+", ".") and inner_lowest_priority == "+":
            return False
        if inner_lowest_priority == "*":
            return False

    return True


if __name__ == '__main__':
    #print(good_expression("(1*2*3+4*5*(6*7+4*(3*2+1))*(8+9))*2"))
    print(good_expression("(a+b)*(c*d)"))
