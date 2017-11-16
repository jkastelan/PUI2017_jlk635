
# PUI - Homework 8

## Jon Kastelan

#### compiled by #JKtours


# The Chernoff faces of CUSP 2017/18

The visualization I have chosen is a plot of **Chernoff faces**. 

I compiled a series of aggregate country level statistics for each of the countries represented by CUSP students in the 2017/18 class - along with a few additional misc. countries for comparison purposes. The statistics were mainly urban in nature, relating to the overall economy, mobility, health, education, technology, industry and law and order. A summary of the data is provided in the data section later. The R code is also [provided](https://raw.githubusercontent.com/jkastelan/PUI2017_jlk635/master/HW8_jlk635/HW8_jlk635_Code_for_Chernoff_faces_in_R.txt) in the repo for reference.


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

Let's start with a simple comparison of countries which look similar. One notes a strong geographical correlation by continent. Note: the variable 'Continent' **is not** included in our analysis, however one can observe similar faces amongst a lot of the European countries e.g. Armenia, Denmark, France, Greece, Spain, and the United Kingdom. The notable omission here is Germany which appears to have different GDP per capita, larger refugee population, and mobile phone subscription rates than other comparable European countries.

Likewise for the Central and South American countries, we see good similarities in the faces for Argentina, Brazil, Chile, Colombia and Costa Rica.

Assessing the countries which are very different to others, the United States, China, Germany, Russia and South Africa all appear very different (although worth noting China and the US look most similar to eachother compared to other countries). It is interesting to note that Canada appears more similar to Australia, rather than the United States; even though the Canada and the US are closer in geographical proximity.

Comparing key features, the ears of Pakistan, Israel, the Philippines and South Africa appear to be the biggest amongst all countries. The ears represent the two variables Fertility rate and Intentional homicides (per 100,000 people), which indicate both reproductive rates and avoidable deaths are higher in these countries. Russia and South Africa have the highest crude death rates (deaths per 1,000 people) as indicated by the width of their faces.

Larger noses in China, Russia and the United States represent both the total size of military force (nose length), and total km of rail ines (nose width).

The style of hair in China and the United States represent the number of Scientific and technical journal articles published which is higher in those countries. And looking at the % of population using the Internet by country represented by the height of the hair, this is larger for the US, China, Denmark, Germany and Russia; and lower for Greece, Pakistan and Indonesia. China and the US are also the largest polluters based on CO2 emissions (kt), total; represented by the height of the face.

Lastly, let's assess Unemployment by country, represented by the smiles. Happy faces represent low unemployment, and sad faces represent higher unemployment. Singapore, South Korea and Germany appear to have the lowest unemployment rates; whilst Armenia, Spain, Greece and South Africa have higher rates of Unemployment.




## What are Chernoff faces and why are they useful?

Chernoff faces were invented by the statistician Herman Chernoff in the early 1970's as a method to display multivariate data on a human face. The idea behind using faces is that humans easily recognize and relate to faces and notice small changes without difficulty. 

Each day we see hundreds of faces, and our brains are busy computing patterns to determine if we recognise someone we know and respond accordingly. They're relatable, and humans naturally form an emotional connection to faces (unlike a bar chart or scatter plot), because we spend our days reading, interpretting (processing), and assessing whether we like it or not. Judging faces - what 'looks good' and what doesn't.

Here's a nice link to another analysis looking at [The Faces of Crime](http://flowingdata.com/2010/08/31/how-to-visualize-data-with-cartoonish-faces/crime-chernoff-faces-by-state-edited-2/) (by state) in the United States.



## Data sources and processing

The data for this analysis was sourced from the World Bank: World Development indicators (WDI) [website](https://data.worldbank.org/data-catalog/world-development-indicators). The indicator name, code, definition and source are provided at the bottom of this section. The year selected was **2012**.

Data was missing for a few variables in specific countries. In the case of missing data, a value was assigned based on one of median, mean or quantiles, depending on which of the variables were missing and obeserved skewness of the variable across countries for which information was available (e.g. the mean CO2 emissions may have been skewed by larger polluters, so a median was used instead).  


|**Variable No.** |**Indicator Name** |**Code** |**Long definition**|**Source** |
|:---------------:|:------------------|:--------|:-----------------------------------------|:----------|
1 |CO2 emissions (kt) |EN.ATM.CO2E.KT |Carbon dioxide emissions are those stemming from the burning of fossil fuels and the manufacture of cement. They include carbon dioxide produced during consumption of solid, liquid, and gas fuels and gas flaring. |Carbon Dioxide Information Analysis Center, Environmental Sciences Division, Oak Ridge National Laboratory, Tennessee, United States. |
2 |Death rate, crude (per 1,000 people) |SP.DYN.CDRT.IN |Crude death rate indicates the number of deaths occurring during the year, per 1,000 population estimated at midyear. Subtracting the crude death rate from the crude birth rate provides the rate of natural increase, which is equal to the rate of population change in the absence of migration. |(1) United Nations Population Division. World Population Prospects, (2) Census reports and other statistical publications from national statistical offices, (3) Eurostat: Demographic Statistics, (4) United Nations Statistical Division. Population and Vital Statistics Reprot (various years), (5) U.S. Census Bureau: International Database, and (6) Secretariat of the Pacific Community: Statistics and Demography Programme. |
3 |GDP per capita, PPP (constant 2011 international $) |NY.GDP.PCAP.PP.KD |GDP per capita based on purchasing power parity (PPP). PPP GDP is gross domestic product converted to international dollars using purchasing power parity rates. An international dollar has the same purchasing power over GDP as the U.S. dollar has in the United States. GDP at purchaser's prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in constant 2011 international dollars. |World Bank, International Comparison Program database. |
4 |New businesses registered (number) |IC.BUS.NREG |New businesses registered are the number of new limited liability corporations registered in the calendar year. |World Bank's Entrepreneurship Survey and database (http://econ.worldbank.org/research/entrepreneurship). |
5 |Researchers in R&D (per million people) |SP.POP.SCIE.RD.P6 |Researchers in R&D are professionals engaged in the conception or creation of new knowledge, products, processes, methods, or systems and in the management of the projects concerned. Postgraduate PhD students (ISCED97 level 6) engaged in R&D are included. |United Nations Educational, Scientific, and Cultural Organization (UNESCO) Institute for Statistics. |
6 |Unemployment, total (% of total labor force) (national estimate) |SL.UEM.TOTL.NE.ZS |Unemployment refers to the share of the labor force that is without work but available for and seeking employment. Definitions of labor force and unemployment differ by country. |International Labour Organization, ILOSTAT database. Data retrieved in March 2017. |
7 |Refugee population by country or territory of asylum |SM.POP.REFG |Refugees are people who are recognized as refugees under the 1951 Convention Relating to the Status of Refugees or its 1967 Protocol, the 1969 Organization of African Unity Convention Governing the Specific Aspects of Refugee Problems in Africa, people recognized as refugees in accordance with the UNHCR statute, people granted refugee-like humanitarian status, and people provided temporary protection. Asylum seekers--people who have applied for asylum or refugee status and who have not yet received a decision or who are registered as asylum seekers--are excluded. Palestinian refugees are people (and their descendants) whose residence was Palestine between June 1946 and May 1948 and who lost their homes and means of livelihood as a result of the 1948 Arab-Israeli conflict. Country of asylum is the country where an asylum claim was filed and granted. |United Nations High Commissioner for Refugees (UNHCR), Statistics Database, Statistical Yearbook and data files, complemented by statistics on Palestinian refugees under the mandate of the UNRWA as published on its website. Data from UNHCR are available online at: www.unhcr.org/en-us/figures-at-a-glance.html. |
8 |Mobile cellular subscriptions (per 100 people) |IT.CEL.SETS.P2 |Mobile cellular telephone subscriptions are subscriptions to a public mobile telephone service that provide access to the PSTN using cellular technology. The indicator includes (and is split into) the number of postpaid subscriptions, and the number of active prepaid accounts (i.e. that have been used during the last three months). The indicator applies to all mobile cellular subscriptions that offer voice communications. It excludes subscriptions via data cards or USB modems, subscriptions to public mobile data services, private trunked mobile radio, telepoint, radio paging and telemetry services. |International Telecommunication Union, World Telecommunication/ICT Development Report and database. |
9 |Individuals using the Internet (% of population) |IT.NET.USER.ZS |Internet users are individuals who have used the Internet (from any location) in the last 3 months. The Internet can be used via a computer, mobile phone, personal digital assistant, games machine, digital TV etc. |International Telecommunication Union, World Telecommunication/ICT Development Report and database. |
10 |Population, total |SP.POP.TOTL |Total population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship. The values shown are midyear estimates. |(1) United Nations Population Division. World Population Prospects, (2) Census reports and other statistical publications from national statistical offices, (3) Eurostat: Demographic Statistics, (4) United Nations Statistical Division. Population and Vital Statistics Report (various years), (5) U.S. Census Bureau: International Database, and (6) Secretariat of the Pacific Community: Statistics and Demography Programme. |
11 |Scientific and technical journal articles |IP.JRN.ARTC.SC |Scientific and technical journal articles refer to the number of scientific and engineering articles published in the following fields: physics, biology, chemistry, mathematics, clinical medicine, biomedical research, engineering and technology, and earth and space sciences. |National Science Foundation, Science and Engineering Indicators. |
12 |Armed forces personnel, total |MS.MIL.TOTL.P1 |Armed forces personnel are active duty military personnel, including paramilitary forces if the training, organization, equipment, and control suggest they may be used to support or replace regular military forces. |International Institute for Strategic Studies, The Military Balance. |
13 |Rail lines (total route-km) |IS.RRS.TOTL.KM |Rail lines are the length of railway route available for train service, irrespective of the number of parallel tracks. |World Bank, Transportation, Water, and Information and Communications Technologies Department, Transport Division. |
14 |Fertility rate, total (births per woman) |SP.DYN.TFRT.IN |Total fertility rate represents the number of children that would be born to a woman if she were to live to the end of her childbearing years and bear children in accordance with age-specific fertility rates of the specified year. |(1) United Nations Population Division. World Population Prospects, (2) Census reports and other statistical publications from national statistical offices, (3) Eurostat: Demographic Statistics, (4) United Nations Statistical Division. Population and Vital Statistics Reprot (various years), (5) U.S. Census Bureau: International Database, and (6) Secretariat of the Pacific Community: Statistics and Demography Programme. |
15 |Intentional homicides (per 100,000 people) |VC.IHR.PSRC.P5 |Intentional homicides are estimates of unlawful homicides purposely inflicted as a result of domestic disputes, interpersonal violence, violent conflicts over land resources, intergang violence over turf or control, and predatory violence and killing by armed groups. Intentional homicide does not include all intentional killing; the difference is usually in the organization of the killing. Individuals or small groups usually commit homicide, whereas killing in armed conflict is usually committed by fairly cohesive groups of up to several hundred members and is thus usually excluded. |UN Office on Drugs and Crime's International Homicide Statistics database. |
16 |Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population) |SI.POV.DDAY |Poverty headcount ratio at $1.90 a day is the percentage of the population living on less than $1.90 a day at 2011 international prices. As a result of revisions in PPP exchange rates, poverty rates for individual countries cannot be compared with poverty rates reported in earlier editions. |World Bank, Development Research Group. Data are based on primary household survey data obtained from government statistical agencies and World Bank country departments. Data for high-income economies are from the Luxembourg Income Study database. For more information and methodology, please see PovcalNet (http://iresearch.worldbank.org/PovcalNet/index.htm). |
17 |Adolescents out of school (% of lower secondary school age) |SE.SEC.UNER.LO.ZS |Adolescents out of school are the percentage of lower secondary school age adolescents who are not enrolled in school. |United Nations Educational, Scientific, and Cultural Organization (UNESCO) Institute for Statistics. |
18 |Air transport, passengers carried |IS.AIR.PSGR |Air passengers carried include both domestic and international aircraft passengers of air carriers registered in the country. |International Civil Aviation Organization, Civil Aviation Statistics of the World and ICAO staff estimates. |
|||||




## Visualisation self-assessment and critique
Overall, the visualisation looks nice and provides an interesting way to compare and contrast many variable across countries.

For the data munging part, it would have been nice to visualize the additional variables we had available; Poverty %, Adolescent school attendance % and Air traffic passengers, which we could have potentially visualized with a neck width, neck length and shoulder breadth. There were a few crude assumptions made to populate missing data. Specifically, assigning median or quantile values to the countries with missing values for selected variables could be improved in a follow-up analysis to obtain more applicable figures. We could also use more current data - 2012 is a little dated now.

The graphics in this package look a little 1990's, so perhaps this could be improved for a more visual and meaningful insight. 

The color scheme isn't perfect either, and with further time I'd look to enhance this, potentially remove color all together and present outlines of faces which would put more emphasis on the shapes and sizes of observed features (rather than color).

It would be good also to include the legend as part of the chart, rather than below. A visual representation of the legend, similar to the example in The Faces of Crime dataset would also benefit.

Lastly, I left a couple of countries out (accidently.., whoops). I'd include India, Mexico and Taiwan in a follow-up piece.

**Hope you enjoyed the analysis, feedback welcome! (email: jlk635 at nyu.edu)**

**Thank you**
