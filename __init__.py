# agentic_pacman_rlhf/__init__.py

"""
Agentic Pac-Man RLHF

This package includes modular reinforcement learning agents (Q-learning, Value Iteration),
search utilities, and analysis tools for training Pac-Man to make intelligent decisions using
both classical RL and feedback-enhanced tuning (RLHF style).

Modules:
- agents.qlearning_agents: Q-learning logic and training
- agents.value_iteration_agents: Value iteration for grid-based planning
- core.search: Search algorithms (BFS, DFS, etc.)
- core.search_agents: Search-based agent behavior
- utils.analysis: Evaluation and reward metric tools
"""

__version__ = "1.0"
__author__ = "Rohit Reddy Bheemireddy"

# Convenience imports
from .agents import qlearning_agents, value_iteration_agents
from .core import search, search_agents
from .utils import analysis
