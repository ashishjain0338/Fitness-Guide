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
    plt.bar(x_data , y_data[i] , color = "#7ac36a",label = 'Regular',alpha=1 )
    plt.bar(x_data, y_data[i + 4] , color = "#f15a60", label='Snacks' ,alpha=1)
    plt.bar(x_data, y_data[i + 8] , color = "#5a9bd4", label='Total',alpha = 0.4)
    # plt.plot(x_data, y_data[i], 'b--',label='Regular')
    # plt.plot(x_data, y_data[i + 4],'r--', label='Snacks')
    # plt.plot(x_data, y_data[i + 8], label='Total', alpha=1)
    plt.xticks(rotation=45)
    plt.hlines(requiement[i], 0, x_data[-1], colors='black', linestyles='dashed',label='My Goal')
    plt.xlabel('Dates')
    plt.ylabel('grams')
    plt.legend(loc="upper right" )
    plt.grid(True)
    plt.show()