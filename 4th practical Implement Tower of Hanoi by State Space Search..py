#Q)Implementation of Tower of Hanoi Using State Space Search
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 0:
        return


    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)


    # Move the largest disk to destination
    print(f"Move disk {n} from {source} -> {destination}")


    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)




# Main program
n = int(input("Enter number of disks: "))


print("\nTower of Hanoi using State Space Search:")
tower_of_hanoi(n, 'A', 'B', 'C')


print("\nMinimum number of moves:", 2**n - 1)
