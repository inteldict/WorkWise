import os
from datetime import datetime, timedelta

from platform import system

if system() == 'Windows':
    from msvcrt import getch

    os.system('color')
else:
    from getch import getch

# define program name and version
PROGRAM_NAME = "WorkWise"
PROGRAM_VERSION = "1.3"


class BColors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


REQUIRED_TIME = timedelta(hours=7, minutes=48)
LUNCH_BREAKS = (
    (timedelta(minutes=0), timedelta(hours=6, minutes=0)),
    (timedelta(minutes=30), timedelta(hours=7, minutes=48)),
    (timedelta(minutes=45), timedelta(hours=9, minutes=0)),
)


def calculate_time(hours: int, minutes: int) -> None:
    default_time = datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
    print("\nHere are some alternatives:")
    for i, (lunch_break, delta) in enumerate(LUNCH_BREAKS):
        target_time = default_time + delta + lunch_break
        balance_change = delta - REQUIRED_TIME
        hours, minutes = timedelta_hm(balance_change)

        print(colorize(hours, f"{i+1}. Checkout at {target_time.strftime('%H:%M')}: "
                              f"Lunch break: {lunch_break.total_seconds() // 60:02.0f}m, "
                              f"time balance change: {hm_formatter(hours, minutes)}"))
    print()


def timedelta_str(td: timedelta) -> str:
    if td.days < 0:
        return '-' + str(timedelta() - td)
    return str(td)


def timedelta_hm(td: timedelta) -> (int, int):
    is_negative = False
    total_seconds = int(td.total_seconds())
    if total_seconds < 0:
        is_negative = True
    total_minutes = total_seconds // 60
    hours, minutes = divmod(abs(total_minutes), 60)
    if is_negative:
        hours = -hours
    return hours, minutes


def hm_formatter(hours, minutes) -> str:
    return f"{hours:02d}:{minutes:02d}"


def colorize(hours: int, out_str: str) -> str:
    if hours < 0:
        return f"{BColors.FAIL}{out_str}{BColors.ENDC}"
    elif hours == 0:
        return f"{BColors.OK_GREEN}{out_str}{BColors.ENDC}"
    else:
        return f"{BColors.WARNING}{out_str}{BColors.ENDC}"


def get_input_time() -> tuple:
    hours = 0
    minutes = 0

    print(f"Welcome to {PROGRAM_NAME} v{PROGRAM_VERSION}!\n")

    while True:
        try:
            time_str = input("Enter the time (HH:MM): ")
            hours, minutes = map(int, time_str.split(':'))
            if not (0 <= hours <= 23):
                print("Invalid hour value! Hour value should be between 0 and 23. Try again.\n")
                continue

            if not (0 <= minutes <= 59):
                print("Invalid minute value! Minute value should be between 0 and 59. Try again.\n")
                continue
            break
        except ValueError:
            print("Invalid time format. Try again.\n")
            continue
    return hours, minutes


def any_key():
    print("Press any key to exit...")
    getch()


def main():
    calculate_time(*get_input_time())
    any_key()


if __name__ == '__main__':
    main()
