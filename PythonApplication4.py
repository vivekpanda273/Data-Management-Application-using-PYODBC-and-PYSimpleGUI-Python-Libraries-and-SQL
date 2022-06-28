import pyodbc
import PySimpleGUI as sg

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-A8U6UNM5\SQLEXPRESS;"
                      "Database=LoginDB;"
                      "Trusted_Connection=yes;")
sg.theme('Python')
layout = [[sg.Text('Name'), sg.Input(key='NAME'),sg.Push(),],
          [sg.Text('Mobile Number'), sg.Input(key='MOBILE_NUMBER'),sg.Push()],
          [sg.Text('Address'), sg.Input(key='ADDRESS'),sg.Push()],
          [sg.Button('Save'), sg.Button('Cancel'),sg.Button('Search'),sg.Button('Delete'),sg.Button('Update')]]
Window = sg.Window('User Data Entry',layout, element_justification='center')
while True:
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
         break
    elif event == 'Save':
         
             cursor =conn.cursor()
             query="EXEC [insertion] @Name= ?, @Mobile_Number= ? , @Address= ? "
             cursor.execute(query,values['NAME'],values['MOBILE_NUMBER'],values['ADDRESS'])
             cursor.commit()
             sg.popup('Data Saved')
             cursor.execute("SELECT * FROM LoginTable")
             for row in cursor:
                print('row=%r' % (row))
    elif event == 'Search':
        cursor =conn.cursor()
        sql="EXEC[Searching] @Mobile_Number=?"
        cursor.execute(sql,values['MOBILE_NUMBER'])
        sg.popup('Data Found')
        records=cursor.fetchall()
        for record in records:
            Window['NAME'].update(record[0])
            Window['ADDRESS'].update(record[2])
            cursor.commit()
    elif event =='Delete':
        cursor= conn.cursor()
        sql="EXEC [Deletion] @Name=?;"
        cursor.execute(sql,values['NAME'])
        cursor.commit()
        sg.popup('Entered data has been deleted')
        cursor.execute("SELECT * FROM LoginTable")
        for row in cursor:
            print('row=%r' % (row))
    elif event=='Update':
        cursor=conn.cursor()
        sql="EXEC[UPDATING] @Name=?,@Mobile_Number=?,@Address=?;"
        cursor.execute(sql,values['NAME'],values['MOBILE_NUMBER'],values['ADDRESS'])
        cursor.commit()
        sg.popup('Data has been Updated')
        cursor.execute("SELECT* FROM LoginTable")
        for row in cursor:
            print('row=%r' % (row))








             





