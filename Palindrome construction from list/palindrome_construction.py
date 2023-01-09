def reverse_word(word: str) -> str:
    """ Reverses an input string.

    Parameters:
        word (str): Input word to be reversed.

    Returns:
        str: Reversed input word
    """
    return word[::-1]


def solver(input_list: list[str]) -> set:
    """Main solver function for the task at hand.
    Given a list of strings, the function outputs a list
    of tuples representing the indices of the strings
    to be concatenated together to create a palindrome.

    Parameters:
        input_list (list[str]): A list of strings out of which
                                palindromes can be constructed.

    Returns:
        set: A set of tuples of indices indicating which two
              words can be paired together to construct a
              palindrome.
    """
    
    output_list: set = []
    
    for index, word in enumerate(input_list):
        
        if reverse_word(word) in input_list:
            output_list.append((index, input_list.index(reverse_word(word))))
            output_list.append((input_list.index(reverse_word(word)), index))
            
        if len(word) > 1 and reverse_word(word[:-1]) in input_list:
            output_list.append((index, input_list.index(reverse_word(word[:-1]))))
                       
    return set(output_list)                   

t = ["code", "edoc", "da", "d"]
print(solver(t))