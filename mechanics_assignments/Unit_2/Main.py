import math
from sympy import symbols, Eq, solve, sin, cos, tan, atan, rad, deg

# Displaying the question
def display_question():
    print("The Question is: ")
    print("Determine the force in each member of the loaded truss.")

# Taking inputs from the user
def getting_inputs():
    print("Enter the following parameters (you can use numbers or variables, e.g., L, F):")
    distance_between_the_supports_a_and_d = input("Distance between the supports A and D: ")
    horizontal_distance_between_d_and_c = input("Horizontal distance between D and C: ")
    horizontal_distance_between_d_and_b = input("Horizontal distance between D and B: ")
    f1 = input("Force F1: ")
    f2 = input("Force F2: ")
    opposite_side_to_angle_theta = input("Opposite side to angle theta: ")
    adjacent_side_to_angle_theta = input("Adjacent side to angle theta: ")

    return {
        "distance_between_the_supports_a_and_d": symbols(distance_between_the_supports_a_and_d) if not distance_between_the_supports_a_and_d.replace('.', '').isdigit() else float(distance_between_the_supports_a_and_d),
        "horizontal_distance_between_d_and_c": symbols(horizontal_distance_between_d_and_c) if not horizontal_distance_between_d_and_c.replace('.', '').isdigit() else float(horizontal_distance_between_d_and_c),
        "horizontal_distance_between_d_and_b": symbols(horizontal_distance_between_d_and_b) if not horizontal_distance_between_d_and_b.replace('.', '').isdigit() else float(horizontal_distance_between_d_and_b),
        "f1": symbols(f1) if not f1.replace('.', '').isdigit() else float(f1),
        "f2": symbols(f2) if not f2.replace('.', '').isdigit() else float(f2),
        "opposite_side_to_angle_theta": symbols(opposite_side_to_angle_theta) if not opposite_side_to_angle_theta.replace('.', '').isdigit() else float(opposite_side_to_angle_theta),
        "adjacent_side_to_angle_theta": symbols(adjacent_side_to_angle_theta) if not adjacent_side_to_angle_theta.replace('.', '').isdigit() else float(adjacent_side_to_angle_theta),
    }

# Calculating angles
def finding_angles(params):
    opposite_side = params['opposite_side_to_angle_theta']
    adjacent_side = params['adjacent_side_to_angle_theta']

    theta_1 = atan(opposite_side / adjacent_side)
    distance_to_e = params['distance_between_the_supports_a_and_d'] - (
        params['horizontal_distance_between_d_and_c'] / tan(theta_1)
    )
    theta_2 = atan(distance_to_e / params['horizontal_distance_between_d_and_b'])
    theta_3 = atan(distance_to_e / params['horizontal_distance_between_d_and_c'])

    return deg(theta_1), deg(theta_2), deg(theta_3)

# Solving for forces at Joint B
def solving_for_joint_b(params, theta_2):
    force_in_a_b, force_in_b_c = symbols('force_in_a_b force_in_b_c')

    y_equation_b = Eq(force_in_a_b * sin(rad(theta_2)) - params['f1'], 0)
    x_equation_b = Eq(force_in_a_b * cos(rad(theta_2)) + force_in_b_c, 0)

    solutions_joint_b = solve([y_equation_b, x_equation_b], (force_in_a_b, force_in_b_c))
    return solutions_joint_b[force_in_a_b], solutions_joint_b[force_in_b_c]

# Solving for forces at Joint C
def solving_for_joint_c(params, theta_3, theta_1, force_in_b_c_value):
    force_in_a_c, force_in_c_d, force_in_b_c = symbols('force_in_a_c force_in_c_d force_in_b_c')

    x_equation_c = Eq(
        force_in_a_c * cos(rad(theta_3)) + force_in_c_d * sin(rad(theta_1)),
        force_in_b_c
    )
    y_equation_c = Eq(
        force_in_a_c * sin(rad(theta_3)),
        force_in_c_d * cos(rad(theta_1)) + params['f2']
    )

    x_equation_c_substituted = x_equation_c.subs(force_in_b_c, force_in_b_c_value)
    y_equation_c_substituted = y_equation_c.subs(force_in_b_c, force_in_b_c_value)

    solutions_joint_c = solve([x_equation_c_substituted, y_equation_c_substituted], (force_in_a_c, force_in_c_d))

    return solutions_joint_c.get(force_in_a_c), solutions_joint_c.get(force_in_c_d)

# Solving for forces at Joint D
def solving_for_joint_d(params, theta_1, force_in_c_d_value):
    force_in_a_d, force_in_c_d = symbols('force_in_a_d force_in_c_d')

    y_equation = Eq(force_in_a_d + force_in_c_d * cos(rad(theta_1)), 0)
    solution_joint_d = solve(y_equation, force_in_a_d)

    solution_for_a_d = solution_joint_d[0].subs(force_in_c_d, force_in_c_d_value)

    return solution_for_a_d

def main_thing():
    display_question()

    inputs = getting_inputs()

    angles = finding_angles(inputs)
    print(f"Calculated Angles (in degrees): {angles[0]}, {angles[1]}, {angles[2]}")

    joint_b_solution = solving_for_joint_b(inputs, angles[1])
    print("Solutions for Joint B:")
    print(f"  Force in AB: {joint_b_solution[0]}")
    print(f"  Force in BC: {joint_b_solution[1]}")

    joint_c_solution = solving_for_joint_c(inputs, angles[2], angles[0], joint_b_solution[1])
    print("Solutions for Joint C:")
    print(f"  Force in AC: {joint_c_solution[0]}")
    print(f"  Force in CD: {joint_c_solution[1]}")

    joint_d_solution = solving_for_joint_d(inputs, angles[0], joint_c_solution[1])
    print("Solutions for Joint D:")
    print(f"  Force in AD: {joint_d_solution}")

if __name__ == "__main__":
    main_thing()
