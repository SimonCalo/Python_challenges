# More refined solution that allocates less memory and does not create all possible permutations

# The key insight to construct this solution was to realise that if you check sublists made by the last n digits in the input list, then
# once you consider a new digit (i.e. you inspect a sublist made by the last n+1 digits in the input list), the digits after the newly considered one will already be in their highest configuration
# because they have already been checked previously, and thus one simply needs to swap that new digit with the closest greater digit to it following it.
# The point is that this closest greater digit will always be the first digit greater than the 'newly considered digit' encountered when looping over the sublist from the right. 


def is_highest_configuration(input_list):

  """
  Helper function to check if the given input permutation is the highest possible one.

  This is done by simply sorting the input list in descending order and checking equality with the input list.

  Parameters:
  input_list (list): The list corresponding to the input number of which we want to find the next greater permutation.

  Returns:
  bool: Whether input_list corresponds to the highest possible permutation of the digits (True) or not (False).
  """

  return input_list == sorted(input_list, reverse = True)


def generate_next_higher_configuration(input_list):

  """
  Helper function to generate the next higher configuration of the given digits.

  The functon simply looks for the first digit greater than the one at position zero when looping over the list in reverse. This will be the new digit that should go at position zero.

  Therefore, this digit is removed from the list, and the returned list is simply made with this digit at location zero, concatenated with a list of the other digits sorted in ascending order.

  This ensures that this will be exactly the next greater configuration of the given digits.

  Parameters:
  input_list (list): The list of which we want to find the next greater permutation.

  Returns:
  list: The list of the digits arranged in the next greater permutation.
  """

  # Loop over the list in reverse order
  for element in reversed(input_list):

    # As soon as you find a digit that is greater than the one at position zero, remove it and return the output list
    if element > input_list[0]:
      input_list.remove(element)

      # The output list contains the removed digit at position zero, and then all the remaining digits sorted in acending order
      return [element] + sorted(input_list)


def solver(input_list):

  """
  Main solver function for the problem at hand.

  Given an input list of digits, this function returns the next greater permutation of those digits.

  If no greater permutation exists, it returns the lowest possible permutation of those digits.

  Parameters:
  input_list (list): The list of which we want to find the next greater permutation.

  Returns:
  list: The list of the digits arranged in the next greater permutation (or the lowest possible permutation).
  """

  # If the given configuration is the highest possible one, return the lowest possible configuration of the digits
  if is_highest_configuration(input_list):
    return sorted(input_list)

  # Loop over the sublists that can be created with the last digits of the input_list, starting from the last 2 digits and going forward
  for i in range(2, len(input_list) + 1):

    # Create a temporary list of the last n digits
    temp_list = input_list[len(input_list) - i: len(input_list)]

    # If the first digit in the temporary list is greater than or equal to the one that follows it, then it means that this sublist is already in its greatest configuration, and we proceed to the next sublist
    if temp_list[0] >= temp_list[1]:
      continue

    # Otherwise we return the first n-len(input_list) digits of input_list concatenated with the next higher permutation of the last n digits
    else:
      return input_list[:len(input_list) - i] + generate_next_higher_configuration(temp_list)
  

# Test the solution
t = [1, 8, 4, 2, 3, 8, 7, 7]
solver(t)