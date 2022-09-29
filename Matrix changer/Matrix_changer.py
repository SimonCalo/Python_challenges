import numpy as np



def ith_border(input_matrix: list, N: int, i: int) -> list:

  """
  Helper function to extract the ith border of a given matrix.

  A border is defined by the elements all being at the same distance from the edge of the matrix. 

  For clarity, the 0th border is given by all the outermost elements in the matrix.

  Parameters:
  input_matrix (list): The matrix of which we want to extract the ith border.

  N (int): The length or heigth of the matrix.

  i (int): The index of the border we want to extract (i.e. 0th, 1st, 2nd, etc.).

  Returns:
  list: The elments present in the ith border of input_matrix.
  """

  # Initialise the output_list
  output_list = []

  # Loop over the matrix, and extract the elements present in the ith border
  for k in range(N):
    for l in range(N):

      # Condition to check whether we are considering the ith border
      if ((k==i or k==(N-1-i)) and (l>=i and l<=(N-1-i))) or ((l==i or l==(N-1-i))and (k>=i and k<=(N-1-i))):

        # If we are in a cell of the ith border, include the element in that cell to the output_list
        output_list.append(input_matrix[k][l])

  return output_list


def fill_ith_border_clockwise(elements: list, i: int, N: int, matrix_to_fill:np.array) -> None:

  """
  Helper function to fill the elments in the ith border of a given np.array in clock-wise order starting from the top-left corner.

  A border is defined by the elements all being at the same distance from the edge of the matrix. 

  For clarity, the 0th border is given by all the outermost elements in the matrix.

  Parameters:
  elements (list): The elements we want to insert in the ith border.

  i (int): The index of the border we want to extract (i.e. 0th, 1st, 2nd, etc.).

  N (int): The length or heigth of the matrix.

  matrix_to_fill (np.array): The matrix whose ith border is to be filled.

  Returns:
  None.
  """

  # Loop over the elements of the top side of the border, from left to right
  for index in range(i, N-i):
    # Insert the first element in the elements list, then remove it
    matrix_to_fill[i][index] = elements[0]
    elements.pop(0)

  # Loop over the elements of the right side of the border, from top to bottom
  for index in range(i+1, N-i):
    matrix_to_fill[index][N-1-i] = elements[0]
    elements.pop(0)

  # Loop over the elements of the bottom side of the border, from right to left
  for index in range(N-2-i, i-1, -1):
    matrix_to_fill[N-1-i][index] = elements[0]
    elements.pop(0)

  # Loop over the elements of the left side of the border, from bottom to top
  for index in range(N-2-i, i, -1):  
    matrix_to_fill[index][i] = elements[0]
    elements.pop(0)

  return


def modify_matrix(input_matrix: list) -> np.array:

  """"
  Main function used to modify the input matrix as requested in the problem.

  This function takes an NxN matrix, and (by calling the appropriate helper functions) outputs an NxN matrix where the elements in each of the borders has been sorted in ascending order and placed clock-wise starting from the top-left corner.

  Parameters:
  input_matrix (list): This is a list of lists, such that they form an NxN matrix.

  Returns:
  np.array: An array representing the final matrix with the borders sorted and placed in the right order.
  """

  # Extract the dimensionality of the input matrix
  N = len(input_matrix)


  # Extract the number of borders present in the input matrix
  n_borders = int(np.ceil(N/2))

  # Create the output matrix in the form of a np.array
  output_matrix = np.empty((N,N))
  output_matrix[:] = np.nan


  # Loop over the number of borders in the input matrix
  for i in range(n_borders):

    # For each border, call the helper function to extract the elements of that border
    border_elements = ith_border(input_matrix, N, i)

    # Sort the elements of the given border
    border_elements.sort()

    # Fill the ith border of the output matrix with the sorted elements in clock-wise order
    fill_ith_border_clockwise(border_elements, i, N, output_matrix)

  return output_matrix  

# Test the solution 

test_matrix = [[1,2,3,4,5, 20], [6,7,8,9,10, 20], [11,12,13,14,15, 20], [16,17,18,19,20, 20], [21,22,23,24,25, 20], [20,20,20,20,20,20]]

modify_matrix(test_matrix)