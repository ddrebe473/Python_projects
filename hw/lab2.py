# Lab 2 - Iteration
# 02/10/2020
# Objectives
# Learn to use loops to solve a problem
# Learn to repeatedly prompt for input
# Exercises
# Write a Java program that will prompt the user for a number and print out a triangle with those dimensions. For example, if the user enters 5, return the following:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
# Write a Python program that will prompt the user for the grades for an exam, computes the average, and returns the result. Your program must be able to handle an unspecified number of grades.
# (Hint: Tell the user to enter -1 when they finished entering grades)

# Be sure to test your code with a variety of values and number of grades. 3. Write a Java program that will repeatedly display a menu of choices to a user and prompt them to enter an option. You should use the following options: 1. Say Hello - This should print "Hello" to console. 2. Addition - This should prompt the user to enter 2 numbers and return the sum of the two. 3. Multiplication - This should prompt the user to enter 2 numbers and return the product of the two. 4. Exit - Leave the program

# The program should continue to return to the menu until the user enters 4.

n = int(input("n:"))

for i in range(0, n+1):
    for j in range(0, i+1):
        print(j, end="  ")
    print()


rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("*", end="  ")
    print("\n")
