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

    def __init__(self, route_id: int, color: str, handholds: int, groups: list) -> None:
        if not isinstance(route_id, int):
            raise TypeError("'route_id' should be an integer.")
        self.id = route_id
        self.color = color
        self.handholds = handholds
        for group in groups:
            if not isinstance(group, Group):
                raise TypeError("'groups' should be a list of 'Group' objects.")
        self.groups = groups.copy()

    def __repr__(self) -> str:
        return f"'Route {self.id} - {self.color} {[group.name for group in self.groups]} ({self.handholds})'"

    def __hash__(self) -> int:
        return hash(self.id)


class Participant:
    """person who climbs routes"""
    name: str
    group: Group
    rank: int = 0
    points: dict
    result: float = 0  # a score between 0 and 100

    def __init__(self, name: str, group: Group) -> None:
        if not isinstance(group, Group):
            raise TypeError("'group' should be a Group object.")
        self.name = name
        self.group = group
        self.points = {
            route: 0
            for route in routes if self.group in route.groups
        }

    def __repr__(self) -> str:
        return f"{self.name}({self.group.name})"

    def insert_points(self, route: int, points: list) -> None:
        """insert how many points the participant has scored for the given route

        Args:
            route_id: id of the route
            points: scored points for each try

        Raises:
            ValueError: if the participant should not climb this route
            ValueError: if the participant has more than max points
        """
        if self.group not in route.groups:
            raise ValueError(f"'{route}' ist nicht gedacht für '{self}'")
        for value in points:
            if value > route.handholds:
                raise ValueError(
                    f"'{self}' kann nicht {value} Griffe bei '{route}' haben."
                )
        self.points[route] = points

    def compute_result(self) -> float:
        """computes the total points of the participant

        Returns:
            total points
        """
        self.result = sum(
            max(value * weight for value, weight in zip(points, TRY_WEIGHTS))
            / route.handholds
            for route, points in self.points.items()
        ) * (100 / ROUTES_PER_PARTICIPANT)
        return self.result


def compute_ranks(participants: list) -> None:
    """Compute ranks of participants and save results (sorted) in 'data/ergebnisse.csv'."""
    for participant in participants:
        participant.compute_result()

    participants_per_group = {}
    head = ["Name", "Gruppe", "Rang"]
    for group in groups:
        participants_per_group[group] = [p for p in participants if p.group == group]

        for participant, rank in zip(
            participants_per_group[group],
            rankdata([-p.result for p in participants_per_group[group]], method="dense"),
        ):
            participant.rank = rank

    participants.sort(
        key=lambda participant: (participant.group.id, participant.rank)
    )
    for participant in participants:
        print(
            f"{participant.rank:>2}",
            f"{participant.result:>6.2f}",
            ("{:<%s}" % max(len(group.name) for group in groups)).format(participant.group.name),
            participant.name,
        )

    np.savetxt(
        "data/ergebnisse.csv",
        [head] + [[p.name, p.group.name, p.rank] for p in participants],
        delimiter=",",
        fmt="%s",
    )

# load data
# where should this be?
with open('data/gruppen.csv', 'r', encoding="utf-8") as data:
    groups = [
        Group(int(line["ID"]), line["Bezeichnung"])
        for line in csv.DictReader(data)
    ]
    group_dict = {group.id: group for group in groups}

with open("data/routen.csv", "r", encoding="utf-8") as data:
    routes = [
        Route(
            int(line["ID"]),
            line["Farbe"],
            int(line["Anzahl Griffe"]),
            [group for group in groups if line[str(group.id)] == "yes"],
        )
        for line in list(csv.DictReader(data))
    ]

with open("data/teilnehmer.csv", "r", encoding="utf-8") as data:
    participants = [
        Participant(
            line["Name"],
            group_dict[int(line["Gruppe"])]
        ) for line in csv.DictReader(data)
    ]
