class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10) 
node2 = Node(20) 
node3 = Node(30) 
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

# head = node1  ------------------>insertion at the beginning of the linkedlist
# new_node = Node(5)
# new_node.next = head
# head = new_node
# current = head
# while head is not None:   
#     print(head.data,end = "->")
#     head = head.next
# print("None")



# new_node = Node(50)    ---------------->insertion at the end
# head = node1
# current = head
# while current.next is not None:
#     current = current.next
# current.next = new_node

# while head is not None:   
#    print(head.data,end = "->")
#    head = head.next
# print("None")



# if head is not None: ------------------>deletion from the beginning
#     head = head.next
# while head is not None:  
#     print(head.data,end = "->")
#     head = head.next
# print("None")


# head = node1   ------------>deletion at the end
# current = head
# while current.next.next is not None:
#     current = current.next
# current.next = None


# head = node1 -------------->deletion of a particular node
# current = head
# while current.next.data !=30:
#     current = current.next
# current.next = current.next.next


# current = node1       ----------->printing the linkedlists
# while current is not None:
#     print(current.data,end = "->")
#     current = current.next
# print("None")


# while head is not None:        ----------->nothing
#     print(head.data,end = "->")
#     head = head.next
# print("None")