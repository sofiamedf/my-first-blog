# imports
import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# data frame xlsx
df = pd.read_excel("../data/alles_vre.xlsx")

# subplot for 2 y-axes
fig = make_subplots(specs=[[{"secondary_y": True}]])

# plots - stockholm
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_sthlm"], name="Cases Stockholm", line=dict(color='#3366CC', width=1.5), mode='lines'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_sthlm"],
                    name="Incidence Stockholm", line=dict(color='#3366CC', width=1.5, dash='dot'), mode='lines'),
    secondary_y=True,
)

# plots - södermanland
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_sml"], name="Cases Södermanland", line=dict(color='#DC3912', width=1.5), mode='lines'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_sml"],
    				name="Incidence Södermanland", line=dict(color='#DC3912', width=1.5, dash='dot'), mode='lines'),
    secondary_y=True,
)

# plots - västerbotten
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_vbttn"], name="Cases Västerbotten", line=dict(color='#109618', width=1.5), mode='lines'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_vbttn"],
    				name="Incidence Västerbotten", line=dict(color='#109618', width=1.5, dash='dot'), mode='lines'),
    secondary_y=True,
)

# plots - örebro
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_oret"], name="Cases Örebro", line=dict(color='#990099', width=1.5), mode='lines'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_oret"],
    				name="Incidence Örebro", line=dict(color='#990099', width=1.5, dash='dot'), mode='lines'),
    secondary_y=True,
)

# plots - incidence Sweden total
fig.add_trace(
    go.Scatter(x=df["year"], y=df["Sweden Total"],
                    name="Cases Sweden", line=dict(color='black', width=1), mode='lines'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_sve"],
    				name="Incidence Sweden", line=dict(color='black', width=1, dash='dash'), mode='lines'),
    secondary_y=True,
)

# plots - utbrstm
fig.add_trace(
    go.Scatter(x=df["year"], y=df["SE-VREfmB-1707"],
                    name="Cases VREfmB-1707", line=dict(color='#F58518', width=2), mode='lines'),
    secondary_y=False,
)

# x-axis title
fig.update_xaxes(title_text="Year")

# y-axes titles
fig.update_yaxes(title_text="<b>Cases</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Incidence (100k ppl/y)</b>", secondary_y=True)

# background color
fig.layout.plot_bgcolor = "#FAFAFA"

# title
fig.update_layout(title_text="Vancomycin-resistant enterococci in 4 Swedish counties 2010-2019")

# text font mm
fig.update_layout(
#    legend_title="Legend Title",
    font=dict(
        family="Helvetica",
        size=15,
        color="black"
    )
)

# show figure
fig.show()

# make other files
plotly.offline.plot(fig, filename="../html/vre_cases_inc_4_static.html")
fig.write_image("../images/vre_cases_inc_4_static.png")

# bra att ha-saker:
# from IPython.display import display
# import xlrd
# plotly.offline.plot(fig, filename='static_vre.html')
# fig.write_image("images/vre_static.png")
