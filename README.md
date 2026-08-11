# Sistema de Gerenciamento de Pousada

Sistema web desenvolvido com **Python e Django** como projeto prático durante um curso de Django.

O projeto simula o gerenciamento de uma pousada, permitindo organizar informações relacionadas a hóspedes, quartos e reservas, além de trabalhar com diferentes níveis de acesso ao sistema.

O desenvolvimento teve como objetivo aplicar, na prática, conceitos de desenvolvimento web com Django, modelagem de dados, persistência de informações, formulários, autenticação e controle de acesso.

---

## Sobre o projeto:

A aplicação foi desenvolvida para auxiliar no gerenciamento das principais informações de uma pousada.

O sistema é estruturado em módulos responsáveis pelo gerenciamento de:

- Hóspedes
- Quartos
- Reservas
- Usuários

Também foram definidos dois tipos de usuário:

- **Administrador da pousada:** possui acesso mais amplo às funcionalidades do sistema.
- **Recepcionista:** possui acesso mais limitado, de acordo com as permissões definidas na aplicação.

O projeto foi desenvolvido para fins de aprendizagem e prática dos conceitos estudados durante um curso de Django.

---

## Funcionalidades

Entre as funcionalidades implementadas no sistema estão:

- Cadastro de reservas
- Listagem das reservas cadastradas
- Associação de reservas a hóspedes
- Associação de reservas a quartos
- Registro das datas de entrada e saída
- Controle do status das reservas
- Persistência das informações em banco de dados
- Gerenciamento de usuários
- Diferentes níveis de acesso ao sistema

### Status das reservas

As reservas podem assumir os seguintes estados:

- **Reservada**
- **Hospedada**
- **Finalizada**
- **Cancelada**

### Tipos de usuário

O sistema possui diferentes níveis de acesso:

**Administrador**
- Possui acesso mais amplo às funcionalidades administrativas do sistema.

**Recepcionista**
- Possui acesso limitado às funcionalidades permitidas para esse perfil.

> As permissões são utilizadas para restringir o acesso a determinadas funcionalidades de acordo com o tipo de usuário.

---

## Tecnologias utilizadas

- **Python**
- **Venv**
- **Django**
- **HTML**
- **SQLite**
- **Django ORM**

---

## Conceitos praticados

Durante o desenvolvimento do projeto foram trabalhados conceitos como:

- Estrutura e organização de projetos Django
- Models
- Views
- Forms
- Templates
- Django ORM
- Modelagem de dados
- Chaves estrangeiras (`ForeignKey`)
- Relacionamento entre entidades
- Validação de formulários
- Persistência de dados
- Autenticação e controle de acesso
- Diferentes níveis de permissão entre usuários
- Rotas e navegação entre páginas
- Separação da aplicação em diferentes módulos

---

## Estrutura do projeto

O sistema foi organizado em diferentes aplicações Django, separando as responsabilidades de cada parte da aplicação.

```text
sistema-gerenciamento-pousada/
│
├── hospedes/       # Gerenciamento de hóspedes
├── quartos/        # Gerenciamento de quartos
├── reservas/       # Gerenciamento de reservas
├── usuários/       # Gerenciamento de usuários e acessos
├── CM_Pousada/     # Configurações principais do projeto Django
├── db.sqlite3      # Banco de dados local
└── gerenciar.py    # Gerenciamento da aplicação Django
