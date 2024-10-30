from BFS import     SearcherBFS
from DFS import     SearcherDFS
from AStar import   SearcherAStar
from GBFS import    Gready


def printAlgorithm(searcher):
    for idx, state in enumerate(searcher.move(), 1):
        print(f"State {idx}:")
        print(f"  Stack_E: {state['Stack_E']}")
        print(f"  Stack_A_Odd: {state['Stack_A_Odd']}")
        print(f"  Stack_B_Even: {state['Stack_B_Even']}")
        print(f"  Stack_C_Odd: {state['Stack_C_Odd']}")
        print(f"  Stack_D_Even: {state['Stack_D_Even']}")
        print(f"  num_expanded: {state['num_expanded']}")
        print("-" * 40)


if __name__ == "__main__":
    algorithm = input("Enter which algorithm do you wanna use ? BFS/DFS/A*/GBFS :")
    #print(algorithm.upper())
    if algorithm.upper() == "BFS":
        print("_____________Breath First Algorithm_______________")
        problem = "Coins Arrangement Problem"
        solver = SearcherBFS(problem)
        solver.move()

    elif algorithm.upper() == 'DFS':
        print("____________Depth First Algorithm_______________")
        problem = None 
        searcher = SearcherDFS(problem)
        printAlgorithm(searcher) 

    elif algorithm.upper() == 'A*':
        print("_____________AStar Algorithm_______________")
        problem = "Coins Arrangement Problem"
        solver = SearcherAStar(problem)
        solver.move()
    
    elif algorithm.upper() == 'GBFS':
        print("_____________Gready Best First Algorithm_______________")
        problem = None 
        searcher = Gready(problem)
        printAlgorithm(searcher) 
    
    else:
        print("please input one of these options with correct spelling BFS/DFS/AStar/GBFS")
