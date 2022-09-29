You are given an N by N matrix of numbers. Using this matrix, you have to construct a modified N by N matrix containing the same numbers as the original one. The way to construct the modified matrix is the following:
- Take each border of the original matrix,
- sort the elements in that border from lowest to highest,
- insert the sorted elements in the same border of the new matrix in clock-wise order starting from the top-left corner of the border.

To illustrate the procedure more clearly, let's look at an example. In this example, the original matrix, is the following:

[[10, 2, 8],
 [6, 5, 25],
 [1, 0, 9]]

As you can see, this matrix has two border: the outermost numbers and then the central element (5).
Therefore, we begin by extracting all the elements in the outermost border, we sort them from lowest to highest, and we insert them back into a new matrix in clock-wise order starting from the top-left corner. The central element 5 is the only element in that border, and therefore will not be changed.
The resulting matrix will be:

[[0, 1, 2],
 [25, 5, 6],
 [10, 9, 8]]