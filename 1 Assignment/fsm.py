class dfsm:
    def __init__(self): #constructor for dfsm
        self.getTransitions()
        self.getInitialState()
        self.getFinalStates()

    def getInitialState(self):
        initial = int(input("Enter the start state : ")) #start state of the fsm
        self.initial = initial

    def getFinalStates(self):
        no_of_final_states = int(input("Enter number of final states : ")) 
        final = []
        for i in range(0, no_of_final_states):
            final.append(int(input("Enter the final states : "))) #set of final states
        self.final = final

    def getTransitions(self):
        no_of_symbols = int(input("Enter number of symbols in the language : ")) #number of elements in w
        symbols = []
        for i in range(0, no_of_symbols): #symbols in w
            symbols.append(input("Enter symbol " + str(i+1) + " : "))

        no_of_states = int(input("Enter number of states in fsm : ")) #number of states in fsm
        transitions = {} #declaring an empty transition
        for i in range(0, no_of_states):
            transitions[i] = {} #declaring an empty transition for ith state
            temp = {}
            for j in symbols:
                nextState = int(input("Enter next state from " + str(i) + " for the symbol '" + j + "' : "))
                temp.update( { j : nextState } ) #creating a temperory transition list for ith state
            transitions[i].update(temp) #updating transition for ith state
        self.transitions = transitions
    
    def evaluate(self, word): #evaluates the given word
        state = self.initial #initiating start state
        for c in word: #iterating through word
            state = self.transitions[state][c] #state transition
        return state in self.final #returns 1 if state is in final stat