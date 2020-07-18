# creating data frame
import numpy as np
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]),
    pd.Series(['sineui', 89, 31]),
    pd.Series(['ikjoong', 68, 91]),
    pd.Series(['yoonsoo', 88, 75])
]

df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)
print(df1)


names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names,
    'english_score': english_scores,
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names),
    'english_score': np.array(english_scores),
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names),
    'english_score': pd.Series(english_scores),
    'math_score': pd.Series(math_scores)
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)
print(df1)


my_list = [
    {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
    {'name': 'sineui', 'english_score': 89, 'math_score': 31},
    {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
    {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)
print(df.dtypes)

# comma-separated values
iphone_df = pd.read_csv('data/iphone.csv', header=None)
iphone_df = pd.read_csv('data/iphone.csv', index_col = 0) # set first column as row names
type(iphone_df)

