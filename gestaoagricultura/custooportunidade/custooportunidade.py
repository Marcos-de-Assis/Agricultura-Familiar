def analise_custo_oportunidade(nome_cult_existe, preco_vend_unid1, cust_unidad1, area_plant1, prod_unid_area1, novo_cultivar, preco_vend_unid2, cust_unidad2, area_plant2, prod_unid_area2):
    # Calcular a renda estimada para o projeto existente
    renda_estimada1 = area_plant1 * prod_unid_area1 * (preco_vend_unid1 - cust_unidad1)
    produtividade_projeto_existente = renda_estimada1 / area_plant1

    # Calcular a renda estimada para o novo projeto
    renda_estimada2 = area_plant2 * prod_unid_area2 * (preco_vend_unid2 - cust_unidad2)
    produtividade_novo_projeto = renda_estimada2 / area_plant2

    # Determinar qual cultura tem melhor custo oportunidade
    if produtividade_projeto_existente > produtividade_novo_projeto:
        melhor_custo_oportunidade = "Cultura existente"
        diferenca_renda = produtividade_projeto_existente - produtividade_novo_projeto
    else:
        melhor_custo_oportunidade = "Nova cultura"
        diferenca_renda = produtividade_novo_projeto - produtividade_projeto_existente

    return renda_estimada1, renda_estimada2, melhor_custo_oportunidade, diferenca_renda
