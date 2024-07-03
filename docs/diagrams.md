# Arquitetura e Desenvolvimento

O modelo foi desenvolvido utilizando a funcionalidade `tool_call`, que permite ao modelo criar respostas chamando funções preestabelecidas na API da OpenAI quando necessário.

```mermaid
sequenceDiagram
participant User
participant GPT API
participant get_products()

Note Right of GPT API: Definição da tool_call para a função get_products()
User ->> GPT API: Preciso de uma TV...
activate GPT API
GPT API -->> GPT API: Chamada da tool_call
GPT API ->> get_products(): "smart TVs"
get_products() ->> GPT API: ["SmartTV 55p 4k", "TV 32p full HD"]
GPT API -->> GPT API: Processamento da resposta de get_products()
deactivate GPT API
GPT API ->> User: Temos a SmartTV 55p e uma TV 32p ...
```

Dessa forma, o modelo pode obter os dados necessários quando achar oportuno. Uma das funcionalidades disponíveis no modelo `gpt-3.0-turbo-0125` é a capacidade de paralelizar as respostas das tool_calls, como demonstrado abaixo:

```mermaid
sequenceDiagram
participant User
participant GPT API
participant get_products()
participant store_fullname()

Note Right of GPT API: Definição da tool_call para get_products()
Note Right of GPT API: Definição da tool_call para store_fullname()

User ->> GPT API: Olá, meu nome é X. Preciso de uma A...
activate GPT API

GPT API -->> GPT API: Chamada da tool_call fullname
GPT API -->> GPT API: Chamada da tool_call products

GPT API ->> store_fullname(): fullname "X"
store_fullname() ->> GPT API: "OK"
GPT API ->> get_products(): "A"
get_products() ->> GPT API: produtos a, b e c

GPT API -->> GPT API: Processamento das respostas
deactivate GPT API
GPT API ->> User: Olá X, nós temos a b e c
```

## Configurando à Sua Maneira

Você pode melhorar a obtenção de dados modificando as configurações das funções das tool_calls. Acesse [gpt_functions.json](/app/json/gpt_functions.json) e faça suas próprias modificações para melhorar os resultados do modelo. Dessa forma, você pode definir como e quando as tool_calls serão chamadas.

```json
{
    "type": "function",
    "function": {
        "name": "get_products",
        "description": "Obter os produtos que o cliente pode se interessar",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": [],
                    "description": "Categorias de produtos que o cliente está buscando ou é viável recomendar, ex.: laptops, smartwatch. Somente recomende produtos se a resposta dessa função for válida, caso não, não recomende ou aceite vender outros produtos"
                }
            },
            "required": ["category"]
        }
    }
}
```

Acima temos a configuração da função `get_products()`. No campo `enum`, a aplicação atualizará as categorias disponíveis para venda. Dessa forma, podemos buscar os produtos da categoria quando a função for ativada.

## Regras de Negócio

As regras de negócio são definidas no início de cada chat. Você pode adicionar ou modificar as regras alterando o arquivo [init_chat_system.json](/app/json/init_chat_system.json).

## Dados de Clientes

Os dados dos clientes e seus pedidos são armazenados no arquivo [orders.json](/app/json/orders.json). Esse arquivo permite verificar se o modelo está captando e armazenando os dados corretamente.

## Live Update System

É possível atualizar os produtos oferecidos sem a necessidade de atualizar o modelo. Isso é feito atualizando as configurações das tool_calls quando um novo produto ou categoria é adicionado. Consulte a classe [GPTFunctions](/app/model/functions/read_functions.py) para mais informações.