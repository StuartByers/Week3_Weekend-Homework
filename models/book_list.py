from models.book import *

book1 = Book("Bourne Identity", "Robert Ludlum", "Fiction")
book2 = Book("12 Rule For Life", "Jordan B. Peterson", "Self Help")
book3 = Book("Shoe Dog", "Phil Kinight", "Autobiography")
book4 = Book("Watchmen", "Alan Moore", "Graphic Novel")
book5 = Book("48 Laws Of Power", "Robert Greene", "Non-Fiction")

book_list=[book1, book2, book3, book4, book5]

def add_new_book(new_book):
    book_list.append(new_book)