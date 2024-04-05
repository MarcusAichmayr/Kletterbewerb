import os
from set_data import participants_from_json, compute_ranks, save_ranks

try:
    participants = participants_from_json()
    compute_ranks(participants)
    save_ranks(participants)
    os.chdir("latex/urkunden")
    os.system("pdflatex urkunden.tex")
except FileNotFoundError:
    print("Trage zuerst Punkte ein, um Urkunden zu generieren.")
