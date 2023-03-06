Projeto Biblioteca Bates

# biblioteca_bates

1. Crie seu ambiente virtual:

```Git bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/Scripts/activate
```

## Instalação dependencias

**`pip install -r requirements.txt`**

## atualizando as Instalação dependencias

**`pip freeze > requirements.txt`**

## Rota de books sem autenticação

**`GET : /api/books/`** `lista todo os livros `
**`GET : /api/books/<book_id>/`** `lsita um livro em especifico `

## Rota de Books autorizadas somente para is_superuser/ funcionario
