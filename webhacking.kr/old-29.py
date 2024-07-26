# sqli

db = "select database()"
table = "select table_name form information_schema.tables where table_schema={}".format(db)
table_one_column = "select group_concat(table_name) form information_schema.tables where table_schema={}".format(db)
tb_name = ""
column_name = "select column_name from information_schema.columns where table_schema={} and table_name={}".format(db, tb_name)
col_name = ""
value = "select {} from {}".format(tb_name, col_name)

