class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"the employee with {self.id} is {self.name}")

class programmer(employee):
    def showlang(self):
      print("the language is python")

# class persons(programmer(employee)):xx
#     def showstyle(self):
#       print("the language is python")

e1 = employee("rohan mehra" , 320)
e1.showdetails()
e2 = programmer("aditi chowdhury" , 120)
e2.showdetails()
e2.showlang()
# e3 = persons("riya chowdhury" , 1210)xx
# e2.showdetails()
# e3.showstyle()
