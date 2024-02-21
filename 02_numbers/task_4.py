def format_seconds(seconds):
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour

    days = seconds // seconds_in_day
    seconds %= seconds_in_day

    hours = seconds // seconds_in_hour
    seconds %= seconds_in_hour

    minutes = seconds // seconds_in_minute
    seconds %= seconds_in_minute

    return f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}"


# Example:
total_seconds = 100000
formatted_time = format_seconds(total_seconds)
print("Formatted time:", formatted_time)
