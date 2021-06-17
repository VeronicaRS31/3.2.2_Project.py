# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]
n_and_s_countries = ['United States', 'Canada', 'Ecuador', 'Colombia', 'Argentina', 'Brazil']
european_countries = ['Germany', 'Greece', 'Italy', 'Denmark', 'Portugal', 'Sweden']
african_countries = ['Kenya', 'Egypt', 'South Africa', 'Morocco', 'Ethiopia', 'Senegal']
asian_countries = ['China', 'North Korea', 'South Korea', 'Japan', 'Indonesia', 'Russia']

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in n_and_s_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, label=c, marker="d", linestyle="--")

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()


'''
8:code
9 Question: Based on the countries i choose in north america and south america, you can see that the us has always had 
 steady electricity, and the other countries in south america the population is also gaining access to more electricity. 
 European countries all have access to electricty. All african countries population who has acess to electricty is increasing, but
 the percentage is still low compared to european and north american countries. In asian coutnries is a similar pattern with
 african countries except most of them have a higher percent of population with electricity
 10:it looks like graphs everyone else did in class
 
How does access to electricity affect countries' access to computing innovations? computers require electricty to charge and operate so countries who lack this important tool are not going to have the same acesss to computer innovations as coutnries with more electricity
How can analyzing data like this be used to affect global change? Analyzing this data can show the need to others of countries, which can help them get help.
'''
