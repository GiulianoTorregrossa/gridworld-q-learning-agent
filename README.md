# Gridworld Q-Learning Agent

## Description
Explore reinforcement learning with this interactive Q-learning gridworld simulation. This project features a Python implementation of a Q-learning agent in a grid-based environment, designed to demonstrate key concepts of reinforcement learning in a clear and hands-on manner. Ideal for students, educators, and AI enthusiasts interested in the basics of Q-learning algorithms.

## Features
- Implementation of Q-learning algorithm.
- Customizable grid-world environment.
- Parametric starting positions for the agent and the goal.
- Adjustable learning parameters for the Q-learning agent.
- Ability to visualize the learning process in the gridworld.
- Flexible configuration for various simulation scenarios.

## Setup and Installation
1. Ensure Python (version 3.x or above) is installed on your machine.
2. Clone this repository:
   ```
   git clone https://github.com/GiulianoTorregrossa/gridworld-q-learning-agent.git
   ```
3. Install necessary dependencies:
   ```
   pip install numpy
   ```
   
## Running the Simulation
To start the simulation with default parameters, run:

```bash
python main.py
```

You can also customize the simulation by adjusting various parameters in the `main.py` script.

### Customizable Parameters
The simulation can be customized using the following parameters:
- `size_of_grid`: Size of the gridworld (default is 5) (5x5 grid).
- `agent_start_x`: Starting x-coordinate of the agent (default is 0).
- `agent_start_y`: Starting y-coordinate of the agent (default is 0).
- `goal_x`: x-coordinate of the goal position (default is bottom-right corner).
- `goal_y`: y-coordinate of the goal position (default is bottom-right corner).
- `learning_rate`: Learning rate for Q-learning (default is 0.1).
- `discount_factor`: Discount factor for Q-learning (default is 0.9).
- `exploration_rate`: Initial exploration rate (default is 1.0).
- `min_exploration_rate`: Minimum exploration rate (default is 0.01).
- `exploration_decay_rate`: Decay rate for exploration (default is 0.995).
- `n_episodes`: Number of episodes to run the simulation (default is 1000).
- `render`: Set to `True` to visually render the gridworld (default is `False`).

### Fixed Parameters
- `n_actions`: Number of possible actions (Fixed at 4 - up, down, left, right).

### Conditional Rendering
The gridworld is rendered conditionally to optimize performance and visualization:
- It renders every 50 episodes and on the last episode.
- This allows you to observe the agent's progress at regular intervals without rendering every single step, which can be resource-intensive.

## Contributing
Contributions to the project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear commit messages.
4. Push the changes to your fork and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
Feel free to contact me for any questions or feedback at torregrossagiuliano@gmail.com.