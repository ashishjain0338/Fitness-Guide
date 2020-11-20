import matplotlib.pyplot as plt
import pandas as pd
datafile = 'Output.xlsx'
dat = pd.read_excel(datafile)
x_data = dat['Day'].tolist()
y_data = []
for x in dat:
    if(x == 'Day' or x == 'Total'):
        continue
    y_data.append(dat[x].tolist())

four_determinant = ['Calories','Proteins','Fats','Carbhohydrates']
requiement = [1800 , 50, 70, 260]

for i in range(0,4):
    plt.title(four_determinant[i])
    plt.bar(x_data , y_data[i] , color = "#003f5c",label = 'Regular' )
    plt.bar(x_data, y_data[i + 4] , color = "#bc5090", label='Snacks' )
    plt.bar(x_data, y_data[i + 8] , color = "#ffa600", label='Total',alpha = 0.4)
    plt.xticks(rotation=45)
    plt.hlines(requiement[i], 0, x_data[-1], colors='black', linestyles='dashed')
    plt.xlabel('Dates')
    plt.ylabel('grams')
    plt.grid(True)
    plt.show()