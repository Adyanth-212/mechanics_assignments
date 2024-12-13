import matplotlib.pyplot as plt
import numpy as np

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

if __name__ == "__main__":
    # Test the function with example parameters
    create_graph(R=1, theta=45, force_length=1.5)
