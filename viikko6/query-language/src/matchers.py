class QueryBuilder:
    def __init__(self):
        self._matchers = []
        self._connective = "and"
    
    def and_method(self):
        self._connective = "and"
        return self
    
    def oneOf(self, *matchers):
        #halutaan muutkin kutsut mukaan
        self._matchers += matchers
        self._connective = "or"
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value,attr))
        return self
    
    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value,attr))
        return self

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def build(self):
        if not self._matchers:
            return All()
        if self._connective == "and":
            return And(*self._matchers)
        elif self._connective == "or":
            return Or(*self._matchers)

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False

class All:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True

class Not:
    def __init__(self, ehto):
        self._ehto = ehto
    
    def test(self, player):
        return not self._ehto.test(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
