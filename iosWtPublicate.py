import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('data/social_net_stats.csv')

users_with_zero_publications_and_ios = ((df['publications'] == 0) & (df['platform'] == 'iOS')).sum()
total_users_ios = (df['platform'] == 'iOS').sum()
fraction_users_without_publications_on_ios = users_with_zero_publications_and_ios / total_users_ios

print(round(fraction_users_without_publications_on_ios, 3))
