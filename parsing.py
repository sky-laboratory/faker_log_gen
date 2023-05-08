import re 
import pandas as pd 
from typing import *

patterns = re.compile(r'^\S+ \S+ \S+ \[(.*)\] "(.*)" (\S+) (\S+)$')

def parsing_preprocessing(path: pd.DataFrame) -> Generator[str, None, Any]:
    for line in open(path):
        for m in patterns.finditer(line):
            yield m.groups()
            

path: str = '/Users/imhaneul/Documents/sky-laboratory/faker_log_gen/access_log_20230508-230002.log'
columns: List[str] = ["time", "request", "status", "byte"]
df = pd.DataFrame(parsing_preprocessing(path), columns=columns)
df["time"] = pd.to_datetime(df["time"], format='%d/%b/%Y:%X', exact=False)
df.to_csv("access_log.csv", index=False)            