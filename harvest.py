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
    def __init__(self, mtype, shape, color, field_num, harvester):
        """Initialize a melon."""

        self.mtype = mtype
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

    all_melons = []

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_types['yw'], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_types['yw'], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_types['cas'], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_types['cren'], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_types['cren'], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_types['cren'], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_types['musk'], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_types['yw'], 7, 10, 3, "Sheila")

    all_melons.append(melon_1)
    all_melons.append(melon_2)
    all_melons.append(melon_3)
    all_melons.append(melon_4)
    all_melons.append(melon_5)
    all_melons.append(melon_6)
    all_melons.append(melon_7)
    all_melons.append(melon_8)
    all_melons.append(melon_9)

    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() is True:
            print "Harvested by {harvester} from field # {field_num} CAN BE SOLD".format(
                harvester=melon.harvester, field_num=melon.field_num)
        else:
            print "Harvested by {harvester} from field # {field_num} NOT SELLABLE".format(
                harvester=melon.harvester, field_num=melon.field_num)


if __name__ == "__main__":
    c = make_melon_types()
    #print_pairings(c)
    d = make_melon_type_lookup(c)
    #print d
    #print d['musk'].is_bestseller
    melon_types = make_melon_types()
    melons_by_id = make_melon_type_lookup(melon_types)
    melons = make_melons(melons_by_id)
    get_sellability_report(melons)
    print melons[0].mtype.first_harvest  # how to get attributes of the other class
