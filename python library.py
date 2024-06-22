class books:
    def __init__(self):
        self.nobooks = 0
        self.books = []
        

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"the library has {self.nobooks} books")
        for book in self.books:
            print(book)

b1 = books()
b1.addbooks("harry potter")
b1.addbooks("physics")
b1.addbooks("biology")
b1.addbooks("chemistry")
b1.showinfo()

