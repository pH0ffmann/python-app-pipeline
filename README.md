# Aplicação Python Simples com Pipeline CI

Esta aplicação é uma aplicação simples em Python, desenvolvida para rodar e construir uma pipeline de CI/CD utilizando diversas ferramentas de segurança e testes. A principal finalidade é demonstrar a integração de ferramentas de **SAST**, **DAST**, execução de testes unitários com **pytest** e scans de segurança em container com **Trivy**. 

A pipeline está configurada com as seguintes ferramentas de análise:

## Ferramentas de SAST (Static Application Security Testing)
A pipeline utiliza as seguintes ferramentas de **SAST** para análise de segurança estática do código:

- [**Semgrep**](https://semgrep.dev/): Ferramenta de análise de segurança estática para código-fonte.
- [**Safety**](https://pyup.io/safety/): Verifica dependências vulneráveis no projeto.
- [**Bandit**](https://bandit.readthedocs.io/en/latest/): Analisador de segurança estática focado em código Python.

## Ferramentas de DAST (Dynamic Application Security Testing)
A pipeline também integra ferramentas de **DAST** para realizar testes de segurança dinâmicos:

- [**OWASP ZAP**](https://www.zaproxy.org/): Ferramenta de teste de segurança dinâmica para identificar vulnerabilidades em tempo de execução.

## Execução de Testes

A pipeline executa testes unitários utilizando o **pytest**, para garantir que a aplicação está funcionando conforme o esperado antes de rodar as análises de segurança.

## Ferramentas de Container Security ##

- [**Trivy**](https://trivy.dev/latest/): Scanner de segurança para detectar vulnerabilidades em imagens de containers e arquivos de configuração.

## Integração com Discord

No final do processo de CI, a pipeline está configurada para enviar os relatórios das ferramentas de segurança e testes para um canal do **Discord**, garantindo que as equipes possam acompanhar os resultados de maneira prática e em tempo real.

## Estrutura da Pipeline

- **SAST (Semgrep, Safety, Bandit)**: Ferramentas de análise estática para detectar problemas de segurança no código.
- **DAST (OWASP ZAP)**: Ferramenta de teste dinâmico que realiza varreduras de segurança no aplicativo em execução.
- **Testes**: Execução de testes com o **pytest**.
- **Trivy**: Ferramenta de segurança para container.
- **Integração com o Discord**: Envio dos relatórios para o Discord, com o uso de webhooks, após a execução da pipeline.

## Dependências

A aplicação e pipeline utilizam as seguintes dependências:

- **Python**: 3.12 ou superior.
- **Semgrep**
- **Safety**
- **Bandit**
- **OWASP ZAP**
- **Pytest**
- **Trivy**

## Dependências de Chaves

Para que a pipeline funcione corretamente, as seguintes chaves devem ser configuradas nos **Secrets** do GitHub:

- **DISCORD_WEBHOOK**: URL do webhook do Discord para enviar relatórios.
- **SAFETY_API_KEY**: Chave API para utilizar a ferramenta **Safety**.
- **SEMGREP_APP_TOKEN**: Token da aplicação **Semgrep**.

---

<div align="center">
  <strong>Desenvolvido para portfólio por Pablo Hoffmann</strong><br>
  <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWs5dHkybHMya2ExbGoweTZ1NXMzbm1pbjFzeWJ5ZHN5YTkzc212MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HH0YHdOjABrihGvwhk/giphy.webp"/>
</div>

