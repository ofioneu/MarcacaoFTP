import ftplib
import os
import json
import datetime
from datetime import datetime, date
import time
import shutil
import sys


def main():
    global arquivo
    conf=open('config.json').read()
    configuracao=json.loads(conf)
    host=str(configuracao['host'])
    user=configuracao['user']
    passw=configuracao['passw']
    origem=configuracao['origem']
    destino=configuracao['destino']
    backup=configuracao['backup']

    
    
    for _, _, arquivo in os.walk(origem):
        pass
    
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, passw)    
    except:
        sys.exit()
    
    finally:
        ftp.cwd(destino)

        for i in range(len(arquivo)):
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%Y-%m-%d %H-%M-%S') 
            
            with open(origem+arquivo[i],'rb') as file:
        
                try:        
                    ftp.storbinary('STOR '+arquivo[i] , file)
                    
                                  
                except:
                    ftp.quit()
                    sys.exit()
                
                    
            os.rename(origem + arquivo[i], backup + data_e_hora_em_texto + ' ' + arquivo[i])
        ftp.quit()
        sys.exit()                   

if __name__ == '__main__':
    main()