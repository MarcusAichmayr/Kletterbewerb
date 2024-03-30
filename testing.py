# In[]:
import random  # pylint: disable=import-outside-toplevel
# import csv

# from computing_ranks import Group, Route, Participant, compute_ranks

exec(open("computing_ranks.py").read())

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

# In[]:
# assigns random points for participants

for participant in participants:
    for route in participant.points:
        participant.insert_points(
            route, [random.randint(0, route.handholds) for _ in range(3)]
        )

compute_ranks(participants)

# %%
# for testing
# generate many participants and assign points randomly
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
    Participant(random.choice(names) + str(i), random.choice(groups)) for i in range(50)
]

for participant in participants3:
    for route in participant.points:
        participant.insert_points(
            route, [random.randint(0, route.handholds) for _ in range(3)]
        )

compute_ranks(participants3)

# In[]:
# wolli = Participant("Wollnashorn", "Mini")
# wolli.insert_points(1, [6, 5, 8])
# wolli.insert_points(2, [15, 13, 15])
# wolli.insert_points(5, [8, 5, 8])
# mammi = Participant("Mammut", "Mini")
# mammi.insert_points(1, [0, 3, 2])
# mammi.insert_points(2, [0, 0, 5])
# mammi.insert_points(5, [0, 5, 6])
# tigi = Participant("Säbelzahntiger", "Mini")
# tigi.insert_points(1, [6, 6, 6])
# tigi.insert_points(2, [6, 6, 6])
# tigi.insert_points(5, [6, 6, 6])
# berry = Participant("Höhlenbär", "Mini")
# berry.insert_points(1, [6, 0, 0])
# berry.insert_points(2, [6, 0, 0])
# berry.insert_points(5, [6, 0, 0])
# berry2 = Participant("Höhlenbär", "Kinder")
# berry2.insert_points(2, [6, 0, 0])
# berry2.insert_points(3, [6, 0, 0])
# berry2.insert_points(4, [6, 0, 0])

# participants2 = [wolli, mammi, tigi, berry, berry2]

# compute_ranks(participants2)

# %%
