from dbobjects import *

def main():
    # table = Table(table_id=12)
    # page = Page(page_id=1)
    # page.add_row(2)
    # page.add_row(3)
    # page.add_row(4)
    # print(str(page))

    # rows_list = [1,2,3,4,67,84]
    # print(lista[4])

    db = Database(db_id=1)
    db.add_table()
    db.add_row(table_id=0)

    # page_id = 1
    # length = 2
    # max_length = 2

    # f'Page(\n\tpage_id={page_id},\n\trows_list={rows_list},\n\tlength={length},\n\tmax_length={max_length}\n)'

    # def p():
    #     obj_str = f'Page(\n\tpage_id={page_id},\n\t'
        
    #     obj_str += '[\n\t\t'
    #     for item in rows_list:
    #         obj_str += str(item)
    #     obj_str += '\n\t]'
    #     obj_str +=f'\n\tlength={length},\n\tmax_length={max_length}\n)'
    #     return obj_str
    # print(p())
main()