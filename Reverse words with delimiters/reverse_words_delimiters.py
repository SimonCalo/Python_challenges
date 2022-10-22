def are_characters_of_different_nature(c1: str, c2: str) -> bool:

  """
  Helper function to check whether two characters are of different nature.

  The function returns True if one of the characters is a letter and the other is not.

  Parameters:
  c1 (str): The first character.

  c2 (str): The second character.

  Returns:
  bool: Whether the two characters are not both letters.
  """


  if c1.isalpha():
    return not c2.isalpha()
  else:
    return c2.isalpha()


def generate_two_lists(input_string: str) -> tuple:

  """
  Helper function to generate a list of letters and a list of delimiters.

  The function returns a tuple containing the list of words and the list of delimiters, both in the order in which they appear in input_string.

  Parameters:
  input_string (str): The string from which we want to extract words and delimiters.

  Returns:
  tuple: The list of words and the list of delimiters.
  """
  
  # Initialise useful objects.
  index = 0
  list_to_append_things_in = []
  other_list = []
  str_to_append = ""

  # Loop over input_string up to the last characters, in order to avoid errors when checking whether a character and the following one are of different nature.
  while index < len(input_string) - 1:

    # Add the character at the given index to the string that will be appended to the current list.
    str_to_append += input_string[index]

    # Check if the current character and the following one are of different nature.
    # If they are, then we should append the current string to a list, and re-start the process by re-initialising an empty string.
    if are_characters_of_different_nature(input_string[index], input_string[index+1]):
      list_to_append_things_in.append(str_to_append)
      str_to_append = ""

      # Reverse the roles of list_to_append_things_in and other_list, because we want to make sure that one them only contains words, and the other only contains delimiters.
      new_list_to_append_things_in = other_list[:]
      other_list = list_to_append_things_in[:]
      list_to_append_things_in = new_list_to_append_things_in

    # Proceed to the next character in input_string.
    index += 1

  # Add the last character to the final substring, and append it to the last list that was being used to append strings in.
  list_to_append_things_in.append(str_to_append + input_string[-1])

  # Based on the last character of input_string, order the two lists such that the first one is always the one containing words, and the second the one containing delimiters.
  if input_string[-1].isalpha():
    return list_to_append_things_in, other_list
  else:
    return other_list, list_to_append_things_in



def solver(input_string: str) -> str:

  """
  Main solver function.

  This function takes an input string containing words and delimiters and reverses the order of the words while maintaining the order of the delimiters.

  Parameters:
  input_string (str): The string in which we want to reverse the order of the words while maintaining the order of the delimiters.

  Returns:
  str: The string with reversed order of the words.
  """

  # Initialise the output string as an empty one.
  output_string = ""

  # Use the helper function to generate a list of words and one of delimiters in the order in which they appear in input_string.
  list_of_words, list_of_delimiters = generate_two_lists(input_string)

  # Reverse the order of the elements in list_of_words since we want to ensure that they appear reversed in the final output string.
  list_of_words.reverse()

  # Based on the what input_String starts with, decide whether to start from the list of delimiters or the one of words.
  if input_string[0].isalpha():
    list_to_loop_over, other_list = list_of_delimiters, list_of_words
  else:
    list_to_loop_over, other_list = list_of_words, list_of_delimiters

  # Loop over the list and add in turn a word and a delimiter (or vice versa depending on what the input begins with) to the output string.
  for index in range(len(list_to_loop_over)):
    output_string += other_list[index] + list_to_loop_over[index]

  # Add any possible remaining word or delimiter to the output string.
  if len(other_list) > len(list_to_loop_over):
    output_string += other_list[-1]

  return output_string
  
# Test the solution.
solver(";hello//world:here/")
