# processamento.py
import pandas as pd

def aplicar_regras(dados):
    """
    Função para aplicar regras no cruzamento de dados.
    Exemplo: Comparar valores entre as colunas 'Coluna1' e 'Coluna2'.
    """
    dados['Resultado'] = dados.apply(lambda row: 'Coluna1 > Coluna2' if row['Coluna1'] > row['Coluna2'] else 'Coluna2 >= Coluna1', axis=1)
    return dados

def processar_excel(caminho_excel):
    """
    Função para ler o arquivo Excel e aplicar as regras.
    """
    try:
        # Carregar o arquivo Excel
        dados = pd.read_excel(caminho_excel)
        
        # Aplicar as regras predefinidas
        dados_cruzados = aplicar_regras(dados)
        
        # Retornar o dataframe processado
        return dados_cruzados

    except Exception as e:
        raise Exception(f"Erro ao processar o arquivo: {e}")
