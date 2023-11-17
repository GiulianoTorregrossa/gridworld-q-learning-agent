from src.gridworld import Gridworld
from src.q_learning_agent import QLearningAgent


def run_simulation(size_of_grid=5, agent_start_x=None, agent_start_y=None, goal_x=None, goal_y=None,
                   n_actions=None, learning_rate=None, discount_factor=None, exploration_rate=None,
                   min_exploration_rate=None, exploration_decay_rate=None, n_states=None,
                   n_episodes=1000, render=False):
    """
    Runs the gridworld simulation with a Q-learning agent.

    Parameters:
    - size_of_grid (int): Size of the gridworld. If not specified, defaults to the Gridworld class default.
    - agent_start_x (int): Starting x-coordinate of the agent. If not specified, defaults to the Gridworld class default.
    - agent_start_y (int): Starting y-coordinate of the agent. If not specified, defaults to the Gridworld class default.
    - goal_x (int): x-coordinate of the goal. If not specified, defaults to the Gridworld class default.
    - goal_y (int): y-coordinate of the goal. If not specified, defaults to the Gridworld class default.
    - learning_rate (float): Learning rate for Q-learning. If not specified, defaults to the QLearningAgent class default.
    - discount_factor (float): Discount factor for Q-learning. If not specified, defaults to the QLearningAgent class default.
    - exploration_rate (float): Initial exploration rate for Q-learning. If not specified, defaults to the QLearningAgent class default.
    - min_exploration_rate (float): Minimum exploration rate for the agent.
    - exploration_decay_rate (float): Decay rate for the exploration rate.
    - n_episodes (int): Number of episodes to run the simulation. Defaults to 20000 if not specified.
    - render (bool): Whether to visually render the gridworld during the simulation (default False).
    """

    # Set defaults or calculations for n_states and n_actions
    n_states = size_of_grid * size_of_grid  # Calculate n_states based on grid size
    n_actions = 4  # Fixed to four actions (up, down, left, right)

    # Initialize environment and agent with provided parameters or defaults
    gridworld_params = ["size_of_grid", "agent_start_x", "agent_start_y", "goal_x", "goal_y"]
    gridworld_args = {key: value for key, value in locals().items() if value is not None and key in gridworld_params}
    gridworld = Gridworld(**gridworld_args)

    agent_params = ["n_states", "n_actions", "learning_rate", "discount_factor", "exploration_rate", "min_exploration_rate", "exploration_decay_rate"]
    agent_args = {key: value for key, value in locals().items() if value is not None and key in agent_params}
    agent = QLearningAgent(**agent_args)

    # Training loop
    for episode in range(n_episodes):
        state = agent.get_state_index(gridworld.reset(), size_of_grid)
        done = False
        step = 0

        while not done:
            step += 1
            action_num = agent.select_action(state)
            action = agent.action_to_string(action_num)

            new_state, reward, done = gridworld.step(action)
            new_state = agent.get_state_index(new_state, size_of_grid)

            agent.update_q_table(state, action_num, reward, new_state)
            state = new_state

            if render and (episode % 50 == 0 or episode == n_episodes-1):
                gridworld.render()  # Render the gridworld

            if done:
                print(f"Episode: {episode}, Step: {step}, Epsilon: {agent.exploration_rate}")
                agent.decay_exploration_rate()  # Update the exploration rate using the agent's method
