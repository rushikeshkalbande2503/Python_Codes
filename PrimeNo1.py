
if num > 1:
    for i in range(2,int(num/2)+1):
        if(num % i == 0):
            print(num,"Given no is not a prime number")
            break
    else:
        print(num," is prime number")
else:
    print(num," is prime number")
    
