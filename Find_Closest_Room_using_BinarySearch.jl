# Function to find the closest 3 rooms to the meeting location using binary search
function findclosestRoomsBinarySearch(sortedAvailableRooms, meetingLocation):
    closestRooms = [] # Initialize an empty list to store closest rooms

    # Binary search to find the initial room closest to the meeting location

    initialRoomIndex = binarySearch(sortedAvailableRooms, meetingLocation)

    # Check rooms around the initial room for the closest 3 rooms

    for i from max(0, initialRoomIndex - 1) to min(initialRoomIndex + 1,
    length(sortedAvailableRooms) - 1):
        closestRooms.append(sortedAvailableRooms[i])
        
    return closestRooms
  