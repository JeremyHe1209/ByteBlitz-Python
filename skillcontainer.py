from skill import *

class SkillContainer:
    skills = list[Skill]
    def __init__(self, skills : list[Skill]) -> None:
        self.skills = skills
        return
    def findskill(self, name : str) -> Skill:
        for skill in self.skills:
            if skill.name == name:
                return skill
        return None
    def addskill(self, skill : Skill) -> None:
        if self.findskill(skill.name) == None:
            self.skills.append(skill)
        return
    def removeskill(self, name : str) -> None:
        for skill in self.skills:
            if skill.name == name:
                self.skills.remove(skill)
                break
        return