

# PUI - Homework 8

## Jon Kastelan

#### compiled by #JKtours


# The Chernoff faces of CUSP 2017/18

The visualization I have chosen is a plot of Chernoff faces. I compiled a series of aggregate country level statistics for each of the countries represented by CUSP students in the 2017/18 class (along with a few additional misc. countries for comparison purposes). The statistics were mainly urban in nature, and could relate to the overall economy, mobility, health, education, technology, industry and law and order. A summary of the data is provided in the data section later. The code is also provided for reference.


## Visualisation
<kbd>![alt text](HW8_jlk635_Chernoff_faces_in_R.png "Chernoff faces of CUSP 2017/18 (and a few other countries)")</kbd>

#### Legend
The variables represented by characteristics of the Chernoff faces are as follows:


|**Variable No.** |**Chernoff face representation** |**Indicator Name** |
|:----------:|:----------|:------------|
1 |Height of face   |CO2 emissions (kt), total |
2 |Width of face   |Death rate, crude (per 1,000 people) |
3 |Structure of face |GDP per capita, PPP (constant 2011 international $) |
4 |Height of mouth  |New businesses registered (number) |
5 |Width of mouth   |Researchers in R&D (per million people) |
6 |Smiling     |Unemployment, total (% of total labor force) (national estimate) |
7 |Height of eyes    |Refugee population by country or territory of asylum (number) |
8 |Width of eyes    |Mobile cellular subscriptions (per 100 people) |
9 |Height of hair   |Individuals using the Internet (% of population) |
10 |Width of hair  |Population, total |
11 |Style of hair   |Scientific and technical journal articles, total |
12 |Height of nose   |Armed forces personnel, total |
13 |Width of nose  |Rail lines (total route-km) |
14 |Width of ear   |Fertility rate, total (births per woman) |
15 |Height of ear   |Intentional homicides (per 100,000 people) |
16 |[not fitted] |Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population) |
17 |[not fitted] |Adolescents out of school (% of lower secondary school age) |
18 |[not fitted] |Air transport, passengers carried |
|||

## Interpretation

The Chernoff faces provide a novel representation of each of the countries with 15 variables plotted on each face. There aren't a lot of techniques which could allow one to plot and visualize this number of variables in a simplified plot.

Let's start with a simple comparison of countries which look similar. One notes a strong geographical correlation by continent. Note: the variable 'Continent' **is not** included in our analysis, however one can observe similar faces amongst a lot of the European countries (e.g. Armenia, Denmark, France, Greece, Spain, and the United Kingdom. The notable omission here is Germany which appears to have different GDP per capita, larger refugee population, and mobile phone subscription rates than other comparable European countries.

Likewise for the South American countries, we see good similarities in the faces for Argentina, Brazil, Chile, Colombia and Costa Rica.

Assessing the countries which are very different to others, the United States, China, Germany, Russia and South Africa all appear very different (although worth noting China and the US look most similar to eachother compared to other countries). It is interesting to note that Canada appears more similar to Australia, rather than the United States (even though the Canada and the US are closer in geographical proximity).

Comparing key features, the ears of Pakistan, Israel, the Philippines and South Africa appear to be the biggest amongst all countries. The ears represent the two variables Fertility rate and Intentional homicides (per 100,000 people), which indicate both reproductive rates and avoidable deaths are higher in these countries.

Larger noses in China, Russia and the United States represent both the total size of military force (nose length), and total km of rail ines (nose width).

The style of hair in China and the United States represent the number of Scientific and technical journal articles published which is higher in those countries. And looking the % of population using the Internet by country represented by the height of the hair, this is larger for the US, China, Denmark, Germany and Russia; and lower for Greece, Pakistan and Indonesia.

Lastly, let's assess Unemployment by country, represented by the smiles. Happy faces represent low unemployment, and sad faces represent higher unemployment. Singapore, South Korea and Germany appear to have the lowest unemployment rates; whilst Armenia, Spain, Greece and South Africa have higher rates of Unemployment.



## What are Chernoff faces and why are they useful?

Chernoff faces were invented by the statistician Herman Chernoff in the early 70s as a method to display multivariate data on a human face. The idea behind using faces is that humans easily recognize and relate to faces and notice small changes without difficulty. 

Each day we see hundreds of faces, and our brains are busy computing patterns to determine if we recognise someone we know and respond accordingly. They're relatable, and humans naturally form an emotional connection to faces (unlike a bar chart or scatter plot), because we spend our days reading, interpretting (processing), and assessing whether we like it or not, judging faces - what 'looks good' and what doesn't.




## Data sources and processing


## Visualisation self-assessment and critique

