import os

def LimpaTela():
    os.system('cls')
    print(" +----------------------------------------------------------------------------+")
    print(" |    << Gerador de dados para Etiqueta V.1.0 - Desenvolvido Miguel Jr. >>    |")
    print(" +----------------------------------------------------------------------------+","\n")
    

def main():
    LimpaTela()
    EntradaDados()

def EntradaDados():
    Linha1 = input("  >> Linha 1: ")
    Linha2 = input("  >> Linha 2: ")
    Linha3 = input("  >> Linha 3: ")
    Qt_total = int(input("  >> Quantidade total do trabalho: "))
    Qt_p_pct = int(input("  >> Quantidade por pacote: "))
    Qt_pct_int = Qt_total // Qt_p_pct
    if Qt_total % Qt_p_pct > 0:
        Qt_pct_fra = (Qt_total-(Qt_p_pct * Qt_pct_int))
        Qt_etiquetas = Qt_pct_int + 1
        print("  >>",Qt_pct_int,"etiquetas de",Qt_p_pct," e uma etqueta de",Qt_pct_fra,"\n")
    else:
        Qt_etiquetas = Qt_pct_int
        Qt_pct_fra = 0
        print("  >>",Qt_pct_int,"etiquetas de",Qt_p_pct,"\n")
    ### Confirma a inclusão dos dados ###
    Conf_Dados = input("  >> Confirma a inclusão dos dados [S] p/ SIM ou [N] p/ NÃO >>: ")
    if Conf_Dados.upper() == "S":
        GravaDados(Linha1,Linha2,Linha3,Qt_total,Qt_etiquetas,Qt_p_pct,Qt_pct_fra)
    else:
        print("\n"," >>>> OS DADOS NÃO FORAM GRAVADO NO ARQUIVO <<<<")
        Continuar()

def GravaDados(Linha1,Linha2,Linha3,Qt_total,Qt_etiquetas,Qt_p_pct,Qt_pct_fra):
    Dados=[]
    pacote = 0
    while Qt_total > 0:
        pacote = pacote + 1
        if Qt_total >= Qt_p_pct:
            Qt = Qt_p_pct
            Qt_total = Qt_total - Qt_p_pct
        else:
            Qt = Qt_total
            Qt_total=0
        XQt=str(Qt)
        Xpacote=str(pacote)
        XQt_etiquetas=str(Qt_etiquetas)
        Sep=";"
        Barra="/"
        Final="\n"
        XDados=Linha1+Sep+Linha2+Sep+Linha3+Sep+XQt+Sep+Xpacote+Barra+XQt_etiquetas+Final
        Dados.append(XDados)
    arq.writelines(Dados)
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
arq = open('C:/FFOutput/Dados_Etiq.txt', 'w')
arq.writelines("L1;L2;L3;QT;PCT\n")

# Inicia o código
main()

