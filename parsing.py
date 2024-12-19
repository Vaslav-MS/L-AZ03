import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Задание 3

url = 'https://divan.ru/category/divany'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

sofas = soup.find_all('div', class_='LlPhw')
data = []

for sofa in sofas:
    price_element = sofa.find('span', class_='KIkOH')
    if price_element:
        price = price_element.get_text(strip=True)
        price = int(price.replace(' ', '').replace('руб.', '').replace('₽', ''))
        data.append({'Цена': price})

df = pd.DataFrame(data)
df.to_csv('sofa_prices.csv')

average_price = df['Цена'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')

plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Распределение цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

