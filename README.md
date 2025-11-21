# Case TechNow Data Assistant : Visão Geral

A **TechNow** é uma loja de eletrônicos online especializada em produtos de tecnologia como smartphones, notebooks, acessórios, peças de hardware e gadgets em geral. Toda a operação da empresa depende de três conjuntos principais de dados:

* **Produtos**
* **Clientes**
* **Pedidos**

Com o crescimento da equipe e a necessidade de agilizar consultas internas, a TechNow decidiu criar um **Agente de IA** integrado à sua **API própria**, permitindo que colaboradores consultem dados usando **linguagem natural**, de forma segura e sem acesso direto ao banco.

Este README documenta todas as etapas da construção do projeto, desde a estruturação da API até a configuração da Action no Azure AI Foundry.

---

## 📌 1. Objetivo do Projeto

O objetivo foi desenvolver um agente IA capaz de:

* Consultar produtos, clientes e pedidos usando linguagem natural.
* Acessar uma API REST usando **especificação OpenAPI 3.0**.
* Facilitar o trabalho de equipes não técnicas.

---

## 📌 2. Arquitetura Geral

A solução envolve:

1. **Backend (API REST) + Ngrok**
2. **Arquivo OpenAPI em JSON** descritivo dos endpoints
3. **Agente IA no Azure AI Foundry** com integração via Action
4. **Interface de teste no Playground**

Fluxo:

```
Usuário → Agente IA → Action (OpenAPI) → API (Ngrok) → Resposta
```

---


## 📌 3. Desenvolvimento da API

A API foi desenvolvida utilizando o **FastAPI**, framework Python moderno, rápido e eficiente para construir APIs RESTful. O FastAPI facilita a definição de rotas, tratamento de requisições HTTP e a documentação automática dos endpoints via Swagger/OpenAPI.

Após estruturar as rotas principais, foi implementada **a conexão com o MongoDB Atlas**, serviço de banco de dados NoSQL totalmente gerenciado na nuvem. Para integrar o FastAPI ao MongoDB Atlas, foi utilizada a biblioteca `pymongo` (ou `motor` para operações assíncronas). Isso permitiu que produtos, clientes e pedidos fossem consultados diretamente na coleção correspondente do banco de dados online, garantindo escalabilidade e acesso remoto seguro.

A API possui três endpoints principais:

* **GET /products** – retorna lista de produtos consultando o MongoDB Atlas
* **GET /customers** – retorna lista de clientes consultando o MongoDB Atlas
* **GET /orders** – retorna pedidos disponíveis consultando o MongoDB Atlas

Cada rota retorna um JSON estruturado. Exemplos estão no diretório `/openapi` do projeto.


---

## 📌 4. Expondo localmente a API com Ngrok

Para que o Azure consiga acessar a API local, foi utilizado o **Ngrok**, que gera uma URL pública temporária. Para utiliza-lo é necessário criar uma conta no seu site: https://ngrok.com/

### Passos:

1. Instalar o Ngrok
2. Digitar o seguinte comando no prompt
   <p align="center">
<img 
    src="./assets/2025-11-20 221641.png"
    width="800"
/>
</p>

3. Executar:

```
ngrok http 8000
```

4. Capturar a URL gerada, exemplo:

```
https://seu-endereco.ngrok-free.dev
```

Essa URL foi usada no servidor da especificação OpenAPI.

---

## 📌 5. Construção da Especificação OpenAPI

O Azure AI Foundry **não aceita YAML diretamente**, então a especificação foi convertida para **JSON**. A versão final inclui:

* `GET /products`
* `GET /customers`
* `GET /orders`
* Schemas de `Product`, `Customer` e `Order`
  
<p align="center">
<img 
    src="./assets/2025-11-20 215911.png"
    width="800"
/>
</p>  

O arquivo final está disponível em:

```
/openapi/openapi.json
```


---

## 📌 6. Criando a Action no Azure AI Foundry

Passos realizados:

1. Acessar **Azure AI Foundry** → *Agents*
2. Criar um novo agente
3. Ir para a aba **Actions**
4. Selecionar **Add Action → Create from OpenAPI specification**
5. Colar o arquivo JSON da API
6. Validar e concluir

Após isso, o agente passa a reconhecer:

* Products
* Customers
* Orders

E consegue chamar a API automaticamente.

<p align="left">
<img 
    src="./assets/2025-11-20 211527.png"
    width="300"
/>
<img 
    src="./assets/2025-11-20 211619.png"
    width="400"
/>
</p>
 

---

## 📌 7. Testes no Playground

No **Playground do Azure AI**, o agente foi testado com perguntas como:

* "Quais clientes estão cadastrados?"
* "Mostre os pedidos realizados"

O agente identificou automaticamente as ações corretas e fez as chamadas HTTP usando a Action.

<p align="center">
<img 
    src="./assets/2025-11-20 212338.png"
    width="700"
/>
</p>

<p align="center">
<img 
    src="./assets/2025-11-20 213054.png"
    width="700"
/>
</p>

<p align="center">
<img 
    src="./assets/2025-11-20 214043.png"
    width="700"
/>
</p>

Para mais exemplos do agente, clique [aqui](/assets)

---

## ✅ 8. Melhorias Futuras (opcionais)

A seguir estão evoluções planejadas que poderiam tornar o projeto mais robusto, seguro, eficiente e escalável. Elas não são obrigatórias, mas demonstram caminhos reais de crescimento da solução.

### 🔒 Segurança e Governança

* Implementar autenticação JWT na API

* Criar níveis de permissão (admin, leitura, operador)

* Registrar logs de auditoria das ações executadas pelo agente

* Adicionar rate limits por IP/usuário

* Criar versão interna da API (endpoints mais permissivos para admin)

* Implementar CORS mais restritivo

* Sanitização e validação mais rígida de parâmetros de entrada

* Prevenir pipelines perigosos ($out, $merge, $function, etc.)

* Auditoria e rastreamento de consultas feitas pelo agente

### 🚀 Desempenho e Escalabilidade

* Migrar API para cloud (Azure Web Apps ou Container Apps)

* Utilizar containers com CI/CD automatizado

* Configurar monitoramento com Azure Application Insights

* Implementar cache de resultados (Redis) para consultas repetidas

* Adicionar paginação nativa em todos os endpoints

* Usar índices otimizados no MongoDB (compound, TTL, text, etc.)

* Versionamento da API (v1, v2…)

### 🤖 Evolução do Agente IA

* Criar contexto avançado com memória para melhorar consultas

* Adicionar ações complexas (buscas filtradas, recomendações, análises)

* Implementar um módulo de Insights Automáticos (sumários, tendências, estatísticas)

* Criar actions especializadas para análises do tipo “top produtos”, “melhores clientes”, etc.

* Permitir o envio de pipelines com validação segura

* Adicionar detecção de intent (ex.: usuário pede algo que envolve duas coleções → lookup automático)

### 🖥️ Interface e Experiência do Usuário

* Desenvolver dashboard em React ou Next.js

* Criar visualizações (gráficos, tabelas interativas, cards de métricas)

* Implementar autenticação no front-end (Azure AD, OAuth ou JWT)

* Criar home com estatísticas gerais do banco

* Interface para execução manual das consultas do agente

* Criar fluxo CRUD completo pelo front-end

### 📊 Expansão da API

* Adicionar endpoints de criação e atualização com validação

* Criar endpoints individuais:
  * /products/{id}
  * /customers/{id}
  * /orders/{id}

* Implementar paginação, ordenação e filtros nativos

* Adicionar POST /customers e POST /orders

* Criar endpoint seguro para executar pipelines pré-validadas

* Criar endpoints administrativos para manutenção do banco

* Melhorar padronização de erros (HTTPException + JSON estruturado)
---
## 🧩 9. Limitações Atuais (transparência técnica)

Esta seção descreve limitações conhecidas do projeto atual. Elas não impedem o funcionamento, mas indicam pontos a serem evoluídos futuramente.

### 📌 1. Endpoints retornam coleções inteiras
Atualmente, os endpoints /products, /customers e /orders retornam todos os documentos.
Isso causa limitações:

* maior consumo de rede

* o agente precisa analisar tudo manualmente

* consultas como “top 5 marcas” ficam mais lentas

* sem paginação e sem filtros

### 📌 2. Falta de validação robusta de entrada (sem Pydantic)

Sem Pydantic, a API não valida:

* tipos de dados

* formatos inválidos

* parâmetros faltando

Isso torna a API funcional, porém menos segura.

### 📌 3. O Agente está limitado a dados brutos

Por só possuir endpoints de leitura simples:

* não consegue executar agregações reais

* não consegue fazer cálculos complexos direto do banco

* precisa inferir o resultado analisando JSON

* consultas que exigem GROUP BY ou JOIN são restritas

### 📌 4. Ausência de autenticação e controle de acesso

A API está aberta (por simplicidade).
Isso é comum em trabalhos acadêmicos, mas não ideal para produção.

### 📌 5. Falta de paginação, ordenação e filtros nativos

Sem esses recursos:

* cargas muito grandes podem reduzir performance

* processamento fica no lado do cliente ou do agente

### 📌 6. Sem camada de cache ou otimizações de banco

O MongoDB está sendo usado de forma básica:

* sem índices específicos

* sem cache

* sem análise de plano de consulta

### 📌 7. O Agente não possui contexto persistente

O agente é estateless, então:

* não lembra interações anteriores

* não pode manter estado de navegação

---
## 📌 10. Conclusão

O **TechNow Data Assistant** demonstra como integrar dados empresariais a um agente IA usando apenas:

* Um backend simples
* Um arquivo OpenAPI
* O Azure AI Foundry

Essa abordagem permite que colaboradores consultem dados complexos usando linguagem natural, sem acesso direto ao banco e com total rastreabilidade.

## 📬 Contato

Você pode me encontrar nas seguintes plataformas:

[![GitHub](https://img.shields.io/badge/GitHub-%23000000.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/brenda-gouveia)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brenda-gomes-gouveia)
[![Email](https://img.shields.io/badge/Email-%23D14836.svg?style=for-the-badge&logo=gmail&logoColor=white)](mailto:brendaggouveia@gmail.com)

---
## Referencias
* **AI Foundry** https://aka.ms/azureaifoundry
* **Ngrok** https://ngrok.com/
* **MongoDB Atlas** https://www.mongodb.com/atlas
* **FastAPI** https://fastapi.tiangolo.com/

