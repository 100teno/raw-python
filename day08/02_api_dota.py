# %%

import requests
import pandas as pd

url = 'https://api.opendota.com/api/heroes'

response = requests.get(url)

df = pd.DataFrame(response.json())
df.to_csv('heroes.csv', sep=';', index=False)
