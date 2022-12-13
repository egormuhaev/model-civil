class UnitMech:
    def __init__(self, _name) -> None:
        self.name = _name
        self.workTime = 0 
        self.workTimeState = 0
        self.cont = 0
        self.repairTimeState = 0
        self.state = -1 
    


class UnitRepair:
    def __init__(self, _specClass) -> None:
        self.specClass = _specClass
        self.state = 0
        self.repairTime = 0
        self.repairTimeState = 0
        self.machine = 0

