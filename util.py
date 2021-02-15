
import copy

from Database import SEP

def make_path(a:str, b:str, sep:str = SEP) -> str:
    return a + (sep if (len(a)>0 and a[-1]!=sep) else "") + b

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
            elif t == dict:
                dict_deepupdate(target[k], v)
            elif t == set:
                target[k].update(v.copy())
            else:
                target[k] = copy.copy(v)