from gridworld import Gridworld

# Configuration parameters
from q_learning_agent import QLearningAgent

# Variables
SIZE_OF_GRID = 50
AGENT_START_X = 0
AGENT_START_Y = 0
GOAL_X = 30
GOAL_Y = 45
N_ACTIONS = 4  # Up, down, left, right
LEARNING_RATE = 0.2
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = 0.01
EXPLORATION_DECAY_RATE = 0.9995
N_STATES = SIZE_OF_GRID * SIZE_OF_GRID
N_EPISODES = 20000


def initialize_gridworld(size, agent_start_x, agent_start_y, goal_x, goal_y):
    """Initialize and return a Gridworld instance with specified configurations."""
    return Gridworld(size=size, agent_x=agent_start_x, agent_y=agent_start_y, goal_x=goal_x, goal_y=goal_y)


def initialize_agent(n_states, n_actions, learning_rate, discount_factor, exploration_rate):
    """Initialize and return a QLearningAgent instance with specified configurations."""
    return QLearningAgent(n_states, n_actions, learning_rate, discount_factor, exploration_rate)


def train_agent(gridworld, agent, n_episodes, size_of_grid, min_exploration_rate, exploration_decay_rate):
    """Train the agent in the gridworld environment over a specified number of episodes."""
    for episode in range(n_episodes):
        state = QLearningAgent.get_state_index(gridworld.reset(), size_of_grid)
        done = False
        step = 0

        while not done:
            step += 1
            action_num = agent.select_action(state)
            action = QLearningAgent.action_to_string(action_num)

            new_state, reward, done = gridworld.step(action)
            new_state = QLearningAgent.get_state_index(new_state, size_of_grid)

            agent.update_q_table(state, action_num, reward, new_state)
            state = new_state

            if done:
                print(f"Episode: {episode}, Step: {step}, Epsilon: {agent.exploration_rate}")
                agent.exploration_rate = max(min_exploration_rate, agent.exploration_rate * exploration_decay_rate)


if __name__ == '__main__':
    # Initialize environment and agent
    gridworld = initialize_gridworld(SIZE_OF_GRID, AGENT_START_X, AGENT_START_Y, GOAL_X, GOAL_Y)
    agent = initialize_agent(N_STATES, N_ACTIONS, LEARNING_RATE, DISCOUNT_FACTOR, EXPLORATION_RATE)

    # Train the agent
    train_agent(gridworld, agent, N_EPISODES, SIZE_OF_GRID, MIN_EXPLORATION_RATE, EXPLORATION_DECAY_RATE)

