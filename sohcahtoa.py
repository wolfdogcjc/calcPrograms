import math

def solve_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    # Check how many values are given
    known_values = sum(val is not None for val in (a, b, c, A, B, C))

    if known_values < 2:
        print("At least 2 values are needed to solve the triangle.")
        return

    if known_values == 2:
        if a is not None and A is not None:
            # Solve for b and B using law of sines
            b = (a * math.sin(math.radians(B))) / math.sin(math.radians(A))
            B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))
            c = math.sqrt(a ** 2 + b ** 2)
            C = 180 - A - B
        elif b is not None and B is not None:
            # Solve for a and A using law of sines
            a = (b * math.sin(math.radians(A))) / math.sin(math.radians(B))
            A = math.degrees(math.asin(a * math.sin(math.radians(B)) / b))
            c = math.sqrt(a ** 2 + b ** 2)
            C = 180 - A - B
        elif c is not None and C is not None:
            # Solve for a and A using law of sines
            A = math.degrees(math.asin((a * math.sin(math.radians(C))) / c))
            a = (c * math.sin(math.radians(A))) / math.sin(math.radians(C))
            b = math.sqrt(c ** 2 - a ** 2)
            B = 180 - A - C

        # Ensure that one angle is 90 degrees
        if A == 90:
            B = 90 - C
            C = 90
        elif B == 90:
            A = 90 - C
            C = 90
        elif C == 90:
            A = 90 - B
            B = 90

    elif known_values >= 3:
        if c is None:
            # Solve for c using law of sines
            c = (a * math.sin(math.radians(C))) / math.sin(math.radians(A))
        if A is None:
            # Solve for A using law of sines
            A = math.degrees(math.asin((a * math.sin(math.radians(C))) / c))
        if B is None:
            # Solve for B using law of sines
            B = 180 - A - C
        if a is None:
            # Solve for a using law of sines
            a = (c * math.sin(math.radians(A))) / math.sin(math.radians(C))
            b = math.sqrt(c ** 2 - a ** 2)
            B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))

    if a is not None and A is not None:
        # Solve for b and B using law of sines
        if b is None:
            b = (a * math.sin(math.radians(B))) / math.sin(math.radians(A))
        if B is None:
            B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))
        c = math.sqrt(a ** 2 + b ** 2)
        C = 180 - A - B
    elif b is not None and B is not None:
        # Solve for a and A using law of sines
        if a is None:
            a = (b * math.sin(math.radians(A))) / math.sin(math.radians(B))
        if A is None:
            A = math.degrees(math.asin(a * math.sin(math.radians(B)) / b))
        c = math.sqrt(a ** 2 + b ** 2)
        C = 180 - A - B
    elif c is not None and C is not None:
        # Solve for a and A using law of sines
        if a is None:
            A = math.degrees(math.asin((a * math.sin(math.radians(C))) / c))
            a = (c * math.sin(math.radians(A))) / math.sin(math.radians(C))
            b = math.sqrt(c ** 2 - a ** 2)
        if A is None:
            A = math.degrees(math.asin((a * math.sin(math.radians(C))) / c))
        if B is None:
            B = 180 - A - C

        # Ensure that one angle is 90 degrees
        if A == 90:
            B = 90 - C
            C = 90
        elif B == 90:
            A = 90 - C
            C = 90
        elif C == 90:
            A = 90 - B
            B = 90


    # Print the results
    results = []
    if a is not None:
        results.append(f"a = {a:.2f}")
    if b is not None:
        results.append(f"b = {b:.2f}")
    if c is not None:
        results.append(f"c = {c:.2f}")
    if A is not None:
        results.append(f"A = {A:.2f}")
    if B is not None:
        results.append(f"B = {B:.2f}")
    if C is not None:
        results.append(f"C = {C:.2f}")
    print(", ".join(results))

# Example usage
solve_triangle(B=62, b=22.6)
