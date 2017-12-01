"""
Name: John Miller
Date: 27 November 2017
Class: CS 463 - 001
Project: Markov Decision Process
"""
import copy

# Create all constants, Gamma changes from 1 to 0.96 depending on if it is the finite horizon case
# GAMMA = 1
GAMMA = 0.96
PROB_STAY = 0.1
PROB_OPPOSITE = 0.2
PROB_SUCCEED = 0.7


# Create print function to print out grid in proper format
def print_function(grid):

    for i in grid:
        for j in i:

            print(j, end=" ")
        print()


# Create the function to iterate through the neighboring cells
def value_iteration(i, j, start_grid):

    # Create a costs array and set four flags (used for checking opposite directions)
    costs = []
    top, right, down, left = False, False, False, False

    # If there is an edge case, then set the flag to true for which piece
    if i - 1 < 0:                   top   = True
    if i + 1 >= len(start_grid):    down  = True
    if j - 1 < 0:                   left  = True
    if j + 1 >= len(start_grid[i]): right = True

    # Calculate the probability to stay in the current cell
    prob_to_stay = start_grid[i][j] * PROB_STAY
    costs.append(prob_to_stay)

    """* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
    # Start by checking up, if not a wall
    if i > 0:

        # If not on a wall and going up, then down is the opposite direction
        if down:
            prob_to_opp = start_grid[i][j] * PROB_OPPOSITE
        else:
            prob_to_opp = start_grid[i + 1][j] * PROB_OPPOSITE

        # Find the probability to go up successfully
        prob_to_up = start_grid[i - 1][j] * PROB_SUCCEED
        costs.append(prob_to_up + prob_to_opp + prob_to_stay)

    # If you are on a top wall, then find the success and opposite values
    else:
        prob_to_up = start_grid[i][j] * PROB_SUCCEED
        prob_to_opp = start_grid[i + 1][j] * PROB_OPPOSITE

        costs.append(prob_to_up + prob_to_opp + prob_to_stay)

    """* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
    # Then check the right values, if not a wall
    if j < len(start_grid[i]) - 1:

        # If not on a wall and going right, then left is the opposite direction
        if left:
            prob_to_opp = start_grid[i][j] * PROB_OPPOSITE
        else:
            prob_to_opp = start_grid[i][j - 1] * PROB_OPPOSITE

        # Find the probability to go right successfully
        prob_to_right = start_grid[i][j + 1] * PROB_SUCCEED
        costs.append(prob_to_right + prob_to_opp + prob_to_stay)

    # If you are on a right wall, then find the success and opposite values
    else:
        prob_to_right = start_grid[i][j] * PROB_SUCCEED
        prob_to_opp = start_grid[i][j - 1] * PROB_OPPOSITE

        costs.append(prob_to_right + prob_to_opp + prob_to_stay)

    """* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
    # Next check the down values, if not a wall
    if i < len(start_grid[i]) - 1:

        # If not on a wall and going down, then up is the opposite direction
        if top:
            prob_to_opp = start_grid[i][j] * PROB_OPPOSITE
        else:
            prob_to_opp = start_grid[i - 1][j] * PROB_OPPOSITE

        # Find the probability to go down successfully
        prob_to_down = start_grid[i + 1][j] * PROB_SUCCEED
        costs.append(prob_to_down + prob_to_opp + prob_to_stay)

    # If you are on a bottom wall, then find the success and opposite values
    else:
        prob_to_down = start_grid[i][j] * PROB_SUCCEED
        prob_to_opp = start_grid[i - 1][j] * PROB_OPPOSITE

        costs.append(prob_to_down + prob_to_opp + prob_to_stay)

    """* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
    # Finally check the left values, if not a wall
    if j > 0:

        # If not on a wall and going left, then right is the opposite direction
        if right:
            prob_to_opp = start_grid[i][j] * PROB_OPPOSITE
        else:
            prob_to_opp = start_grid[i][j + 1] * PROB_OPPOSITE

        # Find the probability to go left successfully
        prob_to_left = start_grid[i][j - 1] * PROB_SUCCEED
        costs.append(prob_to_left + prob_to_opp + prob_to_stay)

    # If you are on a left wall, then find the success and opposite values
    else:
        prob_to_left = start_grid[i][j] * PROB_SUCCEED
        prob_to_opp = start_grid[i][j + 1] * PROB_OPPOSITE

        costs.append(prob_to_left + prob_to_opp + prob_to_stay)

    return costs


def main():

    # Create reward function
    start_grid = [[0, 0, 3, 10],
                  [0, 5, 0, 60],
                  [5, 10, 5, 0],
                  [45, 0, 0, 5]]

    # Create empty direction matrix
    direction = [["", "", "", ""],
                 ["", "", "", ""],
                 ["", "", "", ""],
                 ["", "", "", ""]]

    # Create two grid copies of the reward function
    new_grid = copy.deepcopy(start_grid)
    new_grid_static = copy.deepcopy(start_grid)

    # Create copy of direction matrix
    new_direction = copy.deepcopy(direction)

    # Run loop 6 times for V^6 or many times for V^* (it will converge)
    # Run a nested for loop through the reward function
    for l in range(1000):
        for i in range(len(start_grid)):
            for j in range(len(start_grid[i])):

                # Find the costs of the neighboring cells, get the max value of those costs
                costs = value_iteration(i, j, new_grid_static)
                max_cost = round(max(costs), 1)

                # Calculate the new cost by doing the reward function cost + gamma * max cost
                # Find the index of the max cost
                new_cost = start_grid[i][j] + (GAMMA * max_cost)
                max_index = costs.index(max(costs))

                # Add the new cost to the new grid copy for the next run through
                new_grid[i][j] = new_cost

                # Check the index values, if index 0 was used you stay, 1 you go up, 2 go right,
                # 3 go down and 4 go left
                if max_index == 0:
                    new_direction[i][j] = " s "
                elif max_index == 1:
                    new_direction[i][j] = " ^ "
                elif max_index == 2:
                    new_direction[i][j] = " > "
                elif max_index == 3:
                    new_direction[i][j] = " v "
                elif max_index == 4:
                    new_direction[i][j] = " < "

        # Create copies of the new grid again
        new_grid = copy.deepcopy(new_grid)
        new_grid_static = copy.deepcopy(new_grid)

        # Create a copy of the direction
        new_direction = copy.deepcopy(new_direction)

        # Print out the grid and direction grid
        print_function(new_grid)
        print()
        print_function(new_direction)
        print()


main()
