def printSubsets(n):     
    for i in range(n + 1): 
          
        if ((n & i) == i): 
            print(i ," ", end = "") 
n =input()
printSubsets(n) 
