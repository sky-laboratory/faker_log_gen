import re
import pandas as pd
import MySQLdb
from typing import *

import re
import pandas as pd

pattern = re.compile(r'^\S+ \S+ \S+ \[(.*)\ \](.*)\ "(.*)" (\S+) (\S+)$')

data = []
path: str = "/Users/imhaneul/Documents/sky-laboratory/faker_log_gen/access_log_20230520-000908.log"

with open(path, "r") as f:
    for line in f:
        match = pattern.match(line.strip())
        if match:
            groups = match.groups()
            groups = (groups[0], groups[1].strip('"'), groups[2], groups[3], groups[4])
            data.append(groups)

df = pd.DataFrame(data, columns=["time", "method", "request", "status", "byte"])
df["method"] = df["method"].str.strip(' """')
print(df)
df["time"] = pd.to_datetime(df["time"], format="%d/%b/%Y:%X", exact=False)
df["time"] = pd.to_datetime(df["time"], format="%Y-%M-%d", exact=False)
df.to_csv("access.csv", index=False)


# host = "localhost"
# port = 3306
# user = "root"
# password = "password"
# db = "data_init"

# conn = MySQLdb.connect(host=host, port=port, user=user, password="", db=db)

# for index, row in df.iterrows():
#     query = f"INSERT INTO log (time, method, request, status, byte) VALUES \
#          ('{row['time']}', '{row['method']}', '{row['request']}', '{row['status']}', '{row['byte']}')"
#     with conn.cursor() as cursor:
#         cursor.execute(query)
#     conn.commit()
