class NinjaDog:

    def __init__(self, name):
        self._name = name
        self._collar = 'White'
        self._weapons = {} 
        self._skills = {}
        self._xp = 0

    @property
    def name(self):
        return self._name

    @property
    def collar(self):
        return self._collar

    @property
    def weapons(self):
        return self._weapons

    @property
    def skills(self):
        return self._skills

    @property
    def xp(self):
        return self._xp

    @name.setter
    def name(self, name):
        self._name = name

    @collar.setter
    def collar(self, collar):
        self._collar = collar

    @weapons.setter
    def weapons(self, name, obj):
        self._weapons[name] = obj

    @skills.setter
    def skills(self, name, obj):
        self._skills[name] = obj

    @xp.setter
    def skills(self, pts):
        self._xp += pts

    def attack(self, weapon):
        return f"Attack with {weapon}!"
    
    def talk(self):
        return f"Bark!"


if __name__ == '__main__':
    ninja = NinjaDog('Nash')
    print(ninja.name)
    print(ninja.collar)
    print(ninja.weapons)
    print(ninja.skills)
    print(ninja.xp)
    ninja.weapons['Paws of Furry'] = 20
    print(ninja.weapons)
