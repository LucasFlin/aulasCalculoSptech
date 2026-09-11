agora = {"Itaúsa", "Ecorodovias", "Taesa", "B3", "Vale"}
ativa = {"B3", "Bradesco", "BB Seguridade", "BR Distribuidora", "Taesa", "CTEEP", "Vale", "Telefônica Brasil"}
genial = {"CPFL", "Minerva", "Cyrela", "Randon", "CTEEP"}
easynvest = {"B3", "Brasil Agro", "Coca-cola", "Taesa", "Vale", "Copel", "Itaúsa", "Ambev"}
elite = {"Bradesco", "BB Seguridade", "Banrisul", "Engie", "Itaúsa", "Sanepar", "Taesa", "CTEEP", "Telefônica", "Vale"}
guide = {"Alupar", "Banco do Brasil", "Cyrela", "CPFL", "Klabin", "Porto Seguro", "Tim", "Vale"}
novaFutura = {"B3", "Cyrela", "Gerdau", "Vivo", "CTEEP", "Banco ABC", "Bradesco", "Minerva", "CESP", "Engie"}

acaoComumGeral = agora & ativa & genial & easynvest & elite & guide & novaFutura
existeComumGeral = "Não existe comum." if len(acaoComumGeral) == 0 else f"Sim, {acaoComumGeral} está(ão) presente(s) em todos os conjuntos."

acaoComumEscolhidas = genial & elite & novaFutura & ativa
existeComumEscolhidas = "Não tem nenhuma" if len(acaoComumEscolhidas) == 0 else acaoComumEscolhidas

unicoGenial = genial - elite - novaFutura - ativa
unicoAtiva = ativa - genial - elite - novaFutura
unicoFutura = novaFutura - ativa - genial - elite
unicoElite = elite - novaFutura - ativa - genial

msgCompara = ''

if genial.issubset(ativa):
    msgCompara += '\n- Genial é subset de Ativa'
if genial.issubset(novaFutura):
    msgCompara += '\n- Genial é subset de Nova Futura'
if genial.issubset(elite):
    msgCompara += '\n- Genial é subset de Elite'
if genial.issuperset(ativa):
    msgCompara += '\n- Genial é superset de Ativa'
if genial.issuperset(novaFutura):
    msgCompara += '\n- Genial é superset de Nova Futura'
if genial.issuperset(elite):
    msgCompara += '\n- Genial é superset de Elite'

if ativa.issubset(genial):
    msgCompara += '\n- Ativa é subset de Genial'
if ativa.issubset(novaFutura):
    msgCompara += '\n- Ativa é subset de Nova Futura'
if ativa.issubset(elite):
    msgCompara += '\n- Ativa é subset de Elite'
if ativa.issuperset(genial):
    msgCompara += '\n- Ativa é superset de Genial'
if ativa.issuperset(novaFutura):
    msgCompara += '\n- Ativa é superset de Nova Futura'
if ativa.issuperset(elite):
    msgCompara += '\n- Ativa é superset de Elite'

if novaFutura.issubset(ativa):
    msgCompara += '\n- Nova Futura é subset de Ativa'
if novaFutura.issubset(genial):
    msgCompara += '\n- Nova Futura é subset de Genial'
if novaFutura.issubset(elite):
    msgCompara += '\n- Nova Futura é subset de Elite'
if novaFutura.issuperset(ativa):
    msgCompara += '\n- Nova Futura é superset de Ativa'
if novaFutura.issuperset(genial):
    msgCompara += '\n- Nova Futura é superset de Genial'
if novaFutura.issuperset(elite):
    msgCompara += '\n- Nova Futura é superset de Elite'

if elite.issubset(ativa):
    msgCompara += '\n- Elite é subset de Ativa'
if elite.issubset(novaFutura):
    msgCompara += '\n- Elite é subset de Nova Futura'
if elite.issubset(genial):
    msgCompara += '\n- Elite é subset de Genial'
if elite.issuperset(ativa):
    msgCompara += '\n- Elite é superset de Ativa'
if elite.issuperset(novaFutura):
    msgCompara += '\n- Elite é superset de Nova Futura'
if elite.issuperset(genial):
    msgCompara += '\n- Elite é superset de Genial'

print(f"""
Existe alguma ação em comum entre todas as corretoras?
{existeComumGeral}

-----------------------------------------------------------------------------------------

Consultoras escolhidas: Genial, Elite, Nova Futura e Ativa:
Ação/Ações em comum: 
{existeComumEscolhidas};

-----------------------------------------------------------------------------------------

Ações únicas de cada corretora:
Genial - {unicoGenial}
Elite - {unicoElite}
Nova Futura - {unicoFutura}
Ativa - {unicoAtiva}

-----------------------------------------------------------------------------------------

Relações entre as corretoras (se houver):{msgCompara}


-----------------------------------------------------------------------------------------

Fim.
""")
