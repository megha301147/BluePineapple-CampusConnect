def print_perfect_nums(n):
    
    for i in range(1,n + 1):
        sum1 = 0
        cnt=0
        for x in range(1, i):
            cnt+1
            if(i % x == 0):
                sum1 = sum1 + x
                if (sum1 == i):
                    print(i)
    return(cnt)               
                              
n = int(input("Enter a number\t"))
cnt = print_perfect_nums(n)
if(cnt == 0):
            print ("No perfect no present between 1 to ",n)
                    
