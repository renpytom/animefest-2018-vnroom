# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default preferences.fullscreen = False

label main_menu:
    return

style text:
    font "Oswald-Medium.ttf"
    color "#fff"
    outlines [ (1, "#000C", 0, 0), (2, "#0008", 0, 0), (3, "#0004", 0, 0)  ]

style button_text:
    font "Oswald-Medium.ttf"
    color "#fff"
    outlines [ (1, "#000C", 0, 0), (2, "#0008", 0, 0), (3, "#0004", 0, 0) ]
    hover_outlines [ (1, "#00FC", 0, 0), (2, "#00F8", 0, 0), (3, "#00F4", 0, 0) ]

init python:
    import os
    import subprocess

    class Launch(Action):
        def __init__(self, project):
            self.project = project

        def __call__(self):

            executable_path = os.path.dirname(renpy.fsdecode(sys.executable))

            if renpy.windows:
                extension = ".exe"
            else:
                extension = ""

            executables = [ "pythonw" + extension ]
            executables.append(sys.executable)

            for i in executables:
                executable = os.path.join(executable_path, i)
                if os.path.exists(executable):
                    break
            else:
                raise Exception("Python interpreter not found: %r", executables)

            # Put together the basic command line.
            cmd = [ executable, "-EO", sys.argv[0] ]

            cmd.append(os.path.join(config.renpy_base, self.project))

            # Launch the project.
            cmd = [ renpy.fsencode(i) for i in cmd ]

            p = subprocess.Popen(cmd)

    def Hover(ss):
        return [
            Show("timer", bg=ss),
            ]

default background = "#000"

screen timer(bg):
    timer .5 action [ SetVariable("background", bg), With(dissolve), Hide("timer") ]

screen launcher():
    add background size (1920, 1080)

    frame:
        style "empty"
        xmargin 50

        has vbox

        text "Animefest 2018 VN Room" size 100

        text "Please select a game to play. Hover for more information.":
            yoffset -5
            size 20

        textbutton "Backstage Pass":
            text_size 40
            action Launch("backstagepass-1i-pc")
            hovered Hover("backstagepass.png")

        textbutton "Corona Borealis":
            text_size 40
            action Launch("Corona Borealis")
            hovered Hover("Corona Borealis.png")

        textbutton "The D (Stands for Demon)":
            text_size 40
            action Launch("TheD")
            hovered Hover("TheD.png")

        textbutton "Hart Connection":
            text_size 40
            action Launch("Hart Connection")
            hovered Hover("Hart Connection.png")

        textbutton "Perceptions of the Dead 2":
            text_size 40
            action Launch("PotD2-1.0-market")
            hovered Hover("POTD2.jpg")

        textbutton "Rising Angels Hope":
            text_size 40
            action Launch("Rising_Angels_Hope-market")
            hovered Hover("RA.png")

        textbutton "The Shadows That Run Alongside Our Car":
            text_size 40
            action Launch("Shadows")
            hovered Hover("Shadows.png")

        textbutton "Without a Voice":
            text_size 40
            action Launch("Without a Voice DEMO")
            hovered Hover("Without a Voice.png")




# The game starts here.

label start:
    $ quick_menu = False

    call screen launcher

    return
