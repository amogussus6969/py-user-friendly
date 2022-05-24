#Simple Gui System

import tkinter as tk

def createWindow(windowName):
    myStr = windowName + "=tk.Tk()"
    exec(myStr)

def createLabel(windowName, labelName, labelText):
    myStr = labelName + "=tk.Label(" + windowName + "," + "text=" + labelText + ")"
    exec(myStr)

def createButton(windowName, buttonName, buttonText, commandFunction):
    myStr = buttonName + "=tk.Button(" + windowName + "," + "text=" + buttonText + ", command=" + commandFunction + ")"
    exec(myStr)

def createEntry(windowName, entryName):
    myStr = entryName + "=tk.Entry(" + windowName + ")"
    exec(myStr)
    
def createFrame(windowName, frameName):
    myStr = frameName + "=tk.Frame(" + windowName + ")"
    exec(myStr)

def createCanvas(windowName, canvasName):
    myStr = canvasName + "=tk.Canvas(" + windowName + ")"
    exec(myStr)

def createListbox(windowName, listboxName):
    myStr = listboxName + "=tk.Listbox(" + windowName + ")"
    exec(myStr)

def createScrollbar(windowName, scrollbarName):
    myStr = scrollbarName + "=tk.Scrollbar(" + windowName + ")"
    exec(myStr)

def createMenu(windowName, menuName):
    myStr = menuName + "=tk.Menu(" + windowName + ")"
    exec(myStr)

def createMenuItem(menuName, menuItemName, menuItemText):
    myStr = menuItemName + "=tk.MenuItem(" + menuName + "," + "text=" + menuItemText + ")"
    exec(myStr)

def createMenuButton(menuName, menuButtonName, menuButtonText, commandFunction):
    myStr = menuButtonName + "=tk.MenuButton(" + menuName + "," + "text=" + menuButtonText + ", command=" + commandFunction + ")"
    exec(myStr)

def createMenuSeparator(menuName):
    myStr = menuName + ".add_separator()"
    exec(myStr)

def createMenuCheckbutton(menuName, menuCheckbuttonName, menuCheckbuttonText, commandFunction):
    myStr = menuCheckbuttonName + "=tk.MenuCheckbutton(" + menuName + "," + "text=" + menuCheckbuttonText + ", command=" + commandFunction + ")"
    exec(myStr)

def createMenuRadiobutton(menuName, menuRadiobuttonName, menuRadiobuttonText, commandFunction):
    myStr = menuRadiobuttonName + "=tk.MenuRadiobutton(" + menuName + "," + "text=" + menuRadiobuttonText + ", command=" + commandFunction + ")"
    exec(myStr)

def createMenuCascade(menuName, menuCascadeName, menuCascadeText):
    myStr = menuCascadeName + "=tk.MenuCascade(" + menuName + "," + "text=" + menuCascadeText + ")"
    exec(myStr)

def createMenuCommand(menuName, menuCommandName, menuCommandText, commandFunction):
    myStr = menuCommandName + "=tk.MenuCommand(" + menuName + "," + "text=" + menuCommandText + ", command=" + commandFunction + ")"
    exec(myStr)

