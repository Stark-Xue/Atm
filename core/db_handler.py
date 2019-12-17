# Author: Mr.Xue
# 2019.10.25

#!usr/bin/python3

"""
handle all the database interactions
"""

def file_db_handle(conn_params):
    """parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    """

    #print("file db: ", conn_params)
    db_path = '%s/%s' %(conn_params['path'], conn_params['name'])
    return db_path

def db_handler(conn_params):
    """connect to db
    :param conn_params: the db connection params set in settings
    :return: a
    """

    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
         pass