#ejercicio 1: define a function called `sign` which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
def sign(number):
    return (number > 0) - (number < 0)

#ejercicio 2: Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

#ejercicio 3:
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Test case where the function returns False but should have returned True
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check if the function returns the expected result
expected = True
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual == expected)  # The result should be True

#ejercicio 4:
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0 # Your code goes here (try to keep it to one line!)

#ejercicio 5a:
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    pass

# Check your answer
q5.a.check()

#ejercicio 5b:
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)
    pass

# Check your answer
q5.b.check()

#ejercicio 5c:
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass

# Check your answer
q5.c.check()

#ejercicio 6:
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return int(ketchup) + int(mustard) + int(onion) == 1
    pass

# Check your answer
q6.check()
