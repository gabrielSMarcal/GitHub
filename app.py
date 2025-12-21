import random

lista_num_sorteado = []
num_limite = 42
num_secreto = None
tentativas = 1


def gerar_num_aleatorio():
    """Gera um número aleatório entre 1 e num_limite."""
    
    global num_limite
    return random.randint(1, num_limite)


def exibir_texto_na_tela(mensagem):
    """Exibe texto na tela."""
    
    print(mensagem)


def texto_inicial():
    """Exibe as mensagens iniciais do jogo."""
    
    exibir_texto_na_tela(f'Escolha um Número entre 1 e {num_limite}!')


def verificar_chute(chute):
    """Verifica se o chute está correto e retorna o resultado"""
    
    global tentativas, num_secreto
    
    if chute == num_secreto:
        exibir_texto_na_tela('\nAcertou!')
        palavra_tentativa = 'tentativas' if tentativas > 1 else 'tentativa'
        mensagem_tentativas = f'Você descobriu o número secreto com: \n{tentativas} {palavra_tentativa}!'
        exibir_texto_na_tela(mensagem_tentativas)
        return True
    else:
        if chute > num_secreto:
            exibir_texto_na_tela('O número secreto é menor')
        else:
            exibir_texto_na_tela('O número secreto é maior')
        tentativas += 1
        return False


def limpar_tela():
    """Limpa a tela (opcional)."""
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def reiniciar_jogo():
    """Reinicia o jogo com um novo número secreto."""
    
    global num_secreto, tentativas
    num_secreto = gerar_num_aleatorio()
    tentativas = 1
    texto_inicial()


def main():
    """Função principal do jogo."""
    
    global num_secreto
    
    num_secreto = gerar_num_aleatorio()
    print('=== Jogo do Número secreto! ===')
    texto_inicial()
    
    jogo_ativo = True
    
    while jogo_ativo:
        try:
            chute = int(input('\nDigite seu chute: '))
            
            if chute < 1 or chute > num_limite:
                exibir_texto_na_tela(f'Por favor, digite um número entre 1 e {num_limite}')
                continue
            
            acertou = verificar_chute(chute)
            
            if acertou:
                resposta = input('\nDeseja jogar novamente? (s/n): ').lower()
                
                if resposta == 's':
                    print ("\nReiniciando o jogo...\n")
                    print('='*40 + '\n')
                    reiniciar_jogo()
                    
                else:
                    exibir_texto_na_tela('\nObrigado por jogar! Até a próxima!')
                    jogo_ativo = False
        
        except ValueError:
            exibir_texto_na_tela('Por favor, digite um número válido!')
            
        except KeyboardInterrupt:
            exibir_texto_na_tela('\n\nJogo interrompido. Até logo!')
            jogo_ativo = False


if __name__ == '__main__':
    main()