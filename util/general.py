
import copy

# https://www.electricmonk.nl/log/2017/05/07/merging-two-python-dictionaries-by-deep-updating/
def dict_deepupdate(target, src):
    # Updates target in place using data from src
    for k, v in src.items():
        if k not in target:
            target[k] = copy.deepcopy(v)
        else:
            t = type(v)
            if t == list:
                target[k].extend(v)
            elif t == tuple:
                target[k] = target[k] + v
            elif t == set:
                target[k].update(v.copy())
            elif t == dict:
                dict_deepupdate(target[k], v)
            else:
                target[k] = copy.copy(v)
