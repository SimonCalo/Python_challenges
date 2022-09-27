This problem is the same as the one given by Daily Coding Problem number 84.

Here is the text for the given problem:

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighbouring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

[[1 0 0 0 0],
[0 0 1 1 0],
[0 1 1 0 0],
[0 0 0 0 0],
[1 1 0 0 1],
[1 1 0 0 1]]

I interpreted a matrix with no zeroes as having no islands, but as soon as there is one zero (with all the other entries 1) then that is considered to be an island in my solution.