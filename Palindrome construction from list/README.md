This problem is the same as the one given by Daily Coding Problem number 167 [Hard].
Personally, I found this problem to be of medium level.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

I included a modification to my solution, such that a pair can also be given by the same word twice, if the given word is a palindrome itself. So, in my solution, the list ["code", "edoc", "da", "d"], returns [(0, 1), (1, 0), (2, 3), (3,3)], since "d" is itself a palindrome. 

This could easily be adjusted by preventing the algorithm to include tuples containing the same index twice, thus resulting in a solution consistent with the one asked by the problem.

