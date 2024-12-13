from mechanics_assignments.Unit_1.graph import create_graph
from parameters import Parameters
from solver import Solver

class ForceCoupleSystem:
    def __init__(self, params):
        self.params = params

    def display_question(self):
        question = """
        The force F acts along the line MA, where M is the midpoint of the radius along the x-axis.
        Determine the Equivalent Force couple system at O for an input angle Theta.
        """
        print("The Question is: ")
        print(question)

    def user_parameters(self):
        self.params.theta = float(input("Enter the angle theta (in degrees): "))
        self.params.R = float(input("Enter the radius R: "))
        self.params.Force = float(input("Enter the Force F: "))


    def print_results(self, solver):
        _, _, _ = solver.findingthetriangle()
        _, _, alpha = solver.findingtheangle()
        moment = solver.moment_calculator()

        print("\nResults:")
        print(f"Alpha: {alpha:.2f}")
        print(f"Moment: {moment:.2f}")



if __name__ == "__main__":
    params = Parameters()
    system = ForceCoupleSystem(params)
    system.display_question()
    system.user_parameters()
    solver = Solver(params)
    system.print_results(solver)
    create_graph(params.R, params.theta, params.Force)


