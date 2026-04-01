"""
=============================================================
  AURORA SIGER — Ignition Zero
  Sistema de Verificação de Pré-Decolagem

  Aluno      : Pedro de Oliveira Reis Sales
  RM         : 572709
  Curso      : Bacharelado em Ciências da Computação
  Instituição: FIAP — Atividade Integradora, Fase 1
=============================================================
"""

import random

# Para reproduzir sempre os mesmos dados, ative a linha abaixo:
# random.seed(7)


# =============================================================
# SEÇÃO 1 — TELEMETRIA
# Simula a leitura dos sensores embarcados da nave.
# =============================================================

def capturar_telemetria():
    """
    Gera os dados de telemetria com valores aleatórios dentro de
    intervalos realistas. Módulos críticos têm 88% de chance de
    estarem online; parâmetros contínuos podem ultrapassar os limites.
    """
    return {
        "temp_interna":      round(random.uniform(14.0, 32.0), 1),
        "temp_externa":      round(random.uniform(-120.0, 22.0), 1),
        "integridade":       random.choices([1, 0], weights=[88, 12])[0],
        "carga_bateria":     round(random.uniform(68.0, 100.0), 1),
        "pressao_propulsor": round(random.uniform(285.0, 410.0), 1),
        "mod_propulsao":     random.choices([1, 0], weights=[88, 12])[0],
        "mod_comunicacao":   random.choices([1, 0], weights=[88, 12])[0],
        "mod_navegacao":     random.choices([1, 0], weights=[88, 12])[0],
    }


leitura = capturar_telemetria()

rotulos = {
    "temp_interna":      "Temperatura interna   (grausC)",
    "temp_externa":      "Temperatura externa   (grausC)",
    "integridade":       "Integridade estrutural [0/1]",
    "carga_bateria":     "Carga da bateria      (%)",
    "pressao_propulsor": "Pressao propulsores   (kPa)",
    "mod_propulsao":     "Modulo propulsao      [0/1]",
    "mod_comunicacao":   "Modulo comunicacao    [0/1]",
    "mod_navegacao":     "Modulo navegacao      [0/1]",
}

print()
print("  AURORA SIGER :: LEITURA DE SENSORES")
print("  " + "-" * 44)
for chave, rotulo in rotulos.items():
    print(f"  {rotulo:<32}  {leitura[chave]}")
print("  " + "-" * 44)
print()


# =============================================================
# SEÇÃO 2 — PSEUDOCÓDIGO (referência comentada)
#
# FUNCAO checar_condicoes(leitura):
#   pendencias <- lista vazia
#
#   SE temp_interna < 18 OU temp_interna > 28:
#       registrar "Temperatura interna fora do intervalo"
#
#   SE temp_externa < -115 OU temp_externa > 15:
#       registrar "Temperatura externa fora do intervalo"
#
#   SE integridade != 1:
#       registrar "Comprometimento estrutural detectado"
#
#   SE carga_bateria < 82:
#       registrar "Carga energetica insuficiente"
#
#   SE pressao_propulsor < 310 OU pressao_propulsor > 390:
#       registrar "Pressao dos propulsores fora da faixa"
#
#   PARA CADA modulo EM [propulsao, comunicacao, navegacao]:
#       SE modulo == 0:
#           registrar "Modulo offline: " + nome
#
#   SE pendencias VAZIA:
#       RETORNAR "LANCAMENTO AUTORIZADO"
#   SENAO:
#       RETORNAR "LANCAMENTO SUSPENSO" + pendencias
#
# FIM
# =============================================================


# =============================================================
# SEÇÃO 3 — VERIFICAÇÃO
# Implementação do algoritmo de decisão em Python.
# =============================================================

def checar_condicoes(dados):
    """
    Executa o checklist de pre-decolagem da nave Aurora Siger.

    Faixas operacionais seguras:
      temp_interna      : 18 a 28 graus C
      temp_externa      : -115 a 15 graus C
      integridade       : 1 (integra)
      carga_bateria     : >= 82%
      pressao_propulsor : 310 a 390 kPa
      modulos criticos  : todos = 1 (online)

    Retorna True se autorizado, False se suspenso.
    """
    pendencias = []

    # Ambiente termico
    if not (18 <= dados["temp_interna"] <= 28):
        pendencias.append(
            f"Temp. interna fora do intervalo: {dados['temp_interna']}C  [seguro: 18-28C]"
        )

    if not (-115 <= dados["temp_externa"] <= 15):
        pendencias.append(
            f"Temp. externa fora do intervalo: {dados['temp_externa']}C  [seguro: -115 a 15C]"
        )

    # Integridade fisica
    if dados["integridade"] != 1:
        pendencias.append("Comprometimento estrutural detectado pelos sensores de fuselagem")

    # Energia
    if dados["carga_bateria"] < 82:
        pendencias.append(
            f"Carga insuficiente: {dados['carga_bateria']}%  [minimo exigido: 82%]"
        )

    # Propulsao
    if not (310 <= dados["pressao_propulsor"] <= 390):
        pendencias.append(
            f"Pressao dos propulsores fora da faixa: {dados['pressao_propulsor']} kPa  [seguro: 310-390 kPa]"
        )

    # Modulos criticos
    modulos = {
        "Propulsao":   dados["mod_propulsao"],
        "Comunicacao": dados["mod_comunicacao"],
        "Navegacao":   dados["mod_navegacao"],
    }
    for nome, status in modulos.items():
        if status != 1:
            pendencias.append(f"Modulo de {nome} reportado como offline")

    # Veredicto
    print()
    print("  AURORA SIGER :: CHECKLIST DE PRE-DECOLAGEM")
    print("  " + "=" * 50)

    if not pendencias:
        print("  VEREDICTO  >>  LANCAMENTO AUTORIZADO")
        print("  Todos os sistemas operacionais. Go for launch.")
    else:
        print("  VEREDICTO  >>  LANCAMENTO SUSPENSO")
        print(f"  {len(pendencias)} pendencia(s) registrada(s):")
        for item in pendencias:
            print(f"    [!] {item}")

    print("  " + "=" * 50)
    print()
    return len(pendencias) == 0


# Execucao com os dados da leitura ao vivo
autorizado = checar_condicoes(leitura)

# Teste com cenario critico (falhas injetadas manualmente)
cenario_critico = {
    "temp_interna":      31.4,   # [!] acima de 28C
    "temp_externa":     -88.0,   # OK
    "integridade":           1,  # OK
    "carga_bateria":     78.2,   # [!] abaixo de 82%
    "pressao_propulsor": 402.0,  # [!] acima de 390 kPa
    "mod_propulsao":         1,  # OK
    "mod_comunicacao":       1,  # OK
    "mod_navegacao":         0,  # [!] offline
}

print("  --- ENTRADA: CENARIO CRITICO (DADOS FORCADOS) ---")
for k, v in cenario_critico.items():
    print(f"  {k:<22} : {v}")

checar_condicoes(cenario_critico)


# =============================================================
# SEÇÃO 4 — BALANÇO ENERGÉTICO
# Calcula energia aproveitavel, perdas e autonomia da missao.
# =============================================================

CAPACIDADE_TOTAL_KWH = 520   # kWh - capacidade maxima das baterias
PERDA_CONVERSAO_PCT  = 6     # % - perdas por calor e resistencia
CONSUMO_LANCAMENTO   = 140   # kWh - gasto do ignition ate orbita estavel
CONSUMO_CRUZEIRO     = 18    # kWh/h - consumo medio em cruzeiro

carga_pct = leitura["carga_bateria"]

energia_bruta   = CAPACIDADE_TOTAL_KWH * (carga_pct / 100)
perdas_kwh      = energia_bruta * (PERDA_CONVERSAO_PCT / 100)
energia_liquida = energia_bruta - perdas_kwh
reserva_missao  = energia_liquida - CONSUMO_LANCAMENTO
autonomia_h     = max(reserva_missao / CONSUMO_CRUZEIRO, 0)

print()
print("  AURORA SIGER :: BALANCO ENERGETICO")
print("  " + "-" * 46)
print(f"  Capacidade instalada            : {CAPACIDADE_TOTAL_KWH} kWh")
print(f"  Carga atual (telemetria)         : {carga_pct}%")
print(f"  Energia bruta disponivel         : {energia_bruta:.1f} kWh")
print(f"  Perdas de conversao ({PERDA_CONVERSAO_PCT}%)       : -{perdas_kwh:.1f} kWh")
print(f"  Energia liquida aproveitavel     : {energia_liquida:.1f} kWh")
print(f"  Consumo estimado do lancamento   : -{CONSUMO_LANCAMENTO} kWh")
print("  " + "-" * 46)
print(f"  Reserva para a missao            : {reserva_missao:.1f} kWh")
print(f"  Autonomia estimada em cruzeiro   : {autonomia_h:.1f} horas")
print("  " + "-" * 46)

if reserva_missao < 0:
    print("  [CRITICO] Energia insuficiente para completar o lancamento!")
elif reserva_missao < 80:
    print("  [ATENCAO] Reserva abaixo de 80 kWh - margem operacional reduzida.")
else:
    print("  [OK] Reserva dentro dos parametros. Missao energeticamente viavel.")
print()


# =============================================================
# SEÇÃO 5 — ANÁLISE DE RISCO ASSISTIDA POR IA
# Classificacao graduada: NOMINAL, ATENCAO ou CRITICO.
# =============================================================

def classificar_risco(dados):
    """
    Analise de risco graduada para cada parametro de telemetria.
    Vai alem do binario: avalia a proximidade dos limites e aponta tendencias.
    """
    relatorio = []

    ti = dados["temp_interna"]
    if 18 <= ti <= 28:
        nivel = "ATENCAO" if ti > 26 else "NOMINAL"
        obs   = f"{ti}C" + (" - proximo do limite superior (28C)" if ti > 26 else "")
    else:
        nivel, obs = "CRITICO", f"{ti}C - FORA DA FAIXA (18-28C)"
    relatorio.append(("Temp. interna", nivel, obs))

    te = dados["temp_externa"]
    if -115 <= te <= 15:
        nivel = "ATENCAO" if te < -100 else "NOMINAL"
        obs   = f"{te}C" + (" - extrema, verificar isolamento" if te < -100 else "")
    else:
        nivel, obs = "CRITICO", f"{te}C - FORA DA FAIXA (-115 a 15C)"
    relatorio.append(("Temp. externa", nivel, obs))

    ig = dados["integridade"]
    relatorio.append((
        "Integridade",
        "NOMINAL" if ig == 1 else "CRITICO",
        "Estrutura integra" if ig == 1 else "DANO ESTRUTURAL DETECTADO"
    ))

    cb = dados["carga_bateria"]
    if cb >= 82:
        nivel = "ATENCAO" if cb < 90 else "NOMINAL"
        obs   = f"{cb}%" + (f" - margem de {cb-82:.1f}pp acima do minimo" if cb < 90 else "")
    else:
        nivel, obs = "CRITICO", f"{cb}% - ABAIXO DO MINIMO DE 82%"
    relatorio.append(("Carga bateria", nivel, obs))

    pp = dados["pressao_propulsor"]
    if 310 <= pp <= 390:
        nivel = "ATENCAO" if pp < 325 or pp > 375 else "NOMINAL"
        obs   = f"{pp} kPa"
        if pp < 325:   obs += " - proximo do limite inferior"
        elif pp > 375: obs += " - proximo do limite superior"
    else:
        nivel, obs = "CRITICO", f"{pp} kPa - FORA DA FAIXA (310-390 kPa)"
    relatorio.append(("Pressao propulsor", nivel, obs))

    for nome_exib, chave in [("Mod. Propulsao",   "mod_propulsao"),
                               ("Mod. Comunicacao", "mod_comunicacao"),
                               ("Mod. Navegacao",   "mod_navegacao")]:
        st = dados[chave]
        relatorio.append((
            nome_exib,
            "NOMINAL" if st == 1 else "CRITICO",
            "Online" if st == 1 else "OFFLINE - sistema inoperante"
        ))

    icones = {"NOMINAL": "OK     ", "ATENCAO": "ATENCAO", "CRITICO": "CRITICO"}

    print()
    print("  AURORA SIGER :: ANALISE DE RISCO (IA)")
    print(f"  {'Parametro':<22} {'Status':<10} Observacao")
    print("  " + "-" * 68)
    for param, status, obs in relatorio:
        print(f"  {param:<22} [{icones[status]}] {obs}")
    print("  " + "-" * 68)

    criticos = sum(1 for _, s, _ in relatorio if s == "CRITICO")
    atencao  = sum(1 for _, s, _ in relatorio if s == "ATENCAO")
    nominais = sum(1 for _, s, _ in relatorio if s == "NOMINAL")
    print(f"  Resumo: {nominais} nominal(is)  |  {atencao} atencao  |  {criticos} critico(s)")
    print()


classificar_risco(leitura)
