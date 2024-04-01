import final_data
import create_dml
import inject_mysql

def resume():
    print('Creating final data...')
    final_data.get_final_data()
    print('Creating DML...')
    create_dml.create_dml()
    print('Executing DML.sql...')
    inject_mysql.inject_mysql()