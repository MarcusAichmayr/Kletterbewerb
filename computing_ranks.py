# In[]:
import csv
from scipy.stats import rankdata
import numpy as np

ROUTES_PER_PARTICIPANT = 3
TRY_WEIGHTS = [1, 0.9, 0.8]
GROUPS = ["Mini", "Kinder", "Jugend"]


class Route:
    """describes a climbing route"""
    id: int
    color: str
    handholds: int
    groups: list

    def __init__(self, route_id: int, color: str, handholds: int, groups: list) -> None:
        self.id = route_id
        self.color = color
        self.handholds = handholds
        self.groups = groups

    def __repr__(self) -> str:
        return "Route %s %s %s (%s)" % (self.id, self.color, self.groups, self.handholds)


class Participant:
    """person who climbs routes"""
    name: str
    group: str
    rank: int = 0
    points: dict
    result: float = 0  # a score between 0 and 100

    def __init__(self, name: str, group: str) -> None:
        self.name = name
        self.group = group
        self.points = {}

    def __repr__(self) -> str:
        return "%s(%s)" % (self.name, self.group)

    def insert_points(self, route_id: int, points: list) -> None:
        """insert how many points the participant has scored for the given route

        Args:
            route_id: id of the route
            points: scored points for each try

        Raises:
            ValueError: if the participant should not climb this route
            ValueError: if the participant has more than max points
        """
        if self.group not in routes[route_id].groups:
            raise ValueError("'%s' ist nicht gedacht für '%s'" % (routes[route_id], self))
        for value in points:
            if value > routes[route_id].handholds:
                raise ValueError(
                    "'%s' kann nicht %s Griffe bei '%s' haben."
                    % (self, value, routes[route_id])
                )
        self.points[route_id] = points

    def compute_result(self) -> float:
        """computes the total points of the participant

        Returns:
            total points
        """
        self.result = sum(
            max(value * weight for value, weight in zip(points, TRY_WEIGHTS))
            / routes[route_id].handholds
            for route_id, points in self.points.items()
        ) * (100 / ROUTES_PER_PARTICIPANT)
        return self.result


with open("data/teilnehmer.csv", "r") as data:
    participants = [
        Participant(child["Name"], child["Gruppe"]) for child in list(csv.DictReader(data))
    ]

with open("data/routen.csv", "r") as data:
    routes = {
        int(route["ID"]): Route(
            int(route["ID"]),
            route["Farbe"],
            int(route["Anzahl Griffe"]),
            [group for group in GROUPS if route[group] == "yes"],
        )
        for route in list(csv.DictReader(data))
    }

## we can still load the points from a csv file
# with open('data/punkte.csv', 'r') as data:
#     points = list(csv.DictReader(data))


def compute_ranks(participants: list) -> None:
    """Compute ranks of participants and save results (sorted) in 'data/ergebnisse.csv'."""
    for participant in participants:
        participant.compute_result()

    participants_per_group = {}
    head = ["Name", "Gruppe", "Rang"]
    for group in GROUPS:
        participants_per_group[group] = [p for p in participants if p.group == group]

        for participant, rank in zip(
            participants_per_group[group],
            rankdata([-p.result for p in participants_per_group[group]], method="dense"),
        ):
            participant.rank = rank

    participants.sort(
        key=lambda participant: (participant.group, -participant.rank), reverse=True
    )
    for participant in participants:
        print(
            "{:>2}".format(participant.rank),
            "{:>6.2f}".format(participant.result),
            ("{:<%s}" % max(len(group) for group in GROUPS)).format(participant.group),
            participant.name,
        )

    np.savetxt(
        "data/ergebnisse.csv",
        [head] + [[p.name, p.group, p.rank] for p in participants],
        delimiter=",",
        fmt="%s",
    )


# In[]:
# for testing
# assigns random points for participants
def test_insert_random_points() -> None:
    """ssigns random points for participants"""
    import random  # pylint: disable=import-outside-toplevel

    for participant in participants:
        for route in routes.values():
            if participant.group in route.groups:
                participant.insert_points(
                    route.id, [random.randint(0, route.handholds) for _ in range(3)]
                )


test_insert_random_points()
# In[]:
compute_ranks(participants)


# In[]:
# # for testing if no data is available
def test_no_data_available() -> None:
    """for testing if no data is available"""
    wolli = Participant("Wollnashorn", "Mini")
    wolli.insert_points(1, [6, 5, 8])
    wolli.insert_points(2, [15, 13, 15])
    wolli.insert_points(5, [8, 5, 8])
    mammi = Participant("Mammut", "Mini")
    mammi.insert_points(1, [0, 3, 2])
    mammi.insert_points(2, [0, 0, 5])
    mammi.insert_points(5, [0, 5, 6])
    tigi = Participant("Säbelzahntiger", "Mini")
    tigi.insert_points(1, [6, 6, 6])
    tigi.insert_points(2, [6, 6, 6])
    tigi.insert_points(5, [6, 6, 6])
    berry = Participant("Höhlenbär", "Mini")
    berry.insert_points(1, [6, 0, 0])
    berry.insert_points(2, [6, 0, 0])
    berry.insert_points(5, [6, 0, 0])
    berry2 = Participant("Höhlenbär", "Kinder")
    berry2.insert_points(2, [6, 0, 0])
    berry2.insert_points(3, [6, 0, 0])
    berry2.insert_points(4, [6, 0, 0])

    participants2 = [wolli, mammi, tigi, berry, berry2]

    compute_ranks(participants2)


test_no_data_available()


# %%
# for testing
# generate many participants and assign points randomly
def test_many_participants() -> None:
    """generate many participants and assign points randomly"""
    import random  # pylint: disable=import-outside-toplevel

    names = [
        "Wollnashorn",
        "Mammut",
        "Höhlenbär",
        "Säbelzahntiger",
        "Riesenhirsch",
        "Pferd",
        "Clementine Simone Nichtsehrweit",
        "Clementine Simony Nichtsehrlang",
    ]
    participants3 = [
        Participant(random.choice(names) + str(i), random.choice(GROUPS)) for i in range(50)
    ]

    for participant in participants3:
        for route in routes.values():
            if participant.group in route.groups:
                participant.insert_points(
                    route.id, [random.randint(0, route.handholds) for _ in range(3)]
                )
    compute_ranks(participants3)


test_many_participants()

# %%
