from sympy import symbols, Eq, solve


class solver:
    def __init__(self, magnitude_of_applied_force_on_beam, length_of_beam, length_of_rectangular_parts_of_force,
                 weight_of_body_at_pulley, length_of_triangular_part_of_force,
                 length_between_start_of_beam_and_hinge_support_at_A, distance_between_force_and_B,
                 total_length_of_force_applied, length_between_A_and_C):
        self.magnitude_of_applied_force_on_beam = magnitude_of_applied_force_on_beam
        self.length_of_beam = length_of_beam
        self.length_of_rectangular_parts_of_force = length_of_rectangular_parts_of_force
        self.weight_of_body_at_pulley = weight_of_body_at_pulley
        self.length_of_triangular_part_of_force = length_of_triangular_part_of_force
        self.length_between_start_of_beam_and_hinge_support_at_A = length_between_start_of_beam_and_hinge_support_at_A
        self.distance_between_force_and_B = distance_between_force_and_B
        self.total_length_of_force_applied = total_length_of_force_applied
        self.length_between_A_and_C = length_between_A_and_C

    def y_equations(self, hinge_reaction_at_A_in_Y_direction, Normal_force_at_C):
        reaction_1 = self.magnitude_of_applied_force_on_beam * self.length_of_rectangular_parts_of_force
        reaction_2 = self.magnitude_of_applied_force_on_beam * (1 / 2) * self.length_of_triangular_part_of_force
        force_at_B = (self.weight_of_body_at_pulley / 2 * 9.81) / 1000  # Treat force symbolically if needed

        equation_for_y = Eq(
            hinge_reaction_at_A_in_Y_direction +
            Normal_force_at_C +
            force_at_B -
            reaction_2 -
            reaction_1,
            0
        )

        return equation_for_y, reaction_1, reaction_2, force_at_B

    def moment_equations(self, reaction_1, reaction_2, force_at_B, hinge_reaction_at_A_in_Y_direction, Normal_force_at_C):
        point_for_reaction_1 = self.length_of_rectangular_parts_of_force / 2
        distance_between_reaction_2_and_A = (
                (self.length_of_rectangular_parts_of_force - self.length_between_start_of_beam_and_hinge_support_at_A) +
                (1 / 3 * self.length_of_triangular_part_of_force)
        )
        distance_between_A_and_Reaction_1 = (
                point_for_reaction_1 - self.length_between_start_of_beam_and_hinge_support_at_A

        )
        distance_between_B_and_A = (
                self.distance_between_force_and_B +
                self.length_of_triangular_part_of_force +
                (self.length_of_rectangular_parts_of_force - self.length_between_start_of_beam_and_hinge_support_at_A)
        )

        equation_for_moment = Eq(
            (-1 * reaction_1 * (self.length_between_start_of_beam_and_hinge_support_at_A)) +
            (-1 * reaction_2 * distance_between_reaction_2_and_A) +
            (distance_between_B_and_A * force_at_B) +
            (Normal_force_at_C * self.length_between_A_and_C),
            0
        )
        print(equation_for_moment)
        print(distance_between_reaction_2_and_A)
        print(distance_between_B_and_A)
        return equation_for_moment, distance_between_reaction_2_and_A, distance_between_B_and_A

    def solve_equations(self):
        # Use sympy symbols for the unknown variables
        hinge_reaction_at_A_in_Y_direction, Normal_force_at_C = symbols(
            'hinge_reaction_at_A_in_Y_direction Normal_force_at_C'
        )

        # Get y-equation and reactions
        eq_y, reaction_1, reaction_2, force_at_B = self.y_equations(
            hinge_reaction_at_A_in_Y_direction,
            Normal_force_at_C
        )

        # Get moment-equation
        eq_moment, _, _ = self.moment_equations(
            reaction_1,
            reaction_2,
            force_at_B,
            hinge_reaction_at_A_in_Y_direction,
            Normal_force_at_C
        )

        # Solve the system of equations
        solutions = solve([eq_y, eq_moment], (hinge_reaction_at_A_in_Y_direction, Normal_force_at_C))

        return solutions


