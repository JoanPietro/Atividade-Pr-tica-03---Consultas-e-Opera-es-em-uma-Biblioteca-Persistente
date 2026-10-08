# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

## Para que serve o campo `disponivel` em `Livro`?
O campo `disponivel` indica se o livro pode ser emprestado ou não. Quando ele está `True`, está disponível; quando fica `False`, significa que o livro está indisponível no momento.

## Por que usar `session.commit()`?
O `session.commit()` salva as alterações no banco de dados. Sem esse comando, a mudança de status do livro após um empréstimo ou devolução não seria persistida e não ficaria visível nas próximas consultas.

