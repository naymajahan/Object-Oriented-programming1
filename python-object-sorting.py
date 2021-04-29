class toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


def print_toy_objects(toy_list):
    for obj in toy_list:
        print(f'toy: {obj.name}, price: {obj.price}')

toy_1 = toy('woody', 1000)
toy_2 = toy('art', 100)
toy_3 = toy('black', 50)

toys = [toy_1, toy_2, toy_3]

### using the sort function
toys.sort(key=toy.sort_priority)

print_toy_objects(toys)


### reverse sorting
toys.sort(key=toy.sort_priority, reverse= True)

print_toy_objects(toys)

### Using the Sorted function

sorted_toys = sorted(toys, key=toy.sort_priority)

print_toy_objects(sorted_toys)


########### USE OF LAMDA FUNCTION (argument  can be passed ,how many times you want)

result = lambda x, y, z: x + y + z

print(result(1, 2, 3))

#### Sorting using lamda function

toys_again = [toy_1, toy_2, toy_3]

toys_again.sort(key=lambda x: x.price)

print_toy_objects(toys_again)


### using lambda in sorted function

sorted_toys_again = sorted(toys, key=lambda x: x.price)

print_toy_objects(sorted_toys_again)


