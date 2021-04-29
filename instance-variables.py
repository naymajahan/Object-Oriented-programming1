#### object oriented programming in python

class StoryBook:

    def __init__(self, name, price, authorName, authorBorne):
        # setting the instance variables here
        self.name = name
        self.price = price
        self.authorName = authorName
        self.authorBorne = authorBorne

    
# creating an instance/object of the storyBook class

book1 = StoryBook('hamlet', 350, 'Shakespeare', 1564)

book2 = StoryBook('The knite runner', 200, 'khalid hossini', 1965)
### modification
book1.name = 'lolipop'

print(book1.name)
print(book2.name)


