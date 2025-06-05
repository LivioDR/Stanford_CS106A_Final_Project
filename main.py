import time
from display_functions import clear_console, print_intro_text, print_progress_bar, print_remaining_time, print_work_animation, print_break_animation

def main():

    # Definition of the time dictionary 
    total_time_secs = {
        "work": 0,
        "break": 0,
        "long_break": 0
    }

    clear_console()  # Clear the console before starting
    # Explain the purpose of the command line app to the user
    print_intro_text()

    # Ask the user to input the times for each category
    total_time_secs["work"] = ask_user_for_time("work routine")
    total_time_secs["break"] = ask_user_for_time("break")
    total_time_secs["long_break"] = ask_user_for_time("long break")

    # Start the Pomodoro timer with a work cycle
    current_cycle = "work"
    work_cycles_count = 0 # this will keep count of work cycles completed to select the type of break
    LONG_BREAK_AFTER_CYCLES = 4 # after how many work cycles we take a long break


    # Main loop for the Pomodoro timer
    while True:
        clear_console() # clearing the console before starting a new cycle
        start_cycle(current_cycle, total_time_secs[current_cycle])

        # Check the current completed cycle
        if current_cycle == "work":
            work_cycles_count += 1
            
            # Every 4 work cycles we'll take a long break
            if work_cycles_count % LONG_BREAK_AFTER_CYCLES == 0:
                current_cycle = "long_break"
            else:
                # Otherwise, just a regular break
                current_cycle = "break"
        # If the current cycle is any type of break, the next one will be work
        else:
            current_cycle = "work"


'''
This function starts the Pomodoro cycle for the given current cycle type
It handles the work, break, and long break cycles, displaying appropriate messages and animations.
It also manages the elapsed time and progress bar display for each cycle by calling their respective functions.
'''
def start_cycle(current_cycle, total_time_secs):
    ANIMATION_FRAME_TIME = 2  # seconds for the animation frames


    for elapsed_time in range(total_time_secs + 1):
        
        # Logic for work messages
        if current_cycle == "work":
            print("You've got this! Keep working!", end=" ") # printing without a new line

            # Display the work animation based on elapsed time
            print_work_animation(elapsed_time, ANIMATION_FRAME_TIME)

        # Logic for break messages
        elif current_cycle == "break":
            print("Time for a break! Relax and recharge!", end=" ") # printing without a new line

            # Display the break animation based on elapsed time
            print_break_animation(elapsed_time, ANIMATION_FRAME_TIME)

        elif current_cycle == "long_break":
            print("Enjoy your long break! You deserve it!", end=" ")

            # Display the break animation based on elapsed time
            print_break_animation(elapsed_time, ANIMATION_FRAME_TIME/2)  # Faster animation for long breaks
        
        # Print the elapsed time and progress bar
        print_progress_bar(elapsed_time, total_time_secs)
        print_remaining_time(elapsed_time, total_time_secs)

        # Sleep for 1 second to wait for the passage of time
        time.sleep(1)

        # Clear the console for the next iteration
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


if __name__ == "__main__":
    main()