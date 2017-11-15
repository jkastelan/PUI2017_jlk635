
# PUI - Homework 8

## Jon Kastelan

#### compiled by #JKtours


# The Chernoff faces of CUSP 2017/18

The visualization I have chosen is a plot of Chernoff faces. I compiled a series of statistics by country for each of the countries represented by CUSP students in the 2017/18 class. The statistics were mainly urban in nature, and could relate to the overall economy, mobility, health, law and order. A summary of the data is provided in the data section later. The code is also provided for reference.


## Visualisation
<kbd>![alt text](HW8_jlk635_Chernoff_faces_in_R.png "Chernoff faces of CUSP 2017/18 (and a few other countries)")</kbd>

#### Legend
The variables represented by the Chernoff faces can be interpreted as follows:


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi-squared |	2, Gender, Age |	Gender: Nominal, Age: Ordinal |	1, Visual Stress (VS) |	Ordinal (reduction in VS) |	2, Overlay colour, Age |	Overlay colour: Nominal |	Does Gender Influence Colour Choice in the Treatment of Visual Stress? |	No difference between overlay colour in treatment of visual stress for either gender |	0.15 |	http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0163326 |
Multivariate Regression |	2, Palmer Drought Severity Index (PDSI), and Year |	PDSI: Continuous ordinal, Year: Interval |	1, Normalized Difference Vegetation Index (NDVIt) (natural logarithm is fitted) |	Continuous |	 |	 |	Do climate (PDSI) and non-climatic (Year) factors impact Normalised difference in Vegetation (NDVI) in Northwest China |	PDSI and/or Year have no effect on NDVI in Northwest China |	0.05 |	http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0126044 |
Logistic Regression |	7, Daily consumption of vegetables, fruits, or berries; Physical activity less than 4hours per week; History of high blood glucose; Use of blood pressure medication; Waist circumfrence; BMI; and Age |	Waist circumfrence; BMI; and Age - Continuous Ordinal, Daily consumption of vegetables, fruits, or berries; Physical activity less than 4hours per week; History of high blood glucose; Use of blood pressure medication - Ordinal |	1, Diabetes Incidence |	Ordinal (Diabetes predicted) |	2, Gender, Cohort year (1987, 1992) |	Gender: Categorical, Cohort year: Categorical |	Can a short questionaire, looking at a few simple factors be used to identify individuals at high(er) risk of developing diabetes. |	Daily consumption of vegetables, fruits, or berries; Physical activity hours per week; History of high blood glucose; Use of blood pressure medication; Waist circumfrence; BMI; and Age do not help identify individuals at risk or incidence of diabetes |	0.05 |	http://care.diabetesjournals.org/content/26/3/725?26/3/725&legid=diacare;26/3/725&patientinform-links=yes&legid=diacare;26/3/725 |
  |||||||||


