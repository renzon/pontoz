# Pontoz

Prova de conceito para transferir dados do SQL Server para BigQuery e depois para geração de relatório

## Camada Visual

1. Criar repositório em controlador de versão
2. Fazer o setup de ambdev
3. Entendendo o Problema
4. Foco no Output, Input é custo
5. DRE, Paths e Arquivos
6. Testando Output
7. Range, List Comprehension e F string
8. Usando templates na camada visual (Jinja2)
9. Utilização de chaves para imprimir valores do python para template
10. Utilização de for para imprimir relatórios mensais no template
11. Zip e extração de fixture de relatórios mensais
12. Round para Porcentagem
13. Sumário do DRE


## Big Query

1. O que é?
2. Instalação
3. Esquemas
4. Instalação Cliente Python
5. Autentis='gio'
s1='iog'
b = []
for i in range(len(s)):
    b+=s[i]
a = []
for j in range(len(s1)):
    a+=s1[j]

# print(b)
from itertools import product
comb=product(a,repeat=len(a))
perm=[]
for n in comb:
    print(n)
    # perm.append(n)
    if n==b:
        print(n)cação
6. Fixtures
7. Esquema via Client
8. Carregamento de Dados
9. Query via Interface Web
10. Query on Python Client
11. Resultado de Busca -> Modelo de Relatório
12. Agrupar Relatórios Mensais -> Relatório
13. Zip, partial, funções geradoras
14. Geração de relatórios mensais do ano
15. Integração BigQuery com Report

# SQL Server

1. Instalando DB
2. Instalando pyodbc
3. Instlaando SQL Alchemy
4. Criação de Schema
5. Fixtures
6. Cycle
7. Problemas do N + 1 selects
8. Carregando Transações em batelada
9. Sql Transaction para BigQuery Row