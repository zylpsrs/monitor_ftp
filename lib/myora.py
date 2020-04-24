import cx_Oracle

class myora (object):
    ''' ref https://www.oracle.com/technetwork/cn/tutorials/229069-zhs.htm '''
    def __init__(self, url, table_name):
        ''' init a oracle connect instance and a cursor, config the monitor table,
        which would create the table if it not exist, and then truncate it '''
        self.con = cx_Oracle.connect(url)
        self.cur = self.con.cursor()
        self.table_name = table_name
        self.__init_table()
        self.__truncate_table()

    def __init_table(self):
        ''' create monitor table when it is not exist '''
        try:
            check = 'select 1 from %s where rownum = 1' % self.table_name
            self.cur.execute(check)
        except:
            create = '''create table {} (
                        host varchar2(30), 
       			dirname  varchar2(500),
       			filename varchar2(100),
       			bytes int,
       			mdtm varchar2(30),
       			crtm varchar2(30))'''.format(self.table_name)
            self.cur.execute(create)
        
    def __truncate_table(self):
        ''' truncate the monitor table '''
        self.cur.execute('truncate table {}'.format(self.table_name))

    def insert_table(self, rows):
        ''' using batch insert rows to monitor table, it will using binding vars '''
        insert = "insert into %s values(:host, :dir, :filename, :bytes, :mdtm, :crtm)" % self.table_name
        self.cur.bindarraysize = 5000
        self.cur.executemany(insert, rows)
        self.con.commit()

    def close(self):
        self.cur.close()
        self.con.close()
