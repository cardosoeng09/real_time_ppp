#FUNCOES AUXILIARES
from datetime import datetime, timedelta
import numpy as np
import os

def transforma_tempo(tempo):
    time=[]
    for i in range(len(tempo)):
        tempo[i]=tempo[i].replace("_",' ')
        time.append(datetime.strptime(tempo[i], '%Y-%m-%d %H:%M:%S.%f'))
    time=np.asarray(time)
    return time

def get_processado(processado_path,coord):
    dados=np.loadtxt(processado_path,dtype=str)
    tempo=dados[:,0]
    xyz=dados[:,1:4].astype(np.float) #novo array para salvar as coordenadas cartesianas
    neu=dados[:,7:10].astype(np.float) #novo array para salvar somente as informações de dE,dN e dU
    time=transforma_tempo(tempo)
    incerteza=dados[:,4:7].astype(np.float)
    dXYZ=xyz-coord #subtrai o array que contem os XYZ obtidos no BNC com as coordenadas 'reais'
    return time,xyz,dXYZ,neu,incerteza

def extrai(file_path,nome_arquivo): #função que extrai 
    #abre-se o arquivo do qual quer se extrair os dados
    if nome_arquivo=="RJ_T20712" or nome_arquivo=="RJ_T20721":
        string_procura="RJ_teste X"
    else:
        string_procura="POAL00BRA0 X"
    with open(file_path, "r") as ins: 
        dados = []
        for line in ins:
            if line.find(string_procura) > 0:
                line=line.rstrip('\n')
                line=line.split()
                dados.append(line)
    #dados é o array que contém as informações de época,X,Y,Z,incerteza X,Y,Z e dE,dN, dU, incerteza dE,dN,dU          
    dados=np.array(dados)
    dados=dados[:,(0,4,9,14,6,11,16,19,24,29,21,26,31)]
    processado_path = file_path[:len(file_path)-4] + '_processado' + file_path[len(file_path)-4:]
    np.savetxt(processado_path,dados,fmt='%s')
    return processado_path#dados

def transforma_tempo_em_hora(time):
    hora=[]
    for i in range(len(time)):
        hora.append(time[i].hour)
    hora=np.asarray(hora)
    return hora

def get_processado_ppp_wizard(path,coord):
    dados=np.loadtxt(path,dtype=str)
    dia=dados[:,0]
    tempo=dados[:,1]
    tempocorreto=[]
    for i in range(len(dia)):
        tempocorreto.append('20'+dia[i]+'_'+tempo[i])
    tempocorreto=np.asarray(tempocorreto)
    x=dados[:,8]
    i_x=dados[:,10]
    y=dados[:,11]
    i_y=dados[:,13]
    z=dados[:,14]
    i_z=dados[:,16]
    xyz=np.array([x,y,z]).T.astype(np.float)
    incerteza=np.array([i_x,i_y,i_z]).T.astype(np.float)
    time=transforma_tempo(tempocorreto)
    dXYZ=xyz-coord
    return time,xyz,dXYZ,incerteza

def grafico_path(nome_arquivo):
    script_dir = os.path.dirname(__file__) #caminho do código (path of the code)
    rel_path = "Graphics"+"/"+nome_arquivo
    grafico_path = os.path.join(script_dir, rel_path)
    if os.path.exists(grafico_path)==False:
        os.mkdir(grafico_path) #creates a folder to keep the graphics (cria uma pasta para armazenar os graficos)
    rel_path = "Logs"+"/"+nome_arquivo+'/'+nome_arquivo+'.ppp'
    file_path=os.path.join(script_dir,rel_path)
    return file_path,grafico_path

def corrige_array_time_ibge(array,nome_arquivo):
    new_array=[]
    for i in range(len(array)):
        string=array[i][0]+' '+array[i][1]
        string=datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)
        new_array.append(string)
    time=np.asarray(new_array)
    if nome_arquivo=='RJ_T20721.19O.pos':
        time=time + timedelta(seconds=1)
    return time

def extrai_ibge(nome_arquivo,file_path): #função que extrai 
    #abre-se o arquivo do qual quer se extrair os dados
    string_procura="RJ_t"
    with open(file_path, "r") as ins: 
        dados = []
        for line in ins:
            if line.find(string_procura) > 0:
                line=line.rstrip('\n')
                line=line.split()
                dados.append(line)
    dados=np.array(dados)    #dados é o array que contém as informações de época,X,Y,Z,incerteza X,Y,Z e dE,dN, dU, incerteza dE,dN,dU
    datetime=dados[:,(4,5)]
    datetime=corrige_array_time_ibge(datetime,nome_arquivo)
    lat=dados[:,(20,21,22)].astype(np.float)
    lon=dados[:,(23,24,25)].astype(np.float)
    alt=dados[:,26].astype(np.float)
    return datetime,lat,lon,alt

def compara_bnc_ibge(nome_arquivo):
    script_dir = os.path.dirname(__file__)
    file_path = script_dir+'/Logs/'+nome_arquivo+'/Coord_transformadas/'+nome_arquivo+'.19O.pos_coord_OUT.txt'
    xyz_ibge=np.loadtxt(file_path,delimiter='|')
    file_path = script_dir+'/Logs/'+'/'+nome_arquivo+'/'+nome_arquivo+'.19O.pos'
    time_ibge,lat,lon,alt=extrai_ibge(nome_arquivo,file_path)
    time_bnc,xyz_bnc,dXYZ,neu,incertezas,grafico_caminho=get_dados_bnc(nome_arquivo)
    bnc=np.concatenate((np.array([time_bnc]).T,xyz_bnc),axis=1)
    ibge=np.concatenate((np.array([time_ibge]).T,xyz_ibge),axis=1)
    comparacao=[]
    tempo_comparacao=[]
    for i in range(len(ibge)):
        for j in range(len(bnc)):
            if ibge[i][0]==bnc[j][0]:
                dX=ibge[i][1]-bnc[j][1]
                dY=ibge[i][2]-bnc[j][2]
                dZ=ibge[i][3]-bnc[j][3]
                comparacao.append([dX,dY,dZ])
                tempo_comparacao.append(ibge[i][0])
                break
    return time_ibge,bnc,ibge,np.asarray(comparacao),np.asarray(tempo_comparacao)

def get_dados_bnc(nome_arquivo):
    coord_poa=np.array([[3467519.42758,-4300378.65527,-3177517.52025]]) #array que guarda as coordenadas de POAL obtidas no SIRGAS-CON (Semana gps 2065)
    coord_rj=np.array([[4285796.90510288,-4019920.95100773,-2472249.93687366]])
    file_path,grafico_caminho=grafico_path(nome_arquivo) #função que retorna o caminho do arquivo que serao feitas as leituras dos dados, e tambem o caminho da pasta para salvar os graficos
    if nome_arquivo.find('ppp_wizard') >= 0: #caso seja uma medica do PPP-Wizard tem que ser diferente a funcao get_processado
        time,xyz,dXYZ,incertezas=get_processado_ppp_wizard(file_path,coord_poa)
        neu=[]
    else:    
        if os.path.isfile(file_path[:len(file_path)-4] + '_processado' + file_path[len(file_path)-4:]) == False: 
            processado_path=extrai(file_path,nome_arquivo) #esse 'if' verifica se o .ppp já foi processado, caso ja tenha sido, não perde tempo fazendo novamente
        else:
            processado_path=file_path[:len(file_path)-4] + '_processado' + file_path[len(file_path)-4:]
        if nome_arquivo.find('RJ') >= 0:
            time,xyz,dXYZ,neu,incertezas=get_processado(processado_path,coord_rj)
        elif nome_arquivo.find('POA') >= 0:
            time,xyz,dXYZ,neu,incertezas=get_processado(processado_path,coord_poa)
    return time,xyz,dXYZ,neu,incertezas,grafico_caminho

def extrai_processado_ibge(nome_arquivo):
    script_dir = os.path.dirname(__file__)
    file_path=script_dir+'/Logs/'+nome_arquivo+'/'+nome_arquivo+'.19O.pos'
    datetime,lat,lon,alt=extrai_ibge(nome_arquivo,file_path)
    lat_lon= np.concatenate((lat,lon,np.array([alt]).T),axis=1)
    nome_novo=file_path+'_coord.txt'
    np.savetxt(nome_novo,lat_lon,fmt='%.5f',delimiter='|')
    with open(nome_novo, 'r') as f:
        s = f.read()
        s = s.replace('.00000', '')
        s = s.replace('.', ',')
        with open(nome_novo, 'w') as file:
            file.write(s)
    return 0