import wandb

print(f'The version of WandB is: {wandb.__version__}')

# assert TEST to show BRANCH PROTECTION based on GitHub Action job (NOT WORKFLOW NAME!)
assert wandb.__version__ == '2.0.24', f'Expected version 2.0.24, instead got {wandb.__version__}'
