from source import tokenRules


class Tokenizer(object):
    def __init__(self, workingFileDirectory):
        self.workingFileObject   = open(str(workingFileDirectory), "r")
        self.workingFileContents = self.workingFileObject.read()

        self.workingFileContents = self.workingFileContents.replace(" ", "")
        self.workingFileContents = self.workingFileContents.replace("_", " ")

        self.workingFileContentLines = []
        workingFileContentsLines = self.workingFileContents.split("\n")

        for line in range(len(workingFileContentsLines)):
            for token in range(len(workingFileContentsLines[line])):
                self.workingFileContentLines.append(int(line) + 1)

        self.workingFileContents = self.workingFileContents.replace("\n", "")

        self.currentTokenIndex = 0

        self.objectScopes = []
        self.chosenIndex  = 0

        self.currentObject = tokenRules.Program.tokenRule
        self.currentObjectLocations = [0]


    def getToken(self):
        return self.workingFileContents[self.currentTokenIndex]

    def getTokenLine(self):
        return self.workingFileContentLines[self.currentTokenIndex]

    class GetOutOfLoop(Exception):
        pass

    def mainloop(self):
        currentTokenSearch = 0
        for index in self.currentObjectLocations:
            try:
                for acceptedToken in self.currentObject[index][0]:
                    if type(acceptedToken) == list:
                        if self.getToken() in acceptedToken[0][0]:
                            self.objectScopes = [(self.currentObject, index)] + self.objectScopes
                            self.currentObject = list(acceptedToken)
                            self.chosenIndex = 0
                            raise self.GetOutOfLoop

                    elif self.getToken() == acceptedToken:
                        self.chosenIndex = int(index)
                        raise self.GetOutOfLoop

            except self.GetOutOfLoop:
                break
            currentTokenSearch += 1


        if currentTokenSearch == len(self.currentObjectLocations):
            raise SyntaxError("Token is invalid: \"" + str(self.getToken()) + "\" on line " + str(self.getTokenLine()))

        if self.chosenIndex + 1 == len(self.currentObject):
            if len(self.objectScopes) > 0:
                self.currentObject = self.objectScopes[0][0]
                self.chosenIndex = self.objectScopes[0][1]
                self.objectScopes.remove(self.objectScopes[0])

        self.currentObjectLocations = self.currentObject[self.chosenIndex][1]

        self.currentTokenIndex += 1


x = Tokenizer("test.tk")
for i in x.workingFileContents:
    x.mainloop()

