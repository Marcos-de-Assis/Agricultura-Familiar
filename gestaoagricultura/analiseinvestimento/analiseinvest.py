def analise_investimento():
    # Entrada de dados do primeiro projeto
    projeto1 = input("Nome do primeiro projeto: ")
    data_implantacao1 = input("Data de implantação do primeiro projeto (dd-mm-yyyy): ")
    recurso_inicial1 = float(input("Valor do capital de investimento inicial do primeiro projeto: "))
    custo_mensal1 = float(input("Custo mensal de operação do primeiro projeto: "))
    receita_estimada1 = float(input("Valor da receita mensal estimada do primeiro projeto: "))
    valor_residual1 = float(input("Valor residual do primeiro projeto: "))
    tma1 = float(input("Taxa mínima de atratividade do primeiro projeto (em decimal, por exemplo, 0.1 para 10%): "))

    # Cálculo do tempo de retorno do primeiro projeto
    tempo_retorno1 = (recurso_inicial1 + (custo_mensal1 * tma1)) / receita_estimada1

    # Verificar se há um segundo projeto para comparação
    novo = input("Há um segundo projeto para comparar? (s/n): ").strip().lower()
    
    if novo == 's':
        # Entrada de dados do segundo projeto
        projeto2 = input("Nome do segundo projeto: ")
        data_implantacao2 = input("Data de implantação do segundo projeto (dd-mm-yyyy): ")
        recurso_inicial2 = float(input("Valor do capital de investimento inicial do segundo projeto: "))
        custo_mensal2 = float(input("Custo mensal de operação do segundo projeto: "))
        receita_estimada2 = float(input("Valor da receita mensal estimada do segundo projeto: "))
        valor_residual2 = float(input("Valor residual do segundo projeto: "))
        tma2 = float(input("Taxa mínima de atratividade do segundo projeto (em decimal, por exemplo, 0.1 para 10%): "))

        # Cálculo do tempo de retorno do segundo projeto
        tempo_retorno2 = (recurso_inicial2 + (custo_mensal2 * tma2)) / receita_estimada2

        # Comparação entre os dois projetos
        if tempo_retorno1 < tempo_retorno2:
            projeto_viavel = projeto1
            temp_retor_menor = tempo_retorno1
        else:
            projeto_viavel = projeto2
            temp_retor_menor = tempo_retorno2

        # Exibir os resultados
        print(f"\nO projeto {projeto1} tem um tempo de retorno estimado de {tempo_retorno1:.2f} meses.")
        print(f"O projeto {projeto2} tem um tempo de retorno estimado de {tempo_retorno2:.2f} meses.")
        print(f"O projeto mais viável é {projeto_viavel}, com um tempo de retorno de {temp_retor_menor:.2f} meses.")
    else:
        # Exibir o resultado do primeiro projeto
        print(f"\nO projeto {projeto1} tem um tempo de retorno estimado de {tempo_retorno1:.2f} meses.")
        print("Não há outro projeto para comparar.")

# Chamada da função para execução
analise_investimento()