#Verifica se um dado argumento "tab" é um tabuleiro válido.
def eh_tabuleiro(tab):
       
    if not (type(tab) == tuple):    # Verifica se tabuleiro(tab) é um tuplo 
            return False
    
    if not (2<=len(tab)<=100):      # Verifica se o número de linhas do tabuleiro está entre 2 e 100
            return False     

    
    for i in tab:                   #Itera sobre cada linha do tabuleiro              
        if type(i) != tuple:        #Verifica se cada linha é um tuplo
            return False
        if not (2<=len(i)<=100):              
            return False
        for x in i:     
            if not (x==0 or x==1 or x==-1):       #Verifica se o tuplo só tem 1,0,-1
                        return False
            
    for i in range(1,len(tab)):
        if not(len(tab[i]) == len(tab[i-1])):       # Verifica se todas as linhas têm o mesmo número de colunas
            return False
    
    for i in tab:                                   ## Verifica se todos os elementos são inteiros
        for x in i:
            if not(type(x) == int):
                return False
    return True

#Verifica se o valor "pos" é uma posição válida.
def eh_posicao(pos):
    if not(type(pos) == int and pos>0 and pos<10000):       # Verifica se a posição é um inteiro e está no intervalo (0, 10000)
        return False
    return True

#Retorna as dimensões de um tabuleiro.
def obtem_dimensao(tab):
    m = len(tab)        #Numero de linhas
    n = len(tab[1])      #Numero de colunas
    r = ()
    r = r + (m,n )
    return r

#Retorna o valor da posição no tabuleiro.
def obtem_valor(tab,pos):
    r = ()

    for i in tab:   #Faz com que todos os elementos do tabuleiro sejam apenas uma tupla
         for x in i:
            r = r + (x, )
            
    return r[pos-1]         #"pos" começa em 1, então usamos "pos-1"

#Retorna um tuplo de tuplos que correspondem às posições do tabuleiro
def obtem_posicao_inteiros(tab):
    m = len(tab)        #Numero de linhas
    n = len(tab[0])     #Numero de colunas
    tuplo1 = ()
    tuplo2= ()
    
    for i in range(1,m*n+1):        # Preenche tuplo1 com inteiros de 1 ao total das posições
        tuplo1 = tuplo1 + (i, )

    for i in range(0, len(tuplo1), n):           # Organiza tuplo1 em grupos de "n" colunas
        tuplo2 = tuplo2 + (tuplo1[i : i + n], )     # Adiciona uma linha de "n" colunas ao tuplo2
    
    #temos assim os numeros das posiçoes ex:((1,2,3,4),(5,6,7,8)...)  
    return tuplo2             

#Retorna a coluna correspondente à posição no tabuleiro.
def obtem_coluna(tab,pos):
    n = len(tab[0])     #numero de colunas
    tuplo3 = ()
    
    for i in obtem_posicao_inteiros(tab):       #Encontra a posição correspondente no tabuleiro para determinar a coluna
        for x in range(0,n):                    #Itera sobre cada linha
            if i[x] == pos:                     # Se o número na posição x da linha i for igual a "pos", encontramos a coluna
                posicao = x                     #Guardamos esse indice
    
    for i in obtem_posicao_inteiros(tab):       #Coletar todas as posições da coluna encontrada
        tuplo3 = tuplo3 + (i[posicao], )        #Adiciona o valor correspondente da coluna ao tuplo3
    return tuplo3

#Retorna a linha correspondente à posição no tabuleiro.
def obtem_linha(tab,pos):

    for i in obtem_posicao_inteiros(tab):           #Percorre o tuplo de inteiros
        for x in i:                                 #Itera sobre cada valor da linha
            if pos == x:                            # Se a posição é igual ao valor da linha
                g = i                               #Guarda o tuplo que queremos 
    return g

#Retorna um tuplo contendo dois tuplos: um com os valores da diagonal principal e outro com os valores da anti-diagonal do tabuleiro que passam pela posição.
def obtem_diagonais(tab,pos):
    m = len(tab)        #Numero de linhas
    n = len(tab[0])     #Numero de colunas
    tuplo3 = ()
    tuplo4 = ()
    tuplo5 = ()
    cont = -1
    cont1 = 1
    cont2 = 1
    cont3 = 1 
    
    for i in range(0,len(obtem_posicao_inteiros(tab))):          #Encontrar a posição da variavél "pos" no tabuleiro
        for x in range(0,n):
            if obtem_posicao_inteiros(tab)[i][x] == pos:
                guardar_pos = x                                  #Índice da coluna onde está "pos"
                guardar_pos_tuplo = i                            #Índice da linha onde está "pos"
    
    #Parte superior esquerda da diagonal 
    while guardar_pos_tuplo + cont >= 0 and guardar_pos + cont >= 0:                                
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo+cont][guardar_pos+cont], )         #Adiciona os valores da diagonal acima e à esquerda da posição "pos"
        cont = cont - 1         #Diminui o contador para continuar em direção à superior esqeurda
    
    tuplo3 = tuplo3 + (pos,)        #Inclui a porpria posição no tuplo
    
    #Parte inferior direita da diagonal 
    while guardar_pos_tuplo + cont1 < m and guardar_pos + cont1 < n:                                       
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo+cont1][guardar_pos+cont1], )            #Adiciona os valores da diagonal abaixo e à direita da posição "pos"
        cont1 = cont1 + 1            #Aumenta o contador para continuar em direção à direita inferior
    

    #Parte inferior esquerda da anti-diagonal 
    while guardar_pos_tuplo + cont2 < m and guardar_pos - cont2 >= 0:
        tuplo4 = tuplo4 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo+cont2][guardar_pos-cont2], )           #Adiciona os valores da diagonal acima e à direita da posição "pos"
        cont2 = cont2 + 1           #Aumenta o contador para continuar em direção à direita superior
    
    tuplo4 = tuplo4 + (pos, )       #Inclui a porpria posição no tuplo
    
    #Parte superior direita da diagonal anti-diagonal
    while guardar_pos_tuplo - cont3 >= 0 and guardar_pos + cont3 < n:
        tuplo4 = tuplo4 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo-cont3][guardar_pos+cont3], )       #Adiciona os valores da diagonal acima e à direita da posição "pos"
        cont3 = cont3 + 1            #Aumenta o contador para continuar em direção à direita superior
    
    tuplo3 = tuple(sorted(tuplo3))
    tuplo4 = tuple(sorted(tuplo4, reverse=True))
    tuplo5 = tuplo5 + (tuplo3,tuplo4 )
    return tuplo5
    
#Converte um tabuleiro em uma string.
def tabuleiro_para_str(tab):
    c = len(tab[1])                             #Numero de colunas
    l = len(tab)                                #Numero de linhas
    posicao, linha, tabela = "", "", ""
    
    for i in range(l):                          #i = 0,1,2,3,4,5...(n de linhas)
        for x in range(c):                      #x = 0,1,2,3,4,5...(n de colunas)
            
            if tab[i][x] == 1:                  #Jogador 1     
                posicao = "X"
            
            elif tab[i][x] == -1:               #Jogador -1  
                posicao = "O"
            
            elif tab[i][x] == 0:                #Espaço livre
                posicao = "+"
            
            if x == 0:                          
                linha = posicao                 #Guarda a posição das posições livres
            
            else:
                linha = linha + "---" + posicao          #Se a posição não é livre ir intercalando com "---"  
        
        if i != (l-1):                            #Se não for a última linha, adiciona separadores verticais entre as linhas
            tabela = tabela + linha + "\n" + ("|   " * (c-1)) + "|" + "\n"
        else:                                       #Se for a última linha, adiciona apenas a linha 
            tabela = tabela + linha
    return tabela

#Verifica se a posição fornecida é válida dentro do tabuleiro dado.
def eh_posicao_valida(tab,pos):
    cont = 0
    if eh_tabuleiro(tab) == False or eh_posicao(pos) == False:          #Verifica se o tabuleiro é válido e se a posição é válida
        raise ValueError("eh_posicao_valida: argumentos invalidos")    
    
    for i in obtem_posicao_inteiros(tab):               #Vai pelas posições validas do tabuleiro
        for x in i:                                             
            if x == pos:                            #Se a posição é encontrada
                cont = 1            
    if cont == 0:                   #Se o contador ainda for 0, a posição não é válida
        return False
    else:
        return True

#Verifica se a posição fornecida está livre no tabuleiro dado.
def eh_posicao_livre(tab,pos):
    tuplo1 = ()
    tuplo2 = ()
    
    #Verificação de argumentos da função
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or pos < 1 or pos > obtem_dimensao(tab)[0] * obtem_dimensao(tab)[1]:
        raise ValueError('eh_posicao_livre: argumentos invalidos')

    for i in tab:
        for x in i:
            tuplo1 = tuplo1 + (x, )     #Adiciona todos os valores do tabuleiro em um único tuplo
    
    if pos > len(tuplo1):       #Se a posição estiver além do tamanho do tuplo, retorna False
        return False
    
    for i in range(len(tuplo1)):            #Armazena no tuplo2 se a posição está livre(True) ou ocupada(False)
        if tuplo1[i] == -1 or tuplo1[i] == 1:
            tuplo2 = tuplo2 + (False, )
        elif tuplo1[i] == 0:
            tuplo2 = tuplo2 + (True, )
    
    #Retorna True se a posição está livre, False se está ocupada
    if tuplo2[pos-1] == True:
        return True
    elif tuplo2[pos-1] == False:
        return False    

#Obtém as posições livres em um tabuleiro.
def obtem_posicoes_livres(tab):
    tuplo1 = ()
    tuplo2 = ()
    
    #Verifica se o argumento é válido
    if eh_tabuleiro(tab) == False:
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    
    for i in tab:
        for x in i:
            tuplo1 = tuplo1 + (x, )             # Adiciona todos os valores do tabuleiro em um único tuplo
    
    for i in range(len(tuplo1)):                #Verifica cada posição em tuplo1 para encontrar posições livres
        if tuplo1[i] == 0:
            tuplo2 = tuplo2 + (i+1, )
    return tuplo2

#Obtém as posições ocupadas por um jogador no tabuleiro.
def obtem_posicoes_jogador(tab, jog):
    tuplo1 = ()
    tuplo2 = ()
    #Verifica se os argumentos são validos
    if eh_tabuleiro(tab) == False or not (jog ==1 or jog==-1):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    
    for i in tab:
        for x in i:
            tuplo1 = tuplo1 + (x, ) #Adiciona todos os valores do tabuleiro em um único tuplo
    
    for i in range(len(tuplo1)):        #Verifica cada posição em tuplo1 para encontrar as posições do jogador
        if tuplo1[i] == jog:            #Se o valor na posição for igual ao jogador
            tuplo2 = tuplo2 + (i+1, )       #Cria um tuplo novo com os dados do antigo mais a posição percorrida
    return tuplo2

#Obtém as posições adjacentes a uma posição específica em um tabuleiro.
def obtem_posicoes_adjacentes(tab, pos):
    cont = 0
    m = len(tab)        #Numero de linhas
    n = len(tab[0])     #Numero de colunas
    tuplo3 = ()

    #Verifica se os argumentos são validos
    if eh_tabuleiro(tab) == False or eh_posicao(pos) == False:
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    
    #Encontrar a posição das linhas e colunas do meu número
    for i in range(0,len(obtem_posicao_inteiros(tab))):
        for x in range(0,n):
            if obtem_posicao_inteiros(tab)[i][x] == pos:
                cont = 1            #Marca que a posição foi encontrada
                guardar_pos = x     #Guarda a coluna da posição encontrada
                guardar_pos_tuplo = i       #Guarda a linha da posição encontrada
                break
    
    if cont == 0:     # Se a posição não foi encontrada, levanta um erro  
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    if guardar_pos_tuplo + 1 < m and guardar_pos + 1 < n:                                               # diagonal abaixo e à direita
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo + 1][guardar_pos + 1],)
    if guardar_pos_tuplo + 1 < m and guardar_pos - 1 >= 0:                                              # diagonal abaixo e à esquerda
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo + 1][guardar_pos - 1],)
    if guardar_pos_tuplo - 1 >= 0 and guardar_pos + 1 < n:                                              # diagonal acima e à direita
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo - 1][guardar_pos + 1],)
    if guardar_pos_tuplo - 1 >= 0 and guardar_pos - 1 >= 0:                                             # diagonal acima e à esquerda
        tuplo3 = tuplo3 + (obtem_posicao_inteiros(tab)[guardar_pos_tuplo - 1][guardar_pos - 1],)
    
    #Tuplo 3 é os numeros das posições das diagonais e vai ser o return final
    
    tuplo4 = obtem_coluna(tab,pos)           #Obtém a coluna da posição fornecida
    for i in range(len(tuplo4)):        
        if tuplo4[i] == pos:
            indice_n_pedido = i             #Guarda o índice da posição
    
    if indice_n_pedido > 0:                  #Se não for a primeira posição, adiciona a posição anterior
        tuplo3 = tuplo3 + (tuplo4[indice_n_pedido - 1], )
    if indice_n_pedido < len(tuplo4) - 1:     #Se não for a última posição, adiciona a próxima
        tuplo3 = tuplo3 + (tuplo4[indice_n_pedido + 1], )
    
    tuplo5 = obtem_linha(tab,pos)       # Obtém a linha da posição fornecida
    for i in range(len(tuplo5)):
        if tuplo5[i] == pos:
              indice_n_pedido_l = i         #Guarda o índice da posição
    
    if indice_n_pedido_l > 0:               #Se não for a primeira posição, adiciona a posição anterior
        tuplo3 = tuplo3 + (tuplo5[indice_n_pedido_l - 1], )
    if indice_n_pedido_l < len(tuplo5) - 1:         #Se não for a última posição, adiciona a próxima
        tuplo3 = tuplo3 + (tuplo5[indice_n_pedido_l + 1], )
    
    return tuple(sorted(set(tuplo3)))

#Calcula a distância entre dois pontos
def distancia_do_centro(x1, y1, x2, y2):
    #Se a diferença entre as coordenadas x for maior que a diferença entre as coordenadas y
    if abs(x1 - x2) > abs(y1 - y2):
        return abs(x1 - x2)     #Retorna a diferença da coordenada x
    else:
        return abs(y1 - y2)         #Retorna a diferença da coordenada y

#Obtém a posição de um dado índice em um tabuleiro.
def obter_posicao(tab, pos):
    linhas, colunas = obtem_dimensao(tab)       #Obtém o número de linhas e colunas do tabuleiro
    indice_linha = (pos - 1) // colunas
    local_coluna = pos - indice_linha * colunas - 1
    
    if indice_linha < len(tab):                     #Se o índice da linha está dentro dos limites do tabuleiro
        return indice_linha, local_coluna           #Retorna a posição 
    return -1, -1                                    #Retorna se a posição não for válida

#Ordena as posições de um tabuleiro com base na distância ao centro.
def ordena_posicoes_tabuleiro(tab, tup):
    
    #Verifica se os argumentos são validos
    if eh_tabuleiro(tab) == False or type(tup) != tuple:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    
    if tup == ():   #Se é vazio retorna vazio
        return ()

    tab_unico = ()
    for linha in obtem_posicao_inteiros(tab):
        for posicao in linha:
            tab_unico += (posicao,)         #Adiciona todas as posições do tabuleiro em um único tuplo

    #Verifica se todas as posições no argumento (tup) estão presentes no tabuleiro
    for posicao in tup:
        if posicao not in tab_unico:
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    
    num_linhas = len(tab)
    num_colunas = len(tab[0])
    distancias = []
    
    #Define a quantidade de sub-listas na lista de distâncias com base nas dimensões do tabuleiro
    if num_linhas > num_colunas:
        for i in range(int(num_linhas / 2) + 2):
            distancias.append([]) 
    else:
        for i in range(int(num_colunas / 2) + 2):
            distancias.append([])  

    #Calcula as coordenadas do centro do tabuleiro
    centro_linha = int(num_linhas / 2)
    centro_coluna = int(num_colunas / 2)

    
    for posicao in tup:      #Calcula a distância de cada posição no tupla ao centro e armazena nas listas 
        x, y = obter_posicao(tab, posicao)
        distancias[distancia_do_centro(x, y, centro_linha, centro_coluna)].append(posicao)
    
    resultado_ordenado = ()
    
    for lista in distancias:        # Ordena as posições dentro de cada lista de distâncias
        resultado_ordenado += tuple(sorted(lista))
    return resultado_ordenado

#Marca uma posição no tabuleiro com o valor do jogador.
def marca_posicao(tab, pos, jog): 
    
    c = len(tab[0]) #Numero de colunas
    tab_unico = ()
    tab_unico_new = ()
    tab_new = ()
    tab_prov = ()
    
    #Verifica se os argumentos são validos
    if eh_tabuleiro(tab) == False or eh_posicao(pos) == False or not(jog == -1 or jog == 1) or eh_posicao_livre(tab,pos) == False:
        raise ValueError("marca_posicao: argumentos invalidos")
    
    for i in tab:
         for x in i:
            tab_unico = tab_unico + (x, )     #Adiciona todas os valores do tabuleiro em um único tuplo
    
    for i in range(len(tab_unico)):
        if i+1 == pos:
            guarda_indice = i           #Guarda o índice da posição a ser marcada
    
    for i in range(len(tab_unico)):
        if i == guarda_indice:
            tab_unico_new = tab_unico_new + (jog, )      #Substitui o valor pela jogada
        else:
            tab_unico_new = tab_unico_new + (tab_unico[i], )        #Mantém os outros valores
    
    #Temos agora um tuplo, já alterado com todas as infomações
    for i in range(0, len(tab_unico_new), c):       #Constrói o novo tabuleiro a partir do tuplo atualizado
        tab_prov = tuple(tab_unico_new[i:i + c])    #Cria uma nova linha
        tab_new = tab_new + (tab_prov, )            #Adiciona a nova linha ao tabuleiro
    return (tab_new)

#Verifica se há k posições consecutivas ocupadas pelo jogador em linhas, colunas ou diagonais em um tabuleiro de jogo.
def verifica_k_linhas(tab, pos, jog, k):

    coluna = obtem_coluna(tab,pos)
    linha = obtem_linha(tab,pos)
    diagonais1 = obtem_diagonais(tab,pos)[0]
    diagonais2 = obtem_diagonais(tab,pos)[1]
    tab_unico = ()
    
    for i in tab:
        for x in i:
            tab_unico = tab_unico + (x, )        #Adiciona todas os valores do tabuleiro em um único tuplo

    #Verifica se os argumentos são válidos
    if eh_tabuleiro(tab) == False or eh_posicao_valida(tab,pos) == False or not(jog == -1 or jog == 1 or type(k) == int) or k <= 0:
        raise ValueError("verifica_k_linhas: argumentos invalidos")

    #Verifica se a posição está ocupada pelo jogador
    if tab_unico[pos-1] != jog:
        return False
    
    #Conta k elementos presentes em uma sequência
    def contagem_k_presentes(a):
        tuplo_verifica = ()
        tuplo_comparado = (jog,) * k  
        
        for i in a:
            tuplo_verifica = tuplo_verifica + (tab_unico[i - 1],) 
        
        for i in range(len(tuplo_verifica) - k + 1):
            if tuplo_verifica[i:i + k] == tuplo_comparado:
                return True
        return False        #Retorna False se não encontrou
    return (contagem_k_presentes(coluna) or contagem_k_presentes(linha) or contagem_k_presentes(diagonais1) or contagem_k_presentes(diagonais2))

#Verifica se o jogo terminou
def eh_fim_jogo(tab,k):
    numero_de_posicoes = len(tab) * len(tab[0])
    
    #Verifica se os argumentos são válidos
    if eh_tabuleiro(tab) == False or not(type(k) == int) or k <= 0:
        raise ValueError("eh_fim_jogo: argumentos invalidos")    
    
    #Se não exisitirem posições livres retorna False
    if not(obtem_posicoes_livres(tab)):
            return True
    
    for pos in range(1, numero_de_posicoes):        #Passa por todas as posições
        if verifica_k_linhas(tab, pos, 1 , k) == True or verifica_k_linhas(tab, pos, -1, k) == True:    # Verifica se o jogador 1 ou jogador -1 tem k posições consecutivas     
            return True
        
    return False

#Pede ao utilizadpr que escreva uma posição livre do tabuleiro, caso não seja uma posição livre a função volta a pedir
def escolhe_posicao_manual(tab):  

    #Verifica se o argumento é válido
    if eh_tabuleiro(tab) == False:
            raise ValueError("escolhe_posicao_manual: argumento invalido") 
    while True: 
        pos_livre = (input("Turno do jogador. Escolha uma posicao livre: "))    #Pede ao utilizador que insira o número

        if pos_livre.isdigit():     #Verifica se o utilizador submeteu um digito
            a = int(pos_livre)
            if (type(a) == int) and eh_posicao(a) and eh_posicao_valida(tab,a): 
                if eh_posicao_livre(tab,a):
                    return a

#Escolhe automaticamente uma posição no tabuleiro para o jogador, a função escolhe a posição com base no nível de dificuldade.
def escolhe_posicao_auto(tab, jog, k, lvl):
    
    #Verifica os argumentos da função
    if eh_tabuleiro(tab) == False or not(jog == -1 or jog == 1 or type(k) == int or k > 1) or lvl not in ["facil", "normal", "dificil"] :
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")    
    
    posicoes_jogaveis = ()

    if lvl == "facil":
            for i in obtem_posicoes_jogador(tab, jog):              #Percorre as posições do jogador 
                for x in obtem_posicoes_adjacentes(tab, i):         #x = posiçoes à volta das posiçoes já ocupadas pelo jogador
                    if eh_posicao_livre(tab,x):                     #Se estiver livre
                        posicoes_jogaveis += (x,)                   #Guardar num tuplo
            if posicoes_jogaveis != ():                             #Se esse tuplo não estiver vazio
                return ordena_posicoes_tabuleiro(tab, posicoes_jogaveis)[0]         
            else:
                return ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))[0]
    elif lvl == "normal":
        
        maior_L_1 = 0
        pos_maior_L_1 = ()
        maior_L_menos1 = 0
        pos_maior_L_menos1 = ()


        pos_livres = obtem_posicoes_livres(tab) 
        for i in pos_livres:                                    #Percorre as posições livres
            tabela_provisoria = marca_posicao(tab,i,1)          #Guarda numa tabela provisória

            for x in range(k,0,-1):                             #Verifica para cada linha de k até 1
                if verifica_k_linhas(tabela_provisoria, i, 1, x):
                    #Atualiza o maior k e posição correspondente
                    if maior_L_1 < x:
                        maior_L_1 = x
                        pos_maior_L_1 = (i,)
                    elif maior_L_1 == x:
                        pos_maior_L_1 = pos_maior_L_1 + (i, )
        
        #Verifica as posições livres para o jogador -1
        for i in pos_livres:
            tabela_provisoria = marca_posicao(tab,i,-1)

            for x in range(k,0,-1):
                if verifica_k_linhas(tabela_provisoria, i, -1, x):
                    
                    if maior_L_menos1 < x:
                        maior_L_menos1 = x
                        pos_maior_L_menos1 = (i, )
                    elif maior_L_menos1 == x:
                        pos_maior_L_menos1 =pos_maior_L_menos1 + (i, )
        
         #Escolha de posição com base nos maiores k
        if jog == -1 and maior_L_menos1 >= maior_L_1:   
            return ordena_posicoes_tabuleiro(tab, pos_maior_L_menos1)[0]
        elif jog == -1 and maior_L_menos1 < maior_L_1:
            return ordena_posicoes_tabuleiro(tab, pos_maior_L_1)[0]
        elif jog == 1 and maior_L_menos1 <= maior_L_1:
            return ordena_posicoes_tabuleiro(tab, pos_maior_L_1)[0]
        elif jog == 1 and maior_L_menos1 > maior_L_1:
            return ordena_posicoes_tabuleiro(tab, pos_maior_L_menos1)[0]

#Iniciar o jogo mnk
def jogo_mnk(cfg,jog,lvl):
    
    #Verifica os argumentos da função
    if type(cfg) != tuple:
        raise ValueError("jogo_mnk: argumentos invalidos")
    if type(cfg[0]) != int or type(cfg[1]) != int or type(cfg[2]) != int:
        raise ValueError("jogo_mnk: argumentos invalidos")
    if not(cfg[0] >= 2 and cfg[0] <= 100):
        raise ValueError("jogo_mnk: argumentos invalidos")
    if not(cfg[1] >= 2 and cfg[0] <= 100):
        raise ValueError("jogo_mnk: argumentos invalidos") 
    if not(cfg[2] <= cfg[0] or cfg[1] <= cfg[2]):
        raise ValueError("jogo_mnk: argumentos invalidos") 
    if not (lvl == "facil" or lvl == "normal" or lvl == "dificil"):
        raise ValueError("jogo_mnk: argumentos invalidos") 
    if not (jog == -1 or jog == 1):
        raise ValueError("jogo_mnk: argumentos invalidos") 
    if not(len(cfg) == 3):
        raise ValueError("jogo_mnk: argumentos invalidos") 
    
    #Imprime que o jogo começou e o simbolo do jogador
    print("Bem-vindo ao JOGO MNK.")
    if jog == -1:
        print("O jogador joga com 'O'.")
    elif jog == 1:
        print("O jogador joga com 'X'.")
    
    #Criar um tabuleiro, vazio
    tab = ()
    for i in range(cfg[0]*cfg[1]):
        tab = tab + (0, )
    subtuplos = []
    for i in range(0, len(tab), cfg[0]):
        subtuplo = tab[i:i+cfg[0]]
        subtuplos.append(subtuplo)
    tab = tuple(subtuplos)
    
    print(tabuleiro_para_str(tab))  #Imprime o tabulerio vazio

    while True:
        
        #Truno do jogador
        print("Turno do jogador. Escolha uma posicao livre: ")
        tab = marca_posicao(tab,escolhe_posicao_manual(tab),jog)
        print(tabuleiro_para_str(tab))
        if eh_fim_jogo(tab,cfg[2]):
            print("VITORIA")
            return(jog)

        #Turno do computador    
        print("Turno do computador (",lvl,"):")
        tab = marca_posicao(tab,escolhe_posicao_auto(tab,jog*-1,cfg[2],lvl),jog*-1)
        print(tabuleiro_para_str(tab))
        if eh_fim_jogo(tab,cfg[2]):
            print("DERROTA")
            return(jog*-1)
