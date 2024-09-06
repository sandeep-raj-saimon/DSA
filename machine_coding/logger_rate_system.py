class Logger:

    def __init__(self, log, timeStamp):
        self.timeKeeper = {}

    def printMessage(self, log, timeStamp):
        if self.timeKeeper[log] is None:
            self.timeKeeper[log] = timeStamp
