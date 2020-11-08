# imports
import pandas as pd
import plotly
import plotly.express as px

# fall per åldersgrupp i sverige 2010-2019

# data frame xlsx
df = pd.read_excel("../data/alles_vre.xlsx")
# print(df.head())

# plotly express scatter plot
fig = px.scatter(df,  x=df["year"], y=["age_0_4", "age_5_9", "age_10_14", "age_15_19", "age_20_29", "age_30_39", "age_40_49",
					"age_50_59", "age_60_69", "age_70_79", "age_80_up"], color_discrete_sequence=px.colors.qualitative.Set1)

# background color
fig.layout.plot_bgcolor = "#F8F8F8"

# title
fig.update_layout(title_text="VRE cases per age group in Sweden 2010-2019")

# x-axis title
fig.update_xaxes(title_text="Year")

# y-axis title
fig.update_yaxes(title_text="Nr of cases")

# show figure
# fig.show()

# make html file
plotly.offline.plot(fig, filename='../html/age_grps_dots.html', auto_open=False)

# bra att ha-saker:
# from IPython.display import display
# import xlrd
# plotly.offline.plot(fig, filename='static_vre.html')
# fig.write_image("images/vre_static.png")
# color_discrete_sequence=px.colors.qualitative.G10
# kan ej bestämma line width i express --> go
