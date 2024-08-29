from prefect import task, flow
# import os

@flow(log_prints=True)
def Game():
    # os.system('python3 Jeu/main.py')
    print("Le jeu est lancé")

