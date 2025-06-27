class SearchAgent:
    def __init__(self, search_function):
        self.search_function = search_function

    def solve(self, problem):
        return self.search_function(problem)
