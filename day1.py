#print numbers from 1 to N
'''def print_numbers(n):
    for i in range(1,n+1):
        print(i)
def main( ):
    n = int(input("Enter number: "))
    print_numbers(n)
if __name__ == "__main__":
    main( )'''

'''#sum of 1st n numbers
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def main():
    n = int(input("Enter number: "))
    result = calculate_sum(n)
    print("Sum of first", n, "numbers is:", result)
#if __name__ == "__main__": main()  this is optional
main()'''

'''def print_even(n):
    for i in range(1,n+1):
        if i %2==0:
            print(i)
def main():
    n= int(input("enter no:"))
    print_even(n)
main'''

'''i = 1
while i<= 5:
    print(i)
    i+=1'''

n=int(input())
i=1
while(i<=n):
    print(i)
    i+=1
    
