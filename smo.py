class EDF:
    currentTime = 0
    Tw = [0 for x in range(10000)]
    Tn = [0 for y in range(10000)]
    faults = [0 for z in range(10000)]
    Q = []
    Qready = []
    currentTask = None
    currentTask2 = None
  

    def __init__(self, Q):
        self.Q = Q

    def GetEDTask(self, removeFromQ):
        timeBuf = 9999999
        taskwED = None
        for i in range(len(self.Qready)):
            newTime = self.Qready[i].getDeadline()
            if timeBuf > newTime:
                timeBuf = newTime
                taskwED = self.Qready[i]
        if removeFromQ:
            self.Qready.remove(taskwED)
        return taskwED

    def ToReadyQueue(self):
        for i in range(len(self.Q)):
            if self.Q[i].getCreationTime() == self.currentTime:
                self.Qready.append(self.Q[i])

    def CheckForDeadlines(self):
        flt = 0
        flti = []
        for i in range(len(self.Qready)):
            if self.Qready[i].getDeadline() < self.currentTime:
                flt += 1
                flti.append(i)
        if self.currentTime == 0:
            self.faults[self.currentTime] = flt
        else:
            self.faults[self.currentTime] = self.faults[self.currentTime - 1] + flt
        for i in range(len(flti)):
            del self.Qready[flti[i]]
            for j in range(i, len(flti)):
                flti[j] -= 1

    # Modelling
    def work(self):
        self.currentTime = 0
        for self.currentTime in range(10000):
            if self.currentTime != 0:
                self.Tn[self.currentTime] = self.Tn[self.currentTime - 1]
            timewait = 0
            self.CheckForDeadlines()
            self.ToReadyQueue()
            if self.currentTask is not None and self.currentTask.getExecutionTime() == 0:
                self.currentTask = None
            elif self.currentTask is not None and self.GetEDTask(False) is not None:
                if self.GetEDTask(False).getExecutionTime() < self.currentTask.getExecutionTime():
                    self.Qready.append(self.currentTask)
                    self.currentTask = self.GetEDTask(True)
            elif self.currentTask is not None:
                self.currentTask.workedOn()
            if self.currentTask is not None:
                self.currentTask2.workedOn()
            if self.getEDTask(False) is None and self.currentTask is None:
                self.currentTask2.workedOn()
                continue
            elif self.currentTask is None:
                self.currentTask = self.getEDTask(True)

    def GetWaitTimes(self):
        return self.Tw

    def GetFaults(self):
        return self.faults

    def GetProcessorFreeTime(self):
        return self.Tn


class RM:
    currentTime = 0
    Tw = [0 for x in range(10000)]
    Tn = [0 for y in range(10000)]
    faults = [0 for z in range(10000)]
    Q = []
    Qready = []
    currentTask = None
    currentTask2 = None

    def __init__(self, Q):
        self.Q = Q

    def getEDTask(self, removeFromQ):
        timeBuf = 9999999
        taskwED = None
        for i in range(len(self.Qready)):
            newTime = self.Qready[i].getDeadline()
            if timeBuf > newTime:
                timeBuf = newTime
                taskwED = self.Qready[i]
        if removeFromQ:
            self.Qready.remove(taskwED)
        return taskwED

    def ToReadyQueue(self):
        for i in range(len(self.Q)):
            if self.Q[i].getCreationTime() == self.currentTime:
                self.Qready.append(self.Q[i])

    def CheckForDeadlines(self):
        flt = 0
        flti = []
        for i in range(len(self.Qready)):
            if self.Qready[i].getDeadline() < self.currentTime:
                flt += 1
                flti.append(i)
        if self.currentTime == 0:
            self.faults[self.currentTime] = flt
        else:
            self.faults[self.currentTime] = self.faults[self.currentTime - 1] + flt
        for i in range(len(flti)):
            del self.Qready[flti[i]]
            for j in range(i, len(flti)):
                flti[j] -= 1

    # Modelling
    def work(self):
        self.currentTime = 0
        for self.currentTime in range(10000):
            if self.currentTime != 0:
                self.Tn[self.currentTime] = self.Tn[self.currentTime - 1]
            timewait = 0
            self.CheckForDeadlines()
            self.ToReadyQueue()
            if self.currentTask is not None and self.currentTask.getExecutionTime() == 0:
                self.currentTask = None
            elif self.currentTask is not None:
                self.currentTask.workedOn()
            if self.currentTask is not None:
                self.currentTask2.workedOn()
            if self.getEDTask(False) is None and self.currentTask is None:
                self.currentTask2.workedOn()
                continue
            elif self.currentTask is None:
                self.currentTask = self.getEDTask(True)

    def GetWaitTimes(self):
        return self.Tw

    def GetFaults(self):
        return self.faults

    def GetProcessorFreeTime(self):
        return self.Tn
