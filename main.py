import matplotlib.pyplot as plt
import random
import er as er
import task
import smo
import numpy

a = []
lam = 1
k = 2
E = er.erDistribution(k, lam)

def GenerateQ():
    Q = []
    i = 0
    time = GenerateTime()
    while i < 10000:
        i += E.GenerateNextInternal() * 8
        t = task.task(i, time)
        Q.append(t)
    return Q

def GenerateTime():
    rnd = random.random()
    if rnd < 0.3:
        ans = random.randrange(7)  # Rxy
    elif 0.3 <= rnd < 0.6:
        ans = random.randrange(5)  # Rxx
    elif 0.6 <= rnd < 0.8:
        ans = random.randrange(3)  # Dx
    else:
        ans = random.randrange(2)  # Mx
    return ans + 40


if __name__ == "__main__":
    QuEDF = []
    QuRM = []
    smos = []
    RMs = []
    Tw = []
    Tww =[]
    Tn = []
    t = [x for x in range(10000)]
    faults = []
    # Changes
    faultschange = []
    Tnchange = []
    Twchange = []
    FullWaitTime = []

    for lam in numpy.arange(1, 20, 0.5):
        E.ChangeLambda(lam)
        temp = GenerateQ()
        QuEDF.append(temp)

    QuRM = QuEDF[:]

    for i in range(len(QuEDF)):
        smos.append(smo.EDF(QuEDF[i]))
        RMs.append(smo.RM(QuRM[i]))

    buf1 = []
    buf2 = []
    buf3 = []

    def calculate(arr):
        for elem in arr:
            elem.work()
            buf1 = elem.GetFaults()
            buf2 = elem.GetWaitTimes()
            buf3 = elem.GetProcessorFreeTime()
            faults.append(buf1[:])
            Tw.append(buf2[:])
            Tn.append(buf3[:])

        for elem in range(len(arr)):
            faultschange.append(faults[elem][9999])
            Tnchange.append(Tn[elem][9999])

        for o in range(len(arr)):
            time = 0
            for elem in range(10000):
                time += Tw[o][elem]
            FullWaitTime.append(time)

        for elem in range(len(arr)):
            Tww.append(FullWaitTime[elem])

        plt.plot(Tnchange, 'r')
        plt.show()
        plt.plot(faultschange, 'g')
        plt.show()
        plt.plot(Tww, 'k')
        plt.show()

        buf1.clear()
        buf2.clear()
        buf3.clear()
        Tw.clear()
        Tn.clear()
        faults.clear()
        faultschange.clear()
        Tnchange.clear()
        Twchange.clear()
        Tww.clear()

    calculate(smos)

    calculate(RMs)




