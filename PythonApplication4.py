
import pyodbc
import PySimpleGUI as sg

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-A8U6UNM5\SQLEXPRESS;"
                      "Database=LoginDB;"
                      "Trusted_Connection=yes;")
sg.theme('Python')
layout = [[sg.Text('Name'), sg.Input()],
          [sg.Text('Mobile Number'), sg.Input()],
          [sg.Text('Address'), sg.Input()],
          [sg.Button('Save'), sg.Button('Cancel')]]
Window = sg.Window('User Data Entry',layout, element_justification='center')
while True:
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
         break
    elif event == 'Save':
         
             Name= values[0]
             Mobile_Number= values[1]
             Address=values[2]
             cursor =conn.cursor()
             sql="INSERT INTO LoginTable(Name,Mobile_Number,Address) VALUES(?,?,?);"
             cursor.execute(sql,(Name,Mobile_Number,Address))
             cursor.commit()
             sg.popup('Data Saved')
             cursor.execute("SELECT * FROM LoginTable")
             for row in cursor:
                print('row = %r' % (row))







             





