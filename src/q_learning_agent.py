import numpy as np


class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0,
                 min_exploration_rate=0.01, exploration_decay_rate=0.995):
        """
        Initializes the Q-learning agent.

        Parameters:
        - n_states (int): The number of states in the environment.
        - n_actions (int): The number of possible actions the agent can take.
        - learning_rate (float): The rate at which the agent learns (alpha). Defaults to 0.1.
        - discount_factor (float): The discount factor (gamma) used to balance immediate and future rewards. Defaults to 0.9.
        - exploration_rate (float): The initial exploration rate (epsilon) for the agent, determining how much to explore versus exploit. Defaults to 1.0.
        - min_exploration_rate (float): The minimum exploration rate. Defaults to 0.1.
        - exploration_decay_rate (float): The rate at which the exploration rate decays. Defaults to 0.995.
        """
        self.q_table = np.zeros((n_states, n_actions))
        self.learning_rate = learning_rate  # Alpha
        self.discount_factor = discount_factor  # Gamma
        self.exploration_rate = exploration_rate  # Epsilon
        self.min_exploration_rate = min_exploration_rate  # Epsilon
        self.exploration_decay_rate = exploration_decay_rate  # Epsilon
        self.n_actions = n_actions  # Number of possible actions

    def select_action(self, state):
        """Select an action for the given state using an epsilon-greedy strategy."""
        if np.random.uniform(0, 1) < self.exploration_rate:
            action = np.random.choice(self.n_actions)  # Explore
        else:
            action = np.argmax(self.q_table[state])  # Exploit
        return action

    def update_q_table(self, state, action, reward, new_state):
        """Update the Q-table based on the action, observed reward, and new state."""
        best_future_q = np.max(self.q_table[new_state])
        self.q_table[state, action] += self.learning_rate * (
                reward + self.discount_factor * best_future_q - self.q_table[state, action])

    def decay_exploration_rate(self):
        """
        Decays the exploration rate of the agent following the exploration decay rate,
        ensuring it does not go below the minimum exploration rate.
        """
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay_rate)

    @staticmethod
    def action_to_string(action_num):
        """Convert numerical action to string representation."""
        actions = ['up', 'right', 'down', 'left']
        return actions[action_num]

    @staticmethod
    def get_state_index(position, grid_size):
        """Get the state index from a grid position."""
        return position[0] * grid_size + position[1]
