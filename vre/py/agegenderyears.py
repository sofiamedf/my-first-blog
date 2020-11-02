# imports
import pandas as pd
import plotly
import plotly.express as px

# data
df = pd.DataFrame({"Percent":["33.3","50.0","63.1","46.8","28.5","48.5","45.8","60.3","51.0","51.4","56.0","54.9","50.6","56.3","54.9","50.3","53.9","62.2","58.7","59.4","66.6","44.4","36.8","53.1","66.6","48.5","54.1","39.6","48.9","48.5","43.9","45.0","49.3","43.6","45.0","49.6","46.0","37.7","41.2","40.5"],
			"Gender":["Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Men","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women","Women"],
			"Year":["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
			})

# plotly express bar plot
fig = px.bar(df, x="Year", y="Percent", color="Gender", title="Könsfördelning VRE-fall i %")

# show figure
fig.show()

# make html file
plotly.offline.plot(fig, filename='gender_vre.html')



# brasklapp: det finns uppemot 6% okänt kön, det kommer påverka t-testet - så jag tänker på det
# om alla de som är okänt skulle hamna i den mindre gruppen dvs kvinnorna så skulle det bli jämt det året och då finns ingen skillnad, förstås

#### Exempelrader ####
# fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
# long_df = px.data.medals_long()
# df.Pop = df.Pop.astype(int)
# df = px.data.tips()
# fig = px.bar(df, x="sex", y="total_bill",
#            color='smoker', barmode='group',
#            height=400)