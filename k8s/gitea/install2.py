# helm repo add gitea-charts https://dl.gitea.io/charts/
import os
import argparse

def shell(cmd):
    print(cmd)
    status_code = os.system(cmd)
    
    if status_code != 0:
        exit(status_code)

shell("helm upgrade --install --create-namespace --namespace gitea gitea-exposer .")