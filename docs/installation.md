# Instalação

> O modelo foi desenvolvido e testado apenas em `Ubuntu/Fedora`. Pode haver instabilidades em outros ambientes.

1. Clone o repositório com `git clone https://github.com/romuro-pauliv/ZRP-challenge.git`
2. Acesse o diretório do projeto com `cd ZRP-challenge`
3. Crie um ambiente virtual de desenvolvimento com `python3 -m venv venv`
4. Ative o ambiente virtual com `source venv/bin/activate`
5. Instale as dependências com `pip install --no-cache-dir -r requirements.txt`
6. Crie um arquivo `.env` com sua chave de API da OpenAI: `echo "OPENAI_API_KEY=[sua API KEY da OpenAI]" > .env`

Após isso, inicialize a API com o seguinte comando:

```bash
flask --app app --debug run --port=5000
```

Com a API inicializada, em outro terminal, você poderá utilizar o LLM Marketplace com o `Terminal Chat`, facilitando o teste do modelo antes de prosseguir com a utilização da API.
