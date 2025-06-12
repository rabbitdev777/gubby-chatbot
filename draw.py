from turtle import *
import tkinter
import commands

screen = Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

command = textinput("entew cowwmand!!", 'Welcome to ur new "friend"(he is evil) gubby!!\n list of commands:\n'
                                        '1) draw a cool spiral!\n'
                                        '2) calculate!\n'
                                        '3) generate music, actually sing a song lol\n'
                                        '4) tell weather\n'
                                        '5) translate\n'
                                        '6) ask gubby what does he like\n'
                                        '7) draw gubby!\n'
                                        '8) ask what does gubby wants on this planet...\n'
                                        '9) exit :(')
while command != "9" and command != "exit" and command is not None and root.winfo_exists():
    bgcolor("white")
    if command == "1":
        commands.drawaspiral()
    elif command == "2":
        commands.calculate()
    elif command == "3":
        commands.singasong()
    elif command == "4":
        commands.weather()
    elif command == "5":
        commands.translate()
    elif command == "6":
        commands.whatgubbylike()
    elif command == "7":
        commands.drawgubby()
    elif command == "8":
        commands.wdgwotp()
    else:
        commands.idk()
        print("vro idk what command is thwat -gubby")
    command = textinput("entew cowwmand!!", 'Welcome to ur new "friend"(he is evil) gubby!!\n list of commands:\n'
                                            '1) draw a cool spiral!\n'
                                            '2) calculate!\n'
                                            '3) generate music, actually sing a song lol\n'
                                            '4) tell weather\n'
                                            '5) translate\n'
                                            '6) ask gubby what does he like\n'
                                            '7) draw gubby!\n'
                                            '8) ask what does gubby wants on this planet...\n'
                                            '9) exit :(')
    canvas.update()

exit()