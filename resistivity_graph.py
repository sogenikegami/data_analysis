import numpy as np
import matplotlib.pyplot as plt
import math

norm_temp = 50
#free standing 
free_c = True
free_w= True
free_c_filepath = '/Users/sogenikegami/Documents/Bachelor_Thesis/FeSeTe_M20_#1-2/20230628_FeSeTe_x=0.6_M20_#1-2_freestanding_cooling1.txt'
free_w_filepath = '/Users/sogenikegami/Documents/Bachelor_Thesis/FeSeTe_M20_#1-2/20230628_FeSeTe_x=0.6_M20_#1-2_freestanding_warming1.txt'
#on sapphire
sap_c = False
sap_w = False
sap_c_filepath=''
sap_w_filepath=''

Flag = [free_c,free_w,sap_c,sap_w]

def file2vec(filepath,norm_temp,norm_index):
    flag = True
    count = 0
    Temp=[]
    Res=[]
    with open(filepath,'r') as f:
        for i in range(7):
            f.readline()
        line = f.readline()
        while flag == True:
            data = line.split()
            Temp.append(float(data[1]))
            Res.append(float(data[3]))
            if norm_temp-0.1 < float(data[1]) and float(data[1]) < norm_temp+0.1:
                norm_index = count
            line = f.readline()
            count += 1
            if line == "":
                flag = False
    return [Temp,Res]


def underK(Temp_low,Temp_high,Temp,Res):
    T_under = []
    R_under = []
    for i in range(len(Temp)):
        if Temp_low < Temp[i] and Temp[i] < Temp_high:
            T_under.append(Temp[i])
            R_under.append(Res[i])
    return [T_under,R_under]


def plot(Flag,Data,imagename,xlabel,ylabel,title):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    if Flag[0]:
        ax.scatter(Data["free_c"][0],Data["free_c"][1],label = 'free,cooling',s=10)
    if Flag[1]:
        ax.scatter(Data["free_w"][0],Data["free_w"][1],label = 'free,warming',s=10)
    if Flag[2]:
        ax.scatter(Data["sap_c"][0],Data["sap_c"][1],label='sapphire,cooling',s=10)
    if Flag[3]:
        ax.scatter(Data["sap_w"][0],Data["sap_w"][1],label = 'sapphire,warming',s=10)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ax.legend()
    plt.title(title)
    plt.savefig(imagename)
    fig.show()

def alltemp(Flag,Data):
    title = "Resistivity FeSeTe(Te=0.6)"
    xlabel = "Temperature[K]"
    ylabel = "Resistivity[Ohm]"
    figname = "/Users/sogenikegami/Documents/Bachelor_Thesis/FeSeTe_strain_test_2306/graph/230629/wholetemp"
    plot(Flag,Data,figname,xlabel,ylabel,title)

def specificT(Flag,wholeData,highT,lowT):
    Data = {}
    if Flag[0]:
        Data["free_c"] = underK(lowT,highT,wholeData["free_c"][0],wholeData["free_c"][1])
    if Flag[1]:
        Data["free_w"] = underK(lowT,highT,wholeData["free_w"][0],wholeData["free_w"][1])
    if Flag[2]:
        Data["sap_c"] = underK(lowT,highT,wholeData["sap_c"][0],wholeData["sap_c"][1])
    if Flag[3]:
        Data["sap_w"] = underK(lowT,highT,wholeData["sap_w"][0],wholeData["sap_w"][1])
    title = "Resistivity FeSeTe(Te=0.6)"
    xlabel = "Temperature[K]"
    ylabel = "Resistivity[Ohm]"
    imgname = str(lowT) + "to" + str(highT)
    path = "/Users/sogenikegami/Documents/Bachelor_Thesis/FeSeTe_strain_test_2306/graph/230629/" + imgname
    plot(Flag,Data,path,xlabel,ylabel,title)

def main():
    wholeData = {}
    if Flag[0]:
        free_c_norm_index = 0
        free_c_data = file2vec(free_c_filepath,norm_temp,free_c_norm_index)
        wholeData["free_c"] = free_c_data
    if Flag[1]:
        free_w_norm_index = 0
        free_w_data = file2vec(free_w_filepath,norm_temp,free_w_norm_index)
        wholeData["free_w"] = free_w_data
    if Flag[2]:
        sap_c_norm_index = 0
        sap_c_data = file2vec(sap_c_filepath,norm_temp,sap_c_norm_index)
        wholeData["sap_c"] = sap_c_data
    if Flag[3]:
        sap_w_norm_index = 0
        sap_w_data = file2vec(sap_w_filepath,norm_temp,sap_w_norm_index)
        wholeData["sap_w"] = sap_w_data
    
    alltemp(Flag,wholeData)
    specificT(Flag,wholeData,16,13)
    specificT(Flag,wholeData,14,13)


if __name__ == "__main__":
    main()



