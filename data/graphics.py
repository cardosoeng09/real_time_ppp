#FUNÇÕES GERADORAS DE GRÁFICOS
import matplotlib.pyplot as plt
from numpy import linalg as LA
import matplotlib.dates as md

def grafico_xyz(ax,datenums,arrayx,y_lim,width):
    ax.plot(datenums,arrayx[:,0],label="dX",linewidth=width)
    ax.plot(datenums,arrayx[:,1],label="dY",linewidth=width)
    ax.plot(datenums,arrayx[:,2],label="dZ",linewidth=width)
    plt.ylabel('Variação X,Y,Z (m)')
    axes = plt.gca()
    axes.set_ylim(y_lim)
    return axes

def grafico_norma_xyz(ax,datenums,arrayx,y_lim,width):
    ax.plot(datenums,LA.norm(arrayx,axis=1),label="Erro 3D",linewidth=width)
    plt.ylabel('Norma dX, dY, dZ (m)')
    axes = plt.gca()
    axes.set_ylim(y_lim)
    return axes

def incerteza(ax,datenums,arrayx,y_lim):
    ax.plot(datenums,LA.norm(arrayx,axis=1),label="Norma incerteza",linewidth=1)
    plt.ylabel('Norma Incerteza X, Y, Z (m)')
    axes = plt.gca()
    axes.set_ylim(y_lim)
    return axes

def conf_geral(ax,grafico_path,file_name,tipo_grafico):
    plt.xlabel('Hora')
    plt.xticks(rotation=45)
    xfmt = md.DateFormatter('%H:%M') ##
    ax.xaxis.set_major_formatter(xfmt) ##
    plt.tight_layout()
    ax.legend(loc='best', shadow=True, fontsize='small')
    plt.savefig(grafico_path+'/'+file_name+'_graphic_'+tipo_grafico+'.png',dpi=300)
    plt.show()
    return 0
    
def graphic(grafico_path,file_name,time,arrayx,tipo_grafico,restricao):
    datenums=md.date2num(time)
    fig, ax = plt.subplots()
    if tipo_grafico=='xyz':
        if file_name=="RJ_T20712" or file_name=="RJ_T20721":
            y_lim=[-1,1]
        else:
            y_lim=[-0.5,0.5]
        grafico_xyz(ax,datenums,arrayx,y_lim,0.3)
    if tipo_grafico=='uncertainty':
        if file_name=="RJ_T20712" or file_name=="RJ_T20721":
            y_lim=[0,2]
        else:
            y_lim=[0,0.4]
        incerteza(ax,datenums,arrayx,y_lim) 
    if tipo_grafico=='result':
        if file_name=="RJ_T20712" or file_name=="RJ_T20721":
            y_lim=[0,2]
        else:
            y_lim=[0,1]
        grafico_norma_xyz(ax,datenums,arrayx,y_lim,0.3)
    conf_geral(ax,grafico_path,file_name,tipo_grafico)
    return datenums

def bnc_ibge_graphic(grafico_path,file_name,time,arrayx,tipo_grafico,y_lim,width):
    datenums=md.date2num(time)
    fig, ax = plt.subplots()
    if tipo_grafico=='xyz':
        grafico_xyz(ax,datenums,arrayx,y_lim,width)
    if tipo_grafico=='result':
        grafico_norma_xyz(ax,datenums,arrayx,y_lim,width)
    conf_geral(ax,grafico_path,file_name,tipo_grafico)
    return 0

def save_graphics(graphic_path,file_name,time,dXYZ,incertezas):
    graphic(graphic_path,file_name,time,dXYZ,'xyz',False)
    graphic(graphic_path,file_name,time,dXYZ,'result',False)
    graphic(graphic_path,file_name,time,incertezas,'uncertainty',False)
    return 0