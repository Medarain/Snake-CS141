from gui import Gui
import time
def main():
    gui = Gui()                       # takes over the screen
    width = gui.get_width()           # gets the width
    height = gui.get_height()         # gets the height
    gui.log("The width is " + str(width))      # logs the output
    gui.log("The height is " + str(height))
    i = 0
    while True:
        gui.clear()           # clear the screen
        # draw everything you want to draw
        gui.draw_text("Hasu", 10, i, "RED", "BLUE")
        i += 1
        gui.refresh()         # show to the user all at once
        time.sleep(0.1)       # sleep for 1/10 of a second
    gui.quit()                        # always quit gracefully
if __name__ == "__main__":
    main()