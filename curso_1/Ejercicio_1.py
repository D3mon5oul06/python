#introduccion: Try adding another line of code in the cell above and re-running it.
print("You've successfully run some Python code")
print("Congratulations!")
print("good day")

#ejercicio 0: create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
____

color = "blue"

# Check your answer
q0.check()


#ejercicio 1: solve the problem

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
____
radius = (diameter/2)

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
____
area = (pi*radius**2)

# Check your answer
q1.check()

#ejercicio 2:
########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

######################################################################
val = a
a = b
b = val
# Check your answer
q2.check()


#ejercicio 3a: Add parentheses to the following expression so that it evaluates to 1.
(5 - 3) // 2

#ejercicio 3b: Add parentheses to the following expression so that it evaluates to 0.
8 - 3 * 2 - (1 + 1)

#ejercicio 4: Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
#involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3
# Check your answer
q4.check()
