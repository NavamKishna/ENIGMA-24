import cmath

def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    if a==0:
        return 0
        
    # Check the discriminant to determine the nature of roots
    elif discriminant > 0:
        # Real and distinct roots
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f"{max(root1, root2):.2f} {min(root1, root2):.2f}"

    elif discriminant == 0:
        # Real and identical roots (double root)
        root = -b / (2*a)
        return f"{root:.2f} {root:.2f}"

    else:
        # Complex roots
        real_part = -b / (2*a)
        imag_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imag_part)
        return f"{root1.real:.2f}+{root1.imag:.2f}i {root1.real:.2f}-{root1.imag:.2f}i"
    
a,b,c=map(float,input().split())
print(quadratic_solver(a, b, c))