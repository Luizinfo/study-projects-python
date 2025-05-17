# AWS Textract Project

Este projeto utiliza o AWS Textract para extrair texto de documentos.

## Criador

- Luiz Antonio

## Dependências

O projeto utiliza as seguintes dependências principais:

- `boto3>=1.38.18`
- `python>=3.13`

Você pode encontrar a lista completa de dependências no arquivo [pyproject.toml](pyproject.toml).

## Como Executar

1.  **Configure suas credenciais da AWS:**
    Certifique-se de que suas credenciais da AWS estejam configuradas corretamente no seu ambiente para que o `boto3` possa interagir com os serviços da AWS. Isso geralmente é feito configurando o AWS CLI ou definindo variáveis de ambiente (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_DEFAULT_REGION`).

2.  **Instale as dependências:**
    Navegue até o diretório do projeto `projects/aws-textract` e instale as dependências. Se você estiver usando `uv` (conforme indicado pelo `uv.lock`):
    ```sh
    uv pip install -r requirements.txt 
    ```
    Ou, se você gerou um `requirements.txt` a partir do `pyproject.toml`:
    ```sh
    pip install -r requirements.txt
    ```
    Caso contrário, você pode instalar diretamente usando `uv` e o `pyproject.toml`:
    ```sh
    uv pip install .
    ```

3.  **Execute o script principal:**
    O script [main.py](main.py) pode ser executado diretamente.
    ```sh
    python main.py
    ```
    Na primeira execução, ele chamará a API do AWS Textract para analisar a imagem `imagens/lista-material-escolar.jpeg` e salvará a resposta em `response.json` na raiz do projeto. Nas execuções subsequentes, se `response.json` existir e não estiver vazio, ele carregará os dados desse arquivo em vez de chamar a API novamente.

    O script imprimirá as linhas de texto detectadas no console.

## Estrutura do Projeto

```
.
├── .python-version
├── imagens/
│   └── lista-material-escolar.jpeg
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```
-   **main.py**: Script principal que interage com o AWS Textract e processa a resposta.
-   **imagens/**: Diretório contendo as imagens a serem analisadas.
-   **pyproject.toml**: Arquivo de configuração do projeto, incluindo dependências.
-   **response.json**: Arquivo gerado (na raiz do workspace) com a resposta da API do AWS Textract (se o script for executado a partir do diretório `projects/aws-textract`, o arquivo `response.json` será criado em `projects/aws-textract/response.json`. O script atual o cria em `c:\Projetos\Python\study-projects-python\response.json`).

## Observações
- O script [main.py](main.py) atualmente salva o arquivo `response.json` na raiz do workspace (`c:\Projetos\Python\study-projects-python\response.json`). Se desejar que ele seja salvo dentro do diretório do projeto `aws-textract`, você precisará ajustar o caminho no script.