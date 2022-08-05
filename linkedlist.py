#Node class
class Node:

    # Constructor to initialise the node object
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

#Linked list class
class LinkedList:

    # Constructor to initialize head
    def __init__(self) -> None:
        self.head = None


    # Function to insert a new node at the beginning
    def push(self, new_data) -> None:

        #create a new node by passing data as an argument.
        new_node = Node(new_data)

        #Make next of new Node as head
        new_node.next = self.head

        #Move the head to point to new Node
        self.head = new_node


    #Function to insert a new node given a previous Node
    def insertAfter(self, prev_node, new_data) -> None:

        #check if prev_node is valid
        if prev_node is None:
            print('Invalid Previous Node')
            return
        
        #create a new node by passing data as an argument.
        new_node = Node(new_data)

        #make next of new node as the next of the prev node
        new_node.next = prev_node.next

        #make next of prev_node as new_node
        prev_node.next = new_node


    # Function to insert a new node at the end of the list
    def append(self, new_data) -> None:

        #create a new node by passing data as an argument. next is set to None
        new_node = Node(new_data)

        #if list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            return
        
        #traverse till the last node 
        last = self.head
        while(last.next):
            last = last.next

        #Change the next of the last node
        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next


#code execution

if __name__ == '__main__':

    #Empty List
    linked_list = LinkedList()

    #insert 9 at the end, List becomes 9->None
    linked_list.append(9)

    linked_list.push(3)

    linked_list.push(1)

    linked_list.insertAfter(linked_list.head.next, 6)

    linked_list.append(17)

    print('Linked List: ')
    linked_list.printList()
        
        

