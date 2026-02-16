"""
Author: <Anastasiia Stoianova>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Step c: Create a dictionary named workout_stats
# dict: keys are friend names (str), values are tuples of 3 workout minutes (int)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (50, 60, 30),
    "Taylor": (20, 30, 25)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    if isinstance(minutes, tuple):
        total = sum(minutes)
        workout_stats[friend + "_Total"] = total
        print(f"{friend}'s total workout minutes: {total}")

print(workout_stats)

# Step e: Create a 2D nested list called workout_list
# list: 2D nested list of workout minutes (each row is a friend, each column is an activity)
workout_list = [list(minutes) for friend, minutes in workout_stats.items() if isinstance(minutes, tuple)]
print(workout_list)

# Step f: Slice the workout_list
# Extract yoga and running minutes (columns 0 and 1) for all friends
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0:2])

# Extract weightlifting minutes (column 2) for the last two friends
print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120
for friend, minutes in workout_stats.items():
    if isinstance(minutes, tuple):
        total = sum(minutes)
        if total >= 120:
            print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats and isinstance(workout_stats[friend_name], tuple):
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend: workout_stats[friend + "_Total"] for friend in workout_stats if isinstance(workout_stats[friend], tuple)}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Highest total: {highest_friend} with {totals[highest_friend]} minutes")
print(f"Lowest total: {lowest_friend} with {totals[lowest_friend]} minutes")
