
# Guia de Contribuição – SISGAR

Bem-vindo ao projeto **SISGAR – Sistema de Gestão de Água em Reservatórios**.
Este documento explica como contribuir corretamente com código, documentação ou ideias.

---

## Fluxo de trabalho básico

### Criar uma branch a partir da `main`
```bash
git checkout -b feat/nome-da-feature
````

Prefixos recomendados:

* `feat/` → nova funcionalidade
* `fix/` → correção de bug
* `docs/` → alterações em documentação
* `chore/` → ajustes menores (CI, dependências, etc.)

### Fazer commits pequenos e claros

Mensagens de commit no formato:

```
tipo: descrição curta
```

Exemplos:

* `feat: adicionar cálculo de curva cota-volume`
* `fix: corrigir erro na máscara de NDWI`

### Rodar testes e linters localmente antes do push

```bash
pytest
ruff check src tests
pre-commit run --all-files
```

### Enviar a branch para o GitHub

```bash
git push origin feat/nome-da-feature
```

### Abrir um Pull Request (PR) para a branch `main`

* O PR será revisado por outro colaborador.
* O CI (GitHub Actions) precisa passar com sucesso antes do merge.
* A branch deve estar atualizada com a `main`.

---

## Regras da branch `main`

A branch `main` está protegida e segue estas regras:

* Não é permitido `git push` direto.
* Todo código novo entra via Pull Request.
* É necessária pelo menos uma aprovação de revisão.
* O CI deve estar aprovado (testes e linters).
* A branch deve estar atualizada com `main` antes do merge.

---

## Convenções adicionais

* **Estrutura do código**: seguir a organização em módulos (`io/`, `processing/`, `hydro/`, `app/`, etc.).
* **Testes**: cada nova função deve ter testes em `tests/`.
* **Documentação**: atualizar `docs/` quando houver novas funcionalidades.
* **Idioma**: mensagens de commit, código e documentação devem ser escritas em português claro.

---

## Exemplos práticos

Criando uma feature:

```bash
git checkout -b feat/calculo-evaporacao
# editar código...
git add .
git commit -m "feat: implementar cálculo de evaporação pelo método Thornthwaite"
git push origin feat/calculo-evaporacao
```

Abrindo PR no GitHub:

* **Título**: `feat: implementar cálculo de evaporação`
* **Descrição**: explicar o que mudou, referências utilizadas e testes realizados.

---

## Outras formas de contribuir

* Revisar Pull Requests de colegas.
* Reportar bugs por meio de Issues.
* Sugerir melhorias, também via Issues.
* Melhorar documentação e exemplos
