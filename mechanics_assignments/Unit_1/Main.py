import math
import sympy as sp
from sympy.abc import alpha
import re
import matplotlib.pyplot as plt
import numpy as np
#Checking if my idiotic github thing w dgfdgfdg dsfgfdgfdg hatever is working why is my dad forcing me to do this and die


def create_graph(R, theta, force_length):
    circle_center = (0, 0)
    theta = np.radians(theta)

    # Calculate points
    A = (R * np.cos(theta), R * np.sin(theta))  # Point A on circumference
    M = (R * np.cos(theta) / 2, 0)  # Point M on x-axis
    B = (R, 0)  # Point B on the circumference and x-axis

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    circle = plt.Circle(circle_center, R, color='lightgray', alpha=0.5)
    ax.add_artist(circle)

    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)

    ax.text(1.2, -0.1, 'x', fontsize=12, ha='center')
    ax.text(-0.1, 1.2, 'y', fontsize=12, va='center')

    ax.plot([0, A[0]], [0, A[1]], color='gray', linestyle='--')
    ax.plot([A[0], M[0]], [A[1], M[1]], color='gray', linestyle='--')
    extension_length = 0.75
    extension_end = (A[0] + extension_length * np.cos(theta), A[1] + extension_length * np.sin(theta))
    ax.plot([A[0], extension_end[0]], [A[1], extension_end[1]], color='black', linestyle='-')

    ax.arrow(
        A[0],
        A[1],
        (extension_length) * np.cos(theta),
        (extension_length) * np.sin(theta),
        head_width=0.05,
        head_length=0.1,
        fc='black',
        ec='black'
    )

    ax.text(A[0], A[1], 'A', fontsize=12, ha='right')
    ax.text(M[0], M[1], 'M', fontsize=12, ha='left')
    ax.text(B[0], B[1], 'B', fontsize=12, ha='left')
    ax.text(M[0] / 2, M[1] - 0.1, 'R/2', fontsize=10, ha='center', va='center')
    ax.text((M[0] + B[0]) / 2, (M[1] + B[1]) / 2, 'R/2', fontsize=10, ha='center', va='top')
    ax.text(0.292, 0.123, 'θ', fontsize=10, ha='right', va='bottom')

    ax.text(extension_end[0] + 0.1, extension_end[1] + 0.1, 'F', fontsize=12, ha='left')
    ax.text(0, 0, 'O', fontsize=12, ha='right', va='top')

    ax.set_aspect('equal', adjustable='datalim')
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show(block=True)
def replace_expression(expr, F_val=None, R_val=None, theta_val=None):
    """
    Replace 'F', 'R', and 'theta' with the appropriate numeric or symbolic values
    using regex to capture the terms dynamically.
    """
    if F_val is not None:
        expr = re.sub(r'(\d*)F', lambda m: f"{F_val * (int(m.group(1)) if m.group(1) else 1)}", expr)

    if R_val is not None:
        expr = re.sub(r'(\d*)R', lambda m: f"{R_val * (int(m.group(1)) if m.group(1) else 1)}", expr)

    if theta_val is not None:
        expr = re.sub(r'(\d*)theta', lambda m: f"{theta_val * (int(m.group(1)) if m.group(1) else 1)}", expr)

    return expr

def check_input(params):
    """
    Convert inputs to SymPy symbolic expressions or numerical values.
    """
    if isinstance(params['Force'], str):
        try:
            force_expr = params['Force']
            params['Force'] = float(eval(replace_expression(force_expr, params['Force'], params['R'], params['theta'])))
        except:
            params['Force'] = sp.sympify(params['Force'])

    if isinstance(params['R'], str):
        try:
            radius_expr = params['R']
            params['R'] = float(eval(replace_expression(radius_expr, params['Force'], params['R'], params['theta'])))
        except:
            params['R'] = sp.sympify(params['R'])

    if isinstance(params['theta'], str):
        try:
            theta_expr = params['theta']
            params['theta'] = float(eval(replace_expression(theta_expr, params['Force'], params['R'], params['theta'])))
        except:
            params['theta'] = sp.sympify(params['theta'])
    elif isinstance(params['theta'], (int, float)):
        params['theta'] = float(params['theta'])

def finding_the_triangle(params):
    """
    Calculate triangle coordinates (X, Y, Z).
    """
    R = params['R']
    theta = params['theta']

    if isinstance(theta, sp.Basic):
        theta_rad = theta
        Z = R * sp.cos(theta_rad) - R / 2
        Y = R * sp.sin(theta_rad)
    else:
        theta_rad = math.radians(theta)
        Z = R * math.cos(theta_rad) - R / 2
        Y = R * math.sin(theta_rad)

    if isinstance(Z, sp.Basic) or isinstance(Y, sp.Basic):
        X = sp.sqrt(Z ** 2 + Y ** 2)
    else:
        X = math.hypot(Z, Y)

    params['X'], params['Y'], params['Z'] = X, Y, Z
    return X, Y, Z

def finding_the_angle(params):
    """
    Calculate angle-related values (P, T, alpha).
    """
    X = params['X']
    R = params['R']
    theta = params['theta']

    if isinstance(theta, sp.Basic):
        P = R * sp.sin(theta)
    else:
        P = R * math.sin(math.radians(theta))

    T = P / X

    if isinstance(T, sp.Basic):
        alpha = sp.asin(T) * (180 / sp.pi)
    else:
        alpha = math.degrees(math.asin(T))

    params['P'], params['T'], params['alpha'] = P, T, alpha
    return P, T, alpha

def moment_calculator(params):
    """
    Calculate moment.
    """
    F = params['Force']
    R = params['R']
    alpha = params['alpha']

    if isinstance(alpha, sp.Basic):
        moment_value = (F * R / 2) * sp.sin(alpha)
    else:
        moment_value = (F * R / 2) * math.sin(math.radians(alpha))

    return moment_value

def main():
    """
    Main function to run the Force-Couple System solver.
    """
    # Display question
    question = """
    The force F acts along the line MA, where M is the midpoint of the radius along the x-axis.
    Determine the Equivalent Force couple system at O for an input angle Theta.
    """
    print("The Question is:")
    print(question)

    # Initialize parameters
    params = {
        'theta': input("Enter the angle theta (can be an expression like '2*theta' or a numeric value in degrees): "),
        'R': input("Enter the radius R (can be an expression like 'R/2' or '2*R'): "),
        'Force': input("Enter the Force F (can be an expression like '2*F'): ")
    }

    # Process inputs
    check_input(params)

    # Calculate triangle coordinates
    X, Y, Z = finding_the_triangle(params)

    # Calculate angle-related values
    P, T, alpha = finding_the_angle(params)

    # Calculate moment
    moment = moment_calculator(params)

    # Print results
    print("Alpha:", alpha, "degrees")
    print("Moment:", moment)

if __name__ == "__main__":
    create_graph(R=1, theta=45, force_length=1.5)
    main()

