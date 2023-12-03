import pandas as pd
from pandas import Series, DataFrame
def top_players_by_year(year, csv_file):
    data_df1 = pd.read_csv(csv_file)
    data_df1.sort_values(by='H', ascending=False, inplace=True)
    selected_data1 = data_df1[data_df1['year'] == year]
    selected_column1 = selected_data1[['batter_name', 'H', 'year']]
    print(selected_column1.head(10))
    print("\n")

    data_df2 = pd.read_csv(csv_file)
    data_df2.sort_values(by='avg', ascending=False, inplace=True)
    selected_data2 = data_df2[data_df2['year'] == year]
    selected_column2 = selected_data2[['batter_name', 'avg', 'year']]
    print(selected_column2.head(10))
    print("\n")

    data_df3 = pd.read_csv(csv_file)
    data_df3.sort_values(by='HR', ascending=False, inplace=True)
    selected_data3 = data_df3[data_df3['year'] == year]
    selected_column3 = selected_data3[['batter_name', 'HR', 'year']]
    print(selected_column3.head(10))
    print("\n")

    data_df4 = pd.read_csv(csv_file)
    data_df4.sort_values(by='OBP', ascending=False, inplace=True)
    selected_data4 = data_df4[data_df4['year'] == year]
    selected_column4 = selected_data4[['batter_name', 'OBP', 'year']]
    print(selected_column4.head(10))
    print("\n")


## 2-1: 1)
top_players_by_year(2015, '2019_kbo_for_kaggle_v2.csv')
top_players_by_year(2016, '2019_kbo_for_kaggle_v2.csv')
top_players_by_year(2017, '2019_kbo_for_kaggle_v2.csv')
top_players_by_year(2018, '2019_kbo_for_kaggle_v2.csv')

## 2-1: 2)
data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
#data2_df.sort_values(by='war', ascending=False, inplace=True)
data_2018 = data_df[data_df['year']==2018]
max_war = data_2018.groupby('cp')['war'].idxmax()
selected_players =data_df.loc[max_war]
print("The highest war in 2018:", selected_players[['batter_name','cp','war']])
print("\n")

## 2-1: 3)
data2_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
selected_columns= ['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']
selected_data = data2_df[selected_columns]
corr_matrix=selected_data.corr()
highest=corr_matrix['salary'].sort_values(ascending=False).index[1]
print("The highest correalation with salary:",highest)