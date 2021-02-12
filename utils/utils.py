from constants import DATA_DIR
import json

def dump_data(filename: str, data):
    with open(DATA_DIR / filename, 'w') as f:
        json.dump(data, f)