def analise_custo_beneficio(proj_existent, dat_inicio_proj_existent, invest_proj_existent, cust_mensal_proj_existent, rec_mensal_proj_existent, novo_implement, dat_inicio_implement, invest_implement, cust_mensal_nov_implement, rec_estimada_mensal, temp_retorno):
    # Calcular o custo total do projeto existente
    custo_total_proj_existent = invest_proj_existent + (cust_mensal_proj_existent * temp_retorno)

    # Calcular o custo total do projeto com a mudança
    custo_total_proj_mudanca = invest_implement + (cust_mensal_nov_implement * temp_retorno)

    # Calcular a diferença de custo entre o projeto existente e o projeto com a mudança
    diferenca_custo = custo_total_proj_mudanca - custo_total_proj_existent

    # Calcular a receita líquida mensal
    rec_liquida = diferenca_custo - rec_estimada_mensal

    return diferenca_custo, rec_liquida

proj_existent = input("Nome do projeto existente: ")
dat_inicio_proj_existent = input("Início do projeto existente (no formato 'dd-mm-aaaa'): ")
invest_proj_existent = float(input("Valor do recurso usado para implantar o projeto: "))
cust_mensal_proj_existent = float(input("Custo mensal do projeto existente: "))
rec_mensal_proj_existent = float(input("Receita mensal do projeto existente: "))

novo_implement = input("Nome do implemento que será implantado: ")
dat_inicio_implement = input("Data de início da mudança (no formato 'dd-mm-aaaa'): ")
invest_implement = float(input("Valor de investimento do implemento: "))
cust_mensal_nov_implement = float(input("Custo mensal com o novo implemento: "))
rec_estimada_mensal = float(input("Nova receita estimada mensal: "))
temp_retorno = int(input("Tempo de retorno sobre o capital investido (em meses): "))

diferenca_custo, rec_liquida = analise_custo_beneficio(proj_existent, dat_inicio_proj_existent, invest_proj_existent, cust_mensal_proj_existent, rec_mensal_proj_existent, novo_implement, dat_inicio_implement, invest_implement, cust_mensal_nov_implement, rec_estimada_mensal, temp_retorno)

print("Impacto nos custos:", diferenca_custo)
print("Receita líquida mensal:", rec_liquida)
