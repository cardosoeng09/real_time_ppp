#CODIGO QUE AUXILIA NA EXTRACAO DE DADOS OBTIDOS ATRAVES DO SOFTWARE BNC, DO PPP-WIZARD e IBGE-PPP. 
#ANTES DE UTILIZAR LEIA O ARQUIVO LEIAME.TXT
from graphics import bnc_ibge_graphic,save_graphics
from auxiliary_functions import get_processado,extrai,get_processado_ppp_wizard, grafico_path, extrai_processado_ibge, extrai_ibge,compara_bnc_ibge,get_dados_bnc

measure1="POAL20636" #Medida utilizando BNC na POAL - Sem especificacoes de antena
measure3="POAL20650" #Medida utilizando BNC na POAL - Com especificacoes de antena
measure4="RJ_T20712" #Medida feita no terraco da secao de Eng. Car. do IME no dia 17/09 - Conexao do notebook (BNC) com 
measure5="POAL20716" #measure de RTPPP feita em 21/09/2019 - simultaneamente com a coleta do PPP-WIZARD #COORDENADAS 3467519.42758  -4300378.65527  -3177517.52025 (coordenadas da semana 2065)
measure6='POAL001_ppp_wizard' #measure de PPP-RTK feita em 21/09 - simultanamente com a coleta do BNC (RTPPP) #COORDENADAS 3467519.42758  -4300378.65527  -3177517.52025 (coordenadas da semana 2065)
measure7="RJ_T20721" #measure feita em 23/09 na praça Gen Tiburcio com BNC
#%% PARTE DO CODIGO QUE GERAM OS GRAFICOS PARA AS MEDIDAS DE 1 A 7 - Graficos de dX,dY,dZ; Norma da incerteza e resultante de dX,dY,dZ
for file_name in ["POAL20636","POAL20650","RJ_T20712","POAL20716","RJ_T20721","POAL001_ppp_wizard"]:
    time,xyz,dXYZ,neu,incertezas,graphic_path=get_dados_bnc(file_name)
    save_graphics(graphic_path,file_name,time,dXYZ,incertezas)
    
#%% PARTE DO CODIGO QUE EXTRAI AS COORDENADAS COM AS RESPECTIVAS EPOCAS DO POS-PROCESSADO DO IBGE-PPP E SALVA UM ARQUIVO FORMATADO CORRETAMENTE PARA CONVERTER AS COORDENADAS GEOGRAFICAS EM COORDENADAS CARTESIANAS UTILIZANDO O SOFTWARE PROGRID
extrai_processado_ibge(measure7)
extrai_processado_ibge(measure4)
#%% #PARA RODAR CORRETAMENTE A PROXIMA CELULA DO CODIGO DEVE UTILIZAR A SAIDA DA CELULA ANTERIOR E CONVERTER AS COORDENADAS GEOGRAFICAS PARA COORDENADAS CARTESIANAS UTILIZANDO O SOFTWARE PRO-GRID DO IBGE, ESSAS COORDENADAS CARTESIANAS SAO UTILIZADAS NA PROXIMA PARTE DO CODIGO 
#%% PARTE DO CODIGO QUE GERAM OS GRAFICOS DE COMPARACAO DAS MEDICOES 4 E 7 COM RELACAO AS COORDENADAS PÓS PROCESSADAS PELO IBGE-PPP    
for file_name in ["RJ_T20721"]:
    time_bnc7,xyz_bnc,dXYZ,neu,incertezas,graphic_path=get_dados_bnc(file_name)
    time_ibge7,bnc_med7,ibge_med7,comp_med7,tempo_comp7=compara_bnc_ibge(file_name)
    bnc_ibge_graphic(graphic_path,file_name+'_comparison',tempo_comp7,comp_med7,'xyz',[-5.5,3],1.2)
    bnc_ibge_graphic(graphic_path,file_name+'_comparison',tempo_comp7,comp_med7,'result',[0,6],1.2)
    
for file_name in ["RJ_T20712"]:
    time_bnc4,xyz_bnc,dXYZ,neu,incertezas,graphic_path=get_dados_bnc(file_name)
    time_ibge4,bnc_med4,ibge_med4,comp_med4,tempo_comp4=compara_bnc_ibge(file_name)
    bnc_ibge_graphic(graphic_path,file_name+'_comparison',tempo_comp4,comp_med4,'xyz',[-2,3],0.3)
    bnc_ibge_graphic(graphic_path,file_name+'_comparison',tempo_comp4,comp_med4,'result',[0,4],0.3)