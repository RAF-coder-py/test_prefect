from prefect import flow
from rich import print
# import os

@flow(log_prints=True)
def Game():
    # os.system('python3 Jeu/main.py')
    print("[red]Le jeu est lancé[/red]")

