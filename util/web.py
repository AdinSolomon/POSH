
SEP = "/"

def make_url(a:str, b:str, sep:str = SEP) -> str:
    return a + (sep if a[-1] != sep else "") + b
def make_url2(parts:list, sep:str = SEP) -> str:
    url = parts.pop(0)
    for part in parts:
        url += (sep if url[-1] != sep else "") + part
    return url
