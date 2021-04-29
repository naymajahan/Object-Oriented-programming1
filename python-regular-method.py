#### object oriented programming in python

class StoryBook:

    def __init__(self, name, price, authorName, authorBorne, no_of_pages):
        # setting the instance variables here
        self.name = name
        self.price = price
        self.authorName = authorName
        self.authorBorne = authorBorne
        self.publishingYear = 2020
        self.no_of_pages = no_of_pages

# Regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, authorName: {self.authorName}')
# Regular method 2
    def get_author_info(self):
        print(f'The author name: {self.authorName}, born : {self.authorBorne}')



# creating an instance/object of the storyBook class

book1 = StoryBook('hamlet', 350, 'Shakespeare', 1564, 500)

book2 = StoryBook('The knite runner', 200, 'khalid hossini', 1965, 230)
book1.get_book_info()
book2.get_author_info()

print(book1.name)
print(book2.name)
print(book1.publishingYear)
print(book2.no_of_pages)

