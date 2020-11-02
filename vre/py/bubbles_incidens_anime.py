# imports
import pandas as pd
import plotly
import plotly.express as px


# data
df = pd.DataFrame({"Region":["Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland","Blekinge","Dalarna","Gotland","Gävleborg","Halland","Jämtland","Jönköping","Kalmar","Kronoberg","Norrbotten","Skåne","Stockholm","Södermanland","Uppsala","Värmland","Västerbotten","Västernorrland","Västmanland","Västra Götaland","Örebro","Östergötland"],
			"Year":["2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2010","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2011","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2012","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2013","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2014","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2015","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2016","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2017","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2018","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019","2019"],
			"Incidens": ["0.0","0.36","0.0","0.36","4.34","0.0","0.89","1.28","0.0","2.81","0.48","2.68","0.0","2.97","0.36","0.77","24.71","16.23","0.5","0.71","0.23","0.0","0.36","1.74","0.36","1.32","0.79","0.88","0.85","0.54","0.4","1.35","1.91","0.36","0.0","0.73","0.0","15.27","0.78","0.37","0.0","0.46","0.65","0.0","0.0","0.0","3.28","0.0","4.42","1.28","2.15","0.4","0.79","3.99","0.36","0.58","0.36","0.0","0.0","0.39","1.06","0.0","0.23","0.65","0.0","0.0","32.37","0.32","0.0","1.46","1.28","3.74","0.8","1.49","2.08","0.0","1.73","0.36","0.0","0.41","0.0","2.6","0.0","0.91","0.64","0.35","0.0","76.43","0.64","1.57","2.03","0.42","7.4","0.4","1.93","2.54","0.71","10.89","1.09","1.52","0.0","0.38","1.22","1.04","1.58","0.0","0.0","0.0","3.19","1.27","0.0","1.14","1.68","2.09","0.0","1.91","2.5","0.0","2.25","1.08","1.13","0.0","0.0","1.33","5.15","0.0","1.26","0.7","1.72","2.45","0.93","0.0","1.7","1.23","0.51","4.78","1.73","2.11","0.0","3.59","0.35","1.88","0.0","4.85","1.43","0.33","0.0","1.25","0.69","1.7","1.4","5.84","0.0","0.55","0.0","3.54","0.0","1.26","4.02","0.0","1.89","7.48","0.0","0.0","5.16","1.77","7.69","0.43","1.25","0.34","0.0","0.69","1.51","4.6","1.1","0.81","1.0","0.79","1.76","6.22","14.93","3.45","1.77","35.16","1.22","1.46","2.63","12.9","0.0","3.75","1.04","3.35","0.69","1.79","0.0","1.37","0.81","0.0","0.39","1.45","4.16","0.67","8.33","0.7","2.2","0.0","0.0","1.44","4.59","1.07"],
			"Pop":["153227","277047","57269","276508","299484","126691","336866","233536","183940","248609","1243329","2054343","270738","335882","273265","259286","242625","252756","1580297","280230","429642","152979","276565","57308","276130","301724","126299","337896","233090","184654","248545","1252933","2091473","272563","338630","272736","259667","242155","254257","1590604","281572","431075","152315","276555","57241","276637","304116","126201","339116","233548","185887","248637","1263088","2127006","274723","341977","273080","260217","241981","256224","1600447","283113","433784","152757","277349","57161","277970","306840","126461","341235","233874","187156","249436","1274069","2163042","277569","345481","273815","261112","242156","259054","1615084","285395","437848","154157","278903","57255","279991","310665","126765","344262","235598","189128","249987","1288908","2198044","280666","348942","274691","262362","243061","261703","1632012","288150","442105","156253","281028","57391","281815","314784","127376","347837","237679","191369","249733","1303627","2231439","283712","354164","275904","263378","243897","264276","1648682","291012","445661","158453","284531","58003","284586","320333","128673","352735","242301","194628","250570","1324565","2269060","288097","361373","279334","265881","245572","267629","1671783","294941","452105","159371","286165","58595","285637","324825","129806","357237","243536","197519","251295","1344689","2308143","291341","368971","280399","268465","245968","271095","1690782","298907","457496","159684","287191","59249","286547","329352","130280","360825","244670","199886","250497","1362164","2344124","294695","376354","281482","270154","245453","273929","1709814","302252","461583","159606","287966","59686","287382","333848","130810","363599","245446","201469","250093","1377827","2377081","297540","383713","282414","271736","245347","275845","1725881","304805","465495"]
			})

# dataframe-kolumnen "Pop" tycker den är en sträng - det är säkert excels fel efter copypasta
# df.column_name = df.column_name.astype(int)
df.Pop = df.Pop.astype(int)


# plotly express scatter plot
fig = px.scatter(df,  x="Year", y="Incidens", title="Incidens av VRE i Sveriges regioner 2010-2019", animation_frame="Year", color="Region", range_x=[2010,2019], range_y=[0,80], size="Pop")


# slow down
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 3000
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 3000

# snygg.com
fig.layout.plot_bgcolor = "#FFFFFF"

# show figure
fig.show()

# make html file
plotly.offline.plot(fig, filename='html/anime_vre_incidens.html')


## ANDRAS RADER ##################
# df = px.data.gapminder()
# px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#           size="pop", color="continent", hover_name="country",
#           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

## Önskelista ##
# kan jag göra nåt med log så att det syns bättre där det är så trångt?
# det här med log för att se bättre funkar sådär
# det blir inte så bra skalor och de kommer ju hoppa mellan olika skalor då, svåra att följa med blicken
#
# har därför tagit bort:
# range_y=[1,10,100], log_y=True i fig scatter plot
# har en dröm om att kunna ändra färgerna så de är mera olika
# försökte med , colorscale=Rainbow
# men det funkade piss
#
# just nu är dock skalan största problemet
# det är så tjockt på botten att man inte ser nåt vettigt!










