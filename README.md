Projeto: **Ferramenta de processamento de arquivos Excel com interface gráfica** 

`Aqui estão as funcionalidades detalhadas:`

### 1. **Carregamento de Arquivos Excel**:

- O projeto permite ao usuário selecionar arquivos Excel do formato `.xlsx` por meio de um **diálogo de seleção de arquivos**. Esse processo é facilitado pela interface gráfica (usando a biblioteca `Tkinter`), que exibe uma caixa de diálogo para procurar e escolher o arquivo.

### 2. **Processamento de Dados com Regras Definidas**:

- O principal objetivo do projeto é **processar dados presentes no arquivo Excel**.
- A função `aplicar_regras()` aplica **regras de comparação** entre duas colunas específicas de uma planilha Excel (`Coluna1` e `Coluna2`). A regra implementada no código compara os valores dessas duas colunas e adiciona uma nova coluna ao DataFrame (`Resultado`), que contém o resultado da comparação.
**Exemplo de regra:** Para cada linha, se o valor de `Coluna1` for maior que o de `Coluna2`, o resultado será `'Coluna1 > Coluna2'`; caso contrário, o resultado será `'Coluna2 >= Coluna1'`.

### 3. **Exibição dos Resultados na Interface Gráfica**:

- Após o processamento, o resultado (um **DataFrame modificado**) é exibido diretamente na interface gráfica do Tkinter. O usuário pode ver o conteúdo do DataFrame como texto na área designada.
- A interface também inclui uma barra de rolagem para facilitar a visualização de grandes volumes de dados.

### 4. **Salvamento Automático do Resultado Processado**:

- Além de exibir o resultado na interface, o projeto também salva automaticamente o resultado em um novo arquivo Excel chamado `dados_cruzados.xlsx`, sem que o usuário precise especificar manualmente o local de salvamento.
- Isso permite que o usuário tenha uma cópia processada do arquivo para análise posterior.

### 5. **Tratamento de Erros**:

- O projeto inclui mecanismos básicos de tratamento de exceções para garantir a robustez:
    - Caso o usuário tente abrir um arquivo que não seja `.xlsx`, um erro é mostrado na interface.
    - Se houver erros durante o processamento do arquivo, como arquivos não encontrados ou falhas de leitura do Excel, mensagens de erro amigáveis são exibidas para o usuário por meio de caixas de diálogo.

### 6. **Interface Gráfica Amigável e Intuitiva**:

- A interface gráfica construída com `Tkinter` é simples e direta:
    - O usuário clica em um botão para selecionar o arquivo.
    - O resultado do processamento é exibido em uma caixa de texto com rolagem, facilitando a visualização.
    - Ao final do processamento, uma **mensagem de sucesso** é exibida, informando ao usuário que o arquivo processado foi salvo.
