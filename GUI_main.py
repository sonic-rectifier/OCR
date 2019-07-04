
import tkinter
from tkinter import filedialog
from tkinter import *
import DigitalPhoenix as DP
from tools import *
from array import *

# CONSTANTS are declared here
# this is where you can swap between odd (remainder of 1) or even (remainder of 0)
X_COORDINATE_MODULUS = 0
SMALLEST_X_INDEX = 0
LARGEST_X_INDEX = 1
SMALLEST_Y_INDEX = 2
LARGEST_Y_INDEX = 3

# Global variables declared here
coordinatesArray = [[0, 0]]


def setNewPageSize(pointValueArray):
    """
    this is the function to set the new size of the page when the
    data is returned from Google

    Parameters:
    pointValueArray: array of integers representing the size of the page
    the values are [smallest x, largest x, smallest y, largest y]

    """
    # first check to see if we have negative numbers
    if pointValueArray[SMALLEST_X_INDEX] < 0:
        pointValueArray[LARGEST_X_INDEX] += abs(pointValueArray[SMALLEST_X_INDEX])
        pointValueArray[SMALLEST_X_INDEX] = 0

    if pointValueArray[SMALLEST_Y_INDEX] < 0:
        pointValueArray[LARGEST_Y_INDEX] += abs(pointValueArray[SMALLEST_Y_INDEX])
        pointValueArray[SMALLEST_Y_INDEX] = 0
    # now figure out the width and height of the panel
    panel_width = pointValueArray[LARGEST_X_INDEX] - pointValueArray[SMALLEST_X_INDEX]
    panel_height = pointValueArray[LARGEST_Y_INDEX] - pointValueArray[SMALLEST_Y_INDEX]

    top.wm_minsize(panel_width, panel_height)


def callback():
    """This is the function that handles the open file button"""

    filename = "handwriting.jpg"
    filename = filedialog.askopenfilename(title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    text = DP.detect_document(filename)
    label.config(text=text)
    coordinates = DP.getCoordinates()
    index = 0
    for sets in coordinates:
        currentSet = [sets[0].x, sets[0].y, sets[1].x, sets[1].y, sets[2].x, sets[2].y, sets[3].x, sets[3].y]
        coordinatesArray.insert(index, currentSet)
        index += 1
    setNewPageSize(findLargestXY(coordinatesArray))


def findLargestXY(coorArray):
    """
    function to take an array of 4 values and return the largest X and Y
    :param coorArray: array of x y pairs
    coorArray[X.Y,X,Y,X,Y,..etc.]
    :return: array of largest X value and largest Y value

    """
    largestX = 0
    largestY = 0
    smallestX = 9999
    smallestY = 9999

    for set in coorArray:
        counter = 0
        for point in set:
            if counter % 2 == X_COORDINATE_MODULUS:
                # number is even so it's a x coordinate
                if point > largestX:
                    largestX = point
                if point < smallestX:
                    smallestX = point
            else:
                # number is odd so it's a y coordinate
                if point > largestY:
                    largestY = point
                if point < smallestY:
                    smallestY = point
            counter += 1
    # pack into a nice array for return
    return_array = [smallestX, largestX, smallestY, largestY]

    return return_array


def addText(textToAdd):
    label.config(text=textToAdd)


if __name__ == "__main__":
    top = tkinter.Tk(className="Digital Phoenix")
    top.configure()
    top.wm_minsize(500, 500)
    # top.wm_maxsize(500, 500)

    # Code to add widgets will go here...
    button = tkinter.Button(command=callback)
    # button["text"] = "Hello World\n(click me)"
    button["text"] = "Load File"
    button.pack(side="top")

    label = tkinter.Label(text="this is a test", fg="black", bg="white")
    label.pack(side="top")
    top.mainloop()


