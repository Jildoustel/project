print('Dit is het csv uitlees programma')

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r, rij in df.iterrows():
    print(3)
    print("Naam is " + rij ["Name"])