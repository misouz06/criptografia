# utilizei como referência o vídeo "Vigenère Cipher In Python" do canal BasselTech no Youtube

def tamanho(mensagem , chave) :

    chave_tamanho = ''
    i = 0

    for string in mensagem :

        if string.isalpha():

            chave_tamanho += chave[i % len(chave)]
            i += 1
    # correção da IA no loop incorreto, que parava na primeira letra 
    # retirou o return que havia colocado e adicionou string vazia 
        else :
            chave_tamanho += ' '
    
    return chave_tamanho

def cifra(string_mensagem , string_chave , mode = "encrypt") :    

    if string_mensagem.isalpha() :

        #correção da IA na verificação de strings maiúsculas ou minúsculas
        primeira_letra_cifra = 'A' if string_mensagem.isupper() else 'a'

        posicao_string_antiga = ord(string_mensagem) - ord(primeira_letra_cifra)
        posicao_string_chave = ord(string_chave.lower()) - ord('a')

        # aplicando a fórmula da cifra
        if mode == 'encrypt' :
            posicao_string_nova = (posicao_string_antiga + posicao_string_chave) % 26
        else :
            posicao_string_nova = (posicao_string_antiga - posicao_string_chave + 26) % 26

        return chr(posicao_string_nova + ord(primeira_letra_cifra))

    return string_mensagem

def encriptada(mensagem , chave) :
    cifra_texto = ''

    tamanho_chave = tamanho(mensagem , chave)
    for string_mensagem , string_chave in zip(mensagem , tamanho_chave) :
        cifra_texto += cifra(string_mensagem , string_chave)

    return cifra_texto


entrada = input("Digite uma mensagem: ")
chave = 'artyom'

saida = encriptada(entrada , chave)

print(f"A palavra {entrada} encriptada é {saida}.")
