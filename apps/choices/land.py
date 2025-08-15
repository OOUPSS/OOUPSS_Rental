from enum import Enum


class Lands(Enum):
    BADEN_WUERTTEMBERG = "Baden-Württemberg"
    BAYERN = "Bayern"
    BERLIN = "Berlin"
    BRANDENBURG = "Brandenburg"
    BREMEN = "Bremen"
    HAMBURG = "Hamburg"
    HESSEN = "Hessen"
    NIEDERSACHSEN = "Niedersachsen"
    MECKLENBURG_VORPOMMERN = "Mecklenburg-Vorpommern"
    NORTH_RHEIN_WESTFALEN = "Nordrhein-Westfalen"
    RHEINLAND_PFALZ = "Rheinland-Pfalz"
    SAARLAND = "Saarland"
    SACHSEN = "Sachsen"
    SACHSEN_ANHALT = "Sachsen-Anhalt"
    SCHLESWIG_HOLSTEIN = "Schleswig-Holstein"
    THUERINGEN = "Thüringen"

    @classmethod
    def choices(cls):
        return [(attr.value, attr.value) for attr in cls]