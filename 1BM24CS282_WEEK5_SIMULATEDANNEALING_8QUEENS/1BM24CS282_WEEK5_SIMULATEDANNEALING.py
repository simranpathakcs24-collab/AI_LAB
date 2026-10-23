import math
import random

def calculateenergy(state):
    energy = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                energy += 1
    return energy
    
def getrandomswapneighbor(state):
    n = len(state)
    neighbor = list(state)
    i, j = random.sample(range(n), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def simulatedannealing(initial_state, t_init=10.0, alpha=0.995, t_min=0.001):
    current_state = list(initial_state)
    current_energy = calculateenergy(current_state)
    t = t_init
    iteration = 0
    print(f"Starting State: {current_state} | Initial Conflicts (Energy): {current_energy}\n")  
    while t > t_min:
        if current_energy == 0:
            break    
        iteration += 1
        neighbor = getrandomswapneighbor(current_state)
        neighbor_energy = calculateenergy(neighbor)     
        delta_e =  current_energy- neighbor_energy 
        if delta_e >=0:
            current_state = neighbor
            current_energy = neighbor_energy
        else:
            probability = math.exp(delta_e / t)
            if random.random() < probability:
                current_state = neighbor
                current_energy = neighbor_energy
        if current_energy == 0:
            print(f"Iteration {iteration:4d} | Temp: {t:6.4f} | Current Conflicts: {current_energy}")
        t *= alpha    
    print("\n")
    if current_energy == 0:
        print(f"SUCCESS! Found a solution in {iteration} iterations:")
        print(f"Final State Configuration: {current_state}")
        displayboard(current_state)
    else:
        print(f"TIMEOUT! System cooled down without finding a clean solution.")
        print(f"Final local minimum state: {current_state} with {current_energy} conflicts.")
def displayboard(state):
    n = len(state)
    for row in range(n):
        print(" ".join("Q" if state[col] == row else "." for col in range(n)))
if __name__ == "__main__":
    initial_configuration = list(range(8))
    random.shuffle(initial_configuration) 
    print("initial state: ")
    displayboard(initial_configuration)
    simulatedannealing(initial_configuration)

