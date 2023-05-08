import pandas as pd 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 


df1 = pd.read_csv("access_log.csv", parse_dates=['time'])
df2 = df1.set_index("time")

df3 = df2['2023-05-08': '2023-08-07']
log_data3 = df3.resample("1d").size()
print(log_data3)

# time
# 2023-05-08     19
# 2023-05-09    537
# 2023-05-10    514
# 2023-05-11    521
# 2023-05-12    523
#              ... 
# 2023-08-03    538
# 2023-08-04    526
# 2023-08-05    508
# 2023-08-06    535
# 2023-08-07     49
# Freq: D, Length: 92, dtype: int64

log_data3.plot.line()
plt.show()

fig = go.Figure(layout=go.Layout(title=go.layout.Title(text="Log -- Visualization")))
fig.add_trace(
    go.Scatter(
        x=log_data3["time"],
        y=log_data3["status"],
        name="total",
        mode="lines",
    )
)

fig.show()
