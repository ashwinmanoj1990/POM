import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getappurl():
        url = config.get('common info','form_authentication_page')
        return url
    
    @staticmethod
    def getusername():
        username = config.get('common info','username')
        return username
    
    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password