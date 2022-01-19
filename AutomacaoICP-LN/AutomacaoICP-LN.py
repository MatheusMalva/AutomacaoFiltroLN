# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:56:54 2021

@author: Microsoft
"""

# Projeto para automatização da busca de leads no LinkedIn.

# Import dos módulos

# Módulos para tratamento do navegador
from selenium import webdriver
from pynput.keyboard import Key , Controller

# Módulos gerais
import pandas as pd
import time
import os




## ETAPAS DO PROCESSO
# 1 - Ler o arquivo ICP
# 2 - Passar por cada categoria do ICP, Item por item
# 3 - Para cada item de cada categoria, identificar qual campo de busca ele está associado
# 4 - Preencher o campo de busca com o item correspondente 
# 5 - Salvar Pesquisa com a nomenclatura adequada


# Mostrando o conteúdo da pasta arquivosPloomes
pasta = os.listdir("Arquivos")
ICP = pd.read_excel("Arquivos/" + pasta[0])

#Retirando NaN e Duplicatas de Segmento

cleanedSegmento = [i for i in ICP["SEGMENTO"] if str(i) != 'nan']
A=len(ICP) - len(cleanedSegmento)
ICPsegmento = pd.read_excel("Arquivos/" + pasta[0],usecols=("C"),keep_default_na = False,skipfooter= A )
ICPsegmento = ICPsegmento.drop_duplicates()
ICPsegmento = ICPsegmento.reset_index(drop=True)
print((ICPsegmento["SEGMENTO"]))


#Retirando NaN e Duplicatas de Estados

cleanedEstados = [i for i in ICP["ESTADO"] if str(i) != 'nan']
A=len(ICP) - len(cleanedEstados)
ICPestado = pd.read_excel("Arquivos/" + pasta[0],usecols=("B"),keep_default_na = False,skipfooter= A )
ICPestado = ICPestado.drop_duplicates()
ICPestado = ICPestado.reset_index(drop=True)
print((ICPestado["ESTADO"]))

#Retirando NaN e Duplicatas de Porte

cleanedPorte = [i for i in ICP["PORTE"] if str(i) != 'nan']
A=len(ICP) - len(cleanedPorte)
ICPporte = pd.read_excel("Arquivos/" + pasta[0],usecols=("D"),keep_default_na = False,skipfooter= A )
ICPporte = ICPporte.drop_duplicates()
ICPporte = ICPporte.reset_index(drop=True)
print((ICPporte["PORTE"]))

#Retirando NaN e Duplicatas de Departamento

cleanedDepartamento = [i for i in ICP["DEPARTAMENTO"] if str(i) != 'nan']
A=len(ICP) - len(cleanedDepartamento)
ICPdepartamento = pd.read_excel("Arquivos/" + pasta[0],usecols=("F"),keep_default_na = False,skipfooter= A )
ICPdepartamento = ICPdepartamento.drop_duplicates()
ICPdepartamento = ICPdepartamento.reset_index(drop=True)
print((ICPdepartamento["DEPARTAMENTO"]))

#Retirando NaN e Duplicatas de Cargo

cleanedCargo = [i for i in ICP["CARGO"] if str(i) != 'nan']
A=len(ICP) - len(cleanedCargo)
ICPcargo = pd.read_excel("Arquivos/" + pasta[0],usecols=("E"),keep_default_na = False,skipfooter= A )
ICPcargo = ICPcargo.drop_duplicates()
ICPcargo = ICPcargo.reset_index(drop=True)
print((ICPcargo["CARGO"]))


# Mostra mensagem ao usuário
print("Aguarde enquanto o filtro no LinkedIn é feito...")


# Variáveis para alocar as informações
df = pd.DataFrame()
df["Segmento"] = ICPsegmento["SEGMENTO"]
df["Estado"] = ICPestado["ESTADO"]
df["Porte"] = ICPporte["PORTE"]
df["Cargo"] = ICPcargo["CARGO"]
df["Departamento"] = ICPdepartamento["DEPARTAMENTO"]






# correção ortográfica dos segmentos
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ADMINISTRACAO AGRICOLA'],['Administração agrícola'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ADMINISTRACAO DE SERVICOS'],['Administração de serviços']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ADMINISTRACAO GOVERNAMENTAL'],['Administração governamental']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ANIMACAO'],['Animação']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ARRECADACAO DE RECURSOS'],['Arrecadação de Recursos']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ARTES CENICAS'],['Artes Cênicas'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ATENDIMENTO MEDICO E HOSPITALAR'],['Atendimento médico e hospitalar']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ATENDIMENTO MEDICO PSIQUIATRICO'],['Atendimento médico psiquiátrico'])           
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['AUTOMACAO INDUSTRIAL'],['automação industrial'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['AVIACAO E AEROESPACIAL'],['Aviação e Aeroespacial']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['CAPITAL DE RISCO E PARTICIPACOES PRIVADAS'],['Capital de risco e participações privadas'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['COMPOSICAO E REVISAO DE TEXTOS'],['Composição e Revisão de Textos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['COMERCIO E DESENVOLVIMENTO INTERNACIONAL'],['Comércio e desenvolvimento internacional'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['CONSTRUCAO'],['Construção']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['CONSTRUCAO DE FERROVIA'],['Construção de Ferrovia']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['CONSTRUCAO NAVAL'],['Construção Naval'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['COSMETICA'],['Cosmética'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['DEFESA E ESPACO'],['Defesa e espaço'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['DESIGN GRAFICO'],['Design Gráfico']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['DISPOSITIVOS MEDICOS'],['Dispositivos Médicos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['EDITORACAO'],['Editoração']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['EDUCACAO A DISTANCIA'],['Educação à distância']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ENGENHARIA MECANICA OU INDUSTRIAL'],['Engenharia mecânica ou industrial']) 
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ENSINO FUNDAMENTAL/MEDIO'],['Ensino fundamental/médio'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['EXECUCAO DA LEI'],['Execução da Lei'])     
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['GESTAO DE INVESTIMENTOS'],['gestão de investimentos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['GESTAO DE ORGANIZACAO SEM FINS LUCRATIVOS'],['Gestão de Organização sem fins Lucrativos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['GESTAO EDUCACIONAL'],['Gestão Educacional'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['IMOBILIARIO'],['Imobiliário'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['IMPORTACAO E EXPORTACAO'],['Importação e Exportação'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['IMPRESSAO'],['Impressão'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['IMOVEIS COMERCIAIS'],['Imóveis Comerciais'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INDUSTRIA AUTOMOTIVA'],['Indústria Automotiva'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INDUSTRIA FARMACEUTICA'],['Indústria Farmacêutica'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INDUSTRIA QUIMICA'],['Indústria química'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INDUSTRIA TEXTIL'],['Indústria têxtil'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INSTALACOES E SERVICOS RECREATIVOS'],['Instalações e Serviços De Recreação'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['INSTITUICOES RELIGIOSAS'],['Instituições Religiosas'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['JUDICIARIO'],['Judiciário'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['LATICINIOS'],['Laticínios'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['LINHAS AEREAS/AVIACAO'],['Linhas Aéreas/Aviação'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['LOGISTICA E CADEIA DE SUPRIMENTOS'],['Logística e Cadeia de Suprimentos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MANUFATURA DE ELETROELETRONICOS'],['Manufatura de eletroeletrônicos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MAQUINARIO'],['Maquinário'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MATERIAIS DE CONSTRUCAO'],['Materiais de Construção'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MIDIA DE DIFUSAO'],['Mídia de difusão'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MIDIA ONLINE'],['Mídia Online'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MINERACAO E METAIS'],['Mineração e Metais'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MUSICA'],['Música'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MUSEUS E INSTITUICOES'],['Museu e Instituições'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['MOVEIS'],['Móveis'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ORGANIZACOES DE PESQUISA E ORIENTACAO'],['Organizações de pesquisa e orientação'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ORGANIZACAO CIVICA E SOCIAL'],['Organização cívica e social'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['ORGANIZACAO POLITICA'],['Organização Política'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PETROLEO E ENERGIA'],['Petróleo e energia'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PLASTICO'],['Plástico'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['POLITICA PUBLICA'],['Política Pública'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PRODUCAO DE MIDIA'],['Produção de mídia'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PRODUTOS ALIMENTICIOS'],['Produtos Alimentícios'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PRODUTOS ELETRONICOS'],['Produtos Eletrônicos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PRATICA JURIDICA'],['Prática Jurídica'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['PRATICA MEDICA'],['Prática Médica'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RECRUTAMENTO E SELECAO'],['Recrutamento e seleção'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['REDES SEM FIO'],['Rede sem fio'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RECURSOS RENOVAVEIS E MEIO AMBIENTE'],['Recursos Renováveis e meio ambiente'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RELACOES GOVERNAMENTAIS'],['Relações Governamentais'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RELACOES INTERNACIONAIS'],['Relações Internacionais'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RELACOES PUBLICAS E COMUNICACOES'],['Relações Públicas e Comunicações'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['RESOLUCAO ALTERNATIVA DE LITIGIOS'],['Resolução alternativa de Litígios'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SAUDE, BEM-ESTAR E EDUCACAO FISICA'],['Saúde, bem-estar e educação física'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SEGURANCA DE REDES E COMPUTADORES'],['Segurança de Redes e Computadores'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SEGURANCA E INVESTIGACOES'],['Segurança e Investigações'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SEGURANCA PUBLICA'],['Segurança Pública'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS AMBIENTAIS'],['Serviços Ambientais'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS DA INFORMACAO'],['Serviços da Informação'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS FINANCEIROS'],['Serviços Financeiros'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS INDIVIDUAIS E FAMILIARES'],['Serviços Individuais e Familiares'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS JURIDICOS'],['Serviços Jurídicos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS PARA EVENTOS'],['Serviços para Eventos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['SERVICOS PUBLICOS'],['Serviços Públicos'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TECNOLOGIA DA INFORMACAO E SERVICOS'],['Tecnologia da Informação e Serviços'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TELECOMUNICACOES'],['Telecomunicações'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TERCEIRIZACAO E OFFSHORING'],['Terceirização e Offshoring'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TRADUCAO E LOCALIZACAO'],['Tradução e Localização'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TRANSPORTE/CAMINHOES/TRENS'],['Transporte/Caminhões/Trens'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TRANSPORTE MARITIMO'],['Transporte Marítimo'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['TREINAMENTO E ORIENTACAO PROFISSIONAL'],['Treinamento e Orientação Profissional'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['VETERINARIA'],['Veterinária'])
ICPsegmento["SEGMENTO"] = ICPsegmento["SEGMENTO"].replace(['VIDRO, CERAMICA E CONCRETO'],['Vidro, Cerâmica e Concreto'])





# INTERAÇÕES COM O NAVEGADOR
# Abrindo o navegador e a conexão com o Chrome
# Observe que é necessário passar o caminho de diretório do Chromedriver como parâmetro
driver = webdriver.Chrome("bin/chromedriver.exe")

# Acessando o google no navegador 
driver.get("http://www.google.com")

 # Acessando o linkedin no navegador 
driver.get("https://www.linkedin.com/login/pt")
    # Acessando a conta do Rhavi
    # elemento HTML de ID do Linkedin
elem = driver.find_element_by_xpath('//*[@id="username"]')

    # Escrevendo na caixa de usuário do LinkedIn
elem.send_keys(str("rhavimoreira@yahoo.com.br"))
 
    # elemento HTML de senha do Linkedin
elem1 = driver.find_element_by_xpath('//*[@id="password"]')
    
    # Escrevendo na caixa de senha do LinkedIn
elem1.send_keys(str("Escalar@2021!"))
    
    # Clicando no elemento para fazer o Log IN
elem1.submit()


# Acessando o SALES NAVIGATOR no navegador 
driver.get("https://www.linkedin.com/sales/search/people")

time.sleep(3)

    
# elemento HTML de “Localidade”
elem4 = driver.find_element_by_xpath('//*[@id="ember65"]/div/div')

# Clicando no elemento para Localidade
elem4.click()

#Elemento de texto (para permitir a escrita na caixa de texto - repete)
elem5 = driver.find_element_by_xpath('//*[@id="ember64-typeahead-region"]')

# Clicando na caixa de texto
elem5.click()
time.sleep(3)
i = 0

while i < len(ICPestado["ESTADO"]):
# escrevendo o nome do estado no campo de estado

    elem5.send_keys(str(ICPestado["ESTADO"][i])) 
    time.sleep(2)
# achando o nome do estado pesquisado
    elem6 = driver.find_element_by_xpath('//*[@id="ember64"]/div[3]/ol/li[1]/button')
# clicando no nome encontrado
    elem6.click()
# Somando ao contador
    i+=1


        
# elemento HTML de “Segmento”
elem7 = driver.find_element_by_xpath('//*[@id="ember82"]/div/button')

# Clicando no elemento para Segmento
elem7.click()

#Elemento de texto (para permitir a escrita na caixa de texto - repete)
elem8 = driver.find_element_by_class_name("text-input--no-border")

# Clicando na caixa de texto
elem8.click()
time.sleep(3)
i = 0
print(ICPsegmento["SEGMENTO"])
while i < len(ICPsegmento["SEGMENTO"]):
# escrevendo o nome do SEGMENTO no campo de Setor
    elem8.send_keys(str(ICPsegmento["SEGMENTO"][i]).lower())
    time.sleep(2)
# achando o SEGMENTO pesquisado
    elem9 = driver.find_element_by_xpath('//*[@id="ember81"]/div[3]/ol/li/button') #font-weight-400
# clicando no nome encontrado
    elem9.click()
# Somando ao contador
    i+=1

# elemento HTML de “Porte”
elem10 = driver.find_element_by_xpath('//*[@id="ember87"]/div/button')

# Clicando no elemento para Segmento
elem10.click()  
time.sleep(3)
i=0
ICPporte["PORTE"].iloc[::-1]

j=len(ICPporte["PORTE"])-1
print(len(ICPporte["PORTE"]))
while j > -1:
    
    if ICPporte["PORTE"][j] == "10001+": # 1o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[9]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)   
        
    elif ICPporte["PORTE"][j] == "5001-10000": # 2o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[8]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)  

    elif ICPporte["PORTE"][j] == "1001-5000": # 3o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[7]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)
        
    elif ICPporte["PORTE"][j] == "501-1000": # 4o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[6]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)
    elif ICPporte["PORTE"][j] == "201-500": # 5o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[5]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)
    elif ICPporte["PORTE"][j] == "51-200": # 6o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[4]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)
    elif ICPporte["PORTE"][j] == "11-50": # 7o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[3]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)
    elif ICPporte["PORTE"][j] == "1-10": # 8o Porte
        elem11 = driver.find_element_by_xpath('//*[@id="ember86"]/div[3]/ol/li[2]/button')
        elem11.click() 
        print(j)
        print(ICPporte["PORTE"][j])
        j-=1
        time.sleep(3)






# elemento HTML de “Cargo”
elem13 = driver.find_element_by_xpath('//*[@id="ember102"]/div/button')

# Clicando no elemento para Cargo
elem13.click()


#Elemento de texto (para permitir a escrita na caixa de texto - repete)
elem14 = driver.find_element_by_xpath('//*[@id="ember101-typeahead"]')

# Clicando na caixa de texto
elem14.click()
i=0
j=0
print(ICPdepartamento["DEPARTAMENTO"])
print(ICPcargo["CARGO"])
print(len(ICPcargo["CARGO"]))
print(len(ICPdepartamento["DEPARTAMENTO"]))
while i < len(ICPcargo["CARGO"]):
    j=0
    while j < len(ICPdepartamento["DEPARTAMENTO"]):
    # Escrevendo o nome cargo + departamento de forma concatenada
        elem14.send_keys(str(ICPcargo["CARGO"][i].lower()) + ' ' + str(ICPdepartamento["DEPARTAMENTO"][j]).lower())
    # apertando enter
        keyboard = Controller()
        keyboard.press(Key.enter)
        time.sleep(3)

        keyboard.release(Key.enter)
        print(ICPcargo["CARGO"][i] +" "+ ICPdepartamento["DEPARTAMENTO"][j])
        print(j)
        print(i)
        j+=1
    i-=1
    i+=2

#tradução dos termos de cargo que estão no ICP
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ADVOGADO'],['ATTORNEY'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ANALISTA'],['ANALYST'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ARQUITETO'],['ARCHITECT'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ATENDENTE'],['CLERK'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['AUDITOR'],['CONTROLLER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['COMPRADOR'],['BUYER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['CONSELHEIRO'],['ADVISOR'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['CONSULTOR'],['CONSULTANT'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['CONTROLADOR'],['CONTROLLER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['COORDENADOR'],['COORDINATOR'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['CORRETOR'],['BROKER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['DIRETOR'],['DIRECTOR'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ENCARREGADO'],['IN CHARGE'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ENFERMEIRO'],['NURSE'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ENGENHEIRO'],['ENGINEER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['ESPECIALISTA'],['SPECIALIST'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['FARMACEUTICO'],['PHARMACEUTICAL'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['FUNDADOR'],['FOUNDER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['GEOLOGO'],['GEOLOGIST'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['GERENTE'],['MANAGER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['INSPETOR'],['INSPECTOR'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['LABORATORISTA'],['LABORATORIST'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['MEDICO'],['DOCTOR'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PERITO'],['EXPERT'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PRESIDENTE'],['PRESIDENT'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PROFESSOR'],['TEACHER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PROGRAMADOR'],['PROGRAMMER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PROJETISTA'],['DESIGNER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PROPRIETARIO'],['OWNER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['PSICOLOGO'],['PSYCHOLOGIST'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['SOCIO'],['PARTNER'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['SUPERINTENDENTE'],['SUPERINTENDENT'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['SUPERVISOR TECNICO'],['SUPERVISOR TECHNICIAN'])
ICPcargo["CARGO"] = ICPcargo["CARGO"].replace(['VENDEDOR'],['SELLER'])



#tradução dos termos de departamento que estão no ICP
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ADMINISTRATIVO'],['ADMINISTRATIVE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['AGROPECUARIA'],['AGRICULTURE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ALMOXARIFADO'],['WAREHOUSE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['AMBIENTAL'],['ENVIRONMENTAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ARQUITETURA'],['ARCHITECTURE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ASSISTANT'],['ASSISTANT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ATENDIMENTO'],['ATTENDANCE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['BENEFICIO'],['BENEFIT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['COMERCIAL'],['COMMERCIAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['COMUNICACOES'],['COMMUNICATIONS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['COMPRAS'],['PURCHASES'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['COMUNICACAO'],['COMMUNICATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['CONFORMIDADE'],['CONFORMITY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['CONTABIL'],['ACCOUNTING'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['CONTRATOS'],['CONTRACTS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['CONTROLADORIA'],['CONTROLLERSHIP'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['CONSELHO'],['COUNCIL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['DADOS'],['DATA'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['DESENVOLVIMENTO'],['DEVELOPMENT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['DOCUMENTOS'],['DOCUMENTS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['EDUCACAO'],['EDUCATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ENERGIA'],['ENERGY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ENGENHARIA'],['ENGINEERING'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ESTOQUE'],['STOCK'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['EVENTOS'],['EVENTS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['FABRICACAO'],['MANUFACTURING'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['FARMACEUTICO'],['PHARMACEUTICAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['FINANCEIRO'],['FINANCIAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['GERAL'],['GENERAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['IMOBILIARIO'],['REAL ESTATE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['IMPORTACAO'],['IMPORT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['IMPRENSA'],['PRESS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['INFRAESTRUTURA'],['INFRASTRUCTURE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['INOVACAO'],['INNOVATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['INTELIGENCIA DE MERCADO'],['MARKET INTELLIGENCE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['INVESTIMENTO'],['INVESTMENT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['JURIDICO'],['LEGAL'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['LABORATORIO'],['LABORATORY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['LOGISTICA'],['LOGISTICS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['MANUFATURA'],['MANUFACTURE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['MANUTENCAO'],['MAINTENANCE'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['MEIO AMBIENTE'],['ENVIRONMENT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['NEGOCIOS'],['BUSINESS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['OBRAS'],['CONSTRUCTION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['OPERACAO'],['OPERATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['ORCAMENTO'],['BUDGET'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['PESQUISA'],['SEARCH'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['PLANEJAMENTO'],['PLANNING'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['PROCESSO'],['PROCESS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['PRODUCAO'],['PRODUCTION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['PROJETO'],['PROJECT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['QUALIDADE'],['QUALITY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['RH'],['HR'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['REDES'],['NETWORKS'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['RELACIONAMENTO'],['RELATIONSHIP'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['REMUNERACAO'],['REMUNERATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['RISCO'],['RISK'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SAUDE'],['HEALTH'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SEGURANCA'],['SAFETY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SEGURANCA DA INFORMACAO'],['INFORMATION SECURITY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SEGURANCA DO TRABALHO'],['WORKPLACE SAFETY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SERVICOS'],['SERVICES'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SUPORTE'],['SUPPORT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['SUPRIMENTOS'],['SUPPLIES'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TELECOMUNICACAO'],['TELECOMMUNICATION'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TI'],['IT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TOPOGRAFIA'],['TOPOGRAPHY'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TRANSPORTE'],['TRANSPORT'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TREINAMENTO'],['TRAINING'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['TRIBUTARIO'],['TAX'])
ICPdepartamento["DEPARTAMENTO"] = ICPdepartamento["DEPARTAMENTO"].replace(['VENDAS'],['SALES'])


#Elemento de texto (para permitir a escrita na caixa de texto - repete)
elem14 = driver.find_element_by_xpath('//*[@id="ember101-typeahead"]')

# Clicando na caixa de texto
elem14.click()
i=0
j=0
print(ICPdepartamento["DEPARTAMENTO"])
print(ICPcargo["CARGO"])
print(len(ICPcargo["CARGO"]))
print(len(ICPdepartamento["DEPARTAMENTO"]))
while i < len(ICPdepartamento["DEPARTAMENTO"]):
    j=0
    while j < len(ICPcargo["CARGO"]):
    # Escrevendo o nome cargo + departamento traduzidos de forma concatenada
        elem14.send_keys(str(ICPdepartamento["DEPARTAMENTO"][i].lower()) + ' ' + str(ICPcargo["CARGO"][j]).lower())
    # apertando enter
        keyboard = Controller()
        keyboard.press(Key.enter)
        time.sleep(3)

        keyboard.release(Key.enter)
        print(ICPdepartamento["DEPARTAMENTO"][i] +" "+ ICPcargo["CARGO"][j])
        print(j)
        print(i)
        j+=1
    i-=1
    i+=2


# elemento HTML todos os filtros

elem14a = driver.find_element_by_xpath('//*[@id="ember46"]/li[13]/button')

# clicando em todos os filtros

elem14a.click()

print("Filtro de ICP pronto. Abra o navegador para visualizar. Não Esqueca de inserir o tipo de Empresa.")
print("Empresa de capital aberto")
print("Empresa privada")
print("Sociedade")
print("Proprietário único")