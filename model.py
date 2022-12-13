from subFunc import *
from units import *
from unit import *


def model(workShiftTime, period, workTeam, coutUM1Bul, coutUM2Man, priceMan, priceBul, priceWorkM1, priceWorkM2, teamDap):
    uM1 = UnitMech("Buldozer")
    uM2 = UnitMech("Manipulator")

    master1 = UnitRepair("6")
    master2 = UnitRepair("3")

    for i in range(period):
        uM1.workTimeState = exp(1)
        uM2.workTimeState = exp(2)
        uM1.workTime += uM1.workTimeState
        uM2.workTime += uM2.workTimeState
        for j in range(workShiftTime * 60):
            freeM(master1, master2, workTeam)
            if uM1.state == -1:
                if uM1.workTimeState == 0:
                    if workTeam:
                        getTimeRepair1(master1, master2, uM1, True)
                    else:
                        getTimeRepair2(master1, uM1, True)
                else:
                    uM1.workTimeState -= 1
            elif uM1.state == 0:
                if workTeam:
                    getTimeRepair1(master1, master2, uM1, True)
                else:
                    getTimeRepair2(master1, uM1, True)
            elif uM1.state == 1:
                if uM1.repairTimeState == 0:
                    uM1.state = -1
                    uM1.workTimeState = exp(2)
                    uM1.workTime += uM1.workTimeState
                else:
                    uM1.repairTimeState -= 1
            

            freeM(master1, master2, workTeam)
            if uM2.state == -1:
                if uM2.workTimeState == 0:
                    if workTeam:
                        getTimeRepair1(master1, master2, uM2, True)
                    else:
                        getTimeRepair2(master1, uM2, True)

                else:

                    uM2.workTimeState -= 1
            elif uM2.state == 0:
             
                if workTeam:
                    getTimeRepair1(master1, master2, uM2, True)
                else:
                    getTimeRepair2(master1, uM2, True)
            elif uM2.state == 1:
                if uM2.repairTimeState == 0:
                    uM2.state = -1
                    uM2.workTimeState = exp(4)
                    uM2.workTime += uM2.workTimeState
                else:
                    uM2.repairTimeState -= 1

        for j in range(8 * 60):
            freeM(master1, master2, workTeam)
            if uM1.state != -1 or uM2.state != -1:
                if uM1.state == 0:
                    if workTeam:
                        getTimeRepair1(master1, master2, uM1, False)
                    else:
                        getTimeRepair2(master1, uM1, False)
                    freeM(master1, master2, workTeam)
                elif uM1.state == 1:
                    if uM1.repairTimeState == 0:
                        uM1.state = -1
                    else:
                        uM1.repairTimeState -= 1
                    freeM(master1, master2, workTeam)

                if uM2.state == 0:
                    if workTeam:
                        getTimeRepair1(master1, master2, uM2, False)
                    else:
                        getTimeRepair2(master1, uM2, False)
                    freeM(master1, master2, workTeam)
                elif uM2.state == 1:
                    if uM2.repairTimeState == 0:
                        uM2.state = -1
                    else:
                        uM2.repairTimeState -= 1
                    freeM(master1, master2, workTeam)
            else:
                break
        
        # print("День: " + str(i))
        # print(str(uM1.name) + " Работа: " + str(uM1.workTime))
        # print(str(uM2.name) + " Работа: " + str(uM2.workTime))
        # print(str(uM1.name) + " Простой: " + str(uM1.cont))
        # print(str(uM2.name) + " Простой: " + str(uM2.cont))
        



    getGlobalData(master1, master2, uM1, uM2, coutUM1Bul, coutUM2Man, priceMan, priceBul, priceWorkM1, priceWorkM2, teamDap, workTeam)
