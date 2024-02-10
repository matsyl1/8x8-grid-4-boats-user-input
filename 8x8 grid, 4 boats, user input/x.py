# imports
import random
import numpy as np

# grid
grid = np.full([8, 8], ".", dtype=str)

# FUNCTIONS--------------------------------------------------------------------------------------
# check for boat overlap
def overlap(boat_coords, new_coords):
    for i in boat_coords:
        if i in new_coords:
            return True
    else:
        return False

# create boat coords (start/end)
def create_boat_coords(size, used_coords):
    while True:
        x1, y1 = random.randint(0, 8 - size), random.randint(0, 8 - size)
        # boat direction (horizontal/vertical)
        if random.choice([True, False]):
            (x2, y2) = x1 + size - 1, y1
        else:
            (x2, y2) = x1, y1 + size -1

        # boat coords (middle)
        new_coords = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        if not overlap(used_coords, new_coords):
            return [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]


# BOATS------------------------------------------------------------------------------------------
# boat 5
boat_5 = create_boat_coords(5, [])
for (x, y) in boat_5:
    grid[y, x] = "5"
# update used_coords with boat 5
used_coords = boat_5[:]

# boat 4
boat_4 = create_boat_coords(4, used_coords)
for (x, y) in boat_4:
    grid[y, x] = "4"
# update used_coords with boat 4
used_coords.extend(boat_4)

# boat 3
boat_3 = create_boat_coords(3, used_coords)
for (x, y) in boat_3:
    grid[y, x] = "3"
# update used_coords with boat 3
used_coords.extend(boat_3)

# boat 2
boat_2 = create_boat_coords(2, used_coords)
for (x, y) in boat_2:
    grid[y, x] = "2"
# update used_coords with boat 2
used_coords.extend(boat_2)


# print grid and all used coords
print(grid)
print(used_coords)
