from sqlalchemy import select

from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    session.query(Livro).delete()
    session.query(Autor).delete()
    session.commit()

    autor_1 = Autor(nome="Machado de Assis", pais="Brasil")
    autor_2 = Autor(nome="George Orwell", pais="Reino Unido")
    autor_3 = Autor(nome="Jane Austen", pais="Reino Unido")

    session.add(autor_1)
    session.add_all([autor_2, autor_3])
    session.commit()

    livros = [
        Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=autor_1, disponivel=True),
        Livro(titulo="Dom Casmurro", ano=1899, autor=autor_1, disponivel=False),
        Livro(titulo="1984", ano=1949, autor=autor_2, disponivel=True),
        Livro(titulo="A Revolução dos Bichos", ano=1945, autor=autor_2, disponivel=False),
        Livro(titulo="Orgulho e Preconceito", ano=1813, autor=autor_3, disponivel=True),
        Livro(titulo="Persuasão", ano=1817, autor=autor_3, disponivel=True),
    ]

    session.add_all(livros)
    session.commit()

    return {"autores": [autor_1, autor_2, autor_3], "livros": livros}
