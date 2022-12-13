from model import model
import os


class App():
    def __init__(self, _teamWork) -> None:
        self.workShiftTime = 16
        self.period = 10
        self.coutUM1Bul = 5000
        self.coutUM2Man = 3000
        self.priceMan = 5000
        self.priceBul = 3000
        self.priceWorkM1 = 1000
        self.priceWorkM2 = 600
        self.teamDap = 500
        self.teamWork = _teamWork

    def startSimulation(self):
        model(self.workShiftTime, self.period, self.teamWork, self.coutUM1Bul, self.coutUM2Man,
              self.priceMan, self.priceBul, self.priceWorkM1, self.priceWorkM2, self.teamDap)



ms = App(False)
ms.startSimulation()

