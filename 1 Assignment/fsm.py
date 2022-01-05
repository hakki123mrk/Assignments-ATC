class dfsm:
    def __init__(self, transitions, initial, final): #constructor for dfsm
        self.transitions = transitions
        self.initial = initial
        self.final = final

    def evaluate(self, word): #evaluates the given word
        state = self.initial #initiating start state
        for c in word: #iterating through word
            state = self.transitions[state][c] #state transition
        return state in self.final #returns 1 if state is in final state

def getTransitions():
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
    return transitions

transitions = getTransitions()
initial = int(input("Enter the start state : ")) #start state of the fsm
no_of_final_states = int(input("Enter number of final states : ")) 
final = []
for i in range(0, no_of_final_states):
    final.append(int(input("Enter the final states : "))) #set of final states

dfsm1 = dfsm(transitions, initial, final) #creating a dfsm
no_of_testcase = int(input("Enter number of test cases : "))
for i in range(0, no_of_testcase):
    try:
        result = dfsm1.evaluate(input("Enter word for test case number " + str(i) + " : "))
    except:
        result = 0
    if result:
        print("Accepted")
    else:
        print("Rejected")