#Author: Eveshogweyore Alle G.
#Implementing the Singly Linked List Data Structure Using Python v3


##### The following classes have been created: #####
# 1. Node                                          #
# 2. LinkedList                                    #
####################################################


##############      1. Node Class     ##############
# This class simply creates a node to be used by   #
# the linked list.                                 #
####################################################


#############      2. LinkedList Class     ##############
# All LinkedList functions are created into this        #
# class. The following are a list of available methods: #
#                                                       #
#                                                       #
# makeList() - Help to dynamically create a             #
#              LinkedList while initializing the class  #
#                                                       #
# print_linked_list() - A neat output for the LinkedList#
#                                                       #
# display_linked_list() - Just a FANCY DISPLAY for the  #
#                         linked list                   #
#                                                       #                
# trav(nodeTrav) - This is a helper method              #
#                  for the traverse() method            #
#                                                       #
# traverse() - This travels through every data in the   #
#              LinkedList using the trav() method       #
#                                                       #
# insert(nodeValue) - Add a value to the end of the     #
#                     LinkedList                        #
#                                                       #
# indexof(search_data) - Check the index of a data      #
#                        value in LinkedList            #
#                                                       #
# contains(search_data) - Check if a data value         #
#                         is present in LinkedList      #
#                                                       #
# delete(value) - Remove the node containing the        #
#                 supplied value                        #
#                                                       #
# reverse(self) - Reverse the current arrangement       #
#                 of the linked list                    #
#                                                       #
# reverse2(self) - A replica of the above method        #
#########################################################


class Node:
    ''' This is a Linked List Node class'''
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''The linked list implementation class'''
    
    def __init__(self, *altList):
        self.head = None
        
        self.iter_temp = 1 # helps to keep track of the iterator method

        if altList != ():
            self.makeList(altList)

    def makeList(self, values):
        '''Help to dynamically create a LinkedList
        while initializing the class'''
        i = 0
        
        while i < len(values):
            
            if i == 0:
                self.head = Node(values[i])
                currentNode = self.head
            else:
                currentNode.next = Node(values[i])
                currentNode = currentNode.next

            i += 1
            

    @property
    def print_linked_list(self):
        '''A neat output for the LinkedList
        e.g. LinkedList(Node 1, Node 2, Node N)'''
        temp = self.head
        the_list = ''
        while (temp):
            the_list += '{}, '.format(temp.data)
            #The below code for testing purposes
            #print(f'[{temp.data}]')
            temp = temp.next
        
        return 'LinkedList({})'.format(the_list[:-2]) #Remove last comma by slicing it off

    def __str__(self):
        '''Call the print_linked_list property'''
        return self.print_linked_list

    @property
    def display_linked_list(self):
        '''Just a FANCY DISPLAY for the linked list
        e.g. LinkedList([Index | Node 1] --> [Index | Node 2] --> [Index | Node N] --> None)'''
        the_list = ''
        presentNode = self.head
        
        for i in range(len(self)):
            the_list += '[{} | {}] --> '.format(i, presentNode.data)
            
            presentNode = presentNode.next
        
        return 'LinkedList({}None)'.format(the_list)

    def __repr__(self):
        '''Call the display_linked_list property'''
        return self.display_linked_list

    def __len__(self):
        '''Checks the length of the linked list'''
        temp = self.head #Point to the Head Node
        length = 0 #Begins at an index of zero

        #Loop through the Nodes and increase the length at each loop
        while (temp):
            length += 1
            temp = temp.next
        
        return length #Return the length

    def __iter__(self):
        '''Create an iterator method to iterate
        through every Node in LinkedList'''
        return self

    def __next__(self):
        '''Loop through every Node in the LinkedList in sequential order'''
        
        #Check the __init__() method for the 'self.iter_temp' variable
        if self.iter_temp == None:
            self.iter_temp = 1
            raise StopIteration
        elif self.iter_temp == 1:
            self.iter_temp = self.head
        else:
            self.iter_temp = self.iter_temp.next

        return self.iter_temp

    def trav(self, nodeTrav=''):
        '''This is a helper method for the traverse() method'''
        #I later modified this code on 31/03/2020
        #Most of the logic I used earlier were only ambiguous
        #I will still make future modifications

        if nodeTrav == '':
            nodeTrav = self.head
        else:
            try: #Avoid 'None.next' which produces an AttributeError
                nodeTrav = nodeTrav.next
            except AttributeError:
                return None
        
        return nodeTrav

    def traverse(self):
        '''This travels through every data in the LinkedList
        ONE AT A TIME'''
        #This method is subject to review in the near future
        
        return self.trav()

    def insert(self, nodeValue):
        '''Add a value to the end of the LinkedList'''
        presentNode = self.head
        newNode = Node(nodeValue) #Create the new Node to be inserted

        #Loop until the Tail Node is reached
        for i in range(len(self)):
            #print(presentNode.data) # Test to see the current Node's value
            if presentNode.next == None:
                tailNode = presentNode
                tailNode.next = newNode
                return True

            presentNode = presentNode.next

        return False

    def indexof(self, search_data):
        '''Check the index of a data value in LinkedList
        NOTE: The index for this LinkedList is zero based'''
        
        presentNode = self.head

        # Traverse through the LinkedList
        for i in range(len(self)):
            if presentNode.next == None:
                return False # Return False if the value is not in LinkedList

            if search_data == presentNode.data:
                return i # Return Index if the value is in LinkedList

            presentNode = presentNode.next

    def contains(self, search_data):
        '''Check if a data value is present in LinkedList'''

        return self.indexof(search_data) != False

    def delete(self, value):
        '''Remove a node containing the supplied value'''

        prevNode = None
        presentNode = self.head

        # Traverse through the LinkedList
        for i in range(len(self)):
                
            #When the value is found
            if presentNode.data == value:
                if presentNode == self.head: #Is the value to delete the head node?
                    self.head = presentNode.next
                else:
                    prevNode.next = presentNode.next

                return presentNode.data

            #When the value is not found
            if presentNode == None: #When the LinkList has reached the end
                return False
            
            #Keep track of the previous node
            #when looping the next time
            prevNode = presentNode

            #Change the value of the present node to the next node
            presentNode = presentNode.next

    def reverse(self):
        """Reverse the current arrangement of the linked list"""
        prevNode = None
        currentNode = self.head

        for i in range(len(self)):
            #Get the next node
            nextNode = currentNode.next

            #Point the next node of the current node
            #back to the previous node
            currentNode.next = prevNode 
            
            prevNode = currentNode #Set the previous node to the current node
            currentNode = nextNode #Set the current node to the next node
        
        self.head = prevNode #Make the last node the head node

    def reverse2(self):
        """Reverse the current arrangement of the linked list"""
        prevNode = None
        presentNode = self.trav()

        for i in range(len(self)):
            nextNode = presentNode.next
            presentNode.next = prevNode

            prevNode = presentNode
            presentNode = nextNode
        
        self.head = prevNode
        

#Instantiate the LinkedList class
the_linked_list = LinkedList()

#Create the head i.e. the first node in the Linked List
the_linked_list.head = Node('John')

#Create the second node and
#point to that node from the head node
second_node = Node('Ore')
the_linked_list.head.next = second_node

#Create the third_node and point to it from previous node
third_node = Node('Fanen')
second_node.next = third_node

#Create the third node and point to it from previous node
fourth_node = Node('Favor')
third_node.next = fourth_node

#Test the insert() method
the_linked_list.insert('Mama')
the_linked_list.insert('Joseph')
the_linked_list.insert('Baladou')
the_linked_list.insert('Dickson')
the_linked_list.insert('Solomon')

#the_linked_list2 = LinkedList(10, 20, 30, 40)
#the_linked_list3 = LinkedList('Ball', 'Shoes', 'Bag', 'Drugs')
#the_linked_list2.reverse2()

#Output the sample linked list created
print(the_linked_list)
print(repr(the_linked_list))
