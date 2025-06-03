import os
import time


def main():

    total_time_secs = ask_user_for_time()
    elapsed_time = 0

    for i in range(total_time_secs + 1):
        print_progress_bar(elapsed_time, total_time_secs)
        time.sleep(1)
        elapsed_time += 1
        clear_console()

def ask_user_for_time():
    # TODO: Implement a function to ask the user for the total time in minutes and seconds
    return 100

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_progress_bar(current, total, bar_length = 50):
    if total <= 0:
        percent = 100
    else:
        percent = current / total

    filled = int(bar_length * percent)
    empty = bar_length - filled
    bar = '[' + '█' * filled + '-' * empty + ']'

    print(bar)

if __name__ == "__main__":
    main()