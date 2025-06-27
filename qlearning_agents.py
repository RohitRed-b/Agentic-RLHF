import random
from collections import defaultdict

class QLearningAgent:
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.q_values = defaultdict(float)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q_values[(state, action)]

    def choose_action(self, state, legal_actions):
        if not legal_actions:
            return None
        if random.random() < self.epsilon:
            return random.choice(legal_actions)
        q_values = [(self.get_q_value(state, a), a) for a in legal_actions]
        return max(q_values)[1]

    def update(self, state, action, next_state, reward, next_legal_actions):
        best_next = max([self.get_q_value(next_state, a) for a in next_legal_actions], default=0.0)
        old = self.get_q_value(state, action)
        self.q_values[(state, action)] = old + self.alpha * (reward + self.gamma * best_next - old)