class persons:
    def __init__(self,n,o):
        print('aditi is a good girl')
        self.name = n
        self.occupation = o
    def info(self):
        print(f'{self.name} is an {self.occupation}')

a = persons("asiti" , "HR")
b = persons("pragati" , "sales")

a.info()
b.info()

