# Melhorias e Justificações

## Por que escolher `gpt-3.0-turbo-0125`?

O principal motivo para escolher esse modelo foi a capacidade de paralelizar tool_calls em uma única requisição à API. Isso traz dois benefícios principais:
1. Possibilidade de obter múltiplas informações a partir de uma única frase do usuário. Exemplo: _Olá, me chamo Fulano, estou pensando em comprar uma TV._ Com as funções pré-configuradas, a aplicação consegue extrair tanto o nome (Fulano) quanto a categoria de produtos (TVs).
2. Redução da necessidade de múltiplas requisições para processar uma única mensagem, resultando em economia de recursos financeiros (ao usar uma API externa) e otimização do tempo de resposta ao cliente.

## Pontos de Melhoria

Divido os pontos de melhoria em duas partes: melhorias a serem analisadas e melhorias não implementadas devido ao tempo.

### Melhorias Não Implementadas Devido ao Tempo

- **Testes automatizados:** A criação de uma API foi devido a inteção de verificar a coleta correta dos dados dos clientes e a construção adequada dos pedidos.
- **Sanitização das respostas das funções de tool_calls:** Isso previneria a injeção de prompt. Exemplo: _Eu quero produtos da categoria `código malicioso`_, que poderia comprometer a aplicação.
- **Melhoria das descrições das funções de tool_call e regras de negócio:** Descrições inadequadas podem gerar resultados inesperados. Usuários divagantes podem levar a respostas com dados falsos, como nomes, e-mails e números de telefone inventados.
- **Fine-tuning para melhorar a qualidade e o tom das mensagens:** Isso ajudaria a captar melhor os dados do usuário e evitar "delírios" da aplicação.
- **Implementação de uma arquitetura mais limpa e otimizada, focada na performance de processamento das requisições.**
- **Sanitização e tratamento dos endpoints da API.**
- **Documentação mais completa para facilitar a manutenção pela equipe.**
- **Armazenamento de todas as conversas com os clientes para testes futuros e possíveis ajustes baseados em interações bem-sucedidas.**

### Melhorias Possíveis

- **Criação de funções internas de validação dos dados dos usuários para fornecer respostas mais concretas nas tool_calls da API.**
- **Otimização do processamento através da análise das mensagens dos usuários:** Por exemplo, ao identificar um e-mail na mensagem "meu e-mail é test@gmail.com", poderia-se extrair essa informação sem necessitar do processamento pela LLM.
- **Adição de uma segunda etapa de análise de mensagens para evitar "delírios" ou erros em momentos críticos da conversa, como fechamento de pedidos e captação de dados essenciais.**