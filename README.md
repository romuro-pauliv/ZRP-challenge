# ZRP Challenge

LLM Chatbot para marketplace utilizando a API da OpenAI com o modelo `gpt-3.0-turbo-0125`.

---

1. [Instalação](/docs/installation.md)
2. [Utilizando Markplace LLM](/docs/using_the_model.md)
   1. [run API](/docs/using_the_model.md#marketplace-api)
   2. [Terminal Chat](/docs/using_the_model.md#terminal-chat)
   3. [Funcionalidades](/docs/using_the_model.md#funcionalidades) 
3. [Diagrama de Arquitetura](/docs/diagrams.md)
   1. [tool_calls functions](/docs/diagrams.md#arquitetura-e-desenvolvimento)
   2. [Modifique funções da sua forma](/docs/diagrams.md#configurando-à-sua-maneira)
   3. [Dados e pedidos de clientes](/docs/diagrams.md#dados-de-clientes)
   4. [Live update system](/docs/diagrams.md#live-update-system)
   5. [Regras de negócio](/docs/diagrams.md#regras-de-negócio)
4. [Melhorias e justificativas](/docs/improvements.md)
   1. [Escolha do modelo](/docs/improvements.md#por-que-escolher-gpt-30-turbo-0125)
   2. [Pontos de melhoria](/docs/improvements.md#pontos-de-melhoria)

---

## Demonstração
Uma pequena demonstração de como o chatbot funciona usando o `Terminal Chat`.

<img src="demo.gif" alt="drawing" width="500"/>

### Panorama Geral

O modelo foi baseado no `gpt-3.0-turbo-0125` devido à sua capacidade de paralelizar respostas das `tool_calls`. O desempenho do modelo é satisfatório em conversas simples, onde os dados do cliente e pedidos são fornecidos de forma clara. Em conversas mais complexas, ele ainda consegue obter os dados necessários e processar os pedidos, embora com alguma dificuldade.

Para mais informações, acesse os links acima relacionados a cada tópico de seu interesse.

Um abraço a todos da ZRP e agradeço pela oportunidade!
