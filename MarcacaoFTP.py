import ftplib
import os
import json
import datetime
from datetime import datetime, date
import time
import shutil


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
        print(arquivo)

    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, passw)
        print('Conectado com sucesso!')
    
    except:
        print("Falha de conexao FTP!")
    
    finally:
        ftp.cwd(destino)      
        
        
        for i in range(len(arquivo)):
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%Y-%m-%d %H-%M-%S')
            #shutil.copy(origem+arquivo[i], backup)
            
            
            
            with open(origem+arquivo[i],'rb') as file:
                print('Arquivo de origem aberto!')
                try:        
                    ftp.storbinary('STOR '+arquivo[i] , file)
                    print("Arquivo enviado com sucesso!!")
                except:
                    print("Erro ao enviar o arquivo!")
            os.rename(origem + arquivo[i], backup + data_e_hora_em_texto + ' ' + arquivo[i])

        ftp.quit()

if __name__ == '__main__':
    main()