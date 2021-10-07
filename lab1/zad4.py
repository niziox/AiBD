import pandas as pd
import numpy as np

data = np.array([['Arkadiusz', 'Kontek', 21, 'male'], ['Maciej', 'Gdzik', 34, 'male'],
                 ['Aleksandra', 'Podkowa', 18, 'female'], ['Robert', 'Kowak', 66, 'male'],
                 ['Agnieszka', 'Martin', 30, 'female']])

df = pd.DataFrame(data=data, columns=['name', 'surname', 'age', 'sex'], index=np.arange(1, len(data)+1))

print(df.info())

display(df.describe())

display(df.head(3))
