from datetime import datetime


def get_current_date():
    """Return the current date."""
    return datetime.now().strftime("%Y-%m-%d")


def get_current_datetime():
    """Return the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")