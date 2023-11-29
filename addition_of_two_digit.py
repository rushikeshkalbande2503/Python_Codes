#addition
def add(n1,n2):
    return n1+n2

#substraction
def sub(n1,n2):
    return n1-n2

#multiplication
def mul(n1,n2):
    return n1*n2

#division
def div(n1,n2):
    return n1/n2

#creating the dictionary for operation
opreations= {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div

    }

num1=int(input("Whats the first number?: "))
num2=int(input("Whats the second number? "))

for symbol in opreations:
    print(symbol)
operation_symbol=input("Pick up operation from line above:")

calculation_function=opreations[operation_symbol]
answer= calculation_function(num1,num2)

print(f"{num1}{opreations}{num2}= {answer}")
    

