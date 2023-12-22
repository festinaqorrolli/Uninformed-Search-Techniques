from itertools import combinations, permutations

# BFS
# Time complexity: O(weeks x (players/group_size)^players/group_size)
# Space complexity:O((players/group_size)^max_weeks)
#
# DFS
# Time complexity:O(players^(group_size×weeks))
# Space complexity:O(players x weeks)

def is_valid_grouping(grouping, history):
    for week in history:
        for group in week:
            if set(group).intersection(set(grouping)):
                return False
    return True

def bfs_social_golfer(players, group_size, max_weeks):
    queue = [([], 0)]
    iteration = 0  # For tracking iterations
    while queue:
        history, week = queue.pop(0)
        print(f"BFS iteration: {iteration}, Week: {week}")  # Print current iteration and week
        iteration += 1

        if week == max_weeks:
            return history  # Found a valid schedule

        if len(history) == week:
            history.append([])

        if len(history[week]) == players // group_size:
            queue.append((history, week + 1))  # Move to the next week
            continue

        # Fix: Only consider players already grouped in the current week
        current_week_players = set(player for group in history[week] for player in group)
        remaining_players = set(range(players)) - current_week_players
        for group in combinations(remaining_players, group_size):
            if is_valid_grouping(group, history):
                new_history = [w[:] for w in history]
                new_history[week].append(group)
                queue.append((new_history, week))

    return None

def dfs_social_golfer(weeks, num_golfers, group_size):
    # Create a list to hold the groups for each week
    schedule = [[] for _ in range(weeks)]

    # Helper function to check if a golfer has already played with any other golfer in the group in previous weeks
    def has_played_with(golfer, group, week):
        for prev_week in range(week):
            for prev_group in schedule[prev_week]:
                if golfer in prev_group and any(g in prev_group for g in group):
                    return True
        return False

    # Recursive function to try and assign golfers to groups
    def assign_to_group(week, group, remaining_golfers):
        if week == weeks:  # If all weeks are scheduled, we are done
            return True
        if not remaining_golfers:  # If no golfers left, move to next week
            return assign_to_group(week + 1, [], list(range(num_golfers)))
        if len(group) == group_size:  # If the group is full, add to the schedule
            schedule[week].append(group)
            return assign_to_group(week, [], remaining_golfers)

        for i, golfer in enumerate(remaining_golfers):
            if not has_played_with(golfer, group, week):
                if assign_to_group(week, group + [golfer], remaining_golfers[:i] + remaining_golfers[i+1:]):
                    return True
                # If we are here, it means we need to backtrack
                schedule[week] = schedule[week][:-1]
        return False

    if assign_to_group(0, [], list(range(num_golfers))):
        return schedule
    else:
        return "No solution could be found."

# User input for the problem parameters
players = int(input("Enter the number of players: "))
group_size = int(input("Enter the size of each group: "))
max_weeks = int(input("Enter the maximum number of weeks: "))

# User input for selecting the algorithm
choice = input("Choose the algorithm to solve the Social Golfer Problem (BFS/DFS): ").strip().upper()

# Solve the problem using the chosen algorithm
if choice == 'BFS':
    print("Solving using BFS...")
    schedule = bfs_social_golfer(players, group_size, max_weeks)
elif choice == 'DFS':
    print("Solving using DFS...")
    schedule = dfs_social_golfer(max_weeks, players, group_size)
else:
    print("Invalid choice. Please select 'BFS' or 'DFS'.")
    schedule = None

# Print the schedule if one is found
if schedule:
    print("A valid schedule has been found:")
    for week, groups in enumerate(schedule):
        print(f"Week {week + 1}: {[' '.join(map(str, g)) for g in groups]}")
else:
    print("No valid schedule could be found.")
