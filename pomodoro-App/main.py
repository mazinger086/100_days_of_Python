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

def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    title.config(text="Timer", fg=GREEN)
    #reset check_marks
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def star_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    # If it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    # If it's 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # De esta manera modificas el texto del canvas
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) #ms - llamado a la funcion - args - 1
    else:
        star_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        # if reps % 2 == 0:
        checkmark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
# window.minsize(width=305, height=300)
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # De esta manera haces referencia a la imagen
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



#Labels
title = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 36, "bold"), fg=GREEN)
title.grid(row=0, column=1)


checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
checkmark.grid(row=3, column=1)

# Buttons
start_btn = Button(text="Start", font=(FONT_NAME, 14, "normal"), highlightthickness=0, command=star_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 14, "normal"), highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)






window.mainloop()