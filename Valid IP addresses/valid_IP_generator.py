def check_validity_of_one(input_digits: str) -> bool:

    """Function to check whether a number (in the form of a string of digits)
    represents a valid unit of an IP address.
    This is evaluated based on the conditions stated in the problem.

    Parameters:
        input_digits (str): The digits composing the number to be checked.

    Returns:
        bool: Whether the digits form a valid number as a unit of an IP address.  
    """
    zero_condition: bool = input_digits == "0"
    condition1: bool = input_digits[0] != "0"
    condition2: bool = int(input_digits) <= 255

    return zero_condition or (condition1 and condition2)


def construct_all_valid_IPs(input_digits: str, n_to_find: int= 4) -> list:

    """Function to construct all possible valid IP addresses from a string 
    of digits. This function allows for the flexibility of imagining that 
    IP addresses were made of n subunits, with n=4 by default. The validity
    of an IP address is determed according to the details outlined in the
    problem. This function uses a recursive approach.

    Parameters:
        input_digits (str): The input digits from which to construct all 
                            possible valid IP addressers.
        n_to_find (int, default 4): The number of subunits that sould form
                                    the IP address.

    Returns:
        list: A list with all possible valid IP addresses.                                                  
    """

  # Construct baseline case, corresponding to the evaluation
  # of the last subunit.
    if n_to_find == 1:
        if check_validity_of_one(input_digits):
            return True, [input_digits]
        else:
            return False, []  

    list_of_valid_IPs: list = []
    max_range: int = min(4, len(input_digits))

  # Loop over all possible lenghts of the first subunit.
    for i in range(1, max_range):
        first_number: str = input_digits[0:i] # Construct the first subunit.
    # If the subunit is valid, proceed with the following ones.
        if check_validity_of_one(first_number):
            new_input: str = input_digits[i:len(input_digits)]
            condition, list_of_possible_suffixes = construct_all_valid_IPs(
            input_digits=new_input, n_to_find=n_to_find-1
            )
        else:
            continue
        if condition: # If there are valid suffixes, proceed.
            for suffix in list_of_possible_suffixes:
                list_of_valid_IPs.append(f"{first_number}.{suffix}")
 

    if n_to_find == 4: # For the initial case constructing the entire
                     # 4 subunits, only return a list.
        return list_of_valid_IPs    
    return len(list_of_valid_IPs) != 0, list_of_valid_IPs   
