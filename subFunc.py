from unit import exp
import math


def freeM(m1, m2, workTeam):
    if m1.machine != 0: 
        if m1.machine.repairTimeState == 0:
            m1.machine = 0
            m1.state = 0
    if m2.machine != 0:
        if m2.machine.repairTimeState == 0:
            m2.machine = 0
            m2.state = 0


def getTimeRepair1(m1, m2, uM, status):
    if uM.name == "Buldozer":
        if m1.state == 0 and m2.state == 0:
            time = exp(1.5)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            m2.state = 1
            m2.repairTimeState = time
            m2.repairTime += time
            m1.machine = uM
            m2.machine = uM
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
        elif m1.state == 1 and m2.state == 0:
            time = exp(2)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
            m1.machine = uM
        elif m1.state == 0 and m2.state == 1:
            uM.state = 0
            if status:
                uM.cont += 1
        else:
            uM.state = 0
            if status:
                uM.cont += 1

        

    if uM.name == "Manipulator" and uM.repairTimeState == 0:
        if m1.state == 0 and m2.state == 0:
            time = exp(0.25)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            m2.state = 1
            m2.repairTimeState = time
            m2.repairTime += time
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
            m1.machine = uM
            m2.machine = uM
        elif m1.state == 1 and m2.state == 0:
            time = exp(1)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
            m1.machine = uM
        elif m1.state == 0 and m2.state == 1:
            time = exp(2)
            m2.state = 1
            m2.repairTimeState = time
            m2.repairTime += time
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
            m2.machine = uM
        else:
            uM.state = 0
            if status:
                uM.cont += 1



def getTimeRepair2(m1, uM, status):
    if uM.name == "Buldozer" and uM.repairTimeState == 0:
        if m1.state == 0:
            time = exp(2)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            m1.machine = uM
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
        elif m1.state == 1:
            uM.state = 0
            if status:
                uM.cont += 1

    if uM.name == "Manipulator" and uM.repairTimeState == 0:
        if m1.state == 0:
            time = exp(1)
            m1.state = 1
            m1.repairTimeState = time
            m1.repairTime += time
            uM.state = 1
            uM.repairTimeState = time
            if status:
                uM.cont += time
            m1.machine = uM
        elif m1.state == 1:
            uM.state = 0
            if status:
                uM.cont += 1


def getGlobalData(m1, m2, u1, u2, coutUM1Bul, coutUM2Man, priceMan, priceBul, priceWorkM1, priceWorkM2, teamDap, workTeam):
    print("#" * 10 + " Отчет " + "#" * 10)

    print(str(u1.name) + " Работал: " + str(u1.workTime/60) + " часов")
    print(str(u1.name) + " Проистаивал: " + str(u1.cont/60) + " часов")

    print(str(u2.name) + " Работал: " + str(u2.workTime/60) + " часов")
    print(str(u2.name) + " Проистаивал: " + str(u2.cont/60) + " часов")

    print(str(m1.specClass) + " Работал: " + str(m1.repairTime/60) + " часов")
    print(str(m2.specClass) + " Работал: " + str(m2.repairTime/60) + " часов")


    wtU1 = math.ceil((u1.cont/60)* coutUM1Bul)
    wtU2 = math.ceil((u2.cont/60) * coutUM2Man)
    wM1 = math.ceil((m1.repairTime/60) * priceWorkM1)
    wM2 = math.ceil((m2.repairTime/60) * priceWorkM2)

    wTeam = math.ceil(((u1.cont/60) + (u2.cont/60)) * teamDap)

    pU1 = math.ceil((u1.workTime/60) * priceBul)
    pU2 = math.ceil((u2.workTime/60) * priceMan)

    

    if workTeam:
        print("Суммарные расходы: " + str(wtU1 + wtU2 + wM1 + wM2 + wTeam))
        print("Доход: " + str(pU1 + pU2))
        print("Читстая прибыль: " + str((pU1 + pU2) - (wtU1 + wtU2 + wM1 + wM2 + wTeam)))
    else:
        print("Суммарные расходы: " + str(wtU1 + wtU2 + wM1))
        print("Доход: " + str(pU1 + pU2))
        print("Читстая прибыль: " + str((pU1 + pU2) - (wtU1 + wtU2 + wM1)))

    print("#" * 20)


    

    


