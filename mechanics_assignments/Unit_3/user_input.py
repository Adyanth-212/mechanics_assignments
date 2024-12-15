from sympy import symbols
from solver import solver
import matplotlib.pyplot as plt


def display_question():
    question = """
    Determine the reactions at A and C for the beam subjected to the combination
    of point and distributed loads.
    (Note: All forces are in Kilo Newtons, However the weight entered should be in Kilograms,
    In this question All upward forces are taken as Positive.
    The Magnitude of applied force on the beam is in unit KN/M)
    """
    print("The Question is: ")
    print(question)


def get_input(prompt):

    while True:
        user_input = input(prompt)
        try:
            # Try converting to a float first
            return float(user_input)
        except ValueError:
            try:
                # Try symbolic conversion
                symbolic_input = sympify(user_input)

                # Check if the input is a pure symbol (like 'L', 'F')
                if isinstance(symbolic_input, Symbol):
                    return symbolic_input

                # Check for negative values
                if symbolic_input.is_number and symbolic_input < 0:
                    print("Error: Input cannot be negative. Please try again.")
                    continue

                return symbolic_input
            except Exception:
                print("Invalid input. Please enter a numeric value or a valid symbolic expression.")


def getting_the_inputs():
    # Get necessary inputs from the user
    length_of_beam = get_input("Length of the beam (e.g., 10 or L): ")
    magnitude_of_applied_force_on_beam = get_input("Magnitude of applied force on beam (e.g., 20 or F): ")
    length_of_rectangular_parts_of_force = get_input("Length of rectangular part of force (e.g., 5 or R): ")
    weight_of_body_at_pulley = get_input("Weight of the body at the pulley (e.g., 100 or W): ")
    total_length_of_force_applied = get_input("Total Length of Force Applied (e.g., 8 or T): ")
    distance_between_end_of_beam_and_roller_support_at_C = get_input(
        "Distance between end of beam and roller support at C (e.g., 2 or D): ")
    distance_between_C_and_point_at_which_cable_touches_B = get_input(
        "Distance between C and point at which cable touches B (e.g., 3 or P): ")
    length_between_start_of_beam_and_hinge_support_at_A = get_input(
        "Length between start of beam and hinge support at A (e.g., 1 or A): ")

    # Derived values based on inputs
    length_of_triangular_part_of_force = total_length_of_force_applied - length_of_rectangular_parts_of_force
    distance_between_force_and_B = length_of_beam - (
            total_length_of_force_applied +
            distance_between_C_and_point_at_which_cable_touches_B +
            distance_between_end_of_beam_and_roller_support_at_C
    )
    length_between_A_and_C = length_of_beam - (
            length_between_start_of_beam_and_hinge_support_at_A +
            distance_between_end_of_beam_and_roller_support_at_C
    )

    return {
        "length_of_beam": length_of_beam,
        "magnitude_of_applied_force_on_beam": magnitude_of_applied_force_on_beam,
        "length_of_rectangular_parts_of_force": length_of_rectangular_parts_of_force,
        "weight_of_body_at_pulley": weight_of_body_at_pulley,
        "length_of_triangular_part_of_force": length_of_triangular_part_of_force,
        "distance_between_force_and_B": distance_between_force_and_B,
        "distance_between_end_of_beam_and_roller_support_at_C": distance_between_end_of_beam_and_roller_support_at_C,
        "distance_between_C_and_point_at_which_cable_touches_B": distance_between_C_and_point_at_which_cable_touches_B,
        "length_between_start_of_beam_and_hinge_support_at_A": length_between_start_of_beam_and_hinge_support_at_A,
        "total_length_of_force_applied": total_length_of_force_applied,
        "length_between_A_and_C": length_between_A_and_C
    }


def validate_inputs(inputs):
    errors = []

    # List of inputs to check for non-negative values
    non_negative_checks = [
        ("length_of_beam", "Length of beam"),
        ("magnitude_of_applied_force_on_beam", "Magnitude of applied force"),
        ("length_of_rectangular_parts_of_force", "Length of rectangular parts of force"),
        ("weight_of_body_at_pulley", "Weight of body at pulley"),
        ("length_of_triangular_part_of_force", "Length of triangular part of force"),
        ("total_length_of_force_applied", "Total length of force applied"),
        ("distance_between_end_of_beam_and_roller_support_at_C", "Distance between end of beam and roller support"),
        ("distance_between_C_and_point_at_which_cable_touches_B", "Distance between C and cable touch point"),
        ("length_between_start_of_beam_and_hinge_support_at_A", "Length between start of beam and hinge support")
    ]

    # Validate non-negative inputs
    for key, description in non_negative_checks:
        value = inputs.get(key)
        # Skip symbolic inputs
        if isinstance(value, str):
            continue

        if value is not None and value < 0:
            errors.append(f"Error: {description} cannot be negative. Current value: {value}")

    # Additional logical checks
    if inputs.get("total_length_of_force_applied") > inputs.get("length_of_beam"):
        errors.append(f"Error: Total length of force applied ({inputs.get('total_length_of_force_applied')}) "
                      f"cannot exceed beam length ({inputs.get('length_of_beam')})")

    # Return errors
    return errors


def mainthing():
    display_question()
    inputs = getting_the_inputs()

    # Validate inputs before proceeding
    validation_errors = validate_inputs(inputs)
    if validation_errors:
        print("Input Validation Failed. Please correct the following issues:")
        for error in validation_errors:
            print(error)
        return  # Stop execution if there are validation errors

    answer = solver(
        inputs["magnitude_of_applied_force_on_beam"],
        inputs["length_of_beam"],
        inputs["length_of_rectangular_parts_of_force"],
        inputs["weight_of_body_at_pulley"],
        inputs["length_of_triangular_part_of_force"],
        inputs["length_between_start_of_beam_and_hinge_support_at_A"],
        inputs["distance_between_force_and_B"],
        inputs["total_length_of_force_applied"],
        inputs["length_between_A_and_C"]
    )
    results = answer.solve_equations()
    print("The results for the reactions are:")
    print(results)


mainthing()
