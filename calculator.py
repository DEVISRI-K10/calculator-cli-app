def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2==0:
        raise ValueError("cannot divide by zero")
    return n1/n2
def get_user_input():
    try:
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number:"))
        op=input("enter the operation(+,-,*,/):")
        if op not in['+','-','*','/']:
            raise ValueError("Invalid operation! use +,-,*,or/.")
        return num1,num2,op
    except ValueError as e:
        if "invalid literal" in str(e):
            print("error:please enter valid numbers.")
        else:
            print(f"error:{e}")
        return None
def calculate(num1,num2,op):
    operations={
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide
    }
    try:
        result=operations[op](num1,num2)
        return result
    except ValueError as e:
        print(f"error:{e}")
        return None
def main():
    print("Welcome to the CLI Calculator app")
    print("enter two numbers and an operation (+,-,*,/).")
    
    while True:
        user_input=get_user_input()
        if user_input is None:
            continue
        num1,num2,op=user_input
        result=calculate(num1,num2,op)

        if result is not None:
            print(f"result:{num1}{op}{num2}={result}")

        again=input("Do you want to perform another calculation?(yes/no):").lower()
        if again!='yes':
            print("Thank You for using the CLI Calculator app!")
            break
__name__=="__main__"
main()