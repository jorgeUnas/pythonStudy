#Make a list of the first 10 squares and cubes

single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
print(squares)
  
cubes = [item**3 for item in single_digits]
print(cubes)