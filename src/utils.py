DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def next_week_day(day):
    try:
        index = DAYS.index(day)
    except ValueError:
        return "Invalid day"

    # Calculate the index of the next day
    next_index = (index + 1) % len(DAYS)

    # Return the next day of the week
    return DAYS[next_index]