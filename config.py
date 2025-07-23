import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '351b2a6a-633d-4daf-aa03-64ebcca6c0f6'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'vv4eJ/GPOw/2zR1dFP3HSjYxKrImK1fixqJoiWYwJ1OEToN9u+3zwsk1DfU84/ziI7HCkJsoSbty+AStcJqJqQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=images11;AccountKey=vv4eJ/GPOw/2zR1dFP3HSjYxKrImK1fixqJoiWYwJ1OEToN9u+3zwsk1DfU84/ziI7HCkJsoSbty+AStcJqJqQ==;EndpointSuffix=core.windows.net'

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Identity Platform
    CLIENT_ID = os.environ.get('CLIENT_ID') or '0fe821c6-5724-4b37-a2b9-940b571722bd'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'qAH8Q~ryTqqo.VkNRe_qKov2792QygQdcveENaJg'
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH') or "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
