def refined_solver(input_string: str) -> bool:

  """
  Refined solver for the problem.
  The key insight to construct this refined solver was to notice that looping over the string twice was unnecessary, as the same information could be retrieved by looping over it only once.
  Therefore, the functioning of the solver is similar to the brute force one, with the difference that now one also keeps track of the number of trailing open brackets, and at the end the function checks whether there are no trailing open brackets.

  Parameters:
  input_string(str): The string we want to check whether it is balanced or not.

  Returns:
  bool: True if the string is balanced, False otherwise.
  """ 

  # Make sure the input is of the right type.
  assert type(input_string) is str, "Invalid input type. Input must be a string"

  # Initialise counters to keep track of too many closed brackets, and trailing open brackets.
  parenthesis_counter: int = 0
  n_trailing_open_brackets: int = 0

  # When looping over the string, the number of trailing open brackets decreseases if we encounter a ) or a *, but it can never be less than zero.
  for character in input_string:

    if character == ")":
      parenthesis_counter -= 1
      n_trailing_open_brackets = max(0, n_trailing_open_brackets - 1)

    elif character == "(":
      parenthesis_counter += 1
      n_trailing_open_brackets += 1  

    elif character == "*":
      parenthesis_counter+=1
      n_trailing_open_brackets = max(0, n_trailing_open_brackets - 1)

    else:
      print("Invalid character in the string")
      return False    

    # If there are too many closed brackets thta cannot be compensated by the preceding characters, prematurely interrupt the function and return False.
    if parenthesis_counter < 0:
      return False

  # To be valid, there should be no trailing open brackets.
  return n_trailing_open_brackets == 0