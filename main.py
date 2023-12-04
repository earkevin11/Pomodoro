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
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #to change the text inside the tomato, we must use canvas.itemconfig
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="TIMER")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps +=1

    # If it's the 8th rep, long 25 min break
    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="LONG BREAK",fg=RED)
    #if reps is at 2 / 4 / 6, short 5 min break
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="SHORT BREAK",fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="GET TO WORK",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count/60)
    # modulo gets the remainder as seconds
    count_sec = count % 60
    # type int == type string?? this is called dynamic typing. Python allows dynamic changing of a variable type
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down , count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks = marks + "✓"
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#This stores our tomato.png file into the variable
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
#create text allows us to add text onto the canvas
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME,55,"bold"))
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark_label = Label(text="",fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
checkmark_label.grid(column=1,row=3)


window.mainloop()