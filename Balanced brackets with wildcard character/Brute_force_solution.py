def helper(character: str, dict_of_paren_values: dict, parenthesis_counter: int) -> tuple:

  """
  Helper function for the brute_force_solver.
  This function updates the parethesis_counter based on the character that was encountered in the string.
  If parenthesis_counter is negative, that means we are in a situation with unbalanced brackets, and we return False.

  Parameters:
  character (str): The character just encountered in the input_string to be used to update the parenthesis_counter.
  dict_of_paren_values (dict): The dictionary mapping each parethesis type to a numerical value.
  parenthesis_counter (int): The counter that keeps track of whether we have too many parentheses of one type.

  Returns:
  tuple: A tuple with a boolean, and an int. The boolean keeps track of whether the string is valid or not so far. The int is the new parenthesis_counter to be used in the brute_force_solver.
  """

  # Update parenthesis_counter value.
  if character in dict_of_paren_values.keys():
    parenthesis_counter += dict_of_paren_values[character]

  elif character == "*":
    parenthesis_counter+=1

  # Deal with invalide strings.
  else:
    print("Invalid character in the string")
    return False, 0  

  # If the brackets are unbalanced, return False.
  if parenthesis_counter< 0:
    return False, 0

  # Otherwise return True together with the updated parenthesis_counter value.
  return True, parenthesis_counter 



def brute_force_solver(input_string: str) -> bool:

  """
  Brute force solver for the given problem.
  This function loops over the input string twice: once in the order in which it has been provided, and once in reverse. This is done to check first whether the string is balanced in terms of the closed brackets, and then to check whether it is balanced with respect to the open brackets.
  Therefore, the function relies on the same logic twice, just with flipped roles for open and closed brackets.

  Parameters:
  input_string(str): The string we want to check whether it is balanced or not.

  Returns:
  bool: True if the string is balanced, False otherwise.
  """ 

  parenthesis_counter: int = 0
  # This dictionary is used to convert parenthesis types to numerical values, so that as soon as the parenthesis counter becomes negative, we stop the execution of the code.
  dict_of_paren_values: dict[str, int] = {"(":+1, ")":-1}

  # Loop over the characters in the string. As soon as there are too many closed brackets to be compensated by the preceding open brackets or asteriscs, return False. 
  for character in input_string:

    check , parenthesis_counter: int = helper(character=character, dict_of_paren_values=dict_of_paren_values, parenthesis_counter=parenthesis_counter)
    if not check:
      return False

  # Re-initialise values of objects used to check the validity of the string.
  parenthesis_counter = 0
  dict_of_paren_values = {"(":-1, ")":+1}

  # Loop over the characters of the string in reverse. As soon as there are too many open brackets to be compensated by the preceding closed brackets or asteriscs, return False. 
  for character in reversed(input_string):

    check , parenthesis_counter: int = helper(character=character, dict_of_paren_values=dict_of_paren_values, parenthesis_counter=parenthesis_counter)
    if not check:
      return False

  # If no issue was encountered looping over the string, return True.
  return True     