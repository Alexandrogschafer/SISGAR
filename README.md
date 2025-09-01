# SISGAR – Sistema de Gestão de Água em Reservatórios

O **SISGAR** é um software livre para estimativa e análise da disponibilidade de água em reservatórios.  
O sistema integra dados de sensoriamento remoto, curvas cota–volume e medições de campo para apoiar a gestão quantitativa de recursos hídricos.  

---

## Funcionalidades principais

- Importação de imagens de satélite (ex.: Sentinel-2) e DEM/curvas batimétricas.  
- Geração de máscaras de água (NDWI/MNDWI).  
- Cálculo de área, cota e volume do espelho d’água.  
- Construção e utilização de curvas cota–volume.  
- Estimativa de evaporação e consumo.  
- Simulação de depleção do reservatório.  
- Interface interativa em **Streamlit**.  

---

## Instalação

### Usando `pip` (em breve via PyPI)
```bash
pip install sisgar
````

### Instalação a partir do código-fonte

```bash
git clone https://github.com/Alexandrogschafer/SISGAR.git
cd SISGAR
conda create -n sisgar python=3.11
conda activate sisgar
pip install -e .[dev]
```

---

## Exemplo de uso rápido

Rodar a interface interativa:

```bash
streamlit run src/sisgar/app/dashboard.py
```

Fluxo básico disponível no dashboard:

1. Upload de dados (imagens/curvas).
2. Detecção de cota.
3. Cálculo de área, cota e volume.
4. Geração de curva cota–volume.
5. Integração com séries temporais.
6. Estimativa de evaporação e consumo.
7. Simulação de depleção.

---

## Estrutura do repositório

```
SISGAR/
├── src/sisgar/         # código-fonte
├── tests/              # testes automatizados
├── data/sample/        # exemplos de dados
├── docs/               # documentação
├── LICENSE             # licença MIT
└── README.md           # este arquivo
```

---

## Contribuindo

Contribuições são bem-vindas!
Leia o [CONTRIBUTING.md](CONTRIBUTING.md) para saber como propor melhorias, abrir Issues e enviar Pull Requests.

---

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

## Contato

Autores principal: **Alexandro G. Schafer** e **Pedro Gabriel Mota Pereira**
E-mail: [alschafer@gmail.com](mailto:alschafer@gmail.com)
Repositório: [github.com/Alexandrogschafer/SISGAR](https://github.com/Alexandrogschafer/SISGAR)



Você quer que eu já prepare também um **Roadmap (em Markdown)** para colocar no README (com as etapas v0.9.0 → v1.0.0 → v1.1.0), ou prefere deixar esse detalhe na aba **Projects/Milestones** do GitHub?
```
