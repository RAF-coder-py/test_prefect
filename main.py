from prefect import flow
import os

@flow(log_prints=True)
def main():
    os.system("cd ..")
    os.system("pwd")