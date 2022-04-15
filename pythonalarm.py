# importing all the necassary libraies needed to form the alarm clock
from tkinter import * #the tkinter is the basic python gui. 
import datetime # this imports the date and time modules so that we can work with the current day and manipulate it
import time 
import winsound # allows access to the basic sounds in the windows platform

def alarm(set_alarm_timer): # define a funtion named alarm with the argument set_alarm_timer|it contains a while loop with the boolean function True
    while True:
        time.sleep(1) # this sets the timer for 1s until further commands are executed|kinda like a wait for 1 second "command"
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S") #sets the current time to be represented by the variable "now"
        date = current_time.strftime("%d/%m?%Y") #sets the current date to be represented by the variable "date"
        print("The Set Date is:",date)
        print(now) # prints the current time
        if now == set_alarm_timer: #executes the alarm if the current time is set to the time you set your alarm too
            print("TIME TO WAKE UP!!!")
            winsound.Playsound("sound.wav", winsound.SND_ASYNC)
            break

def actual_time(): #the function named actual time allows the user to set their alarm time
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)




clock = Tk()

clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text= "Enter time in 24 hour format! \nMake Sure to Enter number with 2 characters \n ie. 01 02", fg="red", bg="white", font = "Arial").place(x=60,y=120)
addTime = Label(clock, text = "Hour Min  Sec",font=60).place(x=110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

#Below are the variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Below are the time entries needed to set the alarm clock
hourTime = Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=110,y=30)
minTime = Entry(clock,textvariable = min,bg = "white",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=200,y=30)

#Below allows to take the time iput by the user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x=110,y=70)

clock.mainloop()























