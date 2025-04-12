# Criar um jogo onde dois jogadores (ou um jogador e a CPU) lutam em turnos até que um seja derrotado.

import random

while True:
    print("\n=== DUELO DE HERÓIS ===")
    print("[1] Iniciar Jogo")
    print("[2] Sair")
    escolha = input("Escolha: ")

    if escolha == "2":
        print("Saindo do jogo...")
        break

    elif escolha == "1":
        hp = random.randint(200, 1000)
        hp_jogador = hp
        hp_inimigo = hp

        atq_jogador = random.randint(1, 50)
        def_jogador = random.randint(1, 50)

        atq_inimigo = random.randint(1, 50)
        def_inimigo = random.randint(1, 50)

        print("\n=== Você ===")
        print("HP:", hp_jogador)
        print("ATQ:", atq_jogador, " DEF:", def_jogador)

        print("\n=== Inimigo ===")
        print("HP:", hp_inimigo)
        print("ATQ:", atq_inimigo, " DEF:", def_inimigo)

        turno = 1

        while hp_jogador > 0 and hp_inimigo > 0:
            print(f"\n--- Turno {turno} ---")
            print(f"Seu HP: {hp_jogador} | HP do Inimigo: {hp_inimigo}")
            print("Sua vez: [1] Atacar ou [2] Curar?")
            acao = input("Escolha: ")

            if acao == "1":
                dano = atq_jogador - def_inimigo

                if dano < 0:
                    dano = 0

                hp_inimigo = hp_inimigo - dano
                print(f"\nVocê ataca! Inimigo perde {dano} HP.")

            elif acao == "2":
                cura = random.randint(10, 30)
                hp_jogador = hp_jogador + cura
                print(f"\nVocê se cura em {cura} HP.")

            else:
                print("\nOpção inválida! Você perdeu o turno.")

            if hp_inimigo <= 0:
                print("\nVocê venceu o duelo!")
                break


            escolha_inimigo = random.choice(["atacar", "curar"])

            if escolha_inimigo == "atacar":
                dano = atq_inimigo - def_jogador

                if dano < 0:
                    dano = 0

                hp_jogador = hp_jogador - dano
                print(f"Inimigo ataca! Você perde {dano} HP.")

            else:
                cura = random.randint(10, 30)
                hp_inimigo = hp_inimigo + cura
                print(f"Inimigo se cura em {cura} HP.")

            if hp_jogador <= 0:
                print("\nVocê foi derrotado...")
                break

            turno = turno + 1

    else:
        print("INVALIDO")