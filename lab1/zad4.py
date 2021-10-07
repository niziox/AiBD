import pandas as pd
import numpy as np

# inicjalizacja danych
data = np.array([['Arkadiusz', 'Kontek', 21, 'male'], ['Maciej', 'Gdzik', 34, 'male'],
                 ['Aleksandra', 'Podkowa', 18, 'female'], ['Robert', 'Kowak', 66, 'male'],
                 ['Agnieszka', 'Martin', 30, 'female']])

# utworzenie DataFrame
df = pd.DataFrame(data=data, columns=['name', 'surname', 'age', 'sex'], index=np.arange(1, len(data)+1))

# wyświetlenie informacji o danych
print(df.info())

# wyświetlenie opisu danych danych
print(df.describe())

# wyświetlenie trzech pierwszych rekordów
print(df.head(3))
