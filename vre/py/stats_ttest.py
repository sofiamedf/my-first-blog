# imports
import pandas as pd
from IPython.display import display
from scipy import stats
from scipy.stats import mannwhitneyu
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

# data
df = pd.read_csv('genderpercent.csv')
# display(df.head())

# see column names
# print(df.columns)

# subsetting data
male = df.query('grouping == "men"')['percent']
female = df.query('grouping == "women"')['percent']

# descr stats
# mean, std, quartiles etc
df.groupby('grouping').describe()
display(df.describe())
print('---')

# normal
stats.shapiro(male)
stats.shapiro(female)
display(stats.shapiro(male))
display(stats.shapiro(female))
print('Om p < 0.05 --> icke-normalfördelat material.')
print('---')

# boxplot
sns.boxplot(x='grouping', y='percent', data=df)
plt.savefig('boxplot.png')
# plt.show()

# homogeneity of variance
stats.levene(male, female)
display(stats.levene(male, female))
# nollhypotesen antar att det är homogent - vilket det inte blir med det p-värdet
print('Om p < 0.05 --> homogen varians.')
print('---')

# two-samples t-test
res = pg.ttest(male, female, correction=False)
display(res)

# obs! hårdkodat
# print("Nollhypotesen för Shapiro-Wilks säger normalfördelad grupp. Gör Mann-Whitney!")
