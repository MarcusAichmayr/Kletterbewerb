# In[]:
import csv
from scipy.stats import rankdata
import numpy as np

ROUTES_PER_PARTICIPANT = 3
TRY_WEIGHTS = [1, 0.9, 0.8]


class Group:
    """an age-based group"""
    id: int
    name: str

    def __init__(self, group_id: int, name: str) -> None:
        if not isinstance(group_id, int):
            raise TypeError("'group_id' should be an integer")
        self.id = group_id
        self.name = name

    def __repr__(self) -> str:
        return f"'Gruppe {self.id} - {self.name}'"

    def __hash__(self) -> int:
        return hash(self.id)


class Route:
    """describes a climbing route"""
    id: int
    color: str
    handholds: int
    groups: list

    def __init__(self, route_id: int, color: str, handholds: int, group_ids: list) -> None:
        if not isinstance(route_id, int):
            raise TypeError("'route_id' should be an integer.")
        self.id = route_id
        self.color = color
        self.handholds = handholds
        for group_id in group_ids:
            if not isinstance(group_id, int):
                raise TypeError("'group_ids' should be a list of integers.")
        self.group_ids = group_ids

    def __repr__(self) -> str:
        return f"'Route {self.id} - {self.color} {[group[self.group_ids].name for group in groups]} ({self.handholds})'"

    def __hash__(self) -> int:
        return hash(self.id)


class Participant:
    """person who climbs routes"""
    name: str
    group: Group
    rank: int = 0
    points: dict
    result: float = 0  # a score between 0 and 100

    def __init__(self, name: str, group_id: int) -> None:
        if not isinstance(group_id, int):
            raise TypeError("'group_id' should be an integer.")
        self.name = name
        self.group = groups[group_id]
        self.points = {}

    def __repr__(self) -> str:
        return f"{self.name}({self.group.name})"

    def insert_points(self, route_id: int, points: list) -> None:
        """insert how many points the participant has scored for the given route

        Args:
            route_id: id of the route
            points: scored points for each try

        Raises:
            ValueError: if the participant should not climb this route
            ValueError: if the participant has more than max points
        """
        if self.group.id not in routes[route_id].group_ids:
            raise ValueError(f"'{routes[route_id]}' ist nicht gedacht für '{self}'")
        for value in points:
            if value > routes[route_id].handholds:
                raise ValueError(
                    f"'{self}' kann nicht {value} Griffe bei '{routes[route_id]}' haben."
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

with open('data/gruppen.csv', 'r', encoding="utf-8") as data:
    groups = {
        int(line["ID"]): Group(int(line["ID"]), line["Bezeichnung"])
        for line in csv.DictReader(data)
    }

with open("data/teilnehmer.csv", "r", encoding="utf-8") as data:
    participants = [
        Participant(child["Name"], int(child["Gruppe"])) for child in list(csv.DictReader(data))
    ]

with open("data/routen.csv", "r", encoding="utf-8") as data:
    routes = {
        int(line["ID"]): Route(
            int(line["ID"]),
            line["Farbe"],
            int(line["Anzahl Griffe"]),
            [group.id for group in list(groups.values()) if line[str(group.id)] == "yes"],
        )
        for line in list(csv.DictReader(data))
    }


## we can still load the points from a csv file
# with open('data/punkte.csv', 'r', encoding="utf-8") as data:
#     points = list(csv.DictReader(data))


def compute_ranks(participants: list) -> None:
    """Compute ranks of participants and save results (sorted) in 'data/ergebnisse.csv'."""
    for participant in participants:
        participant.compute_result()

    participants_per_group = {}
    head = ["Name", "Gruppe", "Rang"]
    for group_id in list(groups.keys()):
        participants_per_group[group_id] = [p for p in participants if p.group.id == group_id]

        for participant, rank in zip(
            participants_per_group[group_id],
            rankdata([-p.result for p in participants_per_group[group_id]], method="dense"),
        ):
            participant.rank = rank

    participants.sort(
        key=lambda participant: (participant.group.id, -participant.rank), reverse=True
    )
    for participant in participants:
        print(
            f"{participant.rank:>2}",
            f"{participant.result:>6.2f}",
            ("{:<%s}" % max(len(group.name) for group in list(groups.values()))).format(participant.group.name),
            participant.name,
        )

    np.savetxt(
        "data/ergebnisse.csv",
        [head] + [[p.name, p.group.name, p.rank] for p in participants],
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
            if participant.group.id in route.group_ids:
                participant.insert_points(
                    route.id, [random.randint(0, route.handholds) for _ in range(3)]
                )


test_insert_random_points()
# In[]:
compute_ranks(participants)

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
        Participant(random.choice(names) + str(i), random.choice(list(groups.keys()))) for i in range(50)
    ]

    for participant in participants3:
        for route in routes.values():
            if participant.group.id in route.group_ids:
                participant.insert_points(
                    route.id, [random.randint(0, route.handholds) for _ in range(3)]
                )
    compute_ranks(participants3)


test_many_participants()

# In[]:
# def test_no_data_available() -> None:
#     """for testing if no data is available"""
#     wolli = Participant("Wollnashorn", "Mini")
#     wolli.insert_points(1, [6, 5, 8])
#     wolli.insert_points(2, [15, 13, 15])
#     wolli.insert_points(5, [8, 5, 8])
#     mammi = Participant("Mammut", "Mini")
#     mammi.insert_points(1, [0, 3, 2])
#     mammi.insert_points(2, [0, 0, 5])
#     mammi.insert_points(5, [0, 5, 6])
#     tigi = Participant("Säbelzahntiger", "Mini")
#     tigi.insert_points(1, [6, 6, 6])
#     tigi.insert_points(2, [6, 6, 6])
#     tigi.insert_points(5, [6, 6, 6])
#     berry = Participant("Höhlenbär", "Mini")
#     berry.insert_points(1, [6, 0, 0])
#     berry.insert_points(2, [6, 0, 0])
#     berry.insert_points(5, [6, 0, 0])
#     berry2 = Participant("Höhlenbär", "Kinder")
#     berry2.insert_points(2, [6, 0, 0])
#     berry2.insert_points(3, [6, 0, 0])
#     berry2.insert_points(4, [6, 0, 0])

#     participants2 = [wolli, mammi, tigi, berry, berry2]

#     compute_ranks(participants2)


# test_no_data_available()
