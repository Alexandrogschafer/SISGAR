# SISGAR — Sistema de Gestão de Água em Reservatórios

Ferramenta para **gestão quantitativa** de água em reservatórios: **nível, área, volume e balanço**,
com integração de **imagens** (ex.: Sentinel‑2), **régua limnimétrica** e **curva Cota×Volume**.

## Instalação (desenvolvimento)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
```

## Executar o app (protótipo)

```bash
streamlit run src/sisgar/app/dashboard.py
```

## Estrutura

- `src/sisgar/` — pacote principal (io, processing, hydro, utils, app Streamlit)
- `tests/` — testes unitários
- `data/sample/` — dados de exemplo (pequenos)
- `.github/workflows/ci.yml` — CI com lint e testes

> Observação: publicação de documentação (MkDocs/GitHub Pages) pode ser adicionada futuramente.
