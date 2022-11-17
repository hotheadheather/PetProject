from flask import session
import xlsxwriter
from models import db






# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('donations.xlsx')
worksheet = workbook.add_worksheet()

 # Write some data headers.

worksheet.write(0, 0, 'ID')   
worksheet.write(0, 1, 'First Name')  
worksheet.write(0, 2, 'Last Name')  
worksheet.write(0, 3, 'Email')    
worksheet.write(0, 4, 'Gender') 
worksheet.write(0, 5, 'Food Type')   
worksheet.write(0, 6, 'Amount')  
worksheet.write(0, 7, 'Weight')  
worksheet.write(0, 8, 'Date')    
   

donat = (

    [1,'Heatherrrr', 'Whittlesey', 'hkw@aol.com', 'F', 'Dry Dog Food', 14, 'LBS', '10-31-2022' ],
    [2,'Holly', 'Whittlesey', 'holly@hotmail.com', 'F', 'Wet Dog Food', 45, 'OZ', '10-1-2022'],
    [3,'Alivia', 'Conley', 'liv@aol.com', 'F','Turtle', 17, 'OZ', '11-1-2022'],
    [4,'Ryan', 'Conley', 'ry@aol.com', 'M','Rabbit', 18, 'OZ', '11-6-2022'],
)


# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for id, firstname, lastname, email, gender, foodtype, amount, weight, date in (donat):
    worksheet.write(row, col,    id)
    worksheet.write(row, col + 1, firstname)
    worksheet.write(row, col + 2, lastname)
    worksheet.write(row, col + 3, email)
    worksheet.write(row, col + 4, gender)
    worksheet.write(row, col + 5, foodtype)
    worksheet.write(row, col + 6, amount)
    worksheet.write(row, col + 7, weight)
    worksheet.write(row, col + 8, date)
    
    row += 1

workbook.close()