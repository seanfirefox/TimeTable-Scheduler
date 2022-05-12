from NUSClass import NUSClass


class Lab(NUSClass) :

    def __init__(self, slot, day, start, end, mod) :
        self.slot = slot
        self.day = day
        self.start = start
        self.end = end
        self.mod = mod

    def __str__(self) :
        return self.mod + " LAB " + str(self.slot) + " on Day " + str(self.day) + " @ " + str(self.start) + " - " + str(self.end)

    def __repr__(self) -> str:
        return self.mod + " LAB " + str(self.slot) + " on Day " + str(self.day) + " @ " + str(self.start) + " - " + str(self.end)
    
    def isSameSlot(self, other) :
        return isinstance(other, Lab) and (other.slot == self.slot)

    def willClash(self, b):
        return super().willClash(b)



