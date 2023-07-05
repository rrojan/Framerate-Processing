import os
import time


def clear():
    # For Windows, the name is 'nt', while it is 'posix' for *nix (Mac/Linux)
    clear_cmd = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_cmd)


def get_filecount(path):
    count = 0
    for _path in os.listdir(path):
        if os.path.isfile(os.path.join(path, _path)) and _path != '.keep':
            count += 1
    return count


def calculate_eta(start_time, completed):
    if completed == 0.0:
        return float('inf')
    current_time = time.time()
    elapsed_time = current_time - start_time
    estimated_total_time = elapsed_time / (completed / 100)
    eta = start_time + estimated_total_time
    return eta
