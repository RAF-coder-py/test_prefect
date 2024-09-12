from prefect import flow
import os
import sys

@flow(log_prints=True)
def main():
    # os.system()
    sys.exit(1)