###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """               
    # Create an empty list to store the trips
    trips = []
    
    # Create a copy of the cows dictionary sorted by weight in descending order
    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    
    # While there are cows that have not been transported
    while sorted_cows:
        # Create a new trip list
        trip = []
        
        # While the weight of the cows in the current trip is less than or equal to the weight limit of the spaceship
        total_weight = 0
        i = 0
        while i < len(sorted_cows):
            # Get the heaviest cow from the sorted cows list
            cow = sorted_cows[i]
            
            # If the cow's weight exceeds the remaining weight capacity of the spaceship, skip it
            if cow[1] > limit - total_weight:
                i += 1
                continue
            
            # Add the cow to the current trip list and subtract its weight from the remaining weight capacity of the spaceship
            trip.append(cow[0])
            total_weight += cow[1]
            
            # Remove the cow from the sorted cows list
            sorted_cows.pop(i)
        
        # Add the current trip list to the list of trips
        trips.append(trip)
    
    # Return the list of trips
    return trips
    #result = [] 
    
# Problem 2
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Create a list of cows sorted in decreasing order of weight
    cowsCopy = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    min_trips = None
    # Try all possible partitions of cows and find the one that minimizes the number of trips
    for partition in get_partitions(cowsCopy):
        valid_partition = True
        for trip in partition:
            total_weight = sum(cow[1] for cow in trip)
            if total_weight > limit:
                valid_partition = False
                break
        if valid_partition:
            if min_trips is None or len(partition) < len(min_trips):
                min_trips = partition
    return min_trips
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    # Test greedy algorithm
    start = time.time()
    greedy_result = greedy_cow_transport(cows, limit)
    end = time.time()
    greedy_time = end - start
    print(f"Greedy algorithm took {greedy_time:.6f} seconds and resulted in {len(greedy_result)} trips.")
    
    # Test brute force algorithm
    start = time.time()
    brute_force_result = brute_force_cow_transport(cows, limit)
    end = time.time()
    brute_force_time = end - start
    print(f"Brute force algorithm took {brute_force_time:.6f} seconds and resulted in {len(brute_force_result)} trips.")

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
print(compare_cow_transport_algorithms())


