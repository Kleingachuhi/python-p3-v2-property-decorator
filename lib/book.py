#!/usr/bin/env python3



# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#     def get_title(self):
#         return self._title
#     def set_title(self, title):
#         if isinstance(title, str) and 1<= len(title) <= 100:
#             self._title = title
#             print(self._title)
#         else:
#             raise  ValueError("Must be a string between 1 and 100")
#     title = property(get_title, set_title)
#     def get_price(self):
#         return self._price
#     def set_price(self, price):
#         if isinstance(price, (int, float)) and price >= 0:
#             self._price = price
#             print(self._price)
#         else:
#             raise ValueError("Price must be a number >= 0")
#     price = property(get_price, set_price)
# my_book = Book("The Hobbit", 909)
# The above block of code has simply been replaced by the code that follows:
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title) <= 100:
            self._title = title
        else:
            raise ValueError("Must be a string  with characters between 1 and 100") 
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Must be a number (int or float) > 0")
my_book = Book("1984", 15.99)
