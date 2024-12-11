import random
from datetime import datetime, timedelta

def generate_random_timestamps(start_date, end_date, num_timestamps):
    current_date = start_date
    timestamps = []
    
    while len(timestamps) < num_timestamps:
        timestamps.append(current_date.strftime('%Y-%m-%d'))
        
        # Randomly decide how many days to skip (1 to 10 days)
        skip_days = random.randint(1, 3)  # Change this range for larger skips
        current_date += timedelta(days=skip_days)
        
        # Ensure we don't go past the end date
        if current_date > end_date:
            break
            
    return timestamps

# Define the date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 10)

# Generate 1000 random timestamps
random_timestamps = generate_random_timestamps(start_date, end_date, 1000)

# Print the generated timestamps
print(random_timestamps)

def max_consecutive_days(timestamps, max_gap):
    # Convert string timestamps to datetime objects
    dates = sorted([datetime.strptime(ts, '%Y-%m-%d') for ts in timestamps])
    
    max_consecutive = 0
    current_streak = 1
    
    for i in range(1, len(dates)):
        # Calculate the difference in days
        day_diff = (dates[i] - dates[i - 1]).days
        
        if day_diff <= max_gap + 1:  # Allow for the specified gap
            current_streak += 1
        else:
            max_consecutive = max(max_consecutive, current_streak)
            current_streak = 1  # Reset streak
    
    # Final check for the last streak
    max_consecutive = max(max_consecutive, current_streak)
    
    return max_consecutive

# Calculate maximum consecutive days for different gap conditions
max_zero = max_consecutive_days(random_timestamps, 0)
max_consecutive_1_day = max_consecutive_days(random_timestamps, 1)
max_consecutive_2_days = max_consecutive_days(random_timestamps, 2)
max_consecutive_10_days = max_consecutive_days(random_timestamps, 10)

print(f"Maximum consecutive days: {max_zero}")
print(f"Maximum consecutive days (1 day gap allowed): {max_consecutive_1_day}")
print(f"Maximum consecutive days (2 days gap allowed): {max_consecutive_2_days}")
print(f"Maximum consecutive days (10 days gap allowed): {max_consecutive_10_days}")
