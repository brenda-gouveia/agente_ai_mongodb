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

A API possui três endpoints principais:

* **GET /products** – retorna lista de produtos
* **GET /customers** – retorna lista de clientes
* **GET /orders** – retorna pedidos disponíveis

Cada rota retorna um JSON estruturado. Exemplos estão no diretório `/api` do projeto.

---

## 📌 4. Expondo localmente a API com Ngrok

Para que o Azure consiga acessar a API local, foi utilizado o **Ngrok**, que gera uma URL pública temporária.

### Passos:

1. Instalar o Ngrok 
2. Executar:

```
ngrok http 8000
```

3. Capturar a URL gerada, exemplo:

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
* `operationId` únicos para permitir chamada do agente

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

---

## 📌 7. Testes no Playground

No **Playground do Azure AI**, o agente foi testado com perguntas como:

* "Liste todos os produtos disponíveis"
* "Quais clientes estão cadastrados?"
* "Mostre os pedidos realizados"

O agente identificou automaticamente as ações corretas e fez as chamadas HTTP usando a Action.

---
## 9. Próximos Passos (opcionais)

* Adicionar POST /customers e POST /orders

* Criar interface web (React, Next.js ou Streamlit)

* Criar autenticação por token na API

* Versão interna para admin com mais permissões

### 📌 9.1 Melhorias Futuras

Esta seção apresenta ideias de evolução do projeto, visando aumentar robustez, segurança, usabilidade e escalabilidade.

#### 🔒 Segurança e Governança

* Implementar autenticação JWT na API

* Criar níveis de permissão para diferentes tipos de usuários

* Registrar logs de auditoria das ações do agente

* Configurar rate limits no backend

##### 🚀 Desempenho e Escalabilidade

* Migrar a API para um ambiente cloud (Azure Web Apps ou Container Apps)

* Monitoramento com Application Insights

* Cache de respostas para consultas repetidas


#### 🔧 Evolução do Agente IA

Adicionar contexto avançado via memória

* Criar ações mais complexas, como filtros por categoria, país ou data

* Criar um módulo de "Insights" para resumos automáticos das informações retornadas

#### 🖥️ Interface e Experiência do Usuário

* Criar um dashboard completo em React/Next.js

* Adicionar componentes visuais (gráficos, tabelas dinâmicas)

* Implementar autenticação no front-end e login via Azure AD

#### 📊 Expansão da API

* Adicionar endpoints de criação e atualização de dados com validação

* Criar endpoint para detalhes individuais: /products/{id}, /customers/{id}, /orders/{id}

* Adicionar paginação, ordenação e filtros nativos

* Adicionar POST /customers e POST /orders

* Criar interface web (React, Next.js ou Streamlit)

* Criar autenticação por token na API

* Versão interna para admin com mais permissões
---

## 📌 10. Conclusão

O **TechNow Data Assistant** demonstra como integrar dados empresariais a um agente IA usando apenas:

* Um backend simples
* Um arquivo OpenAPI
* O Azure AI Foundry

Essa abordagem permite que colaboradores consultem dados complexos usando linguagem natural, sem acesso direto ao banco e com total rastreabilidade.
