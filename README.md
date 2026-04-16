# Flix API

Uma API RESTful para gerenciamento de filmes, atores, gêneros e avaliações, desenvolvida com Django e Django REST Framework.

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Virtualenv ou venv

## 🚀 Instalação

### 1. Clonar ou baixar o projeto
```bash
cd caminho/do/projeto
```

### 2. Criar e ativar ambiente virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar migrações do banco de dados
```bash
python manage.py migrate
```

### 5. Criar superusuário (admin)
```bash
python manage.py createsuperuser
```
Siga as instruções e preencha as informações solicitadas.

### 6. Importar dados de atores (opcional)
O projeto inclui um arquivo `actors.csv` com dados fictícios de atores para testes.

Para importar os atores no banco de dados:
```bash
python manage.py import_actors actors.csv
```

Este comando criará 25 atores no banco de dados.

### 7. Executar o servidor de desenvolvimento
```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`

## 📁 Estrutura do Projeto

```
flix-api/
├── actors/              # Aplicação de atores
│   ├── models.py        # Modelo de ator
│   ├── serializers.py   # Serializadores
│   ├── views.py         # Views da API
│   ├── urls.py          # Rotas de atores
│   └── management/      # Comandos personalizados
│       └── commands/
│           └── import_actors.py  # Comando para importar atores do CSV
├── genres/              # Aplicação de gêneros
│   ├── models.py        # Modelo de gênero
│   ├── serializers.py   # Serializadores
│   ├── views.py         # Views da API
│   └── urls.py          # Rotas de gêneros
├── movies/              # Aplicação de filmes
│   ├── models.py        # Modelo de filme
│   ├── serializers.py   # Serializadores
│   ├── views.py         # Views da API
│   └── urls.py          # Rotas de filmes
├── reviews/             # Aplicação de avaliações
│   ├── models.py        # Modelo de avaliação
│   ├── serializers.py   # Serializadores
│   ├── views.py         # Views da API
│   └── urls.py          # Rotas de avaliações
├── app/                 # Configuração principal do projeto
│   ├── settings.py      # Configurações do Django
│   ├── urls.py          # Rotas principais
│   └── wsgi.py          # Configuração WSGI
├── manage.py            # Utilitário de gerenciamento do Django
├── requirements.txt     # Dependências do projeto
└── actors.csv           # Dados fictícios de atores para importação
```

## 🔧 Dependências

- **Django** (6.0.3) - Framework web
- **Django REST Framework** (3.16.1) - Framework para criar APIs REST
- **sqlparse** (0.5.5) - Utilitário para parsing de SQL
- **asgiref** (3.11.1) - Suporte ASGI para Django

## 📚 Modelos de Dados

### Actor (Ator)
- `name`: Nome do ator (CharField)
- `birthday`: Data de nascimento (DateField - opcional)
- `nationality`: Nacionalidade (CharField com opções predefinidas - opcional)

### Genre (Gênero)
- `name`: Nome do gênero (CharField)

### Movie (Filme)
- `title`: Título do filme (CharField)
- `genre`: Gênero do filme (ForeignKey para Genre)
- `release_date`: Data de lançamento (DateField)
- `actors`: Atores do filme (ManyToManyField para Actor)
- `resume`: Sinopse do filme (TextField - opcional)

### Review (Avaliação)
- `movie`: Filme avaliado (ForeignKey para Movie)
- `stars`: Avaliação em estrelas (IntegerField - de 0 a 5)
- `comment`: Comentário sobre o filme (TextField - opcional)

## 🌐 API Endpoints

### Atores
- `GET /actors/` - Listar todos os atores
- `POST /actors/` - Criar novo ator
- `GET /actors/{id}/` - Obter detalhes de um ator
- `PUT /actors/{id}/` - Atualizar um ator
- `DELETE /actors/{id}/` - Deletar um ator

### Gêneros
- `GET /genres/` - Listar todos os gêneros
- `POST /genres/` - Criar novo gênero
- `GET /genres/{id}/` - Obter detalhes de um gênero
- `PUT /genres/{id}/` - Atualizar um gênero
- `DELETE /genres/{id}/` - Deletar um gênero

### Filmes
- `GET /movies/` - Listar todos os filmes
- `POST /movies/` - Criar novo filme
- `GET /movies/{id}/` - Obter detalhes de um filme
- `PUT /movies/{id}/` - Atualizar um filme
- `DELETE /movies/{id}/` - Deletar um filme

### Avaliações
- `GET /reviews/` - Listar todas as avaliações
- `POST /reviews/` - Criar nova avaliação
- `GET /reviews/{id}/` - Obter detalhes de uma avaliação
- `PUT /reviews/{id}/` - Atualizar uma avaliação
- `DELETE /reviews/{id}/` - Deletar uma avaliação

## 👤 Acesso à Administração

Após criar o superusuário, acesse o painel administrativo em:

```
http://127.0.0.1:8000/admin/
```

Use as credenciais criadas durante o `createsuperuser`.

## 📝 Exemplos de Uso

### Criar um novo gênero
```bash
curl -X POST http://127.0.0.1:8000/genres/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Ação"}'
```

### Criar um novo ator
```bash
curl -X POST http://127.0.0.1:8000/actors/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tom Cruise",
    "birthday": "1962-12-03",
    "nationality": "USA"
  }'
```

### Criar um novo filme
```bash
curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mission Impossible",
    "genre": 1,
    "release_date": "1996-05-22",
    "actors": [1],
    "resume": "Um agente secreto tenta salvar seu colega."
  }'
```

### Criar uma avaliação
```bash
curl -X POST http://127.0.0.1:8000/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "movie": 1,
    "stars": 5,
    "comment": "Filme excelente!"
  }'
```

## 🛠️ Comandos Úteis do Django

```bash
# Criar novas migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell interativo do Django
python manage.py shell

# Executar testes
python manage.py test

# Importar atores de um arquivo CSV
python manage.py import_actors <caminho_do_arquivo>
```

## 📥 Importação de Dados

### Importar Atores

Você pode importar dados de atores a partir de um arquivo CSV usando o comando personalizado `import_actors`:

```bash
python manage.py import_actors actors.csv
```

**Formato do arquivo CSV:**

O arquivo CSV deve conter as seguintes colunas:
- `name`: Nome do ator (obrigatório)
- `birthday`: Data de nascimento no formato YYYY-MM-DD (opcional)
- `nationality`: Sigla do país em caixa alta (opcional)

Exemplo:
```csv
name,birthday,nationality
Tom Hanks,1956-07-09,US
Meryl Streep,1949-06-22,US
Leonardo DiCaprio,1974-11-11,US
```

O projeto já inclui um arquivo `actors.csv` com 25 atores fictícios para testes.

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido como parte do curso Django Master.

---

**Nota**: Este é um projeto em desenvolvimento. Consulte as anotações do projeto para obter informações adicionais sobre o desenvolvimento.
