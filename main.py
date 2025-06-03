import os
import time


def main():
    total_time_secs = {
        "work": 0,
        "break": 0,
        "long_break": 0
    }

    # Ask the user to input the times for each category
    total_time_secs["work"] = ask_user_for_time("work routine")
    total_time_secs["break"] = ask_user_for_time("break")
    total_time_secs["long_break"] = ask_user_for_time("long break")

    # Start the Pomodoro timer with a work cycle
    current_cycle = "work"
    work_cycles_count = 0 # this will keep count of work cycles completed to select the type of break

    while True:
        clear_console() # clearing the console before starting a new cycle
        start_cycle(current_cycle, total_time_secs[current_cycle])

        # Check the current completed cycle
        if current_cycle == "work":
            work_cycles_count += 1
            
            # Every 4 work cycles we'll take a long break
            if work_cycles_count % 4 == 0:
                current_cycle = "long_break"
            else:
                # Otherwise, just a regular break
                current_cycle = "break"
        # If the current cycle is any type of break, the next one will be work
        else:
            current_cycle = "work"


def start_cycle(current_cycle, total_time_secs):
    ANIMATION_FRAME_TIME = 2  # seconds for the animation frames

    # work animation emojis and timing
    work_animation = [
        "ʕっ•ᴥ•ʔっ",
        "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
        "ʕ•ᴥ•ʔ",
    ]
    work_animation_length = len(work_animation) * ANIMATION_FRAME_TIME

    # break animation emojis and timing. This will have a different logic than the work animation
    break_animation = [
        "(•_•)",
        "( •_•)>⌐■-■",
        "(⌐■_■)",
        "ᕕ(⌐■_■)ᕗ ♪♬",
        "\(⌐■_■)ノ ♬♪"
    ]


    for elapsed_time in range(total_time_secs + 1):
        
        # Logic for work messages
        if current_cycle == "work":
            print("You've got this! Keep working!", end=" ") # printing without a new line

            # Display the work animation based on elapsed time
            if elapsed_time % work_animation_length < ANIMATION_FRAME_TIME:
                print(work_animation[0])
            if elapsed_time % work_animation_length >= ANIMATION_FRAME_TIME and elapsed_time % work_animation_length < 2*ANIMATION_FRAME_TIME:
                print(work_animation[1])
            if elapsed_time % work_animation_length >= 2*ANIMATION_FRAME_TIME:
                print(work_animation[2])

        # Logic for break messages
        elif current_cycle == "break":
            print("Time for a break! Relax and recharge!", end=" ") # printing without a new line

            # Display the break animation based on elapsed time
            print_break_animation(break_animation, elapsed_time, ANIMATION_FRAME_TIME)

        elif current_cycle == "long_break":
            print("Enjoy your long break! You deserve it!", end=" ")
            print_break_animation(break_animation, elapsed_time, ANIMATION_FRAME_TIME/2)  # Faster animation for long breaks
        
        print_elapsed_time(elapsed_time)
        print_progress_bar(elapsed_time, total_time_secs)
        time.sleep(1) # update every second
        clear_console()



def ask_user_for_time(category):
    user_input = -1
    while user_input <= 0:
        try:
            user_input = int(input(f"Enter the number of minutes for your {category}: "))
            if user_input <= 0:
                print("Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a integer.")
    return user_input * 60  # Convert minutes to seconds

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_progress_bar(current, total, bar_length = 50):
    if total <= 0:
        percent = 100
    else:
        percent = current / total

    filled = int(bar_length * percent)
    empty = bar_length - filled
    bar = '[' + '█' * filled + '▒' * empty + ']'

    print(bar)

def print_elapsed_time(elapsed):
    minutes, seconds = divmod(elapsed, 60)
    print(f"Elapsed time: {minutes:02}min {seconds:02}sec")

def print_break_animation(break_animation, elapsed_time, frame_time):
    # Display the break animation based on elapsed time
    if elapsed_time < frame_time:
        print(break_animation[0])
    elif elapsed_time < 2 * frame_time:
        print(break_animation[1])
    elif elapsed_time < 3 * frame_time:
        print(break_animation[2])
    elif (elapsed_time % (2 * frame_time) - frame_time) >= 0:
        print(break_animation[3])
    else:
        print(break_animation[4])


if __name__ == "__main__":
    main()