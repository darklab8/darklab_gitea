# helm repo add gitea-charts https://dl.gitea.io/charts/
import os
import argparse

def shell(cmd):
    print(cmd)
    status_code = os.system(cmd)
    
    if status_code != 0:
        exit(status_code)

# Create the parser
my_parser = argparse.ArgumentParser(description='')

# Add the arguments
my_parser.add_argument('--gitea_password',
                       type=str,
                       help='token')

# Execute the parse_args() method
args = my_parser.parse_args()

shell(f'helm upgrade --install --create-namespace --namespace gitea gitea . --set gitea.gitea.admin.password="{args.gitea_password}"')