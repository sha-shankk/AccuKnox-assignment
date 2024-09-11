Below code and steps should be followed to match the requirement

   1) The class should be initialized with length and width.
   2) The class should be iterable, yielding its length and width in a specific format when iterated over.

Code Implementation:

******python*****

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # First yield the length in the required format
        yield {'length': self.length}
        # Then yield the width in the required format
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dimension in rect:
    print(dimension)

Explanation:

    __init__ method: This initializes the class with length and width when creating a new Rectangle object.

    __iter__ method: This is what makes the class iterable. The method uses yield to return the length and width in the required format when the object is iterated over.

Output Example:

If we create a Rectangle instance with length=10 and width=5, and then iterate over it:

python

rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)

The output will be:

css

{'length': 10}
{'width': 5}

Notes:

    The yield keyword makes the Rectangle class iterable, allowing it to return one value at a time in the specified format.
    The format {'length': <VALUE>} and {'width': <VALUE>} is exactly what gets output when the class is iterated over.
