# Lab 6 - Lists
# 03/30/2020
# Objectives
# Learn to write and use an ArrayList declaration
# Learn to manipulate the data in an ArrayList
# Exercise
# In this assignment, you will write a user-defined class that will encapsulate an ArrayList of CTAStations called CTARoute. You will allow users to look up stations by name, add new stations, and delete existing stations.

# Solution
# Create a class that will implement a CTARoute with the following UML diagram:

# UML Diagram

# In the previous lab, you only needed to concern yourself with the Green Line. In this lab, however, you will need to be able to handle two CTA routes, the Red and Green lines. The information for all of these stations should be read from CTAStops.csv. The format is similar to before, but with two extra columns to list the location of each stop along either the Red or Green lines. The order is as follows: Name, Latitude, Longitude, Location, Wheelchair, Red Line, Green Line Note: A - 1 for Red/Green line means that the station is not on that route.

# In addition to a new CTARoute class, you will also need to modify you menu to have the following options:

# Display the names of all stations
# Display the stations with wheelchair access
# Display the nearest station to a location
# Display information for a station with a specific name
# Display information for all stations
# Add a new station
# Delete an existing station
# Exit
# Adding a station should ask for each variable individually as well as the name of the route that the station is on.
# Adding a station should ask for the names of the previous and following stations and insert the new station into the correct position.
# Removing an existing station needs to task for the name of the station and the route(s) that is appears on.
