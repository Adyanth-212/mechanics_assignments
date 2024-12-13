from parameters import beam_variables
from solver import solver
import matplotlib.pyplot as plt


def display_question():
    question = """
    Determine the reactions at A and C for the beam subjugated to the combination
    of point and distributed loads
    """
    print("The Question is: ")
    print(question)


def getting_the_inputs():
    # Get necessary inputs from the user
    length_of_beam = float(input("Length of the beam (m): "))
    magnitude_of_applied_force_on_beam = float(input("Magnitude of applied force on beam (N): "))
    length_of_rectangular_parts_of_force = float(input("Length of rectangular part of force (m): "))
    weight_of_body_at_pulley = float(input("Weight of the body at the pulley (N): "))
    total_length_of_force_applied = float(input("Total Length of Force Applied(m): "))
    distance_between_end_of_beam_and_roller_support_at_C = float(
        input("Distance between end of beam and roller support at C (m): "))
    distance_between_C_and_point_at_which_cable_touches_B = float(
        input("Distance between C and point at which cable touches B (m): "))
    length_between_start_of_beam_and_hinge_support_at_A = float(
        input("Length between start of beam and hinge support at A (m): "))

    # Derived values based on inputs
    length_of_triangular_part_of_force = total_length_of_force_applied - length_of_rectangular_parts_of_force
    distance_between_force_and_B = length_of_beam - (total_length_of_force_applied + distance_between_C_and_point_at_which_cable_touches_B + distance_between_end_of_beam_and_roller_support_at_C)

    length_between_A_and_C = length_of_beam - (length_between_start_of_beam_and_hinge_support_at_A + distance_between_end_of_beam_and_roller_support_at_C)

    # Placeholder values for hinge and normal forces, to be solved
    hinge_reaction_at_A_in_Y_direction = 0  # We'll solve this
    Normal_force_at_C = 0  # We'll solve this

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
        "hinge_reaction_at_A_in_Y_direction": hinge_reaction_at_A_in_Y_direction,
        "Normal_force_at_C": Normal_force_at_C,
        "total_length_of_force_applied": total_length_of_force_applied,
        "length_between_A_and_C": length_between_A_and_C
    }



def validate_inputs(inputs):
    errors = []
    if inputs["magnitude_of_applied_force_on_beam"] < 0:
        errors.append("Error: The magnitude of the applied force cannot be negative.")
    if inputs["length_of_beam"] <= 0:
        errors.append("Error: The length of the beam must be greater than zero.")
    if inputs["length_of_rectangular_parts_of_force"] < 0:
        errors.append("Error: The length of the rectangular part of the force cannot be negative.")
    if inputs["weight_of_body_at_pulley"] < 0:
        errors.append("Error: The weight of the body at the pulley cannot be negative.")
    if inputs["length_of_triangular_part_of_force"] < 0:
        errors.append("Error: The length of the triangular part of the force cannot be negative.")
    if inputs["length_of_rectangular_parts_of_force"] > inputs["magnitude_of_applied_force_on_beam"]:
        errors.append("Error: Rectangular force length cannot exceed total applied force length.")

    if errors:
        for error in errors:
            print(error)
        return False
    return True


def mainthing():
    display_question()
    inputs = getting_the_inputs()

    while True:
        if validate_inputs(inputs):
            answer = solver(
                inputs["magnitude_of_applied_force_on_beam"],
                inputs["length_of_beam"],
                inputs["length_of_rectangular_parts_of_force"],
                inputs["weight_of_body_at_pulley"],
                inputs["length_of_triangular_part_of_force"],
                inputs["length_between_start_of_beam_and_hinge_support_at_A"],
                inputs["distance_between_force_and_B"],
                inputs["total_length_of_force_applied"],
                inputs["length_between_A_and_C"]  # Add this line
            )
            results = answer.solve_equations()
            print("The results for the reactions are:")
            print(results)
            break
        else:
            print("Invalid Inputs detected, please make sure to enter valid inputs")
            inputs = getting_the_inputs()



if __name__ == "__main__":
    mainthing()
