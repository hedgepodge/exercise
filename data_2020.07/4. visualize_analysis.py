## Visualization

%matplotlib inline
import pandas as pd
df = pd.read_csv('data/broadcast.csv', index_col = 0)
df.plot(kind = 'line') # default
df.plot(y = 'KBS')
df.plot(y = ['KBS', 'JTBC'])
df[['KBS', 'JTBC']].plot()
df['KBS'].plot()

df.loc[2017].plot(kind = 'pie')

df = pd.read_csv('data/sports.csv', index_col = 0)
df.plot(kind = 'bar')
df.plot(kind = 'barh')
df.plot(kind = 'bar', stacked = True)
df['Female'].plot(kind = 'bar')

df = pd.read_csv('data/body.csv', index_col = 0)
df.plot(kind = 'hist', y = 'Height', bins = 15)

df = pd.read_csv('exam.csv')
df.head()
df['math score'].describe()

df.plot(kind = 'box', y = ['math score', 'reading score', 'writing score'])
df.plot(kind = 'scatter', x = 'math score', y = 'reading score')
df.plot(kind = 'scatter', x = 'math score', y = 'writing score')

# seaborn : Statistical Data Visualization
# !pip install seaborn==0.9.0

# KDE: kernel density estimation
import seaborn as sns
body_df = pd.read_csv('body.csv', index_col = 0)
body_df['Height'].value_counts().sort_index().plot()
sns.kdeplot(body_df['Height'], bw = 0.5)

body_df.plot(kind = 'hist', y = 'Height', bins = 15)
sns.distplot(body_df['Height'], bins = 15)

body_df.plot(kind = 'box', y = 'Height')
sns.violinplot(y=body_df['Height'])

body_df.plot(kind = 'scatter', x = 'Height', y = 'Weight')
sns.kdeplot(body_df['Height'], body_df['Weight'])

sns.lmplot(data = body_df, x = 'Height', y = 'Weight')

laptops_df = pd.read_csv('laptops.csv')
laptops_df['os'].unique()
sns.catplot(data = laptops_df, x = 'os', y = 'price', kind = 'strip')

laptops_df['processor_brand'].unique()
sns.catplot(data = laptops_df, x = 'os', y = 'price', kind = 'strip')
sns.catplot(data = laptops_df, x = 'os', y = 'price', kind = 'swarm', hue = 'processor_brand') # hue: coloring



## Analysis

body_df.corr()
sns.heatmap(df.corr())
sns.heatmap(df.corr(), annot=True)

# EDA: exploratory data analysis
df = pd.read_csv('young_survey.csv')
basic_info = df.iloc[:, 140:]
basic_info.describe()
basic_info['Gender'].value_counts()
basic_info['Handedness'].value_counts()
basic_info['Education'].value_counts()
sns.violinplot(data = basic_info, y = 'Age')
sns.violinplot(data = basic_info, x = 'Gender', y = 'Age', hue = 'Handedness')
sns.jointplot(data = basic_info, x = 'Height', y = 'Weight')

music = df.iloc[:, :19]
sns.heatmap(music.corr())
df.corr()['Age'].sort_values(ascending = False)
df.corr()['Getting up'][1:19].sort_values(ascending = False)

anal = df[['Branded clothing', 'Healthy eating', 'Musical instruments', 'New environment', 'Prioritising workload', 'Spending on looks', 'Workaholism', 'Writing', 'Writing notes']]
sns.heatmap(anal.corr())

df.corr().loc['Musical instruments', 'Writing']
df.corr().loc['Spending on looks', 'Branded clothing']
df.corr().loc['Writing notes', 'New environment']
df.corr().loc['Workaholism', 'Healthy eating']
df.corr().loc['Prioritising workload', 'Healthy eating']

# q
df = pd.read_csv('occupations.csv', index_col = 0)
df.loc[df['gender']=='F']['occupation'].value_counts()
df.loc[df['gender']=='M']['occupation'].value_counts()

# cluster analysis
df = pd.read_csv('young_survey.csv')
interests = df.loc[:, 'History':'Pets']
corr = interests.corr()
corr['History'].sort_values(ascending = False)
sns.clustermap(corr)

# q
df = pd.read_csv('titanic.csv')
df['Ageg'] = df['Age'] // 10 * 10
df['Ageg'].value_counts().sort_values(ascending = False)
df[['Ageg', 'Fare']].sort_values(by = 'Fare', ascending = False)
df['Survived'].value_counts()
df['Pclass'].value_counts()
df.plot(kind='scatter', x='Pclass', y='Survived')
sns.kdeplot(df['Pclass'], df['Survived'])
sns.stripplot(data=df, x="Survived", y="Age")
sns.violinplot(data=df, x="Survived", y="Age")
sns.stripplot(data=df, x="Survived", y="Age", hue="Sex")

# groupby
df = pd.read_csv('data/broadcast.csv', index_col = 0)
df.plot()
df['Total'] = df.sum(axis = 'columns')
df.plot(y = 'Total')
df['Group 1'] = df.loc[:, 'KBS':'SBS'].sum(axis = 'columns')
df['Group 2'] = df.loc[:, 'TV CHOSUN':'MBN'].sum(axis = 'columns')
df.plot(y = ['Group 1', 'Group 2'])

# containing string
df = pd.read_csv('albums.csv', encoding = 'latinl')
df['Genre'].unique()
df[df['Genre'] == 'Blues']
df[df['Genre'].str.contains('Blues')]
df[df['Genre'].str.startswith('Blues')]
df['Contains Blues'] = df['Genre'].str.contains('Blues')
 
df = pd.read_csv('parks.csv')
address = df['소재지도로명주소'].str.split(n = 1, expand = True) # divide first blank only
df['관할구역'] = address[0]

df = pd.read_csv('laptops.csv')
brand_nation = {
    'Dell':'U.S.',
    'Apple':'U.S.',
    'Acer':'Taiwan',
    'HP':'U.S.',
    'Lenovo':'China',
    'Alienware':'U.S.',
    'Microsoft':'U.S.',
    'Asus':'Taiwan'
    }
df['brand_nation'] = df['brand'].map(brand_nation)
 
nation_groups = df.groupby('brand_nation')
type(nation_groups)
nation_groups.count()
nation_groups.max()
nation_groups.mean()
nation_groups.first()
nation_groups.last()
nation_groups.plot(kind = 'box', y = 'price')
nation_groups.plot(kind = 'hist', y = 'price')
 
price_df = pd.read_csv('vegetable_price.csv')
quantity_df = pd.read_csv('vegetable_quantity.csv')
pd.merge(price_df, quantity_df, on = 'Product')
pd.merge(price_df, quantity_df, on = 'Product', how = 'left')
pd.merge(price_df, quantity_df, on = 'Product', how = 'right')
pd.merge(price_df, quantity_df, on = 'Product', how = 'outer')
 
 
# enhancing data quality
df = pd.read_csv('attendance.csv', index_col = 0)
df.isnull().sum()
df.dropna()
df.dropna(inplace = True)
df = pd.read_csv('attendance.csv', index_col = 0)
df.dropna(axis = 'columns')
df.fillna(df.mean())
df.fillna(df.median(), inplace = True)
 
df = pd.read_csv('dust.csv', index_col = 0)
df.index.value_counts()
df.loc['07월 31일']
df.drop_duplicates(inplace = True)
 
df = df.T.drop_duplicates().T # cannot use inplace parameter
 
df = pd.read_csv('beer.csv', index_col = 0)
df.plot(kind = 'box', y = 'abv')
df['abv'].describe()
q1 = df['abv'].quantile(0.25)
q3 = df['abv'].quantile(0.75)
iqr = q3 - q1
condition = (df['abv'] < q1 - 1.5 * iqr) | (df['abv'] > q3 + 1.5 * iqr)
df[condition]
df.loc[2250, 'abv'] = 0.055
df.loc[2250]
df[contition].index
df.drop(df[condition].index, inplace = True)
df.plot(kind = 'box', y = 'abv')
 
df = pd.read_csv('exam_outlier.csv', index_col = 0)
df[df['writing score'] > 100]
df.drop(51, inplace = True)
df.plot(kind = 'scatter', x = 'reading score', y = 'writing score')
df.corr()
 
condition = (df['writing score'] > 90) & (df['reading score'] < 40)
df[condition]
df.drop(373, inplace = True)
df.plot(kind = 'scatter', x = 'reading score', y = 'writing score')
df.corr()
 
# q
df = pd.read_csv('data/movie_metadata.csv')
q1 = df['budget'].quantile(0.25)
q3 = df['budget'].quantile(0.75)
iqr = q3 - q1
df[df['budget'] < q3 + 5 * iqr].plot(kind = 'scatter', x = 'budget', y = 'imdb_score')
 
# q
df.drop(df.sort_values(by = 'budget', ascending = False).head(15).index, inplace = True)
df.plot(kind = 'scatter', x = 'budget', y = 'imdb_score')
