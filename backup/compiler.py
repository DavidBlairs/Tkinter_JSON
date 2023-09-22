import tkinter

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

            widgetAttributes = {}
            manmadeAttributes = {}
            for key in currentObjDictionary:
                if key[0] == "c":
                    widgetAttributes[key.split(".")[1]] = currentObjDictionary[key]
                if key[0] == "s":
                    manmadeAttributes[key.split(".")[1]] = currentObjDictionary[key]

            self.widgets.append((widgetAttributes, manmadeAttributes))

        self.FrameDictionary["Tk"] = tkinter.Tk()

        for widget in self.widgets:
            for frame in self.FrameDictionary:
                if frame == widget[1]["master"]:
                    tempMaster = self.FrameDictionary[frame]
            tempFrameClass = getattr(tkinter, widget[1]["objectType"])(tempMaster)

            for option in widget[0]:
                try:
                    tempFrameClass.config(**{option: widget[0][option]})
                except:
                    tempFrameClass.grid(**{option: widget[0][option]})

            self.FrameDictionary[widget[1]["objectName"]] = tempFrameClass
        self.FrameDictionary["Tk"].mainloop()



