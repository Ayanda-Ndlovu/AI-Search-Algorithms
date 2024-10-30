import heapq
from collections import deque

class SearcherAStar:
    def __init__(self, problem):
        self.problem = problem
        self.initial_state = (deque([1, 2, 3, 4, 5, 6, 7, 8]), [], [], [], [], 0)
        self.num_expanded = 0  
        self.frontier = [] 

    def heuristic(self, state):
        Queue_E = state[0]
        return len(Queue_E)  # The fewer coins left the closer we are to the goal

    def empty_stack(self, stack):
        return len(stack) == 0

    def add_to_stack(self, stack, coin):
        stack.append(coin)

    def is_even(self, node):
        return node % 2 == 0

    def is_odd(self, node):
        return node % 2 != 0

    def is_valid(self, coin, top_coin):
        return top_coin is not None and coin < top_coin

    def move(self):
        # adding an initial state into queue
        initial_Queue_E, initial_A, initial_B, initial_C, initial_D, initial_cost = self.initial_state
        heapq.heappush(self.frontier, (self.heuristic(self.initial_state), self.initial_state))

        while self.frontier:
            _, (Queue_E, Stack_A_Odd, Stack_B_Even, Stack_C_Odd, Stack_D_Even, g_cost) = heapq.heappop(self.frontier)

            if not self.empty_stack(Queue_E):
                coin = Queue_E.popleft() 
                self.num_expanded += 1 

                # Copying stacks for the next state
                new_A, new_B, new_C, new_D = list(Stack_A_Odd), list(Stack_B_Even), list(Stack_C_Odd), list(Stack_D_Even)

                # Evaluate odd numbers and add them to appropriate stacks
                if self.is_odd(coin):
                    if not self.empty_stack(Stack_A_Odd):
                        A_top_coin = Stack_A_Odd[-1]
                        if self.is_valid(coin, A_top_coin):
                            self.add_to_stack(new_A, coin)
                        else:
                            if not self.empty_stack(Stack_C_Odd):
                                C_top_coin = Stack_C_Odd[-1]
                                if self.is_valid(coin, C_top_coin):
                                    self.add_to_stack(new_C, coin)
                                else:
                                    if len(Stack_A_Odd) > 1 and len(Stack_C_Odd) > 1:
                                        A_top_coin = Stack_A_Odd[-1]
                                        C_top_coin = Stack_C_Odd[-1]
                                        if self.is_valid(A_top_coin, C_top_coin):
                                            new_C.append(Stack_A_Odd.pop())
                                        else:
                                            new_A.append(Stack_C_Odd.pop())
                                    if not self.empty_stack(Stack_A_Odd):
                                        new_A.append(coin)
                                    else:
                                        new_C.append(coin)
                            else:
                                new_C.append(coin)
                    else:
                        new_A.append(coin)

                # Evaluate even numbers and add them to appropriate stacks
                else:
                    if not self.empty_stack(Stack_B_Even):
                        B_top_coin = Stack_B_Even[-1]
                        if self.is_valid(coin, B_top_coin):
                            self.add_to_stack(new_B, coin)
                        else:
                            if not self.empty_stack(Stack_D_Even):
                                D_top_coin = Stack_D_Even[-1]
                                if self.is_valid(coin, D_top_coin):
                                    self.add_to_stack(new_D, coin)
                                else:
                                    if len(Stack_B_Even) > 1 and len(Stack_D_Even) > 1:
                                        B_top_coin = Stack_B_Even[-1]
                                        D_top_coin = Stack_D_Even[-1]
                                        if self.is_valid(B_top_coin, D_top_coin):
                                            new_D.append(Stack_B_Even.pop())
                                        else:
                                            new_B.append(Stack_D_Even.pop())
                                    if not self.empty_stack(Stack_B_Even):
                                        new_B.append(coin)
                                    else:
                                        new_D.append(coin)
                            else:
                                new_D.append(coin)
                    else:
                        new_B.append(coin)

                # a new state after move
                new_state = (Queue_E, new_A, new_B, new_C, new_D, g_cost + 1)  # Increasing g_cost by 1 for every move
                f_cost = g_cost + 1 + self.heuristic(new_state) 
                heapq.heappush(self.frontier, (f_cost, new_state))

                # Output state
                print(f"State {self.num_expanded}:")
                print(f"  Queue_E: {Queue_E}")
                print(f"  Stack_A_Odd: {new_A}")
                print(f"  Stack_B_Even: {new_B}")
                print(f"  Stack_C_Odd: {new_C}")
                print(f"  Stack_D_Even: {new_D}")
                print(f"  num_expanded: {self.num_expanded}")
                print("----------------------------------------")

def main():
    problem = "Coins Arrangement Problem"
    solver = SearcherAStar(problem)
    solver.move()

if __name__ == "__main__":
    main()
