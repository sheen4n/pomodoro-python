from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    start_button["state"] = "normal"

    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Start Button
def start():
    start_button["state"] = "disabled"

    global reps
    reps += 1

    if reps % 2 == 1:
        minutes = WORK_MIN
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        timer_label.config(text="Break", fg=RED)
    else:
        minutes = SHORT_BREAK_MIN
        timer_label.config(text="Break", fg=PINK)

    count_down(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    canvas.itemconfig(timer_text, text=format_seconds_to_minute(count))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            ticks = "✓" * (reps // 2 + 1)
            tick_label.config(text=ticks)
        start()


def format_seconds_to_minute(seconds):
    min_text = str(seconds // 60).rjust(2, '0')
    sec_text = str(seconds % 60).rjust(2, '0')
    return f"{min_text}:{sec_text}"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

# Tick Label
tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

start_button = Button(text="Start", command=start, highlightthickness=1, highlightbackground=YELLOW, fg="black")
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", command=reset, highlightthickness=1, highlightbackground=YELLOW, fg="black")
reset_button.grid(row=2, column=2)

window.mainloop()
