import os

def LimpaTela():
    os.system('cls')
    print(" +----------------------------------------------------------------------------+")
    print(" |                   << Gerador de dados para Etiqueta SELENE >>              |")
    print(" |                      << JR Systens - V.1.0 - 13/06/2018 >>                 |")
    print(" +----------------------------------------------------------------------------+","\n")

def ID():
    # Carrega número sequencial
    arq_ID = open('G:/Etiq_Selene/ID_Selene.txt', 'r')
    Valor = arq_ID.readlines()
    for linha in Valor:
        ID = int(linha)
    arq_ID.close()
    EntradaDados(ID)
    
def main():
    LimpaTela()
    ID()

def EntradaDados(ID):
    # Entrada de Dados
    print("  >> Última ID registrada:",ID," Proximo:",(ID+1))
    IC = input("  >> Código do produto: ")
    DESC = input("  >> Descrição: ")
    DLT = input("  >> Dia do Lote [DD]: ")
    MLT = input("  >> Mês do Lote [MM]: ")
    ALT = input("  >> Ano do Lote [AAAA]: ")
    LT = DLT+"."+MLT+"."+ALT
    FB = DLT+MLT+ALT
    ANO = int(ALT)+1
    AVC = str(ANO)
    VD = DLT+MLT+AVC
    print("  >> Lote:",LT," - Fabricação: ",FB," - Validade: ",VD)
    CQT = int(input("  >> Quantidade total do trabalho: "))
    QTP = int(input("  >> Quantidade padrão por pacote: "))
    QT_INT = CQT // QTP
    if CQT % QTP > 0:
        QT_FRA = (CQT-(QTP * QT_INT))
        print("  >>",QT_INT,"etiquetas de",QTP," e uma etqueta de",QT_FRA,"\n")
    else:
        QT_FRA = 0
        print("  >>",QT_INT,"etiquetas de",QTP,"\n")
    # Confirma a inclusão dos dados
    Conf_Dados = input("  >> Confirma a inclusão dos dados [S] p/ SIM ou [N] p/ NÃO >>: ")
    if Conf_Dados.upper() == "S":
        GravaDados(IC,LT,FB,CQT,QTP,VD,ID,DESC)
    else:
        print("\n"," >>>> OS DADOS NÃO FORAM GRAVADO NO ARQUIVO <<<<")
        Continuar()

def GravaDados(IC,LT,FB,CQT,QTP,VD,ID,DESC):
    Dados=[]
    XID = ID
    while CQT > 0:
        if CQT >= QTP:
            QT = QTP
            CQT = CQT - QTP
        else:
            QT = CQT
            CQT = 0

        FN = "050220482000163"        
        LG = "0"
        if QT >= 1000:
            QT = QT//1000
            XQT = str(QT)
            SQT = XQT+",000"
        else:
            XQT = str(QT)
            SQT = "0,"+XQT
        VL = "0"
        DM = "0"
        XID = XID + 1
        SID=str(XID)
        s=";"
        f="\n"
        XDados=FN+s+IC+s+LT+s+FB+s+LG+s+SQT+s+VL+s+DM+s+VD+s+SID+s+DESC+f
        ##print(XDados)
        Dados.append(XDados)
    arq.writelines(Dados)

    #Regitrando a ultima ID
    arq_ID = open('G:/Etiq_Selene/ID_Selene.txt', 'w')
    arq_ID.writelines(SID)
    arq_ID.close()
    
    print("\n"," >>>> Dados Gravados com sucesso <<<<")
    Continuar()
    
    

def Continuar():
    print("\n"," -----------------------------------------------------------------------------")
    pause = input("  >> [C] p/ continuar ou [S] p/ Sair >>: ")
    if pause.upper() == "S":
        arq.close()
        exit
    else:
        main()

# Cria o arquivo
arq = open('G:/Etiq_Selene/Dados_Selene.txt', 'w')
arq.writelines("FN;IC;LT;FB;LG;QT;VL;DM;VD;ID;DESC\n")


# Inicia o código
main()

