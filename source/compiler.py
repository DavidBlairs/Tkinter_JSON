import tkinter
import os

class Compiler(object):
    def __init__(self, workingFileContents):
        self.workingFileContents = str(workingFileContents)[1:-1]
        self.widgets = []
        self.CompleteWidgets = []

        self.FrameDictionary = {}

    def compile(self):
        FrmBsWidgets = self.workingFileContents.split(">")[1:]
        for obj in FrmBsWidgets:
            spliced = obj[1:-1].split(",")
            currentObjDictionary = {}

            spliced = list(filter(None, spliced))

            for dictObj in spliced:
                aspects = dictObj.split(":")

                if aspects[1][0] == "\"":
                    aspects[1] = str(aspects[1][1:-1])

                elif aspects[1][0] == "#":
                    aspects[1] = float(aspects[1][1:-1])
                    if aspects[1].is_integer():
                        aspects[1] = int(aspects[1])

                aspects[0] = aspects[0][1:-1]
                currentObjDictionary[aspects[0]] = aspects[1]

            manmadeAttributes = {}
            configAttributes = {}
            gridAttributes = {}

            for key in currentObjDictionary:
                if key[0] == "s":
                    manmadeAttributes[key.split(".")[1]] = currentObjDictionary[key]
                if key[0] == "c":
                    configAttributes[key.split(".")[1]] = currentObjDictionary[key]
                if key[0] == "g":
                    gridAttributes[key.split(".")[1]] = currentObjDictionary[key]

            self.widgets.append((manmadeAttributes, configAttributes, gridAttributes))

        self.Window = tkinter.Tk()
        self.FrameDictionary["Tk"] = tkinter.Frame(self.Window)
        self.FrameDictionary["Tk"].grid(column=0, row=0)

        for widget in self.widgets:
            for frame in self.FrameDictionary:
                if frame == widget[0]["master"]:
                    tempMaster = self.FrameDictionary[frame]
            tempFrameClass = getattr(tkinter, widget[0]["objectType"])(tempMaster)

            for option in widget[1]:
                    tempFrameClass.config(**{option: widget[1][option]})
            for option in widget[2]:
                    tempFrameClass.grid(**{option: widget[2][option]})

            self.FrameDictionary[widget[0]["objectName"]] = tempFrameClass

        self.FrameDictionary["Tk"].mainloop()


        


