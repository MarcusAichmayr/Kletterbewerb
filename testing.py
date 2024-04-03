# %%
"""testing"""

import random  # pylint: disable=import-outside-toplevel
from set_data import *

# In[]:
# assigns random points for participants

for participant in participants:
    for route in participant.points:
        participant.insert_points(
            route, [random.randint(0, route.handholds) for _ in range(3)]
        )

compute_ranks(participants)
print_ranks(participants)
save_ranks(participants)

# %%
routes

# %%
save_participants(participants)

# %%
participants = participants_from_json()
compute_ranks(participants)
print_ranks(participants)

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
participants = [
    Participant(random.choice(names) + str(i), random.choice(groups)) for i in range(50)
]

for participant in participants:
    for route in participant.points:
        participant.insert_points(
            route, [random.randint(0, route.handholds) for _ in range(3)]
        )

compute_ranks(participants)
print_ranks(participants)

# %%
