# Global variables
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    # Return total number of chocolates received by all children
    return sum(chocolates_received)

def reward_child(child_id_rewarded, extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return

    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        return

    # Find index of the child and update chocolates
    index = child_id.index(child_id_rewarded)
    chocolates_received[index] += extra_chocolates

    # Display the updated chocolates list
    print(chocolates_received)

# Test the functions
print(calculate_total_chocolates())   # Should print total chocolates

# Try rewarding valid child
reward_child(20, 2)   # Valid case

# Additional test cases (optional for testing)
# reward_child(60, 3)   # Invalid child ID
# reward_child(30, 0)   # Invalid extra chocolates
