import math

def shortest_path(M,start,goal):
    path_costs = {}
    est_dists = {}
    visited = []
    if not bool(isinstance(start, int)) or not bool(isinstance(goal, int)):
        return []
    for i, r in enumerate(M.roads):
        est_dists[i] = calc_distance(M.intersections[i], M.intersections[goal])
        for c in r:
            if i not in path_costs:
                path_costs[i] = {}
            path_costs[i][c] = calc_distance(M.intersections[i], M.intersections[c])

    start_heuristic = est_dists[start]
    state = start
    frontier = {
        start: {
            'path_cost': 0,
            'total': est_dists[start],
            'path': [start]
        }
    }
    while bool(frontier):
        if ( #goal test
               state == goal and 
               frontier[state]['total'] >= start_heuristic
        ):
            break
        frontier_state = frontier.pop(state)
        for i in M.roads[state]:
            if i in visited:
                continue
            path_cost = frontier_state['path_cost'] + path_costs[state][i]
            if i not in frontier or path_cost < frontier[i]['path_cost']:
                i_path = []
                i_path.extend(frontier_state['path'])
                i_path.append(i)
                frontier.update({
                    i: {
                        'path_cost': path_cost,
                        'total': path_cost + est_dists[i],
                        'path': i_path
                    }
                })
        visited.append(state)
        state = get_next_state(frontier)

    if bool(frontier):
        return frontier[state]['path']
    return []

#https://www.analyticsvidhya.com/blog/2020/02/4-types-of-distance-metrics-in-machine-learning/
#https://www.geeksforgeeks.org/a-search-algorithm/
# I am using Euclidean geometric distance formula d = sqrt((x2-x1)^2 + (y2-y1)^2))
# this distance formula gives us the true distance between two points (state + goal)
# the use case for this distance huestric is applicable when you can move in any direction.
# In our case we have a graph nodes and movement can be in any direction therefore
# it makes sense to use the euclidean distance as our heuristic

# There are two other distance formulae that can be used has heuristics
#   https://www.geeksforgeeks.org/a-search-algorithm/
#   - Manhattan distance or taxicab geometry which is the absolute distance between two points
#       d = |x1-x2| + |y1-y2|
#       * We would use this heuristic when we are allow to move only in four directions. In our case
#       this does not apply since we are allowed to move in any direction in the x,y plane.
#   - Diagonal distance which gives us the maximum absolute value of the 
#       differences between the current point C and goal point G expressed as
#       dx = abs(current_cell.x – goal.x)
#       dy = abs(current_cell.y – goal.y)
#       h = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
#       where D is length of each point
#       and D2 is diagonal distance between each point
#       * We would use this heuristric when we are allowed to move in eight directions only. In our case
#       this does not apply since we are allowed to move in any direction in the x,y plane
def calc_distance(p,q):
    return math.sqrt((q[0]-p[0])**2 + (q[1]-p[1])**2)

def get_next_state(frontier):
    min_path_cost = -1
    min_key = None
    for key, value in frontier.items():
        if min_path_cost == -1:
            min_path_cost = value['total']
            min_key = key
        elif min_path_cost > value['total']:
            min_path_cost = value['total']
            min_key = key
    return min_key
