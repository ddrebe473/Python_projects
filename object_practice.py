class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self._discount = 0

    def getprice(self):
        return self.price - (self.price * self._discount)

    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("Book1", 'man', 45, 2.24)
b2 = Book("Book2", 'women', 653, 12.24)

print(b1.getprice())

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
