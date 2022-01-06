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
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    timer.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    # timer_text.config(text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 2 == 1:
        count_down(work_sec)
        timer.config(text="WORK",fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="BREAK",fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="BREAK", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
def count_down(count):
    global my_timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")



timer = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer.grid(column=1,row=0)

start = Button(text="Start",bg=YELLOW,highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",bg=YELLOW,highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

checkmark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
checkmark.grid(column=1,row=3)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# count_down(5)


window.mainloop()