# Import the necessary packages
from itertools import permutations

def solver(input_list):

  """
  Solver function for the given problem.

  This function constructs all possible permutations of the given digits, and based on the input one, it simply selects the next greater permutation, and converts it back to a list.
  If there is no greater permutation, the function returns the lowest possible permutation of the input digits.

  To do so, this solution relies on the permutations function from the itertools package.

  Parameters:
  input_list (list): The list corresponding to the input number of which we want to find the next greater permutation.

  Returns:
  list: The next greater permutation of the given number, or the smallest possible one if there is no greater permutation of the given number.
  """

  # Convert the input list into a list of strings, so that they can be joined together to form a number
  str_input_list = list(map(str, input_list))
  input_number = int("".join(str_input_list))

  # Initialise an empty list to contain all possible permutations of the input digits
  list_of_permutations = []

  # Loop over all possible permutations of the input digits
  for perm in set(permutations(str_input_list)):

    # Joim the digits together to create a number
    number = "".join(perm)

    # Ignore numbers that start with zero
    if number[0] == "0":
      continue

    list_of_permutations.append(int(number))

  # Sort the list of all possible permutations to be able to retrieve the next greater one
  list_of_permutations.sort()

  # Retrieve the location of the input number in the sorted list
  ind = list_of_permutations.index(input_number)

  # If the input number is the highest possible permutation, then return the zeroeth element of the list
  if ind == len(list_of_permutations) - 1:
    ind = -1

  # Return the next number in the list in the form of a list of integers
  return list(map(int, list(str(list_of_permutations[ind + 1]))))


# Test the solution
t = [1, 8, 4, 2, 7, 2, 9, 0]
solver(t)