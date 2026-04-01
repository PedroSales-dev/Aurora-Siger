# Missão Aurora Siger — Ignition Zero
### Sistema de Verificação de Pré-Decolagem

---

| | |
|---|---|
| **Aluno** | Pedro de Oliveira Reis Sales |
| **RM** | 572709 |
| **Curso** | Bacharelado em Ciências da Computação |
| **Instituição** | FIAP |
| **Disciplina** | Atividade Integradora — Fase 1 |

---

## Sobre o projeto

Este repositório contém o relatório operacional de pré-decolagem da nave **Aurora Siger**, desenvolvido como parte da Atividade Integradora da Fase 1 do curso. O projeto simula o pipeline computacional de verificação de sistemas que precede qualquer lançamento espacial — desde a leitura dos sensores até a decisão final de autorizar ou suspender o lançamento.

O diferencial desta implementação está no uso de **dados gerados aleatoriamente** a cada execução, simulando o comportamento imprevisível de sensores reais. Isso significa que o sistema pode gerar tanto cenários de sucesso quanto de falha — o que torna a validação do algoritmo mais significativa do que trabalhar com dados fixos.

Cada seção do notebook cobre uma camada distinta do problema:

| Seção | Conteúdo |
|---|---|
| 1 — Telemetria | Leitura simulada dos 8 sensores embarcados da nave |
| 2 — Algoritmo | Pseudocódigo e estrutura lógica do sistema de decisão |
| 3 — Python | Implementação da função de verificação + teste com falhas forçadas |
| 4 — Balanço energético | Cálculo de energia aproveitável, perdas e autonomia |
| 5 — Análise de risco (IA) | Classificação graduada: NOMINAL, ATENCAO, CRITICO |
| 6 — Reflexão crítica | Ética, impacto social e sustentabilidade tecnológica |

---

## Estrutura do repositório

```
aurora-siger/
├── aurora_siger.ipynb   # Notebook principal com todo o código e análises
├── aurora_siger.py      # Script Python com todos os módulos do projeto
└── README.md            # Este arquivo
```

---

## Como executar

### Opção 1 — Google Colab (recomendado)

1. Acesse o [Google Colab](https://colab.research.google.com/)
2. Faça o upload do arquivo `aurora_siger.ipynb`
3. Clique em **Runtime > Run all** ou execute célula por célula com `Shift + Enter`
4. Nenhuma biblioteca externa necessária — o projeto usa apenas `random`, nativo do Python

### Opção 2 — Terminal local

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/aurora-siger.git
cd aurora-siger

# Execute o script direto
python3 aurora_siger.py

# Ou abra o notebook
jupyter notebook aurora_siger.ipynb
```

**Pré-requisitos para execução local:** Python 3.8+ e Jupyter Notebook (apenas para o `.ipynb`)

---

## Parâmetros monitorados

| Parâmetro | Faixa segura | Tipo |
|---|---|---|
| Temperatura interna | 18°C a 28°C | Contínuo |
| Temperatura externa | -115°C a 15°C | Contínuo |
| Integridade estrutural | 1 (íntegra) | Binário |
| Carga energética | ≥ 82% | Contínuo |
| Pressão dos propulsores | 310 a 390 kPa | Contínuo |
| Módulo de propulsão | 1 (online) | Binário |
| Módulo de comunicação | 1 (online) | Binário |
| Módulo de navegação | 1 (online) | Binário |

Os dados são gerados com `random.uniform` (valores contínuos) e `random.choices` com pesos (módulos binários), onde módulos têm **88% de chance de estarem online** — criando um sistema que falha com frequência realista.

---

## Exemplos de execução

### Leitura dos sensores
```
  AURORA SIGER :: LEITURA DE SENSORES
  --------------------------------------------
  Temperatura interna   (grausC)    24.2
  Temperatura externa   (grausC)    3.7
  Integridade estrutural [0/1]      0
  Carga da bateria      (%)         76.8
  Pressao propulsores   (kPa)       305.9
  Modulo propulsao      [0/1]       1
  Modulo comunicacao    [0/1]       1
  Modulo navegacao      [0/1]       1
  --------------------------------------------
```

### Resultado do checklist (com falhas)
```
  AURORA SIGER :: CHECKLIST DE PRE-DECOLAGEM
  ==================================================
  VEREDICTO  >>  LANCAMENTO SUSPENSO
  3 pendencia(s) registrada(s):
    [!] Comprometimento estrutural detectado pelos sensores de fuselagem
    [!] Carga insuficiente: 76.8%  [minimo exigido: 82%]
    [!] Pressao dos propulsores fora da faixa: 305.9 kPa  [seguro: 310-390 kPa]
  ==================================================
```

### Balanço energético
```
  AURORA SIGER :: BALANCO ENERGETICO
  ----------------------------------------------
  Capacidade instalada            : 520 kWh
  Carga atual (telemetria)         : 76.8%
  Energia bruta disponivel         : 399.4 kWh
  Perdas de conversao (6%)         : -24.0 kWh
  Energia liquida aproveitavel     : 375.4 kWh
  Consumo estimado do lancamento   : -140 kWh
  ----------------------------------------------
  Reserva para a missao            : 235.4 kWh
  Autonomia estimada em cruzeiro   : 13.1 horas
  ----------------------------------------------
  [OK] Reserva dentro dos parametros. Missao energeticamente viavel.
```

### Análise de risco (IA)
```
  AURORA SIGER :: ANALISE DE RISCO (IA)
  Parametro              Status     Observacao
  --------------------------------------------------------------------
  Temp. interna          [OK     ] 24.2C
  Temp. externa          [OK     ] 3.7C
  Integridade            [CRITICO] DANO ESTRUTURAL DETECTADO
  Carga bateria          [CRITICO] 76.8% - ABAIXO DO MINIMO DE 82%
  Pressao propulsor      [CRITICO] 305.9 kPa - FORA DA FAIXA (310-390 kPa)
  Mod. Propulsao         [OK     ] Online
  Mod. Comunicacao       [OK     ] Online
  Mod. Navegacao         [OK     ] Online
  --------------------------------------------------------------------
  Resumo: 5 nominal(is)  |  0 atencao  |  3 critico(s)
```

---

## Conexão com as disciplinas da Fase 1

- **Computer Science:** lógica booleana, representação binária e sistemas de verificação com estados discretos
- **Pensamento Computacional e Python:** decomposição do problema em funções, pseudocódigo e automação do checklist
- **Prompt e IA:** análise assistida por IA com classificação graduada de risco e identificação de padrões
- **Energias Renováveis e Sustentáveis:** modelo de eficiência energética com perdas de conversão e cálculo de autonomia
- **Formação Social e Sustentabilidade:** reflexão sobre ética em sistemas críticos, acesso à tecnologia espacial e lixo orbital
