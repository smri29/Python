number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid)
print(number_grid[0][2])
print(number_grid[0][0])
print(number_grid[3][0])
print(number_grid[2][2])

for row in number_grid:
   # print(row)
    for col in row:
        print(col)
