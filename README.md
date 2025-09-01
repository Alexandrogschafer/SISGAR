# SISGAR – Sistema de Gestão de Água em Reservatórios

Este repositório contém o código-fonte, documentação e recursos relacionados ao **SISGAR – Sistema de Gestão de Água em Reservatórios**.  
O objetivo do projeto é fornecer uma plataforma aberta e extensível para análise, simulação e gestão de reservatórios hídricos, integrando diferentes fontes de dados (imagens de satélite, curvas batimétricas, réguas limnimétricas etc.).

---

## Estrutura do Repositório
- **`src/`** – Código-fonte principal do SISGAR.
- **`tests/`** – Testes automatizados para garantir a qualidade do software.
- **`data/`** – Dados de exemplo e instruções de uso.
- **`docs/`** – Documentação técnica e científica associada ao projeto.

---

## Funcionalidades Principais
- Estimativa de área, cota e volume do espelho d’água.
- Integração de leituras de réguas limnimétricas.
- Geração e uso de curvas Cota×Volume.
- Simulação de cenários de consumo, evaporação e depleção.
- Processamento de imagens de satélite (ex.: Sentinel-2) para detecção automática de áreas alagadas.

---

## Instalação
Clone o repositório e instale as dependências:

```bash
git clone https://github.com/Alexandrogschafer/SISGAR.git
cd SISGAR
pip install -e .
````

---

## Uso

Execute o dashboard interativo com Streamlit:

```bash
streamlit run src/sisgar/app/dashboard.py
```

---

## Contribuição

Se deseja contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição:

   ```bash
   git checkout -b minha-feature
   ```
3. Realize as alterações e os commits.
4. Abra um Pull Request.

Mais detalhes no arquivo [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).


Quer que eu já prepare os **comandos Git prontos** para você atualizar esse `README.md` no repositório (commit + push), como fizemos com o `CONTRIBUTING.md`?
```
