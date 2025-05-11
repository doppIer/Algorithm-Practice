```python
def find_smallest_of_four():
        # Take the numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        
        # Find the smallest number
        smallest = num1
        
        if num2 < smallest:
            smallest = num2
            
        if num3 < smallest:
            smallest = num3
            
        if num4 < smallest:
            smallest = num4
            
        # show therresult
        print(f"The smallest number is: {smallest}")
        return smallest
        
    except ValueError:
        print("Please enter valid numbers only")

        # Run algorithm
if __name__ == "__main__":
    find_smallest_of_four()