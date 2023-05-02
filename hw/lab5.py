# Lab 5 - Inheritance/Polymorphism
# 03/09/2020
# Objectives
# Be able to code a child class definition (inheritance)
# Demonstrate knowledge of how to use the keyword extends
# Demonstrate knowledge of how to code various non-default constructors using superclass constructors.
# Demonstrate knowledge of how to use super9) in constructors.
# Demonstrate knowledge of how to use super in other subclass methods.
# Exercise
# This week, you will write a user-defined class that will encapsulate a CTAStation. You will then use arrays to store CTAStation data. Solution: Add to your GeoLocation class from last week to include the following:

# A method called calcDistance that takes another GeoLocation and returns a double. Note: This should use the formula Math.sqrt(Math.pow(lat1-lat2,2)+Math.pow(long1-long2,2)).
# A method called calcDistance that takes a long and lat and returns a double. Note: See above formula.
# Create a class that will implement a CTAStation, which should inherit from GeoLocation, with the following UML Diagram:

# UML Diagram

# CTAStopApp
# This app will display a menu of options of which data to extract from the data stored in the CTAStation[]. The API for this app class is as below: You do not need to follow this API exactly, but it may help you to figure out how to break down the tasks:

# main():

# reads stations in the input file and stores the data in an instance of CTAStation[].
# displays the menu options, which should be the following:
# Display Station Names
# Display Station with/without Wheelchair access
# Display Nearest Station
# Exit
# performs the operation requested by the user
# loops until exit is chosen
# displayStationNames():

# Iterates through CTAStation[] and prints the names of the stations
# displayByWheelchair():

# prompts the user for accessibility (y or n)
# checks that the input is y or n, continues to prompt the user for y or n until one has been entered
# if char entered is valid choice:
# determine which boolean to use (y -> true, n -> false)
# loop through CTAStation[] to look at wheelchair and display CTAStations that meet the requirement
# display message if no CTAStations are found
# displayNearest():

# prompts the user for a latitude and longitude
# calls calcDistance
# uses value returned to iterate through CTAStation[] to find the nearest station and displays it to the console.
