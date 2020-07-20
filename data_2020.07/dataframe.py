# l. indexing data frame 

import pandas as pd
iphone_df = pd.read_csv('data/iphone.csv', index_col = 0)
iphone_df.loc['iPhone 8', '메모리']
iphone_df.loc['iPhone X', :]
iphone_df.loc['iPhone X']
type(iphone_df.loc['iPhone X'])
iphone_df.loc[:, '출시일']
iphone_df['출시일']
type(iphone_df['출시일'])

# q1
import pandas as pd
df = pd.read_csv('data/broadcast.csv', index_col=0)
df[['SBS','JTBC']]

# q2
import pandas as pd
samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')
combined_df = pd.DataFrame({
    'day': samsong_df['요일'], 
    'samsong': samsong_df['문화생활비'], 
    'hyundee': hyundee_df['문화생활비']
})
combined_df

# ll. indexing data frame
iphone_df.loc[['iPhone X', 'iPhone 8']]
type(iphone_df.loc[['iPhone X', 'iPhone 8']])
iphone_df[['Face ID', '출시일', '메모리']]
iphone_df.loc['iPhone 8':'iPhone XS']
iphone_df.loc[:'iPhone XS']
iphone_df.loc[:, '메모리':'Face ID']
iphone_df.loc['iPhone 7':'iPhone X':, '메모리':'Face ID']

# lll. conditionally indexing data frame
iphone_df.loc[[True, False, True, True, False, True, False]]
iphone_df.loc[[True, False, False, True]] # presume last three as False
iphone_df.loc[:, [True, False, False, True]]
iphone_df['디스플레이'] > 5
iphone_df.loc[iphone_df['디스플레이'] > 5]
iphone_df['Face ID'] == 'Yes'
iphone_df.loc[iphone_df['Face ID'] == 'Yes']
condition = (iphone_df['디스플레이'] > 5) & (iphone_df['Face ID'] == 'Yes') # or -> |
iphone_df[condition]

# q
import pandas as pd
df = pd.read_csv('data/broadcast.csv', index_col=0)
df.loc[df['SBS'] < df['TV CHOSUN'], ['SBS', 'TV CHOSUN']]

# integer location
iphone_df.iloc[2, 4]
iphone_df.iloc[[1, 3], [1, 4]]
iphone_df.iloc[3:, 1:4]

# add value to data frame
iphone_df.loc['iPhone 8', '메모리'] = '2.5GB'
iphone_df
iphone_df.loc['iPhone 8', '출시 버전'] = 'iOS 10.3'
iphone_df.loc['iPhone 8'] = ['2016-09-22', '4.7', '2GB', 'iOS 11.0', 'No']
iphone_df['디스플레이'] = ['4.7 in', '5.5 in', '4.7 in', '5.5 in', '5.8 in', '5.8 in', '6.5 in']
iphone_df['디스플레이'] = 'No'

iphone_df[['디스플레이', 'Face ID']] = 'x'
iphone_df.loc[['iPhone 7', 'iPhone X']] = 'o'
iphone_df.loc[['iPhone 7': 'iPhone X']] = 'o'

iphone_df = pd.read_csv('data/iphone.csv', index_col = 0)
iphone_df.loc[iphone_df['디스플레이'] > 5] = 'p'
iphone_df.iloc[[1, 3], [1, 4]] = 'v'

iphone_df.loc['iPhone XR'] = ['2018-10-26', '6.1', '3GB', 'iOS 12.0.1', 'Yes']
iphone_df['제조사'] = 'Apple'
iphone_df.drop('iPhone XR', axis = 'index', inplace = True) # index = row
iphone_df.drop('제조사', axis = 'columns', inplace = True)

iphone_df.drop(['iPhone 7', 'iPhone 8', 'iPhone XR'], axis = 'index', inplace = True)

# q
import pandas as pd
df = pd.read_csv('data/body_imperial2.csv', index_col=0)
df["Obesity"] = "Normal"
df.loc[:10,"Gender"] = "Male"
df.loc[11:,"Gender"] = "Female"
df

# set index and column
liverpool_df = pd.read_csv('data/liverpool.csv', index_col = 0)

liverpool_df.rename(columns={'position': 'Position'}, inplace = True)
liverpool_df.rename(columns={'position': 'Position', 'born': 'Born', 'number': 'Number', 'nationality': 'Nationality'}, inplace = True)
liverpool_df.index.name = 'Player Name'
liverpool_df.index
liverpool_df['Player Name'] = liverpool_df.index
liverpool_df.set_index('Number', inplace = True)

# q
import pandas as pd 
df = pd.read_csv('data/toeic.csv')
pass_total = df['LC'] + df['RC'] > 600
pass_both = (df['LC'] >= 250) & (df['RC'] >= 250)
df['합격 여부'] = pass_total & pass_both
df

# q
import pandas as pd
df = pd.read_csv('https://github.com/codeit-courses/data-science/raw/master/Puzzle_before.csv')
df['A'] = df['A'] * 2
df[df.loc[:, 'B':'E'] < 80] = 0
df[df.loc[:, 'B':'E'] >= 80] = 1
df.loc[2, 'F'] = 99
df

# handling big data frame
laptops_df = pd.read_csv('data/laptops.csv')
laptops_df.head(7)
laptops_df.tail(6)

laptops_df.shape
laptops_df.columns
laptops_df.info()
laptops_df.describe()
laptops_df.sort_values(by = 'price', ascending = False, inplace = True)

laptops_df['brand'].unique()
laptops_df['brand'].value_counts()
laptops_df['brand'].describe()

# q
df = pd.read_csv('data/world_cities.csv', index_col = 0)
df['City / Urban area'].value_counts()
df['City / Urban area'].value_counts().shape
df['Country'].value_counts().shape

df["Density"] = df["Population"] / df["Land area (in sqKm)"]
df_high_density = df[df["Density"] > 10000]
df_high_density .info()

density_ranks = df.sort_values(by="Density", ascending = False)
density_ranks['City / Urban area']

countries = df['Country'].value_counts()
countries[countries == 4]

# q
import pandas as pd
df = pd.read_csv('data/enrolment_1.csv')
df["status"] = "allowed"

boolean1 = df["course name"] == "information technology"
boolean2 = df["year"] == 1
df.loc[boolean1 & boolean2, "status"] = "not allowed"

boolean3= df["course name"] == "commerce"
boolean4= df["year"] == 4
df.loc[boolean3& boolean4, "status"] = "not allowed"

allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"
df

# q
import pandas as pd
df = pd.read_csv('data/enrolment_2.csv')

allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

for course in auditorium_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"
for course in large_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
for course in medium_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
for course in small_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"
df

# q
import pandas as pd
df = pd.read_csv('data/enrolment_3.csv')

allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

for i in range(len(auditorium_list)):
    df.loc[(df["course name"] == sorted(auditorium_list)[i]) & allowed, "room assignment"] = "Auditorium-" + str(i + 1)
for i in range(len(large_room_list)):
    df.loc[(df["course name"] == sorted(large_room_list)[i]) & allowed, "room assignment"] = "Large-" + str(i + 1)
for i in range(len(medium_room_list)):
    df.loc[(df["course name"] == sorted(medium_room_list)[i]) & allowed, "room assignment"] = "Medium-" + str(i + 1)
for i in range(len(small_room_list)):
    df.loc[(df["course name"] == sorted(small_room_list)[i]) & allowed, "room assignment"] = "Small-" + str(i + 1)

df.rename(columns={"room assignment": "room number"}, inplace = True)
df
