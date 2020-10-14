class Clock:
    hours = 0
    minutes = 0
    def toString(self, h, m):
        return (str(h) if h > 9 else '0' + str(h)) + ':' + (str(m) if m > 9 else '0' + str(m))

    def __init__(self, hour, minute):
        self.minutes = minute % 60
        self.hours = (hour + int((minute - (minute % 60)) / 60)) % 24

    def __repr__(self):
        return self.toString(self.hours, self.minutes)

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        else:
            return False

    def __add__(self, minutes):
        tempMinutes = (self.minutes + minutes) % 60
        carryOver = int(((self.minutes + minutes) - ((self.minutes + minutes) % 60)) / 60)
        tempHours = (self.hours + carryOver) % 24
        return self.toString(tempHours, tempMinutes)

    def __sub__(self, minutes):
        tempMinutes = (self.minutes - minutes) % 60
        carryOver = int(((self.minutes - minutes) - ((self.minutes - minutes) % 60)) / 60)
        tempHours = (self.hours + carryOver) % 24
        return self.toString(tempHours, tempMinutes)
