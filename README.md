# uv-python-test

Projeto de estudo em **Python 3.12** usando **uv**

## Requisitos
- Python 3.12 (o projeto está fixo para esta versão)
- [uv](https://docs.astral.sh/uv/) instalado

## Como correr
```bash
uv sync                 # instala dependências a partir do lock/pyproject
uv run python main.py   # executa a aplicação
# (se tiveres app Streamlit)
# uv run streamlit run app_streamlit.py
