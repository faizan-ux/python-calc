def calculator(num1,num2,op):
    if(op=="+" or op=="-" or op=="*" or op=="/"):

        if(op=="+"):
            return num1+num2
        if(op=="-"):
            return num1-num2
        if(op=="*"):
            return num1*num2
        if(op=="/"):
            if(op=="/" and num2==0):
                return "Cannot divide by zero"
            else:
                return num1/num2
    else:
        return f"Invalid operator{op}"

FN = float(input("Enter first number"))
op = input("select operation : + , - , * , /")
SN = float(input("Enter second number"))
result = calculator(FN,SN,op)
print(result)

