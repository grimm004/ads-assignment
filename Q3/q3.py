#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

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

#####################################################
from wcrr51_q3 import good_expression


def testq3():
    assert good_expression("1+2+3+4")
    assert not good_expression("(1+2+3+4)")
    assert good_expression("(1+2)*3+4")
    assert not good_expression("((1+2))*3+4")
    assert good_expression("1+2*3+4")
    assert not good_expression("1+(2*3)+4")
    assert good_expression("1*2+3+4")
    assert not good_expression("1*2+(3+4)")
    assert not good_expression("(5*6)+1*2")
    assert good_expression("5+(6+1)*2")
    assert not good_expression("5+(6*1)*2")
    assert not good_expression("((1+3)*3)")
    assert good_expression("(1 * 2 * 3 + 4 * 5) * 6")
    print("all tests passed")
    
#####################################################

if __name__ == '__main__':
    testq3()
