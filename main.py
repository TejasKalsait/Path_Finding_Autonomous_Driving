import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument("--map", "-m", type = str, default = "map1", help = "Location of the map image")
# parser.add_argument("--startX", "-sx", type = float, default = "50", help = "Integer value of strating X position")
# parser.add_argument("--startY", "-sy", type = float, default = "50", help = "Integer value of strating Y position")
# parser.add_argument("--goalX", "-gx", type = float, default = "500", help = "Integer value of goal X position")
# parser.add_argument("--goalY", "-gy", type = float, default = "400", help = "Integer value of goal Y position")

# args = parser.parse_args()

map_img = cv.imread("maps/" + sys.argv[1] + ".png")

max_x = map_img.shape[1]
max_y = map_img.shape[0]

startx = int(sys.argv[2])
starty = int(sys.argv[3])

goalx = int(sys.argv[4])
goaly = int(sys.argv[5])

starting_point = (startx, starty, 0)
goal_point = (goalx, goaly)



# plt.imshow(map_img)
# print("Showing the initial map")
# plt.show()



print("Max area is (X, Y) =", (max_x, max_y))

example_x = 513
example_y = 403

# print(map_img.max(), map_img.min())

#print("example point value", map_img[example_y][example_x][0])

# if map_img[example_y][example_x][0] == 0:
#     print("Example point is in black region")
# else:
#     print("Example point is in white region")
    
    
# Draw the starting point and the ending points

#print("Shape of the map is", map_img.shape)

# plt.imshow(map_img)
# print("Showing the initial map with start and goal")
# plt.show()

class RandomTree():
    
    def __init__(self, starting_point) -> None:
        
        self.start_x = starting_point[0]
        self.start_y = starting_point[1]
        
        self.tree = {starting_point[2] : []}
        
        self.location_map = {starting_point[2] : (self.start_x, self.start_y)}
        
    def addtotree(self, point):
        
        point_x = point[0]
        point_y = point[1]
        point_id = point[2]
        
        self.tree[point_id] = []
        
        self.location_map[point_id] = (point_x, point_y)
        
    def addalink(self, id_1, id_2, dist):       #(self, to, from)
        
        # point1_id = point1[2]
        # point2_id = point2[2]
        
        
        # If the assertion fails, then print the Tree
        assert id_1 in self.tree and id_2 in self.tree, "Assertion Failed so printing the tree and then location map" + "\n" + str(self.tree) + "\n" + str(self.location_map)
        
        self.tree[id_1].append((id_2, dist))
        #self.tree[id_2].add((id_1, dist))
        

def draw_path(map_img, new_node, goal_node):
    
    print("Finding the optimal path")
    
    map_img = cv.line(map_img, (new_node[0], new_node[1]), (goal_node[0], goal_node[1]), (255, 0, 0), 2)
    
    new_node_id = new_node[2]
    #print("Tree looks like", random_tree.tree)
    
    while new_node_id != 0:
        
        parent_node = random_tree.tree[new_node_id]     # Tuple of (parent node id, distance)
        #print("New node id is", new_node_id, "Parent node looks like", parent_node)
        parent_node_id = parent_node[0][0]
        parent_node_dist = parent_node[0][1]
        
        #print("Drawing line between nodes", new_node_id, "and", parent_node_id)
        
        map_img = cv.line(map_img, (random_tree.location_map[new_node_id][0], random_tree.location_map[new_node_id][1]), (random_tree.location_map[parent_node_id][0], random_tree.location_map[parent_node_id][1]), (255, 0, 0), 2)
    
        new_node_id = parent_node_id
        
    return map_img

        
print("Initializing the tree and location map")

random_tree = RandomTree(starting_point)

#print("Tree looks like", random_tree.tree)
#print("Location map looks like", random_tree.location_map)


# Obstacle map

obstacle_map = []
print("Building the obstacle map")

for i in range(map_img.shape[0]):
    for j in range(map_img.shape[1]):
        
        if map_img[j][i][0] == 0:
            obstacle_map.append([i, j])


#print("Obstacle Map's length is", len(obstacle_map))
#print("Last obstacle location", obstacle_map[-1])

# plt.imshow(map_img)
# print("Testing before obstacles")
# plt.show()

# Testing the obstacle map

# Testing the 

# for obs in obstacle_map:
    
#     tempx = obs[0]
#     tempy = obs[1]
    
    #map_img = cv.circle(map_img, (tempx, tempy), 1, (255, 0, 0), 1)
    
map_img = cv.circle(map_img, (starting_point[0], starting_point[1]), 5, (0, 0, 255), 5)
map_img = cv.circle(map_img, (goal_point[0], goal_point[1]), 5, (0, 0, 255), 5)
    

# plt.imshow(map_img)
# print("Testing obstacles")
# plt.show()
    
    
# Testing the RandomTree class
test_tree = False

if test_tree == True:
    testing_point = (300, 400, 1)
    random_tree.addtotree(testing_point)
    random_tree.addalink(starting_point[2], testing_point[2])
    
    map_img = cv.circle(map_img, (testing_point[0], testing_point[1]), 2, (255, 0, 0), 5)

    print("After testing, tree looks like", random_tree.tree)
    print("After testing, location map looks like", random_tree.location_map)
    
    randx = np.random.randint(low = 0, high = max_x)
    randy = np.random.randint(low = 0, high = max_y)
    
    count = 2
    
    new_rand_point = (randx, randy, count)
    
    print("Random generator", randx, randy)
    
    map_img = cv.circle(map_img, (new_rand_point[0], new_rand_point[1]), 2, (255, 255, 0), 5)
    
    
    
    print("New Random point is", new_rand_point)
    
    min_temp_dist = float('inf')
    min_id = -1
    
    for k, v in random_tree.tree.items():
        
        # if k == count:
        #     continue
        print(random_tree.location_map[k][0])
        print(random_tree.location_map[k][1])
        #temp_dist = np.linalg.norm(np.array((new_rand_point[0], random_tree.location_map[k][0])) - np.array((new_rand_point[1], random_tree.location_map[k][1])))
        x2_m_x1 = np.power(new_rand_point[0] - random_tree.location_map[k][0], 2)
        y2_m_y1 = np.power(new_rand_point[1] - random_tree.location_map[k][1], 2)
        temp_dist = np.sqrt(x2_m_x1 + y2_m_y1)
        
        print("Distance is", temp_dist)
        
        if temp_dist < min_temp_dist:
            min_temp_dist = temp_dist
            min_id = k
    
    print("ID of the nearest node is", min_id)
    print("Distance between nearest node and random point is", min_temp_dist)
    
    active_node_id = min_id
    
    active_node = (int(random_tree.location_map[active_node_id][0]), int(random_tree.location_map[active_node_id][1]), active_node_id)
    
    
    # new node between active node and random point
    
    new_node_x = (new_rand_point[0] + random_tree.location_map[active_node_id][0]) / 2
    new_node_y = (new_rand_point[1] + random_tree.location_map[active_node_id][1]) / 2
    
    # if map_img[new_node_y][new_node_x][0] == 0:
        
    #     # That means black region
    #     continue
    
    new_node = (int(new_node_x), int(new_node_y), count)
    print("New node location is", new_node)
    
    map_img = cv.circle(map_img, (int(new_node_x), int(new_node_y)), 1, (255, 0, 0), 3)
    
    # EQUATION OF LINE
    
    x1 = new_node[0]
    y1 = new_node[1]
    
    x2 = active_node[0]
    y2 = active_node[1]
    
    slope = (y2 - y1) / (x2 - x1)
    
    y_intercept = y2 - (slope * x2)
    
    print("Slope and Y-Intercept are", slope, y_intercept)
    
    # Obstacle between active node and new node
    
    low_lim = 0.995
    high_lim = 1.015
    
    for points in obstacle_map:
        
        x_point = points[0]
        y_point = points[1]
        
        # Condition of limit check
        if (x_point > max(active_node[0], new_node[0]) or x_point < min(active_node[0], new_node[0])) or (y_point > max(active_node[1], new_node[1]) or y_point < min(active_node[1], new_node[1])):
            print("Obstacle is outside the two nodes so ignoring it")
            continue
        
        
    
        if ((slope * x_point) + y_intercept) / y_point > low_lim and ((slope * x_point) + y_intercept) / y_point < high_lim:
            
            print("There is obstacle in the middle")
            print("Value is", ((slope * x_point) + y_intercept) / y_point)
            # Two lines debug 
            # Line between obstacle and new node
            map_img = cv.line(map_img, (x_point, y_point), (new_node[0], new_node[1]), (0, 0, 255), 2)
            # Line between active node and new node
            map_img = cv.line(map_img, (active_node[0], active_node[1]), (new_node[0], new_node[1]), (255, 0, 255), 2)
            
            # plt.imshow(map_img)
            # print("DEBUGGGGG")
            # plt.show()
            
            
        
    
    
    plt.imshow(map_img)
    plt.show()
    
    # cv.imshow("Final Output", map_img)
    # cv.waitKey(0)
    
    # cv.destroyAllWindows()
    
    

path_found = False
# This is the count for ID of the node
# It will incremenent with every node
count = 1

dist_threshold = 200

print("Building the Rapidly-exploring Random Tree")

while not path_found:
    
    # Taking a random point
    # And I have compensated for the x and y interchange
    randx = np.random.randint(low = 0, high = max_x)
    randy = np.random.randint(low = 0, high = max_y)
    
    
    #print("New Random number is", new_rand_point)
    if map_img[randy][randx][0] == 0:
        
        # That means black region
        continue
    
    # Random poinnt generate din the white region
    
    new_rand_point = (randx, randy, count)
    count += 1
    
    min_temp_dist = float('inf')
    
    # Find the nearest node from the new point
    
    for k, v in random_tree.tree.items():
        
        # Basically here the key is an ID of the node
        # Value is the set of connected nodes
        
        x2_m_x1 = np.power(new_rand_point[0] - random_tree.location_map[k][0], 2)
        y2_m_y1 = np.power(new_rand_point[1] - random_tree.location_map[k][1], 2)
        temp_dist = np.sqrt(x2_m_x1 + y2_m_y1)
        
        if temp_dist < min_temp_dist:
            min_temp_dist = temp_dist
            min_id = k
            
    if min_temp_dist > dist_threshold:
        # Starting over
        continue
    
            
    active_node_id = min_id
    #print("Active node is", active_node_id)
    
    active_node = (int(random_tree.location_map[active_node_id][0]), int(random_tree.location_map[active_node_id][1]), active_node_id)
    
    
    new_node_x = (new_rand_point[0] + random_tree.location_map[active_node_id][0]) / 2
    new_node_y = (new_rand_point[1] + random_tree.location_map[active_node_id][1]) / 2
    
    new_node = (int(new_node_x), int(new_node_y), count)
    
    if map_img[new_node[1]][new_node[0]][0] == 0:
        
        # That means black region
        continue
    
    # Equation of line between active node and new node
    
    x1 = new_node[0]
    y1 = new_node[1]
    
    x2 = active_node[0]
    y2 = active_node[1]
    
    if x2 - x1 == 0.0:
        continue
    
    slope = (y2 - y1) / (x2 - x1)
    
    y_intercept = y2 - (slope * x2)
    
    #print("Slope and Y-Intercept of active-new line are", slope, y_intercept)
    
    
    # HAVE TO CHECK IF THERE IS NO OBSTACLE BETWEEEN ACTIVE NODE AND NEW_NODE
    
    
    # Basically rhe tolerance for line intersection
    low_lim = 0.98
    high_lim = 1.02
    
    obstacle_found = False
    
    #print("Finding if there is obstacle between active and new nodes")
    
    for points in obstacle_map:
        
        x_point = points[0]
        y_point = points[1]
        
        if (x_point > max(active_node[0], new_node[0]) or x_point < min(active_node[0], new_node[0])) or (y_point > max(active_node[1], new_node[1]) or y_point < min(active_node[1], new_node[1])):
            # print("Obstacle is outside the two nodes so ignoring it")
            continue
        
    
        if ((slope * x_point) + y_intercept) / y_point > low_lim and ((slope * x_point) + y_intercept) / y_point < high_lim:
        #print("This is the obstacle tolerance value", ((slope * x_point) + y_intercept) / y_point)
        #print("There is obstacle in the middle, hence breaking")
            obstacle_found = True
            break
            
    
    if obstacle_found:
        #print("Breaking because found abstacle between two nodes")
        continue
    
    map_img = cv.rectangle(map_img, (new_node[0] - 2, new_node[1] - 2), (new_node[0] + 2, new_node[1] + 2), (0, 0, 255), -1)
    
    # Add to the tree and add connection
    
    random_tree.addtotree(new_node)
    random_tree.addalink(new_node[2], active_node_id, min_temp_dist)
    #print("New node added successfully")
    
    # Drawing link lines
    
    map_img =  cv.line(map_img, (int(new_node[0]), int(new_node[1])), (random_tree.location_map[active_node_id][0], random_tree.location_map[active_node_id][1]), (0, 255, 0), 1)
    
    # if count == 50:
    #     break
    
    # Equation of line between goal node and new node
    #(using the same equations)
    
    x1 = goal_point[0]
    y1 = goal_point[1]
    
    x2 = new_node[0]
    y2 = new_node[1]
    
    if x2- x1 == 0.0:
        continue
    
    slope = (y2 - y1) / (x2 - x1)
    
    y_intercept = y2 - (slope * x2)
    
    #print("Slope and Y-Intercept of goal-new line are", slope, y_intercept)
    
    # HAVE TO CHECK IF THE NEW NODE CAN BE CONNECTED TO GOAL
    
    low_lim = 0.98
    high_lim = 1.02
    
    obstacle_found = False
    
    for points in obstacle_map:
        
        x_point = points[0]
        y_point = points[1]
        
        if (x_point > max(goal_point[0], new_node[0]) or x_point < min(goal_point[0], new_node[0])) or (y_point > max(goal_point[1], new_node[1]) or y_point < min(goal_point[1], new_node[1])):
            #print("Obstacle is outside the two nodes GOAL so ignoring it")
            continue
        
    
        if ((slope * x_point) + y_intercept) / y_point > low_lim and ((slope * x_point) + y_intercept) / y_point < high_lim:
            
            obstacle_found = True
            #print("Cannot reach goal (0.99<gt<1.01))", ((slope * x_point) + y_intercept) / y_point)
            
            # Cannot reach the goal from this new point
            #print("This is the goal tolerance value (0.99<gt<1.01))", ((slope * x_point) + y_intercept) / y_point)
            
            break
            
            
    if not obstacle_found:
        print("Finished Building the Rapidly-exploring Random Tree")
        path_found = True
        #map_img =  cv.line(map_img, (new_node[0], new_node[1]), (goal_point[0], goal_point[1]), (0, 255, 0), 2)
        #print("Location map looks like", random_tree.location_map, "\n")
        #print("Tree looks like", random_tree.tree)

        map_img = draw_path(map_img, new_node, goal_point)
        
    # if count % 5 == 0:
    #     plt.imshow(map_img)
    #     plt.show()
        
        
            
    
    # Checking if the distance between new point and the goal point is less
    
    # x2_m_x1 = np.power(new_node[0] - goal_point[0], 2)
    # y2_m_y1 = np.power(new_node[1] - goal_point[1], 2)
    # temp_dist = np.sqrt(x2_m_x1 + y2_m_y1)
    
    # if temp_dist < 30.0:
    #     path_found = True
    #     # This will break the loop

# plt.imshow(map_img)
# print("Showing the final map")
# plt.show()
#print(sys.argv[1])
cv.imwrite(sys.argv[1] + ".png", map_img)

cv.imshow("Final Output", map_img)
#print("Tree looks like", random_tree.tree)
cv.waitKey(0)
    
cv.destroyAllWindows()