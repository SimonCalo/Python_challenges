def clean_dict (input_d:dict) -> None:

  """
  Helper function to remove unnecessary entry in the dictionary containing location of the letters of interest.

  The function simply removes the first entry of the dictionary, if the first two entry are the same.
  Similarly, it removes the last entry, if the last two entries of the input dictionary are the same.

  This function is not necessary for the execution of the code, but it is used for optimisation purposes.

  The function directly acts on the input dictionary and does not return any object.

  Parameters:
  input_d (dict): The dictionary containing the locations of the various letters of interest.

  Returns:
  None
  """

  # Handle edge cases (if there are less than 2 entries in the dictionary)
  if len(input_d) < 2:
    return

  # If the first two entries in the dictionary have the same value, remove the first one
  if input_d[list(input_d.keys())[0]] == input_d[list(input_d.keys())[1]]:
    del input_d[list(d.keys())[0]]

  # Handle edge cases (if there are less than 2 entries in the dictionary after the first one has potentially been removed)
  if len(input_d) < 2:
    return

  # If the last two entries in the dictionary have the same value, remove the last one
  if input_d[list(input_d.keys())[-1]] == input_d[list(input_d.keys())[-2]]:
    del input_d[list(d.keys())[-1]]



def return_boundaries_of_complete_substring(input_d: dict, characters_set: set, starting_index: int, shortest_length: int) -> list:

  """
  Helper function returning the boundaries (in terms of indices) of a substring containing all the required characters within the initial input string.

  The function relies on the dictionary containing location of the letters of interest to return the boundaries of the complete substring.
  The function is optimised to ensure that as soon as the length of the generated substring is longer than the previously recorded shortest length, the execution is stopped, and an empty list is returned.

  The empty list as a return indicates that no shorter substring containing all the required characters can be generated through this function.
  The list containing a -1 is used to indicate that no further searches should be performed, as the possibility of generating a substring containing all the required character is no longer viable.

  The basic idea behind the working of this function is that while looping over the input_d we check that eventually we encounter all the characters in the characters_set.
  As soon as we do, we stop, and we return the indices (in the original input string) corresponding to the first and last characters encountered.
  If we do not encounter all the required characters, we return the list containing a -1. As soon as the generated substring is longer than the shortest_length, we return the empty list.

  Parameters:
  input_d (dict): The dictionary containing the locations of the various letters of interest.

  characters_set (set): The set containing all the characters that need to appear in the substring.

  starting_index (int): The index of the item in input_d from which we start in our search for the shortest substring.

  shortest_length (int): The length of the last recorded shortest substring.

  Returns:
  list: A list containing the first index and last index of the substring containing all the required characters within the original string. If no such indices can be found, return the empty list.
        If no possible substring containing all the required characters can be generated anymore, the list will contain only 1 entry being a -1.
  """

  index = starting_index

  # Extract the location on the string corresponding to the key of the item at the starting_index in the dictionary
  starting_string_location = list(input_d.keys())[starting_index]

  # Create a copy of the set containing all the required characters
  temp_list = list(characters_set)[:]

  # Loop over the input_d until all the elements in the characters_set have been found
  while len(temp_list) > 0:

    # If it is not possible to encounter all the required characters within the input_d, then return the list containing a -1
    if index >= len(input_d):
      return [-1]

    # If the constructed substring would be longer than shortest_length, return the empty list
    if list(input_d.keys())[index] - starting_string_location > shortest_length:
      return []

    character = input_d[list(input_d.keys())[index]]

    # If a character present in the copy of the characters_set is found, remove it
    if character in temp_list:
      temp_list.remove(character)

    index += 1

  # Return the boundaries of the substring on the original string
  return [starting_string_location, list(input_d.keys())[index - 1]]


def solver(input_string: str, characters_set: set) -> str:

  """
  Main solver function for the problem at hand.

  Given a string and a set of characters, the function outputs the shortest substring containing all the characters in the set.

  Parameters:
  input_string (str): The input string in which we want to find the substring.

  characters_set (set): The set containing all the characters that need to appear in the substring.

  Returns:
  str: The shortest substring. If no substring containing all the characters in the set can be found, return the empty string.
  """

  # Check that the string contains all the characters in the set.
  # If not, return the empty string
  for character in characters_set:
    if character not in input_string:
      return ""

  n_characters = len(characters_set)
  loc_dic = {}

  # Create a dictionary containing all the occurrences of the interesting characters in the string.
  # This dictionary contains the location in the input_string as a key, and the character in characters_set at that location as a value.
  for index, character in enumerate(input_string):
    if character in characters_set:
      loc_dic[index] = character

  # Use the helper function to remove unnecessary entries in loc_dic.
  clean_dict(loc_dic)

  # Initialise the entire string as the shortest substring, and the boundaries of such substring as the first and last characters of the string.
  shortest_distance = len(input_string)
  boundaries_of_shortest_substring = [0, len(input_string) - 1]

  # Loop over the indices of loc_dic up to the number of characters in characters_set.
  # This is in order to ensure the correct functioning of the function return_boundaries_of_complete_substring. Otherwise we would get indices out of bound in the function.
  for i in range((len(loc_dic) - len(characters_set) + 1)):

    # Use the helper function to obtain a list of the boundaries of the shortest substring.
    new_boundaries_of_shortest_substring = return_boundaries_of_complete_substring(loc_dic, characters_set, i, shortest_distance)

    # Handle the case in which we have an empty list.
    # This happens, when the length of the newly generated substring is greater than the previous shortest length of a substring.
    if len(new_boundaries_of_shortest_substring) == 0:
      continue

    # Following the functioning of the helper function return_boundaries_of_complete_substring, if the list contains aonly one entry, it means that it is no longer possible to generate a substring containing all the required characters.
    # Hence we stop the execution and return the last recorded boundaries of the shortest substring.
    elif len(new_boundaries_of_shortest_substring) == 1:
      break

    # Otherwise, we have obtained a valid list for new_boundaries_of_shortest_substring.
    else:
      new_shortest_distance = new_boundaries_of_shortest_substring[1] - new_boundaries_of_shortest_substring[0]

      # Check if the length of the new substring is less than the last shortest length recorded.
      # If so, set the shortest distance to be the newly calculated one, and set the boundaries of the shortest substring to be newly obtained ones.
      if new_shortest_distance < shortest_distance:
        shortest_distance = new_shortest_distance
        boundaries_of_shortest_substring = new_boundaries_of_shortest_substring

        # If the length of the shortest substring has the same number of characters as the characters_set, it means that we cannot generate a shorter substring containing all the required characters.
        # In that case, we stop the execution, and proceed to output the given substring.
        if shortest_distance == len(characters_set):
          break

  return input_string[boundaries_of_shortest_substring[0]: boundaries_of_shortest_substring[1]+1]

# Test the solution.
test_string = "figehaefaaaaaaaaa"
test_set = {'f', 'e', 'h'}
solver(test_string, test_set)
