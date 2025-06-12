from turtle import *
import winsound
import time
import random
from googletrans import Translator
import requests

api_key = "e9091c7b53e643ea41bffc394402b920"
dodo = Turtle()
colors = ["red", "yellow", "green", "cyan", "pink", "orange", "violet", "grey", "blue"]
notes = [262, 294, 330, 349, 392, 440, 494]# c d e f g a b
duration = [200, 300, 400]
def idk():
    clearscreen()
    dodo.color("black")
    dodo.penup()
    dodo.goto(-150,200)
    dodo.pendown()
    dodo.write("vro idk what command is thwat -gubby", font=("Bradley Hand ITC", 15, "normal"))
def drawaspiral():
    clearscreen()
    sides = numinput("gubby draws a spiral. ", "entew the amount of siiiides (write 10 to leave) !! ", 3, 2, 10)
    dodo.speed(1000)
    bgcolor("black")
    while sides != 10 and sides is not None:
        for i in range(360):
            dodo.pencolor(colors[i%len(colors)])
            dodo.forward(i*3/sides+i)
            dodo.right(360/sides+1)
            dodo.width(i*sides/300)
        sides = numinput("gubby draws a spiral. ", "entew the amount of siiiides (write 10 to leave) !! ", 3, 2, 10)

def calculate():
    clearscreen()
    dodo.color("orange")
    espresso = textinput("gubby is a nerd", "enter ur calculation")
    res = eval(espresso)
    dodo.penup()
    dodo.goto(200, 200)
    dodo.pendown()
    dodo.write(f"{espresso} = {res}",  font=("Bradley Hand ITC", 15, "normal"))

def singasong():
    endtime = time.time()+5
    while time.time() < endtime:
        freq = random.choice(notes)
        dur = random.choice(duration)
        winsound.Beep(freq, dur)

def weather():
    clearscreen()
    city = textinput("gubby wants your ip adress. muheheeh", "enter the city ur in: (10 to exit)")
    while city != "10" and city != "exit" and city is not None:
        clearscreen()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}"
        try:
            data = requests.get(url).json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            icon = data["weather"][0]["main"].lower()
        except Exception as e:
            temp, desc, icon = None, f"Error: {e}", None
        if icon == "clear":
            dodo.penup()
            dodo.goto(-150, 130)
            dodo.pendown()
            dodo.begin_fill()
            dodo.color("yellow")
            for i in range(18):
                dodo.forward(150)
                dodo.right(100)
            dodo.end_fill()
            dodo.color("black")
        elif icon == "clouds":
            dodo.setheading(0)
            cloudy()
        elif icon in ('rain', 'drizzle'):
            dodo.setheading(0)
            cloudy()
            rainy()
        elif icon == "snow":
            dodo.setheading(0)
            snowy()
        else:
            dodo.penup()
            dodo.goto(-150, 200)
            dodo.pendown()
            dodo.color("black")
            dodo.write("no weather icon!", font=("Bradley Hand ITC", 15, "normal"))
        text = f"{city}: {desc}, {temp}oC" if temp is not None else desc
        dodo.penup()
        dodo.goto(-150, 200)
        dodo.pendown()
        dodo.write(text, font=("Bradley Hand ITC", 15, "normal"))
        city = textinput("gubby wants your ip adress. muheheeh", "enter the city ur in: (10 to exit)")


def cloudy():
    dodo.speed(100)
    dodo.color("grey")
    dodo.pensize(17)
    dodo.begin_fill()
    dodo.circle(100)
    dodo.end_fill()
    dodo.penup()
    dodo.goto(120,25)
    dodo.pendown()
    dodo.begin_fill()
    dodo.circle(50)
    dodo.end_fill()
    dodo.penup()
    dodo.goto(-120,15)
    dodo.pendown()
    dodo.begin_fill()
    dodo.circle(75)
    dodo.end_fill()


def rainy():
    dodo.pensize(10)
    dodo.color("blue")
    dodo.penup()
    dodo.goto(-130,-30)
    dodo.pendown()
    dodo.left(-90)
    dodo.forward(30)

    dodo.penup()
    dodo.goto(-90,-30)
    dodo.pendown()
    dodo.forward(20)

    dodo.penup()
    dodo.goto(-50,-30)
    dodo.pendown()
    dodo.forward(40)

    dodo.penup()
    dodo.goto(-20,-20)
    dodo.pendown()
    dodo.forward(40)

    dodo.penup()
    dodo.goto(20,-20)
    dodo.pendown()
    dodo.forward(60)

    dodo.penup()
    dodo.goto(50,-20)
    dodo.pendown()
    dodo.forward(20)

    dodo.penup()
    dodo.goto(80,-20)
    dodo.pendown()
    dodo.forward(35)

    dodo.penup()
    dodo.goto(110,-20)
    dodo.pendown()
    dodo.pensize(10)
    dodo.forward(50)


def snowy():
    clearscreen()
    dodo.pensize(7)
    dodo.speed(100)
    dodo.color("light blue")
    dodo.left(90)
    dodo.forward(150)
    dodo.left(180)
    dodo.forward(75)
    dodo.left(90)
    dodo.forward(75)
    dodo.left(180)
    dodo.forward(150)
    dodo.right(60)
    dodo.forward(30)
    dodo.left(180)
    dodo.forward(30)
    dodo.right(80)
    dodo.forward(30)
    dodo.penup()
    dodo.goto(0,150)
    dodo.pendown()
    dodo.right(90)
    dodo.forward(30)
    dodo.left(180)
    dodo.forward(30)
    dodo.right(-90)
    dodo.forward(30)
    dodo.penup()
    dodo.goto(75, 75)
    dodo.pendown()
    dodo.forward(30)
    dodo.left(180)
    dodo.forward(30)
    dodo.right(-90)
    dodo.forward(30)
    dodo.penup()
    dodo.goto(-0,-0)
    dodo.pendown()
    dodo.forward(30)
    dodo.left(180)
    dodo.forward(30)
    dodo.right(-90)
    dodo.forward(30)


def translate():
    clearscreen()
    translator = Translator()
    choice = textinput("gubby is a nerd once again! but a language one.", "choice language:\n"
                                                                          "1: russian to english\n"
                                                                          "2: english to russian\n"
                                                                          "off to exit")
    while choice != "exit" and choice != "off" and choice is not None:
        clearscreen()
        if choice == "1":
            src, dest = "ru", "en"
        elif choice == "2":
            src, dest = "en", "ru"
        else:
            dodo.penup()
            dodo.goto(-150, 200)
            dodo.pendown()
            dodo.write("no commands chosen!", font=("Bradley Hand ITC", 15, "normal"))
            choice = textinput("gubby is a nerd once again! but a language one.", "choice language:\n"
                                                                                  "1: russian to english\n"
                                                                                  "2: english to russian\n"
                                                                                  "off to exit")
            continue
        text = textinput("gubbys text: ", f"write da word or text in {'english' if src == 'en' else 'russian'}")
        result = translator.translate(text, src=src, dest=dest)
        dodo.penup()
        dodo.goto(-150, 200)
        dodo.pendown()
        dodo.write(f"перевод: {result.text}", font=("Bradley Hand ITC", 15, "normal"))
        choice = textinput("gubby is a nerd once again! but a language one.", "choice language:\n"
                                                                              "1: russian to english\n"
                                                                              "2: english to russian\n"
                                                                              "off to exit")


def whatgubbylike():
    clearscreen()
    dodo.color("black")
    dodo.penup()
    dodo.goto(-150,200)
    dodo.pendown()
    dodo.write("i like to eat grass and sleep", font=("Bradley Hand ITC", 15, "normal"))

def drawgubby():
    clearscreen()
    dodo.setheading(0)
    dodo.speed(100)
    dodo.left(30)
    dodo.forward(50)
    dodo.left(60)
    dodo.forward(120)
    dodo.left(60)
    dodo.forward(50)
    dodo.left(30)
    dodo.forward(90)
    dodo.left(30)
    dodo.forward(50)
    dodo.left(60)
    dodo.forward(120)
    dodo.left(60)
    dodo.forward(50)
    dodo.left(30)
    dodo.forward(90)
    dodo.right(90)
    dodo.forward(30)
    dodo.right(90)
    dodo.forward(20)
    dodo.right(90)
    dodo.forward(30)
    dodo.left(90)
    dodo.forward(45)
    dodo.left(90)
    dodo.forward(30)
    dodo.right(90)
    dodo.forward(20)
    dodo.right(90)
    dodo.forward(30)
    dodo.penup()
    dodo.goto(11,180)
    dodo.pendown()
    dodo.forward(60)
    dodo.left(30)
    dodo.forward(30)
    dodo.left(60)
    dodo.forward(80)
    dodo.left(60)
    dodo.forward(30)
    dodo.left(30)
    dodo.forward(60)
    dodo.left(30)
    dodo.forward(30)
    dodo.left(60)
    dodo.forward(80)
    dodo.left(60)
    dodo.forward(30)
    dodo.forward(4)
    dodo.penup()
    dodo.goto(8,270)
    dodo.pendown()
    dodo.left(30)
    dodo.forward(60)
    dodo.left(150)
    dodo.forward(70)
    dodo.penup()
    dodo.right(60)
    dodo.forward(30)
    dodo.pendown()
    dodo.right(60)
    dodo.forward(70)
    dodo.left(150)
    dodo.forward(60)
    dodo.penup()
    dodo.goto(3,225)
    dodo.pendown()
    dodo.right(70)
    dodo.forward(30)
    dodo.right(20)
    dodo.penup()
    dodo.forward(40)
    dodo.pendown()
    dodo.right(20)
    dodo.forward(30)
    dodo.left(110)
    dodo.penup()
    dodo.forward(40)
    dodo.left(90)
    dodo.forward(20)
    dodo.left(30)
    dodo.pendown()
    dodo.forward(30)
    dodo.right(70)
    dodo.forward(20)
    dodo.left(50)
    dodo.forward(18)


def wdgwotp():
    clearscreen()
    dodo.color("red")
    dodo.goto(150,200)
    dodo.write("i wanna wipe out humanity. ", font=("Chiller", 15, "normal"))