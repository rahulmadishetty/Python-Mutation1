# sample.py

def add(a, b):
    return a + b

if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add(a, b)
    print(f"The result is {result}")