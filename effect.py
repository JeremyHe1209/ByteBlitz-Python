# 这个东西还没有写完，所以千万不要碰！

from buff import *
from role import *

class Effect:
    name: str = ""
    type: str = ""
    # All, Enemy, Self or Single
    legalattacktimesdelta: int = 0
    buff = Buff()
    newfigures: [str] = []
    deletefigures: [str] = []
    def __init__(self, name: str, type: str, legalattacktimesdelta: int, buff: Buff, newfigures: [str], deletefigures: [str]):
        self.name = name
        self.buff = buff
        self.legalattacktimesdelta = legalattacktimesdelta
        self.newfigures = newfigures
        self.deletefigures = deletefigures
        return
    def happens(self, battleroles: [Role], round: int, roleid: int, roleids: [int] = []):
        # 对于Single，须在玩家选择时就确保选择合法
        if self.type == "All":
            for role in battleroles:
                role.ahstates.insert([self.buff])
                role.legalattacktimes += self.legalattacktimesdelta
                role.giveFigures(self.newfigures)
                role.deleteFigures(self.deletefigures)
        elif self.type == "Enemy":
            for role in battleroles:
                if isEnemy(role.id, roleid):
                    role.ahstates.insert([self.buff])
                    role.legalattacktimes += self.legalattacktimesdelta
                    role.giveFigures(self.newfigures)
                    role.deleteFigures(self.deletefigures)
        elif self.type == "Self":
            for role in battleroles:
                if isEnemy(role.id, roleid):
                    role.ahstates.insert([self.buff])
                    role.legalattacktimes += self.legalattacktimesdelta
                    role.giveFigures(self.newfigures)
                    role.deleteFigures(self.deletefigures)
        elif self.type == "Single":
            for role in battleroles:
                if role.id in roleids:
                    role.ahstates.insert([self.buff])
                    role.legalattacktimes += self.legalattacktimesdelta
                    role.giveFigures(self.newfigures)
                    role.deleteFigures(self.deletefigures)
        return
