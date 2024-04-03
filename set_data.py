import csv
import json
import os
import warnings
from numpy import savetxt
from scipy.stats import rankdata
from classes import Participant, Group, Route

DATA_DIR = "data/"
if not os.path.exists(DATA_DIR):
    warnings.warn("Directory 'data' not found. Using 'data_template' instead.")
    DATA_DIR = "data_template/"
GENERATED_DIR = "generated/"

if not os.path.exists(GENERATED_DIR):
    os.makedirs(GENERATED_DIR)


def compute_ranks(participants: list[Participant]) -> None:
    """Compute ranks of participants"""

    for participant in participants:
        participant.compute_result()

    participants_per_group = {}
    for group in groups:
        participants_per_group[group] = [p for p in participants if p.group == group]

        for participant, rank in zip(
            participants_per_group[group],
            rankdata([-p.result for p in participants_per_group[group]], method="dense"),
        ):
            participant.rank = int(rank)

    participants.sort(key=lambda participant: (participant.group.id, participant.rank))
    for participant in participants:
        print(
            f"{participant.rank:>2}",
            f"{participant.result:>6.2f}",
            ("{:<%s}" % max(len(group.name) for group in groups)).format(
                participant.group.name
            ),
            participant.name,
        )


def save_ranks(participants: list[Participant]) -> None:
    """save ranks of participants (sorted) in 'ergebnisse.csv'."""

    head = ["Name", "Gruppe", "Rang"]
    savetxt(
        GENERATED_DIR + "ergebnisse.csv",
        [head]
        + [
            [p.name, p.group.name, p.rank]
            for p in sorted(
                participants, key=lambda participant: (participant.group.id, participant.rank)
            )
        ],
        delimiter=",",
        fmt="%s",
    )
    print("Saved results.")


def set_route_data() -> None:
    """save route data in 'generated' directory so that latex can generate 'routenzettel.pdf'"""
    head = ["ID", "Farbe", "Routensetzer", "Gruppen"]
    savetxt(
        GENERATED_DIR + "routen.csv",
        [head]
        + [
            [
                route.id,
                route.color,
                route.creator,
                "/".join(group.name for group in route.groups),
            ]
            for route in routes
        ],
        delimiter=",",
        fmt="%s",
    )
    print("Route data set.")


def save_participants(participants: list[Participant]) -> None:
    """save a list of participants as json"""
    with open(GENERATED_DIR + "teilnehmer.json", "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in participants], f)


def participants_from_json(file: str = None) -> list:
    if not file:
        file = GENERATED_DIR + "teilnehmer.json"
    with open(file) as f:
        participants = json.load(f)
    return [
        Participant(
            p["name"],
            group_dict[p["group"]],
            p["rank"],
            {route_dict[int(route_id)]: points for route_id, points in p["points"].items()},
        )
        for p in participants
    ]


def load_participants() -> list[Participant]:
    """load participants from `teilnehmer.json` if possible or `data/teilnehmer.json`"""
    try:
        return participants_from_json()
    except FileNotFoundError:
        with open(DATA_DIR + "teilnehmer.csv", "r", encoding="utf-8") as data:
            return [
                Participant(line["Name"], group_dict[int(line["Gruppe"])])
                for line in csv.DictReader(data)
            ]


with open(DATA_DIR + "gruppen.csv", "r", encoding="utf-8") as data:
    groups = [Group(int(line["ID"]), line["Bezeichnung"]) for line in csv.DictReader(data)]
group_dict = {group.id: group for group in groups}

with open(DATA_DIR + "routen.csv", "r", encoding="utf-8") as data:
    routes = [
        Route(
            int(line["ID"]),
            line["Farbe"],
            int(line["Anzahl Griffe"]),
            [group for group in groups if line[str(group.id)] == "yes"],
            line["Routensetzer"],
        )
        for line in list(csv.DictReader(data))
    ]
route_dict = {route.id: route for route in routes}

for group in groups:
    group.set_routes(routes)

with open(DATA_DIR + "teilnehmer.csv", "r", encoding="utf-8") as data:
    participants = [
        Participant(line["Name"], group_dict[int(line["Gruppe"])])
        for line in csv.DictReader(data)
    ]

if __name__ == "__main__":
    set_route_data()
    try:
        compute_ranks(participants_from_json())
    except FileNotFoundError:
        pass
