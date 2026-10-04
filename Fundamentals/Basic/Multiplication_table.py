# Iterative Approach

def writetable(n):
    for i in range(1,10+1):
        print(f" {n} * {i} =  {i*n}")    

writetable(5)


# Recursive Approach 

def printtable(n,i=1):
    if(i==11):
        return
    
    print(f"{n} * {i} = ", n*i)
    i+=1
    printtable(n,i)

n = 5
printtable(n)

