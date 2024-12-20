from classes import *

class Mood:
    isangry: bool = False
    ishappy: bool = False
    def __init__(self) -> None:
        self.isangry = False
        self.ishappy = False
        return
    def getIfItIs(self, key: str) -> None:
        if key == "":
            return True
        if key == "angry":
            return self.isangry
        if key == "happy":
            return self.ishappy
        if key == "not angry":
            return not self.isangry
        if key == "not happy":
            return not self.ishappy
        if key == "angry + happy":
            return self.isangry and self.ishappy
        if key == "angry + not happy":
            return self.isangry and (not self.ishappy)
        if key == "not angry + happy":
            return (not self.isangry) and self.ishappy
        if key == "not angry + not happy":
            return (not self.isangry) and (not self.ishappy)
        return False
    def getMoodString(self) -> str:
        if (self.getIfItIs("angry + happy")):
            return "Being so angry that be smiling"
        if (self.getIfItIs("angry + not happy")):
            return "Being angry very much"
        if (self.getIfItIs("not angry + happy")):
            return "Being happy a lot"
        if (self.getIfItIs("not angry + not happy")):
            return "Being normal"
        return ""
