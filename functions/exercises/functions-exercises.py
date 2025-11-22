# Part 1 A -- Make a Line

def make_line(size):
    line = ""
    for i in range(size):
        line += "#"
    return line

print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for i in range(size):
        square += make_line(size)
        if i < size - 1:
            square += "\n"
    return square

print(make_square(5))




# Part 1 C -- Make a Rectangle

def make_rectangle(length, width):
    rectangle = ""
    for w in range(width):
        rectangle += make_line(length)
        if w < width - 1:
            rectangle += "\n"
    return rectangle

print(make_rectangle(7, 3))

# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ""
    for i in range(height):
        stairs += make_line(i + 1)
        if i < height -1:
            stairs += "\n"
    return stairs

print(make_downward_stairs(8))

# Part 2 B -- Make Space-Line 

def make_space_line(num_spaces, num_hashes):
    space_line = ""
    for s in range(num_spaces):
        space_line += " "
    for h in range(num_hashes):
        space_line += "#"
    for s in range(num_spaces):
        space_line += " "
    return space_line

print(make_space_line(3, 3))


# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    isosceles_triangle = ""
    space_var = 2
    hash_var = 1
    for i in range(height):
        isosceles_triangle += make_space_line(height - (space_var - 1), hash_var)
        space_var += 1
        hash_var += 2
        if hash_var <= (2*height - 1):
            isosceles_triangle += "\n"
    return isosceles_triangle

print(make_isosceles_triangle(6))



# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = make_isosceles_triangle(height)
    diamond += "\n"
    space_var = 0
    hash_var = (2 * height) - 1
    for i in range(height):
        diamond += make_space_line(space_var, hash_var)
        space_var += 1
        hash_var -= 2
        if i < height - 1:
            diamond += "\n"
    return diamond

print(make_diamond(5))




