import os
import random

def load_random_puzzle(folder="puzzles"):
    files = [f for f in os.listdir(folder) if f.endswith('.txt')]
    if not files:
        raise FileNotFoundError("No puzzle files found.")
    selected_file = random.choice(files)
    with open(os.path.join(folder, selected_file)) as f:
        return [list(map(int, line.strip())) for line in f.readlines()]
