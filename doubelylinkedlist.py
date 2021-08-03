class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode != None:
            currentNode = currentNode.next
            length += 1
        return length

    def deleteHead(self):
        self.head = self.head.next
        self.head.previous.next = None
        self.head.previous = None

    def


    def insertAt(self, newNode, place):
        if place < 0 or place > self.listLength():
            print("Invalid Position")
            return
        if place == self.listLength():
            self.insertEnd(newNode)
        if place == 0:
            self.insertHead(newNode)
            break
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == place:
                currentNode.previous.next = newNode
                newNode.previous = currentNode.previous
                newNode.next = currentNode
                currentNode.previous = newNode
                break
            currentNode = currentNode.next
            currentPosition += 1

    def insertHead(self,newNode):
        previousHead = self.head
        self.head = newNode
        self.head.next = previousHead
        previousHead.previous = self.head

    def insertEnd(self, newNode):
        if self.head == None:
            self.head = newNode
            return
        currentNode = self.head
        while True:
            if currentNode.next == None:
                break
            else:
                currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode

    def printList(self):
        if self.head == None:
            print("This list is empty")
            return
        currentNode = self.head
        print("Printing from the beginning")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            if currentNode.next == None:
                reverseTraversalNode = currentNode
            currentNode = currentNode.next
        print("Printing from end")
        while True:
            if reverseTraversalNode == None:
                break
            print(reverseTraversalNode.data)
            reverseTraversalNode = reverseTraversalNode.previous

    def deleteAt(self, position):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                currentNode.previous.next = currentNode.next
                currentNode.next.previous = currentNode.previous
                currentNode.next = None
                currentNode.previous = None
            else:
                currentNode = currentNode.next
                currentPosition += 1

nodeOne = Node(10)
nodeTwo = Node(20)
nodeThree = Node(30)
linkList = LinkedList()
linkList.insertEnd(nodeOne)
linkList.insertEnd(nodeTwo)
linkList.insertAt(nodeThree,1)
linkList.printList()
