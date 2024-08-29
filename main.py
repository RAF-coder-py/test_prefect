from prefect import task, flow
import os

@flow()
def Game():
    os.system('python3 Jeu/main.py')
