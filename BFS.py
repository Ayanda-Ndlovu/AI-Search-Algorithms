
class SearcherBFS:
    def __init__(self, problem):
        self.problem = problem
        self.Stack_E = [1, 2, 3, 4, 5, 6, 7, 8] 
        self.Stack_A_Odd = []
        self.Stack_C_Odd = [] 
        self.Stack_B_Even = []
        self.Stack_D_Even = []
        self.num_expanded = 0

    def empty_stack(self, stack):
        return len(stack) == 0

    def add_to_stack(self, stack, coin):
        stack.append(coin)

    def is_even(self, node):
        return node % 2 == 0

    def is_odd(self, node):
        return node % 2 != 0

    def is_valid(self, coin, top_coin):
        return coin < top_coin

    def move(self):
        while not self.empty_stack(self.Stack_E):
            coin = self.Stack_E.pop(0)  # Get the top coin from Stack_E
            self.num_expanded += 1
            
            # evaluating odd numbers and adding them to appropriate Stacks
            if self.is_odd(coin):
                if not self.empty_stack(self.Stack_A_Odd):  # Checking if Stack_A_Odd is available and valid
                    A_top_coin = self.Stack_A_Odd[-1] 
                    if self.is_valid(coin, A_top_coin):
                        self.add_to_stack(self.Stack_A_Odd, coin)
                    else:
                        if not self.empty_stack(self.Stack_C_Odd): # Checking if Stack_C_Odd is available and valid
                            C_top_coin = self.Stack_C_Odd[-1]
                            if self.is_valid(coin, C_top_coin): 
                                self.add_to_stack(self.Stack_C_Odd, coin)
                            else:
                                #--------------------------- if both A and C are not valid then move coins between the even stacks of A and C
                                if len(self.Stack_A_Odd) > 1 and len(self.Stack_C_Odd) > 1:
                                    A_top_coin = self.Stack_A_Odd[-1]
                                    C_top_coin = self.Stack_C_Odd[-1]
                                    if A_top_coin < C_top_coin:
                                        self.add_to_stack(self.Stack_A_Odd, self.Stack_C_Odd.pop())
                                    else:
                                        self.add_to_stack(self.Stack_C_Odd, self.Stack_A_Odd.pop())
                                self.add_to_stack(self.Stack_A_Odd if len(self.Stack_A_Odd) == 0 else self.Stack_C_Odd, coin)
                                #--------------------------------------------------------------
                        else:
                            self.add_to_stack(self.Stack_C_Odd, coin)
                else:
                    self.add_to_stack(self.Stack_A_Odd, coin)

            # evaluating even numbers and adding them to appropriate Stacks
            else:
                if not self.empty_stack(self.Stack_B_Even):  # if B is not empty check if valid and add
                    B_top_coin = self.Stack_B_Even[-1]
                    if self.is_valid(coin, B_top_coin):
                        self.add_to_stack(self.Stack_B_Even, coin)
                    else:
                        if not self.empty_stack(self.Stack_D_Even): # if B is not valid and D is valid put in D
                            D_top_coin = self.Stack_D_Even[-1]
                            if self.is_valid(coin, D_top_coin):
                                self.add_to_stack(self.Stack_D_Even, coin)
                            else:
                                #----------------------------if both B and D are not valid oves then move between the even stacks of B and D
                                if len(self.Stack_B_Even) > 1 and len(self.Stack_D_Even) > 1:
                                    B_top_coin = self.Stack_B_Even[-1]
                                    D_top_coin = self.Stack_D_Even[-1]
                                    if B_top_coin < D_top_coin:
                                        self.add_to_stack(self.Stack_B_Even, self.Stack_D_Even.pop())
                                    else:
                                        self.add_to_stack(self.Stack_D_Even, self.Stack_B_Even.pop())

                                self.add_to_stack(self.Stack_B_Even if len(self.Stack_B_Even) == 0 else self.Stack_D_Even, coin)
                                #--------------------------------------------------
                        else:
                            self.add_to_stack(self.Stack_D_Even, coin) #nif D is empty then add
                else:
                    self.add_to_stack(self.Stack_B_Even, coin) # if B is empty then just add

            # output state
            print(f"State {self.num_expanded}:")
            print(f"  Stack_E: {self.Stack_E}")
            print(f"  Stack_A_Odd: {self.Stack_A_Odd}")
            print(f"  Stack_B_Even: {self.Stack_B_Even}")
            print(f"  Stack_C_Odd: {self.Stack_C_Odd}")
            print(f"  Stack_D_Even: {self.Stack_D_Even}")
            print(f"  num_expanded: {self.num_expanded}")
            print("----------------------------------------")
