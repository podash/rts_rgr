class task:

    deadline = 0
    creationTime = 0
    executionTime = 0
    deadlineMultiplier = 0
    waitTime = 0

    def __init__(self, creationTime, executionTime):
        self.executionTime = int(executionTime)
        self.creationTime = int(creationTime)
        self.deadline = int(creationTime + executionTime * self.deadlineMultiplier)

    def getTimeLimit(self):
        return self.deadline + self.creationTime

    def getDeadline(self):
        return self.deadline

    def workedOn(self):
        self.executionTime = self.executionTime - 1

    def wait(self):
        self.waitTime = self.waitTime + 1

    def getExecutionTime(self):
        return self.executionTime

    def getCreationTime(self):
        return self.creationTime

    def completed(self):
        return True if self.waitTime < 0.001 else False