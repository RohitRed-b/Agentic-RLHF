class ValueIterationAgent:
    def __init__(self, mdp, discount=0.9, iterations=100):
        self.values = defaultdict(float)
        self.discount = discount
        for _ in range(iterations):
            new_values = defaultdict(float)
            for state in mdp.get_states():
                action_values = [sum(p * (r + self.discount * self.values[s])
                                     for (s, p, r) in mdp.get_transitions(state, a))
                                 for a in mdp.get_legal_actions(state)]
                if action_values:
                    new_values[state] = max(action_values)
            self.values = new_values