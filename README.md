# Projeto Formulário Web com Banco de Dados - Containers Docker

## Descrição

Este projeto demonstra a criação de um aplicativo web simples usando Flask e PostgreSQL, encapsulado em containers Docker. O objetivo é apresentar os conceitos básicos de containers e como eles podem ser utilizados para desenvolver e implantar aplicações de forma eficiente e escalável.

## Funcionalidade da Aplicação

A aplicação web trata-se de um formulário simples em HTML e Flask que armazena os dados em um banco de dados PostgreSQL.

## Componentes Docker

- **app-flask:** Contém o código da aplicação Flask.
- **banco-de-dados:** Contém o servidor PostgreSQL.

## Uso e Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/angelicasalvino/projeto-final-conteiner-docker-ada.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd projeto-final-conteiner-docker-ada
    ```

3. Construa as imagens Docker:
    ```bash
    docker-compose build
    ```

4. Inicie os containers:
    ```bash
    docker-compose up
    ```

5. Acesse a aplicação web em seu navegador:
    ```
    http://localhost:5000
    ```

## Detalhes Adicionais

- O arquivo `docker-compose.yml` define os containers e suas configurações.
- O arquivo `requirements.txt` lista as dependências da aplicação Flask.
- O script `app.py` implementa a lógica da aplicação web.
- O banco de dados PostgreSQL é configurado para usar autenticação por senha.

## Docker Compose, Volumes e Redes

- O arquivo `docker-compose.yml` utiliza o Docker Compose para definir e gerenciar os containers da aplicação.
- **Volumes:** Os volumes armazenam dados entre reinicializações dos containers sem que esses sejam perdidos. Neste projeto, o volume `postgres_data` armazena os dados do banco de dados PostgreSQL.
- **Redes:** As redes permitem que os containers se comuniquem entre si. A rede `projeto-network` é criada para que os containers `app-flask` e `banco-de-dados` possam se comunicar.

## Recursos Adicionais

- [Documentação do Docker](https://docs.docker.com/)
- [Documentação do Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/current/)

## Observações

- Este projeto é apenas um exemplo simples para fins didáticos e para entrega final do projeto do curso de conteinerização.
- Em projetos reais, é recomendável usar práticas de segurança mais robustas, como autenticação e criptografia de dados.
- O Docker Hub oferece recursos para gerenciar e distribuir imagens Docker: [Docker Hub](https://hub.docker.com/)

## Images no Docker Hub

As imagens deste projeto estão disponíveis no Docker Hub: [Docker Hub](https://hub.docker.com/repository/docker/angelicasalvino/projeto-final-conteiner-docker-ada/general)

## Contribuições

Sinta-se à vontade para contribuir com este projeto! Envie suas sugestões e pull requests para o repositório GitHub.

## License

Este projeto está licenciado sob a licença MIT.
