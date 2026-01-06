import random
while True:
    print("Pedra, Papel, Tesoura")
    print("Regras: ")
    print("1 - A partida será realizada entre um jogador(a) e um bot")
    print("2 - O jogador que vencer a partida 3 vezes saira ganhador! ")
    print("3 - As opções de jogada são : PEDRA, PAPEL, TESOURA ")
    print("4 - Se divirta!")

    nome_jokenpô = input("Olá jogador(a), seja bem vindo, por favor digite seu nome: ")
    placar_jogador = 0
    placar_bot = 0
    while True:
        opção_jogador = input("Digite sua opção (PEDRA, PAPEL, TESOURA): ").upper()
        opção_bot = random.choice(["PEDRA", "PAPEL", "TESOURA"])
        print(f"O bot escolheu : {opção_bot} e o jogador(a) {nome_jokenpô} escolheu : {opção_jogador}")
        if (opção_jogador == "PEDRA" and opção_bot == "TESOURA") or \
        (opção_jogador == "PAPEL" and opção_bot == "PEDRA") or \
        (opção_jogador == "TESOURA" and opção_bot == "PAPEL"):
            placar_jogador += 1
            print(f"O jogador(a) {nome_jokenpô} venceu a rodada! Placar = {nome_jokenpô} {placar_jogador} X {placar_bot} Bot")
        
        elif (opção_bot == "PEDRA" and opção_jogador == "TESOURA") or \
        (opção_bot == "PAPEL" and opção_jogador == "PEDRA") or \
        (opção_bot == "TESOURA" and opção_jogador == "PAPEL"):
            placar_bot += 1
            print(f"O bot venceu a rodada! Placar = {nome_jokenpô} {placar_jogador} X {placar_bot} Bot")

        elif opção_jogador == opção_bot:
            print(f"A rodada deu empate! Placar = {nome_jokenpô} {placar_jogador} X {placar_bot} Bot")
    
        else:
            print("Opção inválida, tente novamente!")
            continue
    
        if placar_jogador == 3:
            print("O jogador(a) venceu o jogo! Parabéns")
            break
        elif placar_bot == 3:
            print("O bot venceu o jogo! Parabéns")
            break
    while True:
        jogar_de_novo_velha = input(f"Você deseja jogar de novo jogador(a) {nome_jokenpô} (S/N) S para sim e N para não: ").upper()
        if jogar_de_novo_velha == "S":
            print(f"Obrigado por querer jogar de novo jogador {nome_jokenpô}, aproveite!")
            break
        elif jogar_de_novo_velha == "N":
            print(f"Obrigado por jogar, jogador(a) {nome_jokenpô}!")
            exit()
        else:
            print("Opção inválida, tente novamente!")
           

        
        
    
    
    