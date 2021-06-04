def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
        
def func1():
    print("Hello, this is first python function.")
    
def func2():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))
    
    var3 = pow(var1,var2)
    print("Exp:",var3)
    
def func3(var1, var2):
    var3 = var1/var2
    print("Division:",var3)
    
def func4():
    var1 = int(input("Var1:"))
    var2 = int(input("Var2:"))
    
    var3 = var1 * var2
    return var3

def func5(var1,var2):
    var3 = var1 + var2
    return var3
