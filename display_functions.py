import os


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

def print_remaining_time(elapsed, total):
    minutes, seconds = divmod((total-elapsed), 60)
    print(f"Remaining time: {minutes:02}min {seconds:02}sec")


def print_work_animation(elapsed_time, frame_time):
    # work animation emojis and timing
    work_animation = [
        "ʕっ•ᴥ•ʔっ",
        "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
        "ʕ•ᴥ•ʔ",
    ]
    work_animation_length = len(work_animation) * frame_time

    # Display the work animation based on elapsed time
    if elapsed_time % work_animation_length < frame_time:
        print(work_animation[0])
    if elapsed_time % work_animation_length >= frame_time and elapsed_time % work_animation_length < 2*frame_time:
        print(work_animation[1])
    if elapsed_time % work_animation_length >= 2*frame_time:
        print(work_animation[2])


def print_break_animation(elapsed_time, frame_time):

    # break animation emojis and timing. This will have a different logic than the work animation
    break_animation = [
        "(•_•)",
        "( •_•)>⌐■-■",
        "(⌐■_■)",
        "ᕕ(⌐■_■)ᕗ ♪♬",
        "\(⌐■_■)ノ ♬♪"
    ]

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
