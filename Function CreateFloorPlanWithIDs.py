function createFloorPlanWithIDs(coordinates):
    # Find the dimensions of the floor plan
    maxX = findMaxCoordinate(coordinates, 'x')
    maxY = findMaxCoordinate(coordinates, 'y')
    # Initialize a 2D grid
    grid = initializeGrid(maxx, maxY)
    # Place rooms on the grid with unique IDs
    for roomId from 1 to length(coordinates):
        roomCoordinate = coordinates [roomId - 1]
        roomX = roomCoordinate.x
        roomy = roomCoordinate.y
        roomwidth = roomCoordinate.width
        roomHeight = roomCoordinate.height

        # Mark the cells corresponding to the room with its unique ID 
        markcellswithID(grid, roomx, roomy, roomwidth, roomHeight, roomId)
        
        return grid
        
# Function to mark cells with a unique room ID based on room coordinates 
function markCellswithID(grid, x, y, width, height, roomId):
        for i from x to (x + width 1):
            for j from y to (y + height - 1):
        |       grid[i][j] = roomId # Use the room ID as the unique identifier