import numpy as np


class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate, discount_factor, exploration_rate):
        self.q_table = np.zeros((n_states, n_actions))
        self.learning_rate = learning_rate  # Alpha
        self.discount_factor = discount_factor  # Gamma
        self.exploration_rate = exploration_rate  # Epsilon
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

    @staticmethod
    def action_to_string(action_num):
        """Convert numerical action to string representation."""
        actions = ['up', 'right', 'down', 'left']
        return actions[action_num]

    @staticmethod
    def get_state_index(position, grid_size):
        """Get the state index from a grid position."""
        return position[0] * grid_size + position[1]

