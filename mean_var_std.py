import numpy as np

def calculate(list):    

    calculations = dict()
    arr = np.array(list)

    try:
        arr.shape = (3,3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")
        # return

    arr_flat = arr.flatten()

    calculations["mean"] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr_flat.mean().tolist()]
    calculations["variance"] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr_flat.var().tolist()]
    calculations["standard deviation"] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr_flat.std().tolist()]
    calculations["max"] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr_flat.max().tolist()]
    calculations["min"] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr_flat.min().tolist()]
    calculations["sum"] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr_flat.sum().tolist()]

    return calculations

