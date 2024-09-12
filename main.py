from prefect import flow
import os

@flow(log_prints=True)
def main():
    os.system("python3 Jeu/main.py")