class Gridworld:
    def __init__(self, size_of_grid=5, agent_start_x=0, agent_start_y=0, goal_x=None, goal_y=None):
        """
        Initialize the gridworld environment with a specified size_of_grid, agent's starting position,
        and goal position.

        Parameters:
        - size_of_grid (int): The size_of_grid of the grid (default 5). Represents both the width and height as the grid is square.
        - agent_start_x (int): The x-coordinate of the agent's starting position (default 0).
        - agent_start_y (int): The y-coordinate of the agent's starting position (default 0).
        - goal_x (int): The x-coordinate of the goal position. Defaults to the bottom-right corner if not specified.
        - goal_y (int): The y-coordinate of the goal position. Defaults to the bottom-right corner if not specified.
        """
        self.size_of_grid = size_of_grid
        self.grid = [[0 for _ in range(size_of_grid)] for _ in range(size_of_grid)]

        # Set and validate the agent's starting position
        self.start_position = [agent_start_x, agent_start_y]
        if not (0 <= agent_start_x < size_of_grid and 0 <= agent_start_y < size_of_grid):
            raise ValueError("Agent starting position must be within the grid boundaries.")

        # Store the agent's current position
        self.agent_position = self.start_position.copy()

        # Set and validate the goal position
        self.goal = [goal_x if goal_x is not None else size_of_grid - 1,
                     goal_y if goal_y is not None else size_of_grid - 1]
        if not (0 <= self.goal[0] < size_of_grid and 0 <= self.goal[1] < size_of_grid):
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
            self.agent_position[0] = min(self.size_of_grid - 1, self.agent_position[0] + 1)
        elif action == 'left':
            self.agent_position[1] = max(0, self.agent_position[1] - 1)
        elif action == 'right':
            self.agent_position[1] = min(self.size_of_grid - 1, self.agent_position[1] + 1)

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
        divider = ''
        for i in range(self.size_of_grid):
            divider += '--'
        divider = divider[:-1]
        print(divider)
        for row in grid_copy:
            print(' '.join(str(cell) for cell in row))
        print(divider)

        print()

