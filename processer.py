import pandas as pd
from openpyxl import load_workbook
infile = "Data.xlsx"
nut_value_file = "Nuttional Chart.xlsx"
output_file = 'Output.xlsx'

nut = pd.read_excel(nut_value_file)
nut_data = nut.values.tolist()
food_item_value = nut['Item'].tolist()
data = pd.read_excel(infile)
writer = pd.ExcelWriter(output_file , engine='openpyxl')
first_append = True
for x in data.values.tolist():
    day_nut = {'Regular': [0, 0, 0, 0], 'Snack': [0, 0, 0, 0]}
    for y in x[1:]:
        if(str(y) == "nan"):
            continue
        try:
            item = y[:y.index('(')]
            Qty = float(y[y.index('(') + 1 : y.index(')')])
        except:
            item = y
            Qty = 1
        if(item not in food_item_value):
            print(item ,'not found in nutrional Chart')
            continue
        else:
            ind = food_item_value.index(item)


        if (nut_data[ind][2] == 'Regular'):
            for i in range(0,4):
                day_nut['Regular'][i] += (nut_data[ind][3 + i]*Qty/nut_data[ind][1])
        else:
            for i in range(0,4):
                day_nut['Snack'][i] += (nut_data[ind][3 + i]*Qty/nut_data[ind][1])
    day_nut['aggregate'] = [0,0,0,0]
    for i in range(0,4):
        day_nut['aggregate'][i] = day_nut['Regular'][i] + day_nut['Snack'][i]
    df = pd.DataFrame({'Day':x[0].to_pydatetime().strftime('%d/%m'),
                       'Regular-Calories':day_nut['Regular'][0], 'Regular-Proteins':day_nut['Regular'][1], 'Regular-Fat':day_nut['Regular'][2], 'Regular-Carbs':day_nut['Regular'][3],
                       'Snack-Calories': day_nut['Snack'][0], 'Snack-Proteins': day_nut['Snack'][1],
                       'Snack-Fat': day_nut['Snack'][2], 'Snack-Carbs': day_nut['Snack'][3],'Total':'---------->',
                       'Calories': day_nut['aggregate'][0], 'Proteins': day_nut['aggregate'][1],
                       'Fat': day_nut['aggregate'][2], 'Carbs': day_nut['aggregate'][3],
                       },index=[0])

    if first_append:
        first_append = False
        df.to_excel(writer, sheet_name='Regular',index=False)
        writer.save()
    else:
        writer.book = load_workbook(output_file)
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel(output_file)
        df.to_excel(writer, sheet_name='Regular',index=False, header=False, startrow=len(reader) + 1)
        writer.save()



