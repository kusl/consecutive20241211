import random
from datetime import datetime, timedelta
import pytz

def generate_random_timestamps_iso(start_date, end_date, num_timestamps):
    current_date = start_date
    timestamps = []
    
    while len(timestamps) < num_timestamps:
        # Generate timestamp in ISO 8601 format
        timestamps.append(current_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        
        # Randomly decide how many days to skip (1 to 3 days)
        skip_days = random.randint(1, 3)  # Change this range for larger skips
        current_date += timedelta(days=skip_days)
        
        # Ensure we don't go past the end date
        if current_date > end_date:
            break
            
    return timestamps

# Define the date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 10)

# Generate 1000 random timestamps in ISO 8601 format
random_timestamps_iso = generate_random_timestamps_iso(start_date, end_date, 1000)

def max_consecutive_days_iso(timestamps, max_gap, timezone):
    # Convert string timestamps to datetime objects in the specified timezone
    tz = pytz.timezone(timezone)
    dates = sorted([datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(tz) for ts in timestamps])
    
    max_consecutive = 0
    current_streak = 1
    
    for i in range(1, len(dates)):
        # Calculate the difference in days
        day_diff = (dates[i].date() - dates[i - 1].date()).days
        
        if day_diff <= max_gap + 1:  # Allow for the specified gap
            current_streak += 1
        else:
            max_consecutive = max(max_consecutive, current_streak)
            current_streak = 1  # Reset streak
    
    # Final check for the last streak
    max_consecutive = max(max_consecutive, current_streak)
    
    return max_consecutive

# Specify the timezone (e.g., 'America/New_York' for US Eastern Time)
timezone = 'America/New_York'

# Calculate maximum consecutive days for different gap conditions using ISO format
max_consecutive_0_day_iso = max_consecutive_days_iso(random_timestamps_iso, 0, timezone)
max_consecutive_1_day_iso = max_consecutive_days_iso(random_timestamps_iso, 1, timezone)
max_consecutive_2_days_iso = max_consecutive_days_iso(random_timestamps_iso, 2, timezone)
max_consecutive_10_days_iso = max_consecutive_days_iso(random_timestamps_iso, 10, timezone)

print(f"Maximum consecutive days (0 day gap allowed, ISO): {max_consecutive_0_day_iso}")
print(f"Maximum consecutive days (1 day gap allowed, ISO): {max_consecutive_1_day_iso}")
print(f"Maximum consecutive days (2 days gap allowed, ISO): {max_consecutive_2_days_iso}")
print(f"Maximum consecutive days (10 days gap allowed, ISO): {max_consecutive_10_days_iso}")
