
# CRM - Sistema de Gestão de Relacionamento com o Cliente

Projeto desenvolvido para **Trilha de Backend do NADIC**.

Tem como objetivo demonstrar os conhecimentos em **Django Framework** e **Django REST Framework**, simulando um sistema de CRM simples para qualquer tipo de empresa.

---

## 🚀 Funcionalidades

### 📦 Produtos
- Cadastro, edição, remoção e listagem de produtos.
- Controle de estoque.
- Atualização automática de estoque ao realizar vendas.

### 👥 Clientes
- Cadastro, edição, remoção e listagem de clientes.
- Visualização de detalhes do cliente.

### 🛒 Pedidos
- Registro de vendas (com múltiplos produtos por pedido).
- Detalhes de cada pedido (cliente, data, itens e valor total).
- Exclusão de pedidos.

### 💰 Faturamento
- Cálculo automático de faturamento total da empresa.
- Página de listagem de faturamentos.

### 🔑 Autenticação
- **API**: Autenticação via JWT (SimpleJWT).
- **Frontend (templates Django)**: Autenticação via sessão.
- Grupos de usuários:
  - **Seller (Vendedor)** → pode gerenciar produtos, clientes e pedidos.
  - **Owner (Dono)** → possui todas as permissões de vendedor + acesso ao faturamento.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Django 5.2.5**
- **Django REST Framework**
- **SimpleJWT** para autenticação da API
- **SQLite3**
- **HTML + CSS**

---

## 📂 Estrutura de Pastas

```

crm/
├── accounts/        # Gestão de usuários, grupos e autenticação
│   ├── api/         # Endpoints de signup e login (JWT)
│   └── ...
├── core/            # Regras principais do CRM
│   ├── api/         # Endpoints de produtos e faturamento
│   ├── models.py    # Produtos, Clientes, Pedidos, Revenues
│   ├── views.py     # CBVs e FBVs para templates
│   └── ...
├── templates/       # Templates frontend
│   ├── base.html
│   ├── products/
│   ├── customers/
│   ├── orders/
│   └── revenues/
├── static/          # CSS, JS e assets
└── crm/urls.py      # Rotas principais do projeto

````

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/HianSilva/crm-nadic.git
cd crm-nadic
````

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar migrações

```bash
python manage.py migrate core
python manage.py migrate accounts
```

### 5. Criar superusuário

```bash
python manage.py createsuperuser
```

### 6. Rodar servidor local

```bash
python manage.py runserver
```

---

## 📌 Endpoints principais

### API - Autenticação

* `POST /api/accounts/signup/` → Criar conta (adicionado ao grupo "Seller" por padrão).
* `POST /api/accounts/login/` → Login (JWT).
* `POST /api/accounts/token/refresh/` → Renovar token.

### API - Produtos

* `GET /api/products/` → Listar produtos.
* `POST /api/products/` → Criar produto.
* `PUT /api/products/{id}/` → Editar produto.
* `DELETE /api/products/{id}/` → Remover produto.

### API - Faturamento

* `GET /api/revenues/` → Listar faturamento (apenas Owner).

### Django Templates (frontend)

* `/products/` → Listagem de produtos.
* `/orders/` → Listagem de pedidos.
* `/customers/` → Listagem de clientes.
* `/revenues/` → Faturamento

---

## 👨‍💻 Autor

Projeto desenvolvido por **Hian Silva** como exercício prático proposto pela ***Trilha de Backend do Nadic*** para consolidar e demontrar os conhecimentos em Django e Django REST Framework.

