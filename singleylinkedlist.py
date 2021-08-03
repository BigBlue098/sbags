class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print("This is an invalid position")
            return
        if self.isListEmpty() == False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                else:
                    previousNode = currentNode
                    currentPosition += 1
                    currentNode = currentNode.next

    def deleteHead(self):
        tempNode = self.head
        tempHead = tempNode.next
        self.head = tempHead
        del tempNode

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next != None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode != None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertEnd(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head == None:
            print("This list is empty")
            return
        currentNode = self.head
        while True:
            if currentNode == None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self,newNode, position):
        if position == 0:
            self.insertHead(newNode)
            return
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def isListEmpty(self):
        if self.head == None:
            return True
        else:
            return False





firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(15)
linkedList.insertEnd(secondNode)
thirdNode = Node(20)
linkedList.deleteAt(1)
linkedList.printList()
