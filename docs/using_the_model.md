# Utilizando o Modelo

Você pode utilizar o modelo de duas formas: `Terminal Chat` ou diretamente pela API.

## Terminal Chat

Um simples script que faz requisições em loop para a API do modelo, permitindo que você converse com o LLM Marketplace.

Para inicializá-lo:
1. Certifique-se de que você está no ambiente virtual de desenvolvimento: `source venv/bin/activate`
2. Certifique-se de que a API está rodando: `flask --app app --debug run --port=5000`
3. Rode o comando: `python terminal_chat`

## Marketplace API

Para inicializá-la:
1. Certifique-se de que você está no ambiente virtual de desenvolvimento: `source venv/bin/activate`
2. Rode o comando: `flask --app app --debug run --port=5000`

Você pode acessar os endpoints pelo Postman ou criar suas próprias requisições. Abaixo estão os endpoints da API.

| Função                    | Rota                                         | Método | Payload JSON                                               | Info                                                                                                                   |
|---------------------------|----------------------------------------------|--------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ChatBot                   | http://127.0.0.1:5000/chat/                  | `POST` | `{"user_id": "string", "message": "sua mensagem"}`          | `user_id` serve para identificar sua conversa, use qualquer string para identificar seu chat. `message` é a mensagem enviada ao chatbot. |
| Categorias de Produtos    | http://127.0.0.1:5000/products/all_categories| `GET`  | `{}`                                                       | Payload vazio. Retorna todas as categorias de produtos disponíveis.                                                    |
| Produtos                  | http://127.0.0.1:5000/products/all_products  | `GET`  | `{}`                                                       | Payload vazio. Retorna todos os produtos disponíveis no marketplace.                                                   |
| Adicionar Produto         | http://127.0.0.1:5000/products/add_product   | `POST` | `{"category": "string", "product": "object"}`               | Cria um novo produto no marketplace. `category` deve ser o nome da categoria do produto.                               |

Para a rota `Adicionar Produto`, o formato do payload deve seguir o seguinte padrão:

```json
{
    "category": "periféricos",
    "product": {
        "monitor 4K 144hz": {
            "price": "2300",
            "info": "32 polegadas, 144hz, tela OLED"
        }
    }
}
```

PostMan link: [ZRP Challenge](https://teste4-8598.postman.co/workspace/Teste-Workspace~475c561d-4423-4c1d-9c83-a951a88f71e5/collection/24590168-201107cf-d88d-4b90-a045-2ee3c0dd60ad?action=share&creator=24590168)

---

# Funcionalidades

O desenvolvimento do chatbot foi orientado para lidar com demandas de um marketplace real, como mudanças constantes no banco de dados dos produtos. O objetivo foi, além de desenvolver um modelo capaz de utilizar e modificar esses dados, acompanhar o fluxo de alterações dentro do ambiente do marketplace.

As funcionalidades incluem:
1. Buscar produtos de interesse do cliente através de `tool_calls`;
2. Fazer propostas personalizadas com os produtos fornecidos;
3. Obter dados como nome completo, número de telefone, e-mail e forma de pagamento do cliente;
4. Modificar os pedidos do cliente, acrescentando ou removendo produtos conforme necessário;
5. Acompanhar modificações no banco de dados, recomendando novos produtos assim que disponíveis;
6. Armazenar os pedidos com as informações do cliente.

A metodologia utilizada para alcançar esses objetivos será abordada no tópico [Diagrama de Arquitetura](/docs/diagrams.md).