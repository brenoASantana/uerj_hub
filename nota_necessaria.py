def calcular_notas_necessarias():
    # Solicitar a nota da P1
    p1 = float(input("Digite a nota da P1 (0 a 10): "))

    # Calcular a nota necessária na P2 para passar direto
    nota_necessaria_p2_direto = (7 * 2) - p1  # Média de 7 para P1 e P2
    if nota_necessaria_p2_direto <= 10:
        print(f"Você precisa tirar pelo menos {nota_necessaria_p2_direto:.2f} na P2 para passar direto.")
    else:
        print("Você não pode passar direto com a nota da P1 atual.")

    # Calcular a nota necessária na P2 para ir para PF
    nota_necessaria_p2_pf = (4 * 2) - p1  # Média de 4 para P1 e P2
    if nota_necessaria_p2_pf <= 10:
        print(f"Você precisa tirar pelo menos {nota_necessaria_p2_pf:.2f} na P2 para ir para a prova final (PF).")
    else:
        print("Você não pode ir para a prova final com a nota da P1 atual.")

    # Solicitar a nota da P2
    p2 = float(input("Digite a nota da P2 (0 a 10): "))

    # Calcular a média final
    media_final = (p1 + p2) / 2
    if media_final >= 7:
        print("Você foi aprovado direto!")
    elif media_final >= 4:
        print("Você irá para a prova final (PF).")
        # Calcular a nota necessária na PF
        nota_necessaria_pf = (5 * 3) - (p1 + p2)  # Média necessária para 3 notas (P1, P2, PF)
        if nota_necessaria_pf <= 10:
            print(f"Você precisa tirar {nota_necessaria_pf:.2f} na PF para ser aprovado.")
        else:
            print("Nota necessária é maior que 10. Você não poderá ser aprovado.")
    else:
        print("Você foi reprovado direto!")

# Executar a função
calcular_notas_necessarias()
