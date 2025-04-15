# No jogo criado no exercício 11, adicionar as funcionalidades citadas.

import random

while True:
    print("\n=== DUELO DE HERÓIS ===")
    print("[1] Single Player (vs CPU)")
    print("[2] Multiplayer (2 Jogadores)")
    print("[3] Sair")
    escolha = input("Escolha: ")

    if escolha == "3":
        print("Saindo do jogo...")
        break

    elif escolha == "1" or escolha == "2":
        hp = random.randint(200, 1000)
        hp1 = hp
        hp2 = hp

        atq1 = random.randint(1, 50)
        def1 = random.randint(1, 50)

        atq2 = random.randint(1, 50)
        def2 = random.randint(1, 50)

        forca1_turnos = 0
        forca2_turnos = 0

        tela_azul1_turnos = 0
        tela_azul2_turnos = 0

        loop_infinito1 = False
        loop_infinito2 = False

        buffer_overflow1 = False
        buffer_overflow2 = False

        cache_hit1_usado = False
        cache_hit2_usado = False

        turno = 1

        print("\n=== JOGADOR 1 ===")
        print(f"HP: {hp1}")
        print(f"ATQ: {atq1}  DEF: {def1}")

        if escolha == "2":
            print("\n=== JOGADOR 2 ===")
            print(f"HP: {hp2}")
            print(f"ATQ: {atq2}  DEF: {def2}")
        else:
            print("\n=== INIMIGO ===")
            print(f"HP: {hp2}")
            print(f"ATQ: {atq2}  DEF: {def2}")

        while hp1 > 0 and hp2 > 0:
            print(f"\n--- Turno {turno} ---")
            print(f"J1 HP: {hp1} | J2 HP: {hp2}")

            if buffer_overflow1:
                dano = int(hp * 0.05)
                hp1 = hp1 - dano
                print(f"J1 sofre {dano} de Buffer Overflow!")

            if buffer_overflow2:
                dano = int(hp * 0.05)
                hp2 = hp2 - dano
                print(f"J2 sofre {dano} de Buffer Overflow!")

            if loop_infinito1:
                print("J1 perdeu o turno com Loop Infinito!")
                loop_infinito1 = False

            else:
                print("\nJOGADOR 1 - Escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Item")
                acao1 = input("\n-> ")

                if acao1 == "1":
                    if forca1_turnos > 0:
                        ataque = atq1 + 10
                    else:
                        ataque = atq1

                    if tela_azul2_turnos > 0:
                        defesa = 0
                    else:
                        defesa = def2

                    dano = ataque - defesa

                    if random.randint(1, 100) <= 10:
                        dano = dano * 2
                        print("CRÍTICO!")

                    if dano < 0:
                        dano = 0
                    hp2 = hp2 - dano
                    print(f"J1 ataca! J2 perde {dano} HP.")

                elif acao1 == "2":
                    cura = random.randint(10, 30)
                    hp1 += cura
                    print(f"J1 se cura em {cura} HP.")

                elif acao1 == "3":
                    print("Itens: \n[1] Poção de Força \n[2] Buffer Overflow \n[3] Loop Infinito \n[4] Cache Hit \n[5] Tela Azul")
                    item = input("\nUsar item: ")

                    if item == "1":
                        forca1_turnos = 2
                        print("J1 ativou Poção de Força (+10 ATQ por 2 turnos)")

                    elif item == "2":
                        buffer_overflow2 = True
                        print("J1 usou Buffer Overflow em J2!")

                    elif item == "3":
                        loop_infinito2 = True
                        print("J1 causou Loop Infinito em J2!")

                    elif item == "4":
                        if hp1 < hp * 0.25 and not cache_hit1_usado:
                            cura = int(hp * 0.3)
                            hp1 += cura
                            cache_hit1_usado = True
                            print(f"J1 usou Cache Hit e curou {cura} HP!")
                        else:
                            print("Cache Hit indisponível.")

                    elif item == "5":
                        tela_azul2_turnos = 2
                        print("J1 usou Tela Azul! Defesa de J2 zerada por 2 turnos.")

                    else:
                        print("Item inválido.")

                else:
                    print("Ação inválida.")

            if hp2 <= 0:
                print("\nJOGADOR 1 venceu o duelo!")
                break

            if loop_infinito2:
                print("J2 perdeu o turno com Loop Infinito!")
                loop_infinito2 = False
            else:
                if escolha == "2":
                    print("\nJOGADOR 2 - Escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Item")
                    acao2 = input("\n-> ")
                else:
                    acao2 = random.choice(["1", "2"])

                if acao2 == "1":
                    if forca2_turnos > 0:
                        ataque = atq2 + 10
                    else:
                        ataque = atq2

                    if tela_azul1_turnos > 0:
                        defesa = 0
                    else:
                        defesa = def1

                    dano = ataque - defesa

                    if random.randint(1, 100) <= 10:
                        dano *= 2
                        print("CRÍTICO!")

                    if dano < 0:
                        dano = 0
                    hp1 = hp1 - dano
                    print(f"J2 ataca! J1 perde {dano} HP.")

                elif acao2 == "2":
                    cura = random.randint(10, 30)
                    hp2 += cura
                    print(f"J2 se cura em {cura} HP.")

                elif acao2 == "3" and escolha == "2":
                    print("Itens: \n[1] Poção de Força \n[2] Buffer Overflow \n[3] Loop Infinito \n[4] Cache Hit \n[5] Tela Azul")
                    item = input("\nUsar item: ")

                    if item == "1":
                        forca2_turnos = 2
                        print("J2 ativou Poção de Força (+10 ATQ por 2 turnos)")

                    elif item == "2":
                        buffer_overflow1 = True
                        print("J2 usou Buffer Overflow em J1!")

                    elif item == "3":
                        loop_infinito1 = True
                        print("J2 causou Loop Infinito em J1!")

                    elif item == "4":
                        if hp2 < hp * 0.25 and not cache_hit2_usado:
                            cura = int(hp * 0.3)
                            hp2 += cura
                            cache_hit2_usado = True
                            print(f"J2 usou Cache Hit e curou {cura} HP!")
                        else:
                            print("Cache Hit indisponível.")

                    elif item == "5":
                        tela_azul1_turnos = 2
                        print("J2 usou Tela Azul! Defesa de J1 zerada por 2 turnos.")

                    else:
                        print("Item inválido.")

            if hp1 <= 0:
                if escolha == "2":
                    print("\nJOGADOR 2 venceu o duelo!")
                else:
                    print("\nVocê foi derrotado pela CPU...")
                break

            if forca1_turnos > 0:
                forca1_turnos = forca1_turnos - 1

            if forca2_turnos > 0:
                forca2_turnos = forca2_turnos - 1

            if tela_azul1_turnos > 0:
                tela_azul1_turnos = tela_azul1_turnos - 1

            if tela_azul2_turnos > 0:
                tela_azul2_turnos = tela_azul2_turnos - 1

            turno += 1

    else:
        print("INVALIDO")
