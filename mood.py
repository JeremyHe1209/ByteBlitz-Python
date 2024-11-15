class Mood:
    isAngry: bool = False
    isHappy: bool = False
    def __init__(self) -> None:
        self.isAngry = False
        self.isHappy = False
        return
    def getIfItIs(self, key: str) -> None:
        if key == "":
            return True
        if key == "angry":
            return self.isAngry
        if key == "happy":
            return self.isHappy
        if key == "not angry":
            return not self.isAngry
        if key == "not happy":
            return not self.isHappy
        if key == "angry + happy":
            return self.isAngry and self.isHappy
        if key == "angry + not happy":
            return self.isAngry and (not self.isHappy)
        if key == "not angry + happy":
            return (not self.isAngry) and self.isHappy
        if key == "not angry + not happy":
            return (not self.isAngry) and (not self.isHappy)
        return False
    def getMoodString(self) -> str:
        if (self.getIfItIs("angry + happy")):
            return "Bing so angry that be smiling"
        if (self.getIfItIs("angry + not happy")):
            return "Bing angry very much"
        if (self.getIfItIs("not angry + happy")):
            return "Bing happy a lot"
        if (self.getIfItIs("not angry + not happy")):
            return "Bing normal"
        return ""
