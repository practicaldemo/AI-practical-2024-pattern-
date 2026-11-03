def reflex_vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

def simulate_environment(environment):
    print("Initial Environment:", environment)
    while 'Dirty' in environment.values():
        for location, status in environment.items():
            action = reflex_vacuum_agent(location, status)
            print(f"Location: {location} | Status: {status} | Action: {action}")
            if action == 'Suck':
                environment[location] = 'Clean'
    print("Final Environment:", environment)

# Example usage
env = {'A': 'Dirty', 'B': 'Dirty'}
simulate_environment(env)