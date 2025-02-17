import openpyxl as xl
from openpyxl.chart import Reference, BarChart

def process_workbook('transactions.xlsx'): 

    wb = xl.load_workbook('transactions.xlsx')
    sheet = wb['Sheet1']
    corrected_price_cell_name = sheet['d1']
    corrected_price_cell_name.value = 'corrected price'
    chart_cell_name = sheet['f1']
    chart_cell_name.value = 'chart'

    for row in range(2, sheet.max_row + 1):
        price = sheet.cell(row, 3) #this will give the price column
        corrected_price = price.value * 0.9
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price

    values = Reference(sheet,
              min_row=2,
              max_row=sheet.max_row,
              min_col=4,
              max_col=4)

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'f2')

    wb.save(filename)
