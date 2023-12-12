from tabulate import tabulate
import pandas as pd
import random

# Исходный код
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


# Решение
def one_hot_view(data_frame, column_name, delete_origin):
    result = data_frame.copy()
    categories = result[column_name].unique().tolist()
    for category in categories:
        result.loc[result[column_name] != category, category] = 0
        result.loc[result[column_name] == category, category] = 1
    if delete_origin:
        result.drop(columns=[column_name], inplace=True)
    return result


def print_data_frame(data_frame):
    print(tabulate(data_frame, headers='keys'))


print("С сохранением исходного столбца:")
print_data_frame(one_hot_view(data, 'whoAmI', False).head())
print()
print("С удалением исходного столбца:")
print_data_frame(one_hot_view(data, 'whoAmI', True).head())
