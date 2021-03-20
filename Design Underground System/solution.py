class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.checkedIn = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        try:
            startStation, startTime = self.checkedIn.pop(id)
            if startStation not in self.times:
                self.times[startStation] = {}
            if stationName not in self.times[startStation]:
                self.times[startStation][stationName] = [0,0]
            self.times[startStation][stationName][0] += t - startTime
            self.times[startStation][stationName][1] += 1
        except KeyError:
            print(f'ID {id} is not checked in!')

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[startStation][endStation][0] / self.times[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
