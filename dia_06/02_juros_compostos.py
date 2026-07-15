# %%%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """
    juros_compostos servem para calcular o retorno financeiro a partir de um aporte.
    
    aporte: um número inteiro que represente o montante inicial aplicado
    taxa: um número float que represente o rendimento sobre o aporte
    anos: um número inteiro, tempo de aplicação

    """
    return aporte * (1 + taxa) ** anos


# %%
juros_compostos(aporte=1000, taxa=0.13, anos=4)

