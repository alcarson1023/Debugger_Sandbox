import math


def return_array(selections):

    return {'result': selections}

def sort_array(selections):

    sorted_data = sorted(selections)
    
    return {'result': sorted_data}


# For each current point, search in an expanding radius around that point until another point is found.
def nearest_point(selections):
    unused_points = selections
    chosen_path = []
# Initializing variables so nothing complains:
    current_point = unused_points[0]
    unused_points.remove(current_point) # One-time setup task, keeps us from dealing with it in the loops.
    chosen_path.append(current_point)
    potential_point = 'Placeholder' # Start this with a dummy value so it doesn't interfere with anything
    search_distance = 1 # This represents the RADIUS of the search grid.

    while len(unused_points) > 0 and search_distance < 10: # As long as there are still unused points, stay in the while loop.

# Each time this runs, it searches further out until a point is found (or we hit a radius of 10, meaning no point was found).
# Putting Y-axis in the outer loop so that it will run left > right, then top > bottom.
        while len(unused_points) > 0 and search_distance < 10:
            # R = Row position, C = Column position. So "34" is 4rd column, 5th row (since we start from 0)
            for r in range((search_distance * -1), search_distance + 1): # Search from -1 to +1, -3 to +3, and so on.
                if (int(current_point[1]) + r) < 0: # Skip any coordinates that are less than 0
                    continue
                for c in range((search_distance * -1), search_distance + 1):
                    if (int(current_point[0]) + c) < 0:
                        continue
                    
# I convert the string coordinates to numbers, modify them, then turn them back into strings. Skip the current run if it's the starting square.
                    potential_point = str((int(current_point[0]) + c)) + str((int(current_point[1]) + r))
# This breaks from the loop when a point is found, rather than finishing the loop and then breaking.
                    if potential_point in unused_points:
                        # When the next point is found: set it as current > remove it from unused list > add it to the path > reset search distance
                        current_point = potential_point
                        unused_points.remove(current_point)
                        chosen_path.append(current_point)
                        search_distance = 0 # Resets search distance each time a new point is found. Next line increase distance, so we start at 0                        
                        break

            search_distance += 1 # Increase the search radius if no matches are found.

    return {'result': chosen_path}

def pythagorean(selections):
    unused_points = selections
    chosen_path = []
# Initializing variables so nothing complains:
    current_point = unused_points[0]
    unused_points.remove(current_point) # One-time setup task, keeps us from dealing with it in the loops.
    chosen_path.append(current_point)



    while len(unused_points) > 0:
        distance_list = []

        for node in unused_points:
# Gather the distances between the current point and each node in the list along the X & Y axis
            ydistance = int(node[0]) - int(current_point[0])
            xdistance = int(node[1]) - int(current_point[1])
# Use the pythagorean theorem to find the distance between the two point
            distance = math.sqrt(ydistance**2 + xdistance**2)
# Add those distances to a list in order, then grab the node that shares an index with the shortest distance.
            distance_list.append(distance)

# Once the loop is finished, the index of the shortest distance will match the index of the closest node.
        index = distance_list.index(min(distance_list)) # Find the index of the shortest distance available
        closest_node = unused_points[index]
        current_point = closest_node
        unused_points.remove(current_point)
        chosen_path.append(current_point)

    return {'result': chosen_path}


def method_error(method, selections):
    return {'result': f'${method} is not a recognized function.'}