def input_values():
    a = float (input("Enter first value "))
    b = float(input("Enter second value "))
    return (a,b)

def suma ():
    x , y = input_values()
    return x+y

def suba ():
    x, y = input_values()
    return x-y

def diva ():
    x, y = input_values()
    return x // y

def mula ():
    x, y = input_values()
    return x * y
def error_handler():
    print ("Operation not found you dumbfuck")

name = input("Enter your name ")
print ("Hello " + name.upper() + ", Your name is now Zakir Naik")
choose =int(input("Enter choice [1] Add [2] Subtract [3] Divide [4] Multiply "))
# allmyshen = [suma,suba, diva, mula]
# output = allmyshen[choose-1]()
choices  = {
    1: suma,
    2: suba,
    3: diva,
    4: mula
}
output = choices.get(choose,error_handler)()
print("The output is " +str(output))
