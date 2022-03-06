from tkinter import *
import math

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
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfigure(canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# 25min work <-> 5min break => repeat 4 times
# after that, take a 15-30 min break
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break")
        timer_label.config(fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "Break")
        timer_label.config(fg = PINK)
    else:
        count_down(work_sec)
        timer_label.config(text = "Work")
        timer_label.config(fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:    
            start_timer()
            if reps % 2 == 0:
                check_label.config(text ="✔" * int(reps / 2))
        else:
            reps = 0
            timer_label.config(text="Timer", fg=GREEN)
            check_label.config(text="")

    min = math.floor(count / 60)
    if min < 10:
        min = f"0{min}"

    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfigure(canvas_text, text=f"{min}:{sec}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="pomodoro_start/tomato.png")
canvas.create_image(100, 112, image=image)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row= 1, column=1)

# timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row= 0, column=1)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 10, 'bold'), borderwidth=0)
start_button.config(command=start_timer)
start_button.grid(row= 2, column=0)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), borderwidth=0)
reset_button.config(command=reset)
reset_button.grid(row= 2, column=2)

# check_label
check_label = Label(fg=GREEN, bg=YELLOW, font=("bold"))
check_label.grid(row= 3, column=1)

window.mainloop()
