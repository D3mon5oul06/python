#ejercicio 1: Complete the body of the following function according to its docstring.
def round_to_two_places(num):
  
    round_to_two_places=(3.1416)
    return round(num,2)
    
    
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass

# Check your answer
q1.check()

#ejercicio 2: 
n = 280678
ndigits = -3
result =round(n, ndigits)
print = result

#ejercicio 3: 

def to_smash(total_candies, num_friends=3):
    """
    Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between the specified number of friends.
    
    Args:
        total_candies (int): The total number of candies.
        num_friends (int, optional): The number of friends to split the candies between.
            Defaults to 3 if not provided.
    
    Returns:
        int: The number of candies to smash.

    Examples:
        >>> to_smash(91)
        1
        >>> to_smash(91, 4)
        3
    """
    return total_candies % num_friends

# Check your answer
q3.check()