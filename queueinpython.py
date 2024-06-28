class queue:
    def __init__(self):
        self.values = []
    def enqueue(self,item):
        self.values.append(item)
    def dequeue(self):
        # front = self.values[0]
        # self.values = self.values[1:]
        # return front

        if not(self.isEmpty()):
            self.values.pop(0)
        else:
            print("stack underflow")
            return None
        
    def isEmpty(self):
        
          return len(self.values)==0
        
    def front(self):
        if not (self.isEmpty()):
            return self.values[0]
        else:
            print("queue empty")
            return None
    def size(self):
        return len(self.values)
    # def __str__(self):
    #     StringRepr=''
    #     for i in self.values:
    #         StringRepr = str[i]+'\t'
    #     return StringRepr
    

# q = queue()
# q.enqueue(40)
# q.enqueue(80)
# q.enqueue(60)
# q.enqueue(50)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.front())
# print(q.isEmpty())

# print(q.size())

# # q.dequeue()
# # print(q.self.values)
# print(q.values)

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