import os
import pg_util

tables = [
		'customer', 'customer_address',
		'date_dim', 'item',
		'store', 'store_sales']

data_path = # directory of data files
db_name = # database name
bin_path = # path of the binary of Postgres
tmp_csv_path = # path of tmp csv file for bulk loading

create_db = True # If create the database
create_table = True # If create the tables

# start database service
pg_util.start_server()

# postgres credential
user = 'postgres'
password = 'admin'

# create database
if create_db:
	# master_conn = pg_util.connect(user = user, password = password)
	master_conn = pg_util.connect()
	pg_util.execute(master_conn.cursor(), 'create database ' + db_name, verbose = True)
	master_conn.close()

# connect to the database
conn = pg_util.connect(user = user, password = password, db_name = db_name)
cursor = conn.cursor()

# create tables
if create_table:
	sql_path = r'../query_and_templates/create_tables.sql'
	pg_util.execute(cursor, open(sql_path, 'r').read(), verbose = True)

# # insert tuples into tables
# for table in tables:
# 	file_path = os.path.join(data_path, table + '.dat')
# 	pg_util.execute(cursor, 'delete from ' + table + ';', verbose = True)
# 	pg_util.bulk_load_from_csv_file(cursor, file_path, tmp_csv_path, table, delimiter = '|')

cursor.close()
conn.close()
