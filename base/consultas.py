from sqlalchemy import select

from models import Autor, Livro

def _exibir_livros(livros):
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} ({livro.ano}) | Autor: {livro.autor.nome} | Status: {status}")
    return livros


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    stmt = select(Livro).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()
    return _exibir_livros(livros)


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    stmt = select(Livro).where(Livro.disponivel.is_(True)).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()
    return _exibir_livros(livros)


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    stmt = select(Livro).where(Livro.titulo.ilike(f"%{trecho}%")).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()
    return _exibir_livros(livros)


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    stmt = select(Autor).where(Autor.nome.ilike(f"%{nome_autor}%"))
    autor = session.execute(stmt).scalars().first()

    if autor is None:
        print(f"Nenhum autor encontrado para: {nome_autor}")
        return []

