# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Create the base reminder
reminder = ""

# Use match-case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Use an if statement to check if task is time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"
else:
    reminder += " — Consider completing it when you have free time."

# Final output using a loop to emphasize the reminder (for example, repeat it 1 time only)
for _ in range(1):
    print("Note:", reminder)
# --- IGNORE ---