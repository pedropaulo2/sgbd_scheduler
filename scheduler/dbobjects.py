# database -> area -> table -> page -> row 
# sgbd class é responsável por gerenciar os databases, os schedulers de cada database etc

class Row:
    def __init__(self, row_id):
        self.row_id = row_id
        #dictionary representando os atributos e os valores

    def __str__(self):
        return f'Row(\n\t{self.row_id}\n)'

class Page:
    def __init__(self, page_id, rows_list=[], max_length=2):
        self.length = 0
        self.page_id = page_id
        self.rows_list = rows_list
        self.max_length = max_length

    def add_row(self, row_id):
        if self.length < self.max_length:
            new_row = Row(row_id)
            self.rows_list.append(new_row)
            self.length +=1
            #row_id??
            return
    
    def __str__(self):
        #self.rows_list
        #return f'Page(\n\tpage_id={self.page_id},\n\trows_list={self.rows_list},\n\tlength={self.length},\n\tmax_length={self.max_length}\n)'

        obj_str = f'Page(\n\tpage_id={self.page_id},\n\t'
        
        obj_str += '[\n\t\t'
        for row in self.rows_list:
            obj_str += str(row)
        obj_str += '\n\t\t]'
        
        obj_str += f'\n\tlength={self.length},\n\tmax_length={self.max_length}\n)'

class Table:
    def __init__(self, table_id, pages_list=[]):
        self.table_id = table_id
        self.pages_list = pages_list
        self.number_of_rows = 0
    
    def add_page(self, page_id):
        new_page = Page(page_id)
        return new_page
    
    def add_row(self):
        for page in self.pages_list:
            if page.length < page.max_length:
                page.add_row(self.number_of_rows+1)
                self.number_of_rows += 1
                print(str(page))
                return
            
            new_page = Page(page_id=len(self.pages_list))
            new_page.add_row(row_id=self.number_of_rows+1)
            self.number_of_rows += 1
            print(str(new_page))
        pass

class Area:
    def __init__(self, area_id, tables_list=[], max_number_of_tables=2):
        self.area_id = area_id
        self.tables_list = tables_list
        self.number_of_tables = 0
        self.max_number_of_tables = max_number_of_tables

    def add_table(self, table_id):
        if self.number_of_tables < self.max_number_of_tables:
            new_table = Table(table_id)
            self.tables_list.append(new_table)
            self.number_of_tables +=1
            return
    
    def get_table(self, table_id):
        for table in self.tables_list:
            if table.table_id == table_id:
                return table
        return None

class Database:
    def __init__(self, db_id, areas_list=[]):
        self.id = id
        self.areas_list = areas_list

    def add_table(self):
        for area in self.areas_list:
            if area.number_of_tables < area.max_number_of_tables:
                area.add_row(self.number_of_tables+1)
                self.number_of_tables += 1
                return
            
            new_area = Area(area_id=len(self.areas_list))
            new_area.add_table(table_id=self.number_of_tables+1)
            self.number_of_tables += 1
    
    def add_row(self, table_id):
        for area in self.areas_list:
            table = area.get_table(table_id)
            if table is None:
                return
            else:
                table.add_row()

class SGDB:
    def __init__(self):
        pass

    def create_database(self):
        pass
