# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15FUVobjP73D-8VwaAteKmVcfcjXyCoSk
"""

import pandas as pd

import seaborn as sns

penguins = sns.load_dataset("penguins")
penguins.head()

"""## Задача №65.

Использовать 2-3 точечных графика

● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
"""

sns.scatterplot(data = penguins, x="bill_length_mm", y="island")

sns.scatterplot(data = penguins, x="sex", y="bill_length_mm", hue="body_mass_g")

sns.scatterplot(data = penguins, x="body_mass_g", y="flipper_length_mm", hue="island")

sns.scatterplot(data = penguins, x="body_mass_g", y="flipper_length_mm", size= "island")

sns.scatterplot(data = penguins, x="body_mass_g", y="flipper_length_mm", style="island")

"""● Использовать PairGrid с типом графика на ваш выбор

● Изобразить Heatmap

● Использовать 2-3 гистограммы
"""

sns.histplot(data=penguins, x="bill_length_mm")

penguins.head()

cols = ['island', 'bill_length_mm', 'bill_depth_mm',
'flipper_length_mm']
g = sns.PairGrid(penguins[cols])
g.map(sns.scatterplot)

cols = ['species', 'island' ,'bill_length_mm', 'bill_depth_mm',
'flipper_length_mm', 'body_mass_g', 'sex']
g = sns.PairGrid(penguins[cols])
g.map(sns.scatterplot)

"""## Задача №67.

Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""

penguins.head()

temp = []
len(penguins)
for i in range(len(penguins)):
  if penguins['bill_length_mm'][i] <= 35:
    temp.append('low')
  elif penguins['bill_length_mm'][i] >= 42:
    temp.append('high')
  else:
    temp.append('middle')

penguins["показатель длины клюва"] = temp

penguins.head(15)