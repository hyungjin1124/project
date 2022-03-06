from tkinter import *
import time

from matplotlib import image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

IS_GAME_ON = True
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global IS_GAME_ON
    canvas.itemconfigure(canvas_text, text="00:00")
    check_label['text'] = ""
    IS_GAME_ON = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# 25min work <-> 5min break => repeat 4 times
# after that, take a 15-30 min break
def timer():
    global IS_GAME_ON
    IS_GAME_ON = True
    for _ in range(3):
        count_down(WORK_MIN)
        count_down(SHORT_BREAK_MIN)
        if IS_GAME_ON:
            check_label['text'] += "✔"
    count_down(WORK_MIN)
    if IS_GAME_ON:
        check_label['text'] += "✔"
    count_down(LONG_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(total_min):
    for min in range(total_min - 1, -1, -1):
        for sec in range(59, -1, -1):
            if not IS_GAME_ON:
                return 
            canvas.itemconfigure(canvas_text, text=f"{min:02d}:{sec:02d}")
            window.update()
            time.sleep(0.0001)
            
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
start_button.config(command=timer)
start_button.grid(row= 2, column=0)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), borderwidth=0)
reset_button.config(command=reset)
reset_button.grid(row= 2, column=2)

# check_label
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=("bold"))
check_label.grid(row= 3, column=1)

window.mainloop()

