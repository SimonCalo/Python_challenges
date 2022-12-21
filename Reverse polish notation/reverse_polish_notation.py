def evaluate_single_operation(input_list: list) -> float:
    
    """ Evaluate a mathematical operation in the form of a list.
    The list must contain three elements, two of which should be numbers 
    and one should represent a mathematical binary operator.
    
    Parameters:
        input_list (list): A list containing numbers as the first two elements, 
                           and the third should be a binary operator.

    Returns:
        float: The result of the mathematical operation.
    """
    
    return eval(f"{input_list[0]} {input_list[2]} {input_list[1]}")


def solver(input_list: list) -> float:
    
    """ Main solver function for te problem.
    This function performs the operations given by a list 
    in the form of reverse polish notation. 
    It then outputs as single number which is the result of all the operations.
    
    Parameters:
        input_list (list): A list of strings representing the sequence of operations
                           in reverse polish notation form.

    Returns:
        float: The number resulting from all the operations.
    """
    
    numbers_list: list = []

    for element in input_list:
        try:
            element: float = float(element)
            numbers_list.append(element)
        except:
            n2: str = numbers_list.pop()
            n1: str = numbers_list.pop()
            numbers_list.append(evaluate_single_operation([n1, n2, element]))

    return numbers_list[0]  