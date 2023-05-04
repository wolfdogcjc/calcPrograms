import math

def solve_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    """
    Solve a triangle given two sides and one angle, or three sides.
    
    Parameters
    ----------
    a : float, optional
        Length of side a.
    b : float, optional
        Length of side b.
    c : float, optional
        Length of side c.
    A : float, optional
        Angle A in degrees.
    B : float, optional
        Angle B in degrees.
    C : float, optional
        Angle C in degrees.
    
    Returns
    -------
    sides : tuple of floats
        Tuple of side lengths (a, b, c).
    angles : tuple of floats
        Tuple of angles (A, B, C) in degrees.
    """
    # Check how many values are given
    known_values = sum(val is not None for val in (a, b, c, A, B, C))
    
    if known_values < 2:
        print("At least 2 values are needed to solve the triangle.")
        return
    
    if known_values == 2:
        # Two sides and one angle
        if A is not None:
            # Law of Cosines
            if a is None:
                a = (c**2 - b**2 - 2*b*c*math.cos(math.radians(A)))**0.5
            else:
                c = (a**2 + b**2 - 2*a*b*math.cos(math.radians(A)))**0.5
            # Law of Sines
            B = math.degrees(math.asin(a*math.sin(math.radians(A))/c))
            C = math.degrees(math.asin(b*math.sin(math.radians(A))/c))
        elif B is not None:
            # Law of Cosines
            if b is None:
                b = (c**2 - a**2 - 2*a*c*math.cos(math.radians(B)))**0.5
            else:
                c = (a**2 + b**2 - 2*a*b*math.cos(math.radians(B)))**0.5
            # Law of Sines
            A = math.degrees(math.asin(a*math.sin(math.radians(B))/c))
            C = math.degrees(math.asin(b*math.sin(math.radians(B))/c))
        elif C is not None:
            # Law of Cosines
            if c is None:
                c = (a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))**0.5
            else:
                a = (c**2 - b**2 - 2*b*c*math.cos(math.radians(C)))**0.5
            # Law of Sines
            A = math.degrees(math.asin(a*math.sin(math.radians(C))/c))
            B = math.degrees(math.asin(b*math.sin(math.radians(C))/c))
    elif known_values == 3:
        # Three sides
        # Law of Cosines
        A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
        C = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    
    return (a, b, c), (A, B, C)

solve_triangle(B=62, b=22.6)
