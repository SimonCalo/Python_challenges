from random import randint
from Brute_force_solution import brute_force_solver
from Refined_solution import refined_solver

def generate_random_string() -> str:

  """
  Function to generate a random string containing (,) and * as characters.

  Returns:
  str: The string generated.
  """  

  length_of_string: int = randint(1, 10)
  output_string: str = ""
  conversion_dict: dict[int, str] = {1: "(", 2: ")", 3: "*"}

  for character in range(length_of_string):
    output_string += conversion_dict[randint(1, 3)]

  return output_string  

def check() -> bool:

  """
  Function to check the consistency of the two solution methods using a randomly generated string.

  Returns:
  bool: Whether the two methods agree or not.
  """ 


  for i in range(50):
    string: str = generate_random_string()
    if not refined_solver(string) == brute_force_solver(string):
      return False

  return True   

check()   