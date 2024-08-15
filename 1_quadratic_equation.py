import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the nature of the roots
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return complex(real_part, imag_part), complex(real_part, -imag_part)

# Get input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Solve the equation
solutions = solve_quadratic(a, b, c)

# Print the results
print("The solutions are:")
for solution in solutions:
    print(solution)
