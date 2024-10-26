from tkinter import *
import math

BG = "#f8eded"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", font=(FONT_NAME, 31, "bold"), bg=BG, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        label.config(text="Long Break", font=(FONT_NAME, 31, "bold"), bg=BG, fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short Break", font=(FONT_NAME, 31, "bold"), bg=BG, fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", font=(FONT_NAME, 31, "bold"), bg=BG, fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minute = math.floor(count / 60)
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"
    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)

        for _ in range(work_session):
            marks += "✔"
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG)

canvas = Canvas(width=200, height=224, bg=BG, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 125, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", font=(FONT_NAME, 31, "bold"), bg=BG, fg=GREEN)
label.grid(column=2, row=1)

start_button = Button(width=5, height=1, text="Start", bg=BG, command=start_timer)
start_button.grid(column=1, row=3)

end_button = Button(width=5, height=1, text="Reset", command=reset_timer)
end_button.grid(column=3, row=3)

check = Label(text=" ", font=(FONT_NAME, 21), fg="GREEN")
check.grid(column=2, row=4)

window.mainloop()
