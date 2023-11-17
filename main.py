# run_simulation.py
# This script demonstrates the Q-learning algorithm in a gridworld environment.

from src.simulation import run_simulation


def main():
    print("Starting Q-learning Gridworld Simulation")

    # List of all possible parameters for customization
    parameter_list = """
    Available Parameters for Customization:
    - size_of_grid: Size of the gridworld (default is 5) (5x5 grid).
    - agent_start_x: Starting x-coordinate of the agent (default is 0).
    - agent_start_y: Starting y-coordinate of the agent (default is 0).
    - goal_x: x-coordinate of the goal position (default is bottom-right corner).
    - goal_y: y-coordinate of the goal position (default is bottom-right corner).
    - learning_rate: Learning rate for Q-learning (default is 0.1).
    - discount_factor: Discount factor for Q-learning (default is 0.9).
    - exploration_rate: Initial exploration rate (default is 1.0).
    - min_exploration_rate: Minimum exploration rate (default is 0.01).
    - exploration_decay_rate: Decay rate for exploration (default is 0.995).
    - n_episodes: Number of episodes to run the simulation (default is 1000).
    - render: Set to True to visually render the gridworld (default is False).
    """
    print(parameter_list)

    # Default run with predefined settings
    print("Running with default settings:")
    run_simulation(render=True)

    # Custom run example
    print("Running a custom simulation with a different grid size and fewer episodes:")
    run_simulation(size_of_grid=10, n_episodes=5000, render=True)

    # Advanced customization example
    print("Running with advanced settings (small exploration rate and different goal):")
    run_simulation(
        size_of_grid=50,
        agent_start_x=0,
        agent_start_y=0,
        goal_x=35,
        goal_y=45,
        learning_rate=0.2,
        discount_factor=0.9,
        exploration_rate=1,
        min_exploration_rate=0.01,
        exploration_decay_rate=0.9995,
        n_episodes=20000,
        render=False
    )

    print("Simulation complete. Explore the code to see more customization options!")


if __name__ == "__main__":
    main()
