import math
from mechanics_assignments.Unit_1.parameters import Parameters


class Solver:
    def __init__(self, params):
        self.params = params

    def findingthetriangle(self):
        R = self.params.R
        theta = self.params.theta
        if theta >= 0:
            theta = math.radians(theta)
        else:
            theta = math.radians(360 - theta)
        self.params.Z = float(R * math.cos(theta) - R/2)
        self.params.Y = float(R * math.cos(theta))
        self.params.X = math.hypot(self.params.Z, self.params.Y)
        return self.params.X, self.params.Y, self.params.Z

    def findingtheangle(self):
        X = self.params.X
        R = self.params.R
        theta = self.params.theta
        self.params.P = float(R * math.sin(theta))
        self.params.T = float(self.params.P / X)
        self.params.alpha = math.asin(self.params.T)
        self.params.alpha = math.degrees(self.params.alpha)
        return self.params.P, self.params.T, self.params.alpha

    def moment_calculator(self):
        F = self.params.Force
        alpha = self.params.alpha
        R = self.params.R
        return float(F * R / 2 * math.sin(math.radians(alpha)))


if __name__ == "__main__":
    params = Parameters()
    solver = Solver(params)

    # Set sample values for R, theta, and Force
    params.R = 1  # Example value for R
    params.theta = 45  # Example value for theta in degrees
    params.Force = 1.5  # Example value for Force

    X, Y, Z = solver.findingthetriangle()
    P, T, alpha = solver.findingtheangle()
    moment = solver.moment_calculator()

    print(f"X: {X}, Y: {Y}, Z: {Z}")
    print(f"P: {P}, T: {T}, alpha: {alpha}")
    print(f"Moment: {moment}")
