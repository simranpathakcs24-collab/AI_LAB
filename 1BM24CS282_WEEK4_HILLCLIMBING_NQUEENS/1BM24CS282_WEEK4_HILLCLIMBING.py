def calculate_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_best_swap_neighbor(state):
    n = len(state)
    current_cost = calculate_cost(state)
    
    best_state = None
    best_cost = current_cost
    best_pair = (float('inf'), float('inf')) 
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbor_cost = calculate_cost(neighbor)
            
            if neighbor_cost < best_cost:
                best_cost = neighbor_cost
                best_state = neighbor
                best_pair = (i, j)
            elif neighbor_cost == best_cost and neighbor_cost < current_cost:
                if (i, j) < best_pair:
                    best_state = neighbor
                    best_pair = (i, j)
                    
    return best_state, best_cost, best_pair

def run_hill_climbing_swaps(initial_state):
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    
    print(f"Initial State: {current_state} | Initial Cost: {current_cost}\n")
    display_board(current_state)
    
    step = 0
    while True:
        neighbor_state, neighbor_cost, swapped_pair = get_best_swap_neighbor(current_state)
        if neighbor_state is None or neighbor_cost >= current_cost:
            break
            
        step += 1
        print(f"Step {step}: Swapped rows {swapped_pair} -> New State: {neighbor_state} | Cost: {neighbor_cost}")
        display_board(neighbor_state)
        
        current_state = neighbor_state
        current_cost = neighbor_cost
        
    if current_cost == 0:
        print(f"\n Success! Goal configuration reached: {current_state}")
    else:
        print(f"\n Algorithm terminated. Stuck in a local optimum at state {current_state} with cost {current_cost}.")

def display_board(state):
    n = len(state)
    for row in range(n):
        print(" ".join("Q" if state[row] == col else "." for col in range(n)))

if __name__ == "__main__":
    initial_configuration = [3, 1, 2, 0]
    run_hill_climbing_swaps(initial_configuration)
