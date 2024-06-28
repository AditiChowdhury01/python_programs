from queue import queue
def main():
    while 1:
        print("chose an option: ")
        print("1:create queue")
        print("2:delete queue")
        print("3:Enqueue")
        print("4:Dequeue")
        print("5:print queue data")
        print("6:front element")
        print("7:no. of elements")

        if choice ==1:
            q = queue()
            print("queue created")
        elif choice == 2:
            del queue
            print("queue deleted")
        elif choice == 3:
            element = int(input("enter element:"))
            q.enqueue(element)  
        elif choice == 4:
            element = int(input("enter element:"))
            q.dequeue(element)  
        elif choice == 5:
            print(q)
        elif choice == 6:
            print("front element:")
            q.front()
        elif choice == 7:
            print("the no of element is:")
            q.size()  
