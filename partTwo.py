import math  

def main():
    A = int(input("Enter the length of side A\n"))
    B = int(input("Enter the length of side B\n"))
    pythag(A,B)

def pythag(A,B):
    C = (A**2)+(B**2)
    print("C squared is equal to", C)

main()
