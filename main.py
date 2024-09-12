from prefect import flow
# from rich import print
# import os

@flow(log_prints=True)
def main():
    from rich import print
    # os.system('python3 Jeu/main.py')
    print("[green]Le jeu est lancé[/green]")



