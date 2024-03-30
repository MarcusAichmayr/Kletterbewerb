# In[]:
import random  # pylint: disable=import-outside-toplevel
from set_data import participants, groups, routes, compute_ranks

# In[]:
# assigns random points for participants

for participant in participants:
    for route in participant.points:
        participant.insert_points(
            route, [random.randint(0, route.handholds) for _ in range(3)]
        )

compute_ranks(participants)

# %%
from classes import Participant

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

# %%
