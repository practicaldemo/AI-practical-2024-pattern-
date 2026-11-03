

environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Initial position
location = 'A'

# Path cost
path_cost = 0

def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

print("Initial Environment:", environment)

while True:
    status = environment[location] # the room where the vacuum is currently located is dirty or clean.
    action = reflex_agent(location, status)

    print(f"\nVacuum is at {location}")
    print(f"Room Status : {status}")
    print(f"Action Taken: {action}")

    if action == "Suck":
        environment[location] = "Clean"
        path_cost += 1      # Cost for cleaning

    elif action == "Right":
        location = "B"
        path_cost += 1      # Cost for moving

    elif action == "Left":
        location = "A"
        path_cost += 1      # Cost for moving

    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nBoth rooms are clean.")
        break

print("\nFinal Environment:", environment)
print("Total Path Cost:", path_cost)
