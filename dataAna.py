
import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('data/social_net_stats.csv')

users_with_zero_publications = (df['publications'] == 0).sum()
total_users = len(df)
fraction_users_without_publications = users_with_zero_publications / total_users

print(round(fraction_users_without_publications, 3))
