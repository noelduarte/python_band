class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end= " ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bam", "Tzz", "Wham"])

    def count(self):
        print("One, Two, Three, Four!")

    def explode(self):
        print ("!!!!")

class Band(object):
    def __init__(self):
        self.members = {}

    def hire(self, role, musician):
        self.members[role] = musician

    def fire(self, role):
        if role in self.members:
            del self.members[role]

    def begin_playing(self, length):
        self.members['Drummer'].count()
        for role, musician in self.members.items():
            musician.solo(length)

if __name__ == '__main__':
    Taylor = Drummer()
    Michael = Guitarist()
    Carl = Bassist()
    Python_Band = Band()
    Python_Band.hire('Drummer', Taylor)
    Python_Band.begin_playing(5)
    Python_Band.hire('Guitarist', Michael)
    Python_Band.hire('Bassist', Carl)
    Python_Band.begin_playing(2)
    Python_Band.fire('Bassist')
    Python_Band.begin_playing(3)

