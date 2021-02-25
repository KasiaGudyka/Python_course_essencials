# Calculating powers of pairs of non-negative numbers with executing an error if they're negative
class Calculator():
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("number and power should be non-negative")
        else:
            return n**p
        
myCalculator=Calculator()
T=int(input("How many pairs of numbers would you like to calculate? "))
for i in range(T):
    n,p = map(int, input("Insert a number and it\'s power: ").split())
    try:
        ans=myCalculator.power(n,p)
        print("The power of your numbers is:", ans)
    except Exception as e:
        print(e)
