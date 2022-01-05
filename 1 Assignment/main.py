import fsm
dfsm1 = fsm.dfsm() #creating a dfsm
no_of_testcase = int(input("Enter number of test cases : "))
for i in range(0, no_of_testcase):
    try:
        result = dfsm1.evaluate(input("Enter word for test case number " + str(i + 1) + " : "))
    except:
        result = 0
    if result:
        print("Accepted")
    else:
        print("Rejected")