class Gridworld:
    def __init__(self, size=5, agent_x=0, agent_y=0, goal_x=None, goal_y=None):
        """
        Initialize the gridworld environment with a specified size, agent's starting position,
        and goal position.
        """
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

        # Set and validate the agent's starting position
        self.start_position = [agent_x, agent_y]
        if not (0 <= agent_x < size and 0 <= agent_y < size):
            raise ValueError("Agent starting position must be within the grid boundaries.")

        # Store the agent's current position
        self.agent_position = self.start_position.copy()

        # Set and validate the goal position
        self.goal = [goal_x if goal_x is not None else size - 1,
                     goal_y if goal_y is not None else size - 1]
        if not (0 <= self.goal[0] < size and 0 <= self.goal[1] < size):
            raise ValueError("Goal position must be within the grid boundaries.")

    def reset(self):
        """Reset the agent to the starting position and return the initial state."""
        self.agent_position = self.start_position.copy()
        return self.agent_position

    def step(self, action):
        """
        Implement how the agent's position changes based on the action.
        Return the new state, reward, and whether the goal is reached.
        """
        # Movement logic
        if action == 'up':
            self.agent_position[0] = max(0, self.agent_position[0] - 1)
        elif action == 'down':
            self.agent_position[0] = min(self.size - 1, self.agent_position[0] + 1)
        elif action == 'left':
            self.agent_position[1] = max(0, self.agent_position[1] - 1)
        elif action == 'right':
            self.agent_position[1] = min(self.size - 1, self.agent_position[1] + 1)

        # Check if goal is reached
        done = self.agent_position == self.goal

        # Calculate the reward
        reward = 1 if done else -1

        return self.agent_position, reward, done

    def render(self):
        """Display the current state of the grid with the agent and goal positions."""
        grid_copy = [row[:] for row in self.grid]
        grid_copy[self.agent_position[0]][self.agent_position[1]] = 'A'
        grid_copy[self.goal[0]][self.goal[1]] = 'G'
        for row in grid_copy:
            print(' '.join(str(cell) for cell in row))
        print()

