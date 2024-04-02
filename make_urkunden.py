import os
from set_data import compute_ranks, participants_from_json

try:
    compute_ranks(participants_from_json())
    os.chdir("latex/urkunden")
    os.system("pdflatex urkunden.tex")
except FileNotFoundError:
    print("Trage zuerst Punkte ein, um Urkunden zu generieren.")
