''' Assignment by Robyn Keogh, C14354061
    GPS Unit for Hikers.
    Due date: 16/12/2015.
    Menu-driven program that allows users to:
    -View their current location.
    -View and input their own waypoints.
    -Save and retrieve named paths consisting of a sequence of waypoints.
    -Calculate the distance to a waypoint from the current location.
    -Calculate the direction as a compass bearing from the current location to a waypoint.
'''

import random
import math

waypoint_dic = {}  # dictionary to store user waypoints
paths = {}  # dictionary to store paths


def add_to_dict(long, lat, name):  # function that adds waypoints to a dictionary
    instance = Locations()
    instance.waypoints(long, lat, name)
    location = instance.waypoint_name
    location_coord = instance.waypoint_coord
    waypoint_dic[location] = location_coord  # adds the waypoint to the dictionary


class GetCurrentLocation(object):  # class that contains the method for getting the current location
    def current_location(self, long=0, lat=0):
        self.long = round(random.uniform(-11.0, -5.0), 2)  # generates random number and rounds to 2 DP
        self.lat = round(random.uniform(51.0, 55.0), 2)  # ranges for ireland
        self.CurrentLocation = (self.long, self.lat)
        add_to_dict(self.CurrentLocation[0], self.CurrentLocation[1], "CurrentLocation")  #adds current location to dict


class Locations(object):  # class that contains the layout/conversion info for the waypoints
    def waypoints(self, long=0, lat=0, name=' '):
        self.waypoint_coord = (float(long), float(lat))  # converts user input to floats
        self.waypoint_name = name


def get_waypoint():  # function that gets a location name and co-ordinates and checks they are valid
    user_name = input("Please enter the name of the location you wish to input: ")
    user_long = input("Please enter the longitude: ")
    user_lat = input("Please enter the latitude: ")
    user_name = str(user_name)
    user_long = float(user_long)
    user_lat = float(user_lat)
    user_input = True  # user input is assumed to be true

    if not -11.0 <= user_long <= -5.0:  # if the longitude co-ord is not between -11.0 and -5.0 user_input is false
        user_input = False
        print("Error! Please enter a valid Irish longitude co-ordinate.")

    if not 51.0 <= user_lat <= 55.0:  # if the latitude co-ord is not between 51.0 and 55.0 user_input is false
        user_input = False
        print("Error! Please enter a valid Irish latitude co-ordinate.")

    if user_input is True:  # if the input is still True, adds the waypoint to the dictionary
        add_to_dict(user_long, user_lat, user_name)
        print("{}: ({}, {}) was added to the dictionary.".format(user_name, user_long, user_lat))
        return user_name  # returns the waypoint name


def get_current_location():  # function that gets the current location using the class method GetCurrentLocation()
    instance = GetCurrentLocation()
    instance.current_location()
    CurrentLocation = instance.CurrentLocation
    return CurrentLocation  # returns the current location


def calc_distance(destination, current_location):  # function that calculates the distance and returns it
    #  calculate the distance
    #  formula = sqr((x2-x1)^2 + (y2-y1)^2)
    x1 = current_location[0]
    x2 = current_location[1]
    y1 = destination[0]
    y2 = destination[1]
    x_sqr = math.exp(x2 - x1)
    y_sqr = math.exp(y2 - y1)
    distance = round(math.sqrt(x_sqr + y_sqr), 2)
    return distance


def main():
    #
    # Main Menu
    #
    menu_choice = ""
    while menu_choice != "0":  # displays the menu until 0 is pressed and the program ends
        print("\n\tGPS Unit for Hikers.")
        print("-----------------------------------------")
        print("\tChoose an option")
        print("\t1. View the current location.")
        print("\t2. View or input waypoints.")
        print("\t3. Save and retrieve named paths consisting of a sequence of waypoints.")
        print("\t4. Calculate the distance to a waypoint from the current location.")
        print("\t5. Calculate the direction as a compass bearing from the current location to a given waypoint.")
        print("\t0. Exit")

        menu_choice = input("Enter your choice now: ")
        if (len(menu_choice) != 1) or (menu_choice not in "012345"):  # if error in choice input
            print("Error: You must enter a valid choice")

        elif menu_choice == "1":  # option 1 displays the current location to the user
            current_location = get_current_location()
            print("Current location: {}".format(current_location))

        elif menu_choice == "2":  # option 2 lets the user input and view waypoints to/from a dictionary
            print("Do you wish to: \n(a) View the location of an already inputted waypoint.\n(b) Add a new waypoint.")
            choice = input("Enter your choice now: ")
            if (len(choice) != 1) or (choice not in "ab"):
                print("Error! Please enter a valid choice!")

            elif choice == "a":  # View already inputted waypoints
                for keys, values in waypoint_dic.items():
                    print("{} : {}".format(keys, values))

            elif choice == "b":  # enter a new waypoint which will be saved to the dictionary
                get_waypoint()

        elif menu_choice == "3":  # option 3, save and retrieve named paths
            print("(a) View saved paths.")
            print("(b) Input and save a new path.")
            choice = input("Please select an option: ")
            if (len(choice) != 1) or (choice not in "ab"):
                print("Error! Please enter a valid choice!")

            elif choice == "a":  # view saved paths
                for keys, values in paths_dict.items():
                    print("{} : {}".format(keys, values))

            elif choice == "b":  # lets user input and save new paths to a dictionary
                paths_dict = dict()
                waypoint_list = []
                name = input("Please enter the path name: ")
                while True:
                    print("To add waypoints to this path, please enter the name from the list below (case-sensitive)")
                    for keys, values in waypoint_dic.items():  # prints the dictionary for user
                        print("{} : {}".format(keys, values))
                    waypoint = input(" ")
                    waypoint_list.append(waypoint)
                    answer = input("Do you wish to add another waypoint to this path? y/n : ")
                    if answer == "n":
                        break

                for key, values in waypoint_dic.items():  # adds the waypoint to the path if it's not already in it
                    if key in paths_dict:
                        pass
                    else:
                        paths_dict[key] = [values]
                print("You entered the path: {} containing the following waypoints: {}".format(name, paths_dict))

        elif menu_choice == "4":  # option 4, calculate the distance from the current location to a waypoint.
            print("To calculate the distance from the current location to a specific destination,")
            print("Please choose one of the following options: ")
            print("(a) Select a destination from the dictionary.")
            choice = input("(b) Input a new location and waypoint.")
            if (len(choice) != 1) or (choice not in "ab"):
                print("Error! Please enter a valid choice!")

            elif choice == "a":  # lets the user select a location from the dictionary
                get_current_location()
                for keys, values in waypoint_dic.items():  # prints the dictionary for user
                    print("{} : {}".format(keys, values))

                answer = input("Please enter a location from the list above (case-sensitive): ")
                destination = waypoint_dic[answer]
                current_location = waypoint_dic['CurrentLocation']

                distance = calc_distance(destination, current_location)
                print("The distance from the current location to {} is: {}".format(answer, distance))

            elif choice == "b":  # lets the user enter in a new waypoint/location
                get_current_location()
                name = get_waypoint()
                destination = waypoint_dic[name]
                current_location = waypoint_dic['CurrentLocation']

                distance = calc_distance(destination, current_location)
                print("The distance from the current location to {} is: {}".format(name, distance))

        elif menu_choice == "5":  # option 5, calculate the direction as a compass bearing from cur location to waypoint
            current_location = get_current_location()
            print("To calculate the direction from the current location to a waypoint, please enter a waypoint: ")
            name = get_waypoint()
            waypoint = waypoint_dic[name]

            # calculate the bearing
            y = math.sin(waypoint[0] - current_location[0]) * math.cos(waypoint[1])
            x = (math.cos(current_location[1]) * math.sin(waypoint[1])) - (
                math.sin(current_location[1]) * math.cos(waypoint[1]) * math.cos(waypoint[0] - current_location[0]))
            bearing = round(math.atan2(y, x), 2)
            print("The direction to {} from the current location is {} degrees.".format(name, bearing))
            print("End")

        elif menu_choice == "0":  # exits the program
            print("Thank you for using this program! Goodbye!")
            break


# To make program run from main() at beginning.
if __name__ == "__main__":
    main()
