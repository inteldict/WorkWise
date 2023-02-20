# Calculate end of working day in order to reduce/avoid overtime

from datetime import datetime, timedelta

REQUIRED_TIME = timedelta(hours=7, minutes=48)
LUNCH_BREAK = timedelta(minutes=30)


def calculate_time(hours: int, minutes: int) -> str:
    current_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    target_time = current_time + timedelta(hours=hours, minutes=minutes) + REQUIRED_TIME + LUNCH_BREAK
    return target_time.strftime("%Y-%m-%d %H:%M:%S")


def get_input_time():
    hours_str = input("Enter the hour (0-23): ")
    minutes_str = input("Enter the minute (0-59): ")
    hours = int(hours_str)
    minutes = int(minutes_str)
    return hours, minutes


def main():
    print(calculate_time(*get_input_time()))


if __name__ == '__main__':
    main()
