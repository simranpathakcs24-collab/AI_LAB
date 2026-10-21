import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state      
        self.parent = parent    
        self.action = action   
        self.g = g              
        self.h = h              
        self.f = g + h          

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    r, c = idx // 3, idx % 3
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]   
    for dr, dc, action in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_list = list(state)
            new_list[idx], new_list[n_idx] = new_list[n_idx], new_list[idx]
            neighbors.append((tuple(new_list), action))
    return neighbors

def h_manhattan(state, goal):
    dist = 0
    for i, val in enumerate(state):
        if val != 0:
            g_idx = goal.index(val)
            r1, c1 = i // 3, i % 3
            r2, c2 = g_idx // 3, g_idx % 3
            dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def a_star_search(start, goal, heuristic_fn):
   
    start_node = Node(start, g=0, h=heuristic_fn(start, goal))
    open_list = [start_node]
    closed_set = set()
    nodes_expanded = 0
    
    while open_list:
        current = heapq.heappop(open_list)
        nodes_expanded += 1
        
        if current.state == goal:
            path = []
            while current:
                path.append((current.state, current.action))
                current = current.parent
            return path[::-1], nodes_expanded
            
        closed_set.add(current.state)
        
        for n_state, action in get_neighbors(current.state):
            if n_state in closed_set:
                continue
                
            g_new = current.g + 1
            h_new = heuristic_fn(n_state, goal)
            neighbor = Node(n_state, current, action, g_new, h_new)
            heapq.heappush(open_list, neighbor)
            
    return None, nodes_expanded

def print_solution(path, nodes_expanded, heuristic_name):
    print(f"\nusing {heuristic_name}")
    print(f"Total nodes expanded: {nodes_expanded}")
    print(f"Solution steps (Total moves: {len(path) - 1}):")
    for state, action in path:
        action_str = f"Initial State" if action is None else f"Move: {action}"
        print(f"{action_str}")
        print(f"{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")

initial_board = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal_board    = (1, 2, 3, 4, 5, 6, 7, 8, 0)

path_manhattan, expanded_manhattan = a_star_search(initial_board, goal_board, h_manhattan)
print_solution(path_manhattan, expanded_manhattan, "Manhattan Distance Heuristic")
