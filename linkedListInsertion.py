'''
This program implements the basic linked list node insertion operation
Written by: Asif Nashiry
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode


    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def printListForward(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, ' ', end="")
            currentNode = currentNode.next

