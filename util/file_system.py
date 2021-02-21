
SEP = "\\"

def make_path(a:str, b:str, sep:str = SEP) -> str:
    return a + (sep if (len(a)>0 and a[-1]!=sep) else "") + b

