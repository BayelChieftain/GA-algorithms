import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('data/social_net_stats.csv')

# Выберите пользователей, которые просмотрели хотя бы 100 постов и не совершили подписок
filtered_users = df[(df['views'] >= 100) & (df['subscriptions'] == 0)]

# Рассчитайте суммарное количество лайков от выбранных пользователей
total_likes = filtered_users['likes'].sum()

print(round(total_likes, 3))
