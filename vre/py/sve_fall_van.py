# imports
import pandas as pd
import plotly
import plotly.express as px

# alla fall i sverige 2010-2019
# antal vrefmA/BfsA/B och van_saknas

# data frame xlsx
df = pd.read_excel("../data/alles_vre.xlsx")
# print(df.head())

# plotly express scatter plot
fig = px.line(df,  x=df["year"], y=["Sweden Total", "VREfmA", "VREfmB", "VREfsA", "VREfsB", "Not typed"], 
					color_discrete_sequence=px.colors.qualitative.Set1)

# background color
fig.layout.plot_bgcolor = "#F8F8F8"

# title
fig.update_layout(title_text="Total VRE cases in Sweden by van type 2010-2019")

# x-axis title
fig.update_xaxes(title_text="Year")

# y-axis title
fig.update_yaxes(title_text="No. of cases")

# show figure
fig.show()

# make html file
plotly.offline.plot(fig, filename='../html/sve_fall_van.html')

# bra att ha-saker:
# from IPython.display import display
# import xlrd
# plotly.offline.plot(fig, filename='static_vre.html')
# fig.write_image("images/vre_static.png")
# color_discrete_sequence=px.colors.qualitative.G10
# kan ej bestämma line width i express --> go
