class persons:
    name = "aditi"
    occupation = "software developer"
    networth = 10000 
    def info(self):
        print(f"{self.name} is an {self.occupation}")

a = persons()
b = persons()
c = persons()
a.name = "riya"
a.occupation = "software engineer"
# print(a.name , a.occupation)
b.name = "nikita"
b.occupation = "hr"
a.info()
b.info()
c.info()
