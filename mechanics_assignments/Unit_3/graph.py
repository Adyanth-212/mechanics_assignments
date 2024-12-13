import matplotlib.pyplot as plt
import numpy as np
import parameters


def plot_beam_diagram():
    # Beam Lengths
    length_A_B = 5  # m (distance from A to B where the distributed load acts)
    length_B_C = 3  # m (distance from B to C)
    total_length = length_A_B + length_B_C

    # Load Parameters
    max_distributed_load = 15  # kN/m (at A)
    point_load = 20  # kN (2 Mg converted to kN)
    point_load_location = total_length  # at end of beam (C)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw the beam
    ax.plot([0, total_length], [0, 0], color='black', lw=3, label="Beam")

    # Draw pin support at A
    ax.scatter(0, 0, color='blue', s=100, label="Pin Support (A)", zorder=5)
    ax.plot([-0.5, 0.5], [-0.2, -0.2], color='blue', lw=2)

    # Draw roller support at C
    ax.scatter(total_length, 0, color='orange', s=100, label="Roller Support (C)", zorder=5)
    ax.plot([total_length - 0.5, total_length + 0.5], [-0.2, -0.2], color='orange', lw=2)

    # Draw distributed load (triangular)
    x_dist_load = np.linspace(0, length_A_B, 100)
    y_dist_load = -max_distributed_load * (1 - x_dist_load / length_A_B)
    ax.fill_between(x_dist_load, 0, y_dist_load, color='red', alpha=0.5,
                    label=f"Distributed Load ({max_distributed_load} kN/m)")
    for i in range(0, int(length_A_B) + 1):
        ax.arrow(i, 0, 0, -max_distributed_load * (1 - i / length_A_B) / 5, head_width=0.1, head_length=0.3, fc='red',
                 ec='red')

    # Draw point load at C
    ax.arrow(point_load_location, 0, 0, -point_load / 5, head_width=0.2, head_length=0.5, color='green',
             label=f"Point Load ({point_load} kN)")

    # Add distances
    ax.text(length_A_B / 2, 0.5, f"{length_A_B} m", fontsize=10, color='black', ha='center')
    ax.text(length_A_B + length_B_C / 2, 0.5, f"{length_B_C} m", fontsize=10, color='black', ha='center')
    ax.text(total_length / 2, 1, f"Total Length: {total_length} m", fontsize=10, color='black', ha='center')

    # Add labels and legend
    ax.set_title("Beam Diagram with Forces and Supports", fontsize=14)
    ax.set_xlabel("Beam Length (m)", fontsize=12)
    ax.set_ylabel("Force (kN)", fontsize=12)
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Reference line
    ax.legend(loc="upper right", fontsize=10)

    # Formatting
    ax.set_xlim(-1, total_length + 1)
    ax.set_ylim(-max_distributed_load - 5, 5)
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.show()


# Call the function to display the diagram
plot_beam_diagram()
