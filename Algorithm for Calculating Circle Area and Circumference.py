
```python
import math

def calc_circle(r):
    # check the radius its valid or not
    if r < 0:
        return "Can't have negative radius!"
    
    # formulas for circle 
    circ = 2 * math.pi * r  # circumference
    area = math.pi * r**2   # area
    
    return {"radius": r, "circ": circ, "area": area}

        # actually run the program
def main():
    try:
        r = float(input("What's the radius? "))
        result = calc_circle(r)
        
        if type(result) == str:  # check if we got an error
            print(result)
        else:
            print(f"\nOk, for radius {r}:")
            print(f"Circumference = {result['circ']:.4f}")
            print(f"Area = {result['area']:.4f}")
    
    except ValueError:
        print("That's not a number! Try again.")

if __name__ == "__main__":
    main()
```