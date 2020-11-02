# imports
import pandas as pd
from IPython.display import display
from scipy import stats
from scipy.stats import mannwhitneyu
import seaborn as sns
import matplotlib.pyplot as plt
from pingouin import mwu

# data
df = pd.read_csv('mwugenderpercent.csv')
# display(df.head())

# mann-whitney u
# x är mansraden, y är kvinnoraden
# nollhyp = sign skilln gr
# results = mannwhitneyu(df['men'], df['women'])
# display(results)
# results2 = stats.mannwhitneyu(df['men'], df['women'], alternative='two-sided')
# display(results2)
# print('-----------')
results3 = mwu(df['men'], df['women'], tail='two-sided')
display(results3)
print('Om p < 0.05 --> signifikant skillnad mellan grupperna.')

###########################################################################################
#In statistics, the Mann–Whitney U test (also called the Mann–Whitney–Wilcoxon (MWW),     #
#Wilcoxon rank-sum test, or Wilcoxon–Mann–Whitney test) is a nonparametric test of the    #
#null hypothesis that it is equally likely that a randomly selected value from one sample #
#will be less than or greater than a randomly selected value from a second sample.        #
#                                                                                         #
#Under the null hypothesis H0, the probability of an observation from the population 𝑋    #
#exceeding an observation from the second population 𝑌 equals the probability of an       #
#observation from 𝑌 exceeding an observation from 𝑋.                                      #
#Two group means are different (two-tailed)                                               #
###########################################################################################