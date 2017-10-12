############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless,
                 is_bestseller):
        """Initialize a melon."""

        self.name = name
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        if type(pairing) is list:
            self.pairings.extend(pairing)
        else:
            self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    melon_types = []

    musk = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    musk.add_pairing("mint")
    melon_types.append(musk)

    cas = MelonType("Casaba", "cas", 2003, "orange", False, False)
    cas.add_pairing(["strawberries", "mint"])
    melon_types.append(cas)

    cren = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    cren.add_pairing("proscuitto")
    melon_types.append(cren)

    yw = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    melon_types.append(yw)

    return melon_types


def print_pairings(melon_types):
    """Given a list of melon objects, print the melon-pairings."""

    for melon in melon_types:
        pairings = melon.pairings
        print "{name} pairs with".format(name=melon.name)
        print "-" + "\n-".join(pairings) + "\n"


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    all_melon_types = {}

    for melon in melon_types:
        all_melon_types[melon.code] = all_melon_types.get(melon.code, melon)

    return all_melon_types


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, code, shape, color, field_num, harvester):
        """Initialize a melon."""

        self.code = code
        self.shape = shape
        self.color = color
        self.field_num = field_num
        self.harvester = harvester

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field_num != 3:
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



if __name__ == "__main__":
    c = make_melon_types()
    #print_pairings(c)
    d = make_melon_type_lookup(c)
    #print d
    #print d['musk'].is_bestseller

    m = Melon("yw", 7, 10, 3, "Sheila")

    print m.is_sellable()
