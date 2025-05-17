# AWS Rekognition Project

Este projeto demonstra o uso do AWS Rekognition para análise de imagens, incluindo comparação de faces e reconhecimento de celebridades (funcionalidade pretendida).

## Criador

-   Luiz Antonio

## Dependências

O projeto utiliza as seguintes dependências principais:

-   `boto3`: AWS SDK para Python.
-   `Pillow`: Biblioteca para manipulação de imagens.
-   Python (versão especificada em [.python-version](.python-version))

As dependências do projeto estão listadas no arquivo [pyproject.toml](pyproject.toml).

## Como Executar

1.  **Configure suas credenciais da AWS:**
    Certifique-se de que suas credenciais da AWS estejam configuradas corretamente no seu ambiente para que o `boto3` possa interagir com os serviços da AWS. Isso geralmente é feito configurando o AWS CLI ou definindo variáveis de ambiente (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_DEFAULT_REGION`).

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    # No Windows
    .\.venv\Scripts\activate
    # No macOS/Linux
    # source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    Navegue até o diretório do projeto `projects/aws-rekognition` e instale as dependências:
    ```bash
    # Usando pip com pyproject.toml (requer pip >= 21.1)
    pip install .
    ```
    Ou, se você estiver usando `uv` (conforme sugerido pelo `uv.lock`):
    ```bash
    uv pip install .
    ```
    Alternativamente, instale as bibliotecas individualmente se não estiver usando `pyproject.toml` para instalação direta:
    ```bash
    pip install boto3 Pillow
    ```

4.  **Execute os scripts:**

    *   **Comparar Faces (`compare_faces.py`):**
        Este script compara faces entre duas imagens locais.
        ```bash
        python compare_faces.py
        ```
        -   Ele utiliza as imagens `imagens/luiz.jpg` (origem) e `imagens/foto1.jpg` (alvo) por padrão.
        -   Se faces correspondentes forem encontradas, ele imprime a similaridade e desenha caixas delimitadoras na imagem alvo, salvando o resultado em `imagens/output.jpg`.

    *   **Reconhecer Celebridades (`recognize_celebrities.py`):**
        Este script utiliza o AWS Rekognition para identificar celebridades em uma imagem.
        ```bash
        python recognize_celebrities.py
        ```
        -   Ele utiliza a imagem `imagens/emicida.png` por padrão.
        -   Se celebridades forem encontradas, ele imprime os nomes e a confiança da correspondência.
        -   Ele também desenha caixas delimitadoras ao redor das faces das celebridades e salva a imagem resultante em `imagens/output2.png`.

## Estrutura do Projeto

```
.
├── .python-version         # Especificação da versão do Python
├── compare_faces.py        # Script para comparar faces
├── imagens/                # Diretório de imagens
│   ├── emicida.png
│   ├── foto1.jpg
│   ├── luiz.jpg
│   ├── output.jpg          # Imagem de saída da comparação de faces
│   └── output2.png         # Outra imagem de saída (se usada)
├── pyproject.toml          # Arquivo de configuração do projeto e dependências
├── README.md               # Este arquivo
├── recognize_celebrities.py # Script para reconhecimento de celebridades
└── uv.lock                 # Arquivo de lock para o gerenciador de pacotes uv
```

-   **[compare_faces.py](compare_faces.py)**: Script para comparar faces em imagens locais.
-   **[recognize_celebrities.py](recognize_celebrities.py)**: Script para identificar celebridades em uma imagem.
-   **[imagens/](imagens/)**: Contém as imagens de entrada e saída.
-   **[pyproject.toml](pyproject.toml)**: Define metadados do projeto e dependências.