import numpy as np

def add_all_neighbours_to_list(location:list, list_of_checked_locations:list, list_of_land_locations:list) -> None:

  """
  Helper function to add all neighbouring land locations of a given location to list_of_checked_locations.

  If a neighbouring land location is found, then add also all of its land neighbours to list_of_checked_locations.

  Neighbouring cells are considered all cells which are in the surrounding perimeter of the given cell, including those on the diagonal.

  Parameters:
  location (list): This is a list that represents the given land location on the planet, in the form of [row, column].

  list_of_checked_locations (list): A list of lists. Each of the sub-lists represents a land location on the planet that has already been checked for neighbours.

  list_of_land_locations (list): A list of all the land locations on the planet. The locations are given as lists in the form of [row, column].

  Returns:
  None
  """



  # Extract row and column for convenience
  row = location[0]
  column = location[1]

  # Construct all possible surrounding cells
  for i in range(-1,2):
    for j in range(-1,2):

      # We do not want to consider the cell itself
      if i == 0 and j == 0:
        continue

      x = row + i
      y = column + j
      neighbour = [x, y]

      # If the neighbour has already been checked, then go to the next neighbour
      if neighbour in list_of_checked_locations:
        continue  
  
      # If the neighbour has not yet been checked and it is a landslot, then add it to list_of_checked_locations, and add all its neighbours as well to list_of_checked_locations
      elif neighbour in list_of_land_locations:
        list_of_checked_locations.append(neighbour) 
        add_all_neighbours_to_list(neighbour, list_of_checked_locations, list_of_land_locations) 

      else:
        continue  

  return       



def solver(planet:np.array) -> int:

  """
  Solver function for the given problem.

  Given an np.array of zeroes and ones (here called planet), this function counts the number of islands contained.

  For further details of what an island is, see the text file containing a description of the problem.

  This function extracts all the cells with value 1 in the array, and counts the number of separate groups of connected 1's there are in the array.

  The number of islands is then simply the number of distinct groups of connected 1's in the array.

  Parameters:
  planet (np.array): This is the array that represents the planet in which we want to count the number of islands. This can also be replaced by a simple list of lists in Python.

  Returns:
  int: The number of islands contained in the planet.
  """

  # Initialise useful lists and a counter for the number of islands
  list_of_checked_locations = []
  list_of_land_locations = []
  counter = 0

  # Extract all the locations of 1's in the array
  list_of_land_locations_temp = np.argwhere(planet == 1)


  # Convert those locations to a list of lists
  for loc in list_of_land_locations_temp:
    list_of_land_locations.append([loc[0], loc[1]])

  # If the planet is only made of land, return 0
  if len(list_of_land_locations)  == len(planet) * len(planet[0]):
    return 0

  # Loop over all the locations of 1's in the array
  for location in list_of_land_locations:

    # If the location has already been checked directly or because it is a neighbour, then go to the next location
    if location in list_of_checked_locations:
      continue

    list_of_checked_locations.append([location[0], location[1]])  
    counter+=1

    # Call the helper function to add all cells neighbouring the current location to list_of_checked_locations
    add_all_neighbours_to_list(location, list_of_checked_locations, list_of_land_locations)

  return  counter

# Test the solution

planet = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]])
solver(planet)