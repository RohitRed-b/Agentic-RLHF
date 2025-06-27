def breadth_first_search(problem):
    from collections import deque
    queue = deque([(problem.get_start_state(), [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if problem.is_goal_state(state):
            return path
        if state not in visited:
            visited.add(state)
            for next_state, action, _ in problem.get_successors(state):
                queue.append((next_state, path + [action]))
    return []
