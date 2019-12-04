import openpyxl as xl


def write(days: tuple):
    wb = xl.Workbook()
    sheet = wb.active

    COL_TITLE = 1
    COL_TEACH = 2
    COL_GROUP = 3
    COL_CLASSROOM = 4

    cur_row = 1
    for day in days:
        # Merge cells to setup the date
        sheet.merge_cells(start_column=COL_TITLE, end_column=COL_CLASSROOM, start_row=cur_row, end_row=cur_row)
        # Setup the date of the day at the top of each table block and increment st_row number
        sheet.cell(cur_row, COL_TITLE).value = day.date
        cur_row += 1
        for note in day.notes:
            # Setup the Title block

            # Setup end_row value to then merge cells
            e_row = cur_row + len(note.teachers) - 1
            sheet.merge_cells(start_row=cur_row, end_row=e_row, start_column=COL_TITLE, end_column=COL_TITLE)
            # Setup the title
            sheet.cell(cur_row, COL_TITLE).value = note.title

            # Setup each teacher with attributes into a row
            for teacher in note.teachers:
                sheet.cell(cur_row, COL_TEACH).value = teacher.name
                sheet.cell(cur_row, COL_GROUP).value = ', '.join(teacher.groups)
                sheet.cell(cur_row, COL_CLASSROOM).value = teacher.classroom
                cur_row += 1

    wb.save('1.xlsx')
