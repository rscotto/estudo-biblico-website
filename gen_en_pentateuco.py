#!/usr/bin/env python3
"""Generate at-pentateuco/index.en.html from the PT source."""
import re, sys

with open('at-pentateuco/index.html', encoding='utf-8') as f:
    out = f.read()

# ── Head / meta ───────────────────────────────────────────────────────────────
out = out.replace('<html lang="pt-BR">', '<html lang="en">', 1)
out = out.replace('<title>Moisés — Estudo Bíblico Completo</title>',
                  '<title>Moses — Complete Bible Study</title>', 1)

# ── Sidebar static text ───────────────────────────────────────────────────────
out = out.replace('>Voltar à Bíblia<', '>Back to Bible<', 1)
out = out.replace('>Moisés / Pentateuco<', '>Moses / Pentateuch<', 1)
out = out.replace('>Antigo Testamento · 5 Livros<', '>Old Testament · 5 Books<', 1)
out = out.replace('>Os Cinco Livros<', '>The Five Books<', 1)
# nav-section-label "Moisés" (second occurrence — the label, not a nav-name)
out = out.replace('<div class="nav-section-label">Moisés</div>',
                  '<div class="nav-section-label">Moses</div>', 1)
out = out.replace('aria-label="Navegação do Pentateuco"',
                  'aria-label="Pentateuch navigation"', 1)
out = out.replace('aria-label="Abrir menu"', 'aria-label="Open menu"', 1)

# ── Nav names (visible text, data-pt/en already on element) ──────────────────
nav = {
    '>Gênesis<': '>Genesis<',
    '>Êxodo<': '>Exodus<',
    '>Levítico<': '>Leviticus<',
    '>Números<': '>Numbers<',
    '>Deuteronômio<': '>Deuteronomy<',
    '>Visão Geral<': '>Overview<',
    '>Contexto Geográfico<': '>Geographic Context<',
    '>Contexto Político<': '>Political Context<',
    '>Sarça Ardente<': '>Burning Bush<',
    '>Pragas e Êxodo<': '>Plagues &amp; Exodus<',
    '>Bezerro de Ouro<': '>Golden Calf<',
    '>Deserto e Crise<': '>Desert &amp; Crisis<',
    '>Teologia<': '>Theology<',
    '>NT e Cristo<': '>NT &amp; Christ<',
    '>O Pentateuco<': '>The Pentateuch<',
}
for pt, en in nav.items():
    out = out.replace(pt, en)

# nav abbr
out = out.replace('>Gn<', '>Gen<')
out = out.replace('>Êx<', '>Exod<')
out = out.replace('>Lv<', '>Lev<')
out = out.replace('>Nm<', '>Num<')
out = out.replace('>Dt<', '>Deut<')

# ── Hero ──────────────────────────────────────────────────────────────────────
out = out.replace('>Estudo Bíblico Panorâmico<', '>Panoramic Bible Study<', 1)
out = out.replace('>Moisés<', '>Moses<', 1)
out = out.replace('>O Libertador · O Legislador · O Profeta<',
                  '>The Deliverer · The Lawgiver · The Prophet<', 1)
out = out.replace(
    '"Nunca mais houve em Israel profeta como Moisés, a quem o <span style="font-variant:small-caps">Senhor</span> conheceu face a face."\n      <span class="hero-ref">— Deuteronômio 34.10 — NAA</span>',
    '"No prophet has risen in Israel like Moses, whom the <span style="font-variant:small-caps">Lord</span> knew face to face."\n      <span class="hero-ref">— Deuteronomy 34:10 — ESV</span>',
    1
)

# ── Remove data-pt / data-en attributes ──────────────────────────────────────
out = re.sub(r'\s+data-pt="[^"]*"', '', out)
out = re.sub(r"\s+data-pt='[^']*'", '', out)
out = re.sub(r'\s+data-en="[^"]*"', '', out)
out = re.sub(r"\s+data-en='[^']*'", '', out)

# ══════════════════════════════════════════════════════════════════════════════
# Section: visao-geral
# ══════════════════════════════════════════════════════════════════════════════
out = out.replace(
    '<span class="section-tag">Introdução</span>\n      <h1 class="section-title">Quem foi Moisés?</h1>\n      <p class="section-lead">A figura mais monumental do Antigo Testamento — libertador, profeta, mediador, legislador e tipo de Cristo.</p>',
    '<span class="section-tag">Introduction</span>\n      <h1 class="section-title">Who Was Moses?</h1>\n      <p class="section-lead">The most towering figure in the Old Testament — deliverer, prophet, mediator, lawgiver, and type of Christ.</p>',
    1
)
out = out.replace(
    '<p>Moisés é, sem dúvida, a figura central do Pentateuco e uma das mais importantes de toda a Escritura. Seu ministério abrange quatro dos cinco livros que ele mesmo escreveu: Êxodo, Levítico, Números e Deuteronômio. Nenhum personagem do AT recebe tanta atenção biográfica, teológica e narrativa.</p>',
    '<p>Moses is, without question, the central figure of the Pentateuch and one of the most important in all of Scripture. His ministry spans four of the five books he himself wrote: Exodus, Leviticus, Numbers, and Deuteronomy. No other Old Testament figure receives such extensive biographical, theological, and narrative attention.</p>',
    1
)
out = out.replace(
    '<p>Ele viveu aproximadamente <strong>1526–1406 a.C.</strong> (cronologia conservadora), embora datas alternativas variem conforme a abordagem da cronologia egípcia. Sua vida é dividida em três períodos de quarenta anos cada, conforme Atos 7.23, 30, 36.</p>',
    '<p>He lived approximately <strong>1526–1406 BC</strong> (conservative chronology), though alternative dates vary according to different approaches to Egyptian chronology. His life is divided into three forty-year periods, as confirmed in Acts 7:23, 30, 36.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Três Períodos de 40 Anos</div>\n        <p><strong>Período 1 (0–40 anos):</strong> Educação como príncipe no Egito — "instruído em toda a sabedoria dos egípcios" (At 7.22).<br><br>\n        <strong>Período 2 (40–80 anos):</strong> Exílio em Midiã — pastoreio, casamento, formação no deserto.<br><br>\n        <strong>Período 3 (80–120 anos):</strong> Ministério de libertação, legislação e liderança de Israel.</p>',
    '<div class="card-title">Three Periods of 40 Years</div>\n        <p><strong>Period 1 (0–40 years):</strong> Education as an Egyptian prince — "instructed in all the wisdom of the Egyptians" (Acts 7:22).<br><br>\n        <strong>Period 2 (40–80 years):</strong> Exile in Midian — shepherding, marriage, formation in the desert.<br><br>\n        <strong>Period 3 (80–120 years):</strong> Ministry of liberation, legislation, and leadership of Israel.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Títulos e Papéis</div>\n        <p>• <strong>Profeta</strong> — Dt 18.15; 34.10<br>\n        • <strong>Mediador da Aliança</strong> — Gálatas 3.19<br>\n        • <strong>Servo do SENHOR</strong> — Dt 34.5 (Eved YHWH)<br>\n        • <strong>Homem de Deus</strong> — Dt 33.1<br>\n        • <strong>Rei em Jesurum</strong> — Dt 33.5<br>\n        • <strong>Tipo de Cristo</strong> — João 5.46; Hb 3.1–6</p>',
    '<div class="card-title">Titles and Roles</div>\n        <p>• <strong>Prophet</strong> — Deut 18:15; 34:10<br>\n        • <strong>Mediator of the Covenant</strong> — Galatians 3:19<br>\n        • <strong>Servant of the Lord</strong> — Deut 34:5 (Eved YHWH)<br>\n        • <strong>Man of God</strong> — Deut 33:1<br>\n        • <strong>King in Jeshurun</strong> — Deut 33:5<br>\n        • <strong>Type of Christ</strong> — John 5:46; Heb 3:1–6</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Nota Teológica</span>\n      <p>Moisés é o único personagem do AT sobre quem Deus declara ter falado "face a face" (Nm 12.8; Dt 34.10). Isso o distingue de todos os profetas anteriores e posteriores até a vinda de Cristo — o profeta prometido "semelhante a Moisés" (Dt 18.15, 18).</p>',
    '<span class="callout-type">Theological Note</span>\n      <p>Moses is the only Old Testament figure of whom God declares he spoke "face to face" (Num 12:8; Deut 34:10). This distinguishes him from all prophets before and after him until the coming of Christ — the promised prophet "like Moses" (Deut 18:15, 18).</p>',
    1
)
out = out.replace(
    '<h2>Fontes Primárias</h2>\n    <p>A narrativa primária sobre Moisés encontra-se em <strong>Êxodo 2–Deuteronômio 34</strong>. Referências posteriores ocorrem em: Josué 1; Salmo 90 (o único salmo atribuído a Moisés); Salmo 103; Isaías; Jeremias; Ezequiel; Malaquias 4.4; e extensamente no NT (Jo 1.17; At 7; Hb 3; Ap 15.3).</p>',
    '<h2>Primary Sources</h2>\n    <p>The primary narrative about Moses is found in <strong>Exodus 2 – Deuteronomy 34</strong>. Later references appear in: Joshua 1; Psalm 90 (the only psalm attributed to Moses); Psalm 103; Isaiah; Jeremiah; Ezekiel; Malachi 4:4; and extensively in the NT (John 1:17; Acts 7; Heb 3; Rev 15:3).</p>',
    1
)
out = out.replace(
    '"Nunca mais houve em Israel profeta como Moisés, a quem o <span style="font-variant:small-caps">Senhor</span> conheceu face a face, com todos os sinais e maravilhas que o <span style="font-variant:small-caps">Senhor</span> o enviou para fazer na terra do Egito."\n      <span class="scripture-ref">Deuteronômio 34.10–11 — NAA</span>',
    '"And there has not arisen a prophet since in Israel like Moses, whom the <span style="font-variant:small-caps">Lord</span> knew face to face, none like him for all the signs and the wonders that the <span style="font-variant:small-caps">Lord</span> sent him to do in the land of Egypt."\n      <span class="scripture-ref">Deuteronomy 34:10–11 — ESV</span>',
    1
)
out = out.replace(
    '<h2>Nome e Etimologia</h2>\n    <p>O nome <em>Moisés</em> (hebraico: <strong>מֹשֶׁה</strong>, Mosheh) é explicado em Êxodo 2.10 pela filha do Faraó: <em>"porque das águas eu o tirei."</em> A palavra hebraica vem da raiz <em>mashah</em> ("tirar"). Ironicamente, o nome tem paralelo com o egípcio <em>ms/msy</em>, que significa "filho" ou "nascido de" (como em Ramsés = "filho de Rá" e Tutmósis = "filho de Toth"). A fusão semântica é significativa: ele é "tirado das águas" — e assim se torna aquele que tirará Israel do Egito.</p>',
    '<h2>Name and Etymology</h2>\n    <p>The name <em>Moses</em> (Hebrew: <strong>מֹשֶׁה</strong>, Mosheh) is explained in Exodus 2:10 by Pharaoh\'s daughter: <em>"because I drew him out of the water."</em> The Hebrew word comes from the root <em>mashah</em> ("to draw out"). Notably, the name parallels the Egyptian <em>ms/msy</em>, meaning "son" or "born of" (as in Ramesses = "son of Ra" and Thutmose = "son of Thoth"). The semantic fusion is significant: he is "drawn out of the waters" — and thus becomes the one who will draw Israel out of Egypt.</p>',
    1
)
out = out.replace(
    '<span class="name-tag">Latim: Moyses</span>\n      <span class="name-tag">Árabe: موسى Musa</span>',
    '<span class="name-tag">Latin: Moyses</span>\n      <span class="name-tag">Arabic: موسى Musa</span>',
    1
)

# ══════════════════════════════════════════════════════════════════════════════
# Section: contexto-geo
# ══════════════════════════════════════════════════════════════════════════════
out = out.replace(
    '<span class="section-tag">Geografia Bíblica</span>\n      <h1 class="section-title">O Mundo Geográfico de Moisés</h1>\n      <p class="section-lead">Da terra de Gósen ao monte Nebo — os cenários físicos que moldaram o ministério de Moisés.</p>',
    '<span class="section-tag">Biblical Geography</span>\n      <h1 class="section-title">The Geographical World of Moses</h1>\n      <p class="section-lead">From the land of Goshen to Mount Nebo — the physical settings that shaped Moses\'s ministry.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Contextualização Geográfica</span>\n      <p>A narrativa mosaica percorre três regiões distintas: o <strong>Egito</strong> (cativeiro e libertação), a <strong>Península do Sinai</strong> (peregrinação e revelação da Lei) e as <strong>planícies de Moabe</strong> (morte de Moisés). Cada região tem significado teológico próprio.</p>',
    '<span class="callout-type">Geographical Context</span>\n      <p>The Mosaic narrative traverses three distinct regions: <strong>Egypt</strong> (captivity and liberation), the <strong>Sinai Peninsula</strong> (wilderness wandering and the giving of the Law), and the <strong>plains of Moab</strong> (death of Moses). Each region carries its own theological significance.</p>',
    1
)
out = out.replace(
    '<h2>O Egito e a Terra de Gósen</h2>\n    <p>Israel habitou a região de <strong>Gósen</strong> (hebraico: גֹּשֶׁן), identificada com o <strong>Wadi Tumilat</strong>, no <strong>Delta Oriental do Nilo</strong>. Essa área era fértil, adequada para pastoreio, separada dos egípcios (que desprezavam pastores — Gn 46.34) e estrategicamente localizada na fronteira nordeste do Egito.</p>',
    '<h2>Egypt and the Land of Goshen</h2>\n    <p>Israel inhabited the region of <strong>Goshen</strong> (Hebrew: גֹּשֶׁן), identified with the <strong>Wadi Tumilat</strong> in the <strong>Eastern Nile Delta</strong>. This area was fertile, suitable for grazing, separated from the Egyptians (who despised shepherds — Gen 46:34), and strategically located on Egypt\'s northeastern frontier.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Gosén — Identificação</div>\n        <p>Localizada no Delta do Nilo, possivelmente nas proximidades de <strong>Tell el-Dab\'a</strong> (antiga Ávaris/Pi-Ramsés). Escavações arqueológicas revelaram presença semítica intensa nessa região durante o período do Segundo Período Intermediário e início do Novo Reino.</p>',
    '<div class="card-title">Goshen — Identification</div>\n        <p>Located in the Nile Delta, possibly near <strong>Tell el-Dab\'a</strong> (ancient Avaris/Pi-Ramesses). Archaeological excavations have revealed intense Semitic presence in this region during the Second Intermediate Period and early New Kingdom.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Cidades de Armazenamento</div>\n        <p><strong>Pitom</strong> e <strong>Ramsés</strong> (Êx 1.11) foram construídas com trabalho escravo israelita. Pi-Ramsés foi identificada com Tell el-Dab\'a / Qantir. Pitom é possivelmente Tell el-Maskhuta ou Tell er-Retaba.</p>',
    '<div class="card-title">Store Cities</div>\n        <p><strong>Pithom</strong> and <strong>Rameses</strong> (Exod 1:11) were built with Israelite slave labor. Pi-Ramesses has been identified with Tell el-Dab\'a / Qantir. Pithom is possibly Tell el-Maskhuta or Tell er-Retaba.</p>',
    1
)
out = out.replace(
    '<h2>Midiã — O Exílio Formativo</h2>\n    <p>Após matar o egípcio, Moisés fugiu para <strong>Midiã</strong> (Êx 2.15), região localizada na <strong>costa noroeste da Península Arábica</strong>, ao leste do Golfo de Ácaba (atual Arábia Saudita / sul da Jordânia). Lá viveu com Jetro (ou Reuel), sacerdote midianita, casou com Zípora e pastoreou ovelhas por quarenta anos.</p>',
    '<h2>Midian — The Formative Exile</h2>\n    <p>After killing the Egyptian, Moses fled to <strong>Midian</strong> (Exod 2:15), a region located on the <strong>northwestern coast of the Arabian Peninsula</strong>, east of the Gulf of Aqaba (modern Saudi Arabia / southern Jordan). There he lived with Jethro (also called Reuel), a Midianite priest, married Zipporah, and shepherded flocks for forty years.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Monte Horebe / Sinai</span>\n      <p>A queima da sarça ardente ocorreu no <strong>Monte Horebe</strong> (Êx 3.1), identificado com o Monte Sinai. A localização exata é debatida: a tradição cristã desde o século IV aponta para o <strong>Jebel Musa</strong> no sul da Península do Sinai (Egito), mas há hipóteses alternativas como o <strong>Jebel al-Lawz</strong> na Arábia Saudita. A narrativa indica proximidade com Midiã, o que favorece a hipótese arábica.</p>',
    '<span class="callout-type">Mount Horeb / Sinai</span>\n      <p>The burning bush episode occurred at <strong>Mount Horeb</strong> (Exod 3:1), identified with Mount Sinai. The exact location is debated: Christian tradition since the 4th century points to <strong>Jebel Musa</strong> in the southern Sinai Peninsula (Egypt), but alternative proposals include <strong>Jebel al-Lawz</strong> in Saudi Arabia. The narrative indicates proximity to Midian, which favors the Arabian hypothesis.</p>',
    1
)
out = out.replace(
    '<h2>A Rota do Êxodo</h2>\n    <p>A rota exata do Êxodo é um dos temas mais debatidos da arqueologia bíblica. O texto menciona que Deus <em>não os guiou pelo caminho da terra dos filisteus, embora fosse mais curto</em> (Êx 13.17), referindo-se à <strong>Via Maris</strong> costeira, rota militar egípcia bem guarnecida.</p>',
    '<h2>The Route of the Exodus</h2>\n    <p>The exact route of the Exodus is one of the most debated topics in biblical archaeology. The text notes that God <em>did not lead them by the way of the land of the Philistines, although that was nearer</em> (Exod 13:17), referring to the coastal <strong>Via Maris</strong>, a well-garrisoned Egyptian military road.</p>',
    1
)
out = out.replace('<div class="timeline-period">Ponto de partida</div>',
                  '<div class="timeline-period">Starting point</div>', 1)
out = out.replace(
    '<div class="timeline-title">Ramsés → Sucote → Étam</div>\n        <div class="timeline-text">Israel parte de Ramsés (Pi-Ramsés), campa em Sucote e depois em Étam "na borda do deserto" (Êx 13.20). Sucote é possivelmente Tell el-Maskhuta.</div>',
    '<div class="timeline-title">Rameses → Succoth → Etham</div>\n        <div class="timeline-text">Israel departs from Rameses (Pi-Ramesses), camps at Succoth and then at Etham "on the edge of the wilderness" (Exod 13:20). Succoth is possibly Tell el-Maskhuta.</div>',
    1
)
out = out.replace('<div class="timeline-period">Milagre da travessia</div>',
                  '<div class="timeline-period">Miracle of the crossing</div>', 1)
out = out.replace(
    '<div class="timeline-title">Travessia do Mar</div>\n        <div class="timeline-text">O <em>Yam Suph</em> (hebraico: ים סוף) — traduzido "Mar Vermelho" na LXX (Ἐρυθρὰ θάλασσα) — pode referir-se ao Mar Vermelho propriamente, ao Mar de Canas (lago ao norte) ou ao Golfo de Suez. O debate continua em aberto. O ponto central é o milagre divino, não a hidrografia.</div>',
    '<div class="timeline-title">Crossing of the Sea</div>\n        <div class="timeline-text">The <em>Yam Suph</em> (Hebrew: ים סוף) — translated "Red Sea" in the LXX (Ἐρυθρὰ θάλασσα) — may refer to the Red Sea proper, the Sea of Reeds (a northern lake), or the Gulf of Suez. The debate remains open. The central point is the divine miracle, not the hydrography.</div>',
    1
)
out = out.replace('<div class="timeline-period">Peregrinação</div>',
                  '<div class="timeline-period">Wilderness wandering</div>', 1)
out = out.replace(
    '<div class="timeline-title">Deserto do Sinai</div>\n        <div class="timeline-text">Israel percorre os desertos de Sur, Sin, Refidim, chegando ao Monte Sinai onde acampam por quase um ano (Êx 19 – Nm 10).</div>',
    '<div class="timeline-title">Sinai Desert</div>\n        <div class="timeline-text">Israel traverses the deserts of Shur, Sin, and Rephidim, arriving at Mount Sinai where they camp for nearly a year (Exod 19 – Num 10).</div>',
    1
)
out = out.replace('<div class="timeline-period">Crise e desvio</div>',
                  '<div class="timeline-period">Crisis and detour</div>', 1)
out = out.replace(
    '<div class="timeline-title">Cades-Barneia</div>\n        <div class="timeline-text">Após o relatório dos espias (Nm 13–14), Israel permanece 38 anos em Cades-Barneia e nos arredores do deserto de Parã. Cades é identificada com Ein el-Qudeirat ou Ein Qadeis, no nordeste do Sinai.</div>',
    '<div class="timeline-title">Kadesh-Barnea</div>\n        <div class="timeline-text">After the report of the spies (Num 13–14), Israel remains 38 years at Kadesh-Barnea and the surrounding wilderness of Paran. Kadesh is identified with Ein el-Qudeirat or Ein Qadeis, in northeastern Sinai.</div>',
    1
)
out = out.replace('<div class="timeline-period">Fim da jornada</div>',
                  '<div class="timeline-period">End of the journey</div>', 1)
out = out.replace(
    '<div class="timeline-title">Planícies de Moabe → Monte Nebo</div>\n        <div class="timeline-text">Israel contorna Edom e Moabe, derrota os reis Siom e Ogue, acampa nas planícies de Moabe (Abel-Sitim). Moisés sobe ao Monte Nebo (Pisgá), onde contempla Canaã e morre. Nebo é identificado com Jebel Neba, na Jordânia atual, altitude 817m.</div>',
    '<div class="timeline-title">Plains of Moab → Mount Nebo</div>\n        <div class="timeline-text">Israel bypasses Edom and Moab, defeats kings Sihon and Og, and camps on the plains of Moab (Abel-Shittim). Moses ascends Mount Nebo (Pisgah), views Canaan, and dies. Nebo is identified with Jebel Neba in modern Jordan, elevation 817m.</div>',
    1
)
out = out.replace(
    '<h2>Canaã — A Terra Prometida Não Alcançada</h2>\n    <p>A <strong>Terra de Canaã</strong> compreendia aproximadamente o território entre o Rio Jordão a leste, o Mar Mediterrâneo a oeste, o Líbano a norte e o Neguebe a sul — correspondendo ao atual Israel, Palestina, sul do Líbano e partes da Jordânia e Síria. Do Monte Nebo, Moisés contemplou: o Neguebe, o vale do Jordão, Jericó, os montes do norte até o Hermom (Dt 34.1–4).</p>',
    '<h2>Canaan — The Promised Land Not Entered</h2>\n    <p>The <strong>Land of Canaan</strong> encompassed roughly the territory between the Jordan River to the east, the Mediterranean Sea to the west, Lebanon to the north, and the Negev to the south — corresponding to modern Israel, Palestine, southern Lebanon, and parts of Jordan and Syria. From Mount Nebo, Moses surveyed: the Negev, the Jordan Valley, Jericho, and the northern hills as far as Hermon (Deut 34:1–4).</p>',
    1
)

# ══════════════════════════════════════════════════════════════════════════════
# Section: contexto-politico
# ══════════════════════════════════════════════════════════════════════════════
out = out.replace(
    '<span class="section-tag">História e Política</span>\n      <h1 class="section-title">O Cenário Político</h1>\n      <p class="section-lead">O Egito do Novo Reino, o poder do Faraó e o lugar de Israel como povo escravo e depois nação.</p>',
    '<span class="section-tag">History and Politics</span>\n      <h1 class="section-title">The Political Setting</h1>\n      <p class="section-lead">New Kingdom Egypt, the power of Pharaoh, and Israel\'s place as an enslaved people and emerging nation.</p>',
    1
)
out = out.replace(
    '<h2>O Egito do Novo Reino</h2>\n    <p>O contexto político de Moisés é o <strong>Egito do Novo Reino</strong> (c. 1550–1070 a.C.), um dos impérios mais poderosos da antiguidade. Após expulsar os Hicsos (povo semítico que governou o norte do Egito durante o Segundo Período Intermediário), os faraós da <strong>XVIII e XIX Dinastias</strong> reconstituíram o poder egípcio e expandiram seu domínio pelo Levante.</p>',
    '<h2>New Kingdom Egypt</h2>\n    <p>The political context of Moses is <strong>New Kingdom Egypt</strong> (c. 1550–1070 BC), one of the most powerful empires of antiquity. After expelling the Hyksos (a Semitic people who ruled northern Egypt during the Second Intermediate Period), the pharaohs of the <strong>18th and 19th Dynasties</strong> reconstituted Egyptian power and expanded their dominion throughout the Levant.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Contexto Político-Militar</span>\n      <p>O Egito do Novo Reino era uma <strong>teocracia militar</strong>: o Faraó era considerado filho e encarnação de Rá (o deus-sol), intermediário entre deuses e homens. Seu poder era absoluto. O exército egípcio era organizado, com infantaria, carros de guerra e marinha. A expulsão de Israel representava, portanto, não apenas uma derrota militar, mas uma crise teológica para o Egito — os deuses egípcios foram derrotados pelo YHWH de Israel.</p>',
    '<span class="callout-type">Political-Military Context</span>\n      <p>New Kingdom Egypt was a <strong>military theocracy</strong>: Pharaoh was considered the son and incarnation of Ra (the sun god), an intermediary between gods and men. His power was absolute. The Egyptian army was highly organized, with infantry, chariots, and a navy. The departure of Israel represented, therefore, not merely a military defeat but a theological crisis for Egypt — the Egyptian gods had been defeated by the YHWH of Israel.</p>',
    1
)
out = out.replace(
    '<h2>Qual foi o Faraó do Êxodo?</h2>\n    <p>Este é um dos debates mais longos da arqueologia bíblica. Há essencialmente três posições principais:</p>',
    '<h2>Who Was the Pharaoh of the Exodus?</h2>\n    <p>This is one of the longest-running debates in biblical archaeology. There are essentially three main positions:</p>',
    1
)
out = out.replace(
    '<th>Posição</th>\n          <th>Faraó da Opressão</th>\n          <th>Faraó do Êxodo</th>\n          <th>Base</th>',
    '<th>Position</th>\n          <th>Pharaoh of the Oppression</th>\n          <th>Pharaoh of the Exodus</th>\n          <th>Basis</th>',
    1
)
out = out.replace(
    '<td>Cronologia Tardia (c. 1250 a.C.)</td>\n          <td>Seti I (1294–1279)</td>\n          <td>Ramsés II (1279–1213)</td>\n          <td>Êx 1.11 menciona "Ramsés"; LXX; tendência secular</td>',
    '<td>Late Chronology (c. 1250 BC)</td>\n          <td>Seti I (1294–1279)</td>\n          <td>Ramesses II (1279–1213)</td>\n          <td>Exod 1:11 mentions "Rameses"; LXX; secular consensus</td>',
    1
)
out = out.replace(
    '<td>Cronologia Precoce (c. 1446 a.C.)</td>\n          <td>Tutmósis III (1479–1425)</td>\n          <td>Amenotep II (1427–1401)</td>\n          <td>1Rs 6.1 (480 anos antes do 4º ano de Salomão); Jz 11.26; At 13.19</td>',
    '<td>Early Chronology (c. 1446 BC)</td>\n          <td>Thutmose III (1479–1425)</td>\n          <td>Amenhotep II (1427–1401)</td>\n          <td>1 Kgs 6:1 (480 years before Solomon\'s 4th year); Judg 11:26; Acts 13:19</td>',
    1
)
out = out.replace(
    '<td>Proposta alternativa</td>\n          <td>Tutmósis I ou Tutmósis II</td>\n          <td>Hatchepsut / Tutmósis III</td>\n          <td>Algumas correlações com expulsão de semitas</td>',
    '<td>Alternative proposal</td>\n          <td>Thutmose I or Thutmose II</td>\n          <td>Hatshepsut / Thutmose III</td>\n          <td>Some correlations with Semitic expulsions</td>',
    1
)
out = out.replace(
    '<p>A cronologia conservadora (baseada em 1Rs 6.1) situa o Êxodo em <strong>1446 a.C.</strong>, colocando a opressão sob a XVIII Dinastia. Esta data correlaciona bem com as <em>Cartas de Amarna</em> (c. 1360 a.C.), que descrevem invasões dos <em>Habiru</em> em Canaã, possivelmente referindo-se aos israelitas sob Josué.</p>',
    '<p>The conservative chronology (based on 1 Kgs 6:1) places the Exodus in <strong>1446 BC</strong>, setting the oppression under the 18th Dynasty. This date correlates well with the <em>Amarna Letters</em> (c. 1360 BC), which describe invasions by the <em>Habiru</em> in Canaan, possibly referring to the Israelites under Joshua.</p>',
    1
)
out = out.replace(
    '<h2>Israel como Força de Trabalho Escravizada</h2>\n    <p>A política egípcia de escravização de povos conquistados ou refugiados era bem documentada. Os israelitas foram submetidos a <em>corvée</em> (trabalho forçado) em projetos de construção estatais — uma prática comum no Egito antigo. Êxodo 1.11 menciona que construíram <strong>Pitom e Ramsés</strong>, cidades de armazenamento para o Estado egípcio.</p>',
    '<h2>Israel as an Enslaved Workforce</h2>\n    <p>Egypt\'s policy of enslaving conquered or refugee peoples is well documented. The Israelites were subjected to <em>corvée</em> (forced labor) on state construction projects — a common practice in ancient Egypt. Exodus 1:11 states that they built <strong>Pithom and Rameses</strong>, store cities for the Egyptian state.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Política de Controle Demográfico</div>\n        <p>Êxodo 1.10 revela a lógica política do Faraó: temer que Israel, em caso de guerra, se aliasse ao inimigo. O infanticídio masculino (Êx 1.15–22) era uma política de eliminação demográfica — controle de uma minoria percebida como ameaça.</p>',
    '<div class="card-title">Policy of Demographic Control</div>\n        <p>Exodus 1:10 reveals Pharaoh\'s political logic: fear that Israel, in case of war, would join his enemies. The killing of male infants (Exod 1:15–22) was a policy of demographic elimination — control of a minority perceived as a threat.</p>',
    1
)
out = out.replace(
    '<div class="card-title">As Parteiras e a Resistência</div>\n        <p>Sifra e Puá (Êx 1.15) representam o primeiro ato de desobediência civil registrado na Bíblia. Elas temem a Deus mais que ao Faraó — prenunciando a ética do Novo Testamento de "obedecer a Deus antes que aos homens" (At 5.29).</p>',
    '<div class="card-title">The Midwives and Resistance</div>\n        <p>Shiphrah and Puah (Exod 1:15) represent the first act of civil disobedience recorded in the Bible. They fear God more than Pharaoh — foreshadowing the New Testament ethic of "obeying God rather than men" (Acts 5:29).</p>',
    1
)
out = out.replace(
    '<h2>Midiã — Contexto Geopolítico</h2>\n    <p>Os midianitas eram descendentes de Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
    '<h2>Midian — Geopolitical Context</h2>\n    <p>The Midianites were descendants of Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwestern Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who purchased Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses\'s father-in-law, was <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>',
    1
)
out = out.replace(
    '<h2>Os Povos de Canaã</h2>\n    <p>O cenário político da Terra Prometida incluía múltiplos povos-estados (cidades-estado cananéias) e reinos regionais. Durante os quarenta anos de peregrinação, Moisés lida politicamente com:</p>',
    '<h2>The Peoples of Canaan</h2>\n    <p>The political landscape of the Promised Land included multiple peoples (Canaanite city-states) and regional kingdoms. During the forty years of wandering, Moses dealt politically with:</p>',
    1
)
out = out.replace(
    '<span class="name-tag">Edom — Recusa de passagem (Nm 20)</span>\n      <span class="name-tag">Moabe — Maldição de Balaão (Nm 22–24)</span>\n      <span class="name-tag">Amorreus — Siom e Ogue derrotados (Nm 21)</span>\n      <span class="name-tag">Midiã — Guerra (Nm 31)</span>\n      <span class="name-tag">Cananeus de Arade (Nm 21.1–3)</span>',
    '<span class="name-tag">Edom — Denied passage (Num 20)</span>\n      <span class="name-tag">Moab — Balaam\'s curse (Num 22–24)</span>\n      <span class="name-tag">Amorites — Sihon and Og defeated (Num 21)</span>\n      <span class="name-tag">Midian — War (Num 31)</span>\n      <span class="name-tag">Canaanites of Arad (Num 21:1–3)</span>',
    1
)
out = out.replace(
    '<span class="callout-type">Significado Teológico-Político</span>\n      <p>O relato do Êxodo é uma declaração de guerra teológica: YHWH, o Deus de Israel, confronta e derrota o panteão egípcio. Cada praga ataca uma divindade específica egípcia. A décima praga — morte dos primogênitos — é o julgamento final sobre o próprio Faraó-deus. Politicamente, o Êxodo transforma Israel de povo sem terra e sem Estado em uma <strong>nação teocrática constituída pela Aliança do Sinai</strong>.</p>',
    '<span class="callout-type">Theological-Political Significance</span>\n      <p>The Exodus narrative is a declaration of theological war: YHWH, the God of Israel, confronts and defeats the Egyptian pantheon. Each plague targets a specific Egyptian deity. The tenth plague — death of the firstborn — is the final judgment against Pharaoh himself, the god-king. Politically, the Exodus transforms Israel from a landless, stateless people into a <strong>theocratic nation constituted by the Sinai Covenant</strong>.</p>',
    1
)

# ══════════════════════════════════════════════════════════════════════════════
# Section: vida
# ══════════════════════════════════════════════════════════════════════════════
out = out.replace(
    '<span class="section-tag">Biografia</span>\n      <h1 class="section-title">Nascimento, Formação e Chamado</h1>\n      <p class="section-lead">Da cesta nas águas à sarça ardente — a preparação soberana de Deus para seu instrumento.</p>',
    '<span class="section-tag">Biography</span>\n      <h1 class="section-title">Birth, Formation, and Calling</h1>\n      <p class="section-lead">From the basket on the waters to the burning bush — God\'s sovereign preparation of his instrument.</p>',
    1
)
out = out.replace(
    '<h2>Nascimento e Preservação — Êxodo 2.1–10</h2>\n    <p>Moisés nasceu de Amram e Joquebede, da tribo de Levi (Êx 6.20). Sua preservação do decreto de morte do Faraó é um episódio de providência divina: sua mãe o escondeu por três meses e depois o colocou em um <em>tebah</em> (תֵּבָה — a mesma palavra usada para a Arca de Noé), de junco impermeabilizado, no Rio Nilo.</p>',
    '<h2>Birth and Preservation — Exodus 2:1–10</h2>\n    <p>Moses was born to Amram and Jochebed, of the tribe of Levi (Exod 6:20). His preservation from Pharaoh\'s death decree is an episode of divine providence: his mother hid him for three months and then placed him in a <em>tebah</em> (תֵּבָה — the same word used for Noah\'s Ark), a waterproofed papyrus basket, on the Nile River.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Paralelo Tipológico</span>\n      <p>A <em>tebah</em> (cesta/arca) usada para salvar Moisés é a mesma palavra usada para a Arca de Noé (Gn 6–8). Ambas são instrumentos de preservação divina em meio às águas de julgamento. Moisés, salvo das águas, torna-se o libertador de Israel — que também seria salvo "através das águas" na travessia do mar.</p>',
    '<span class="callout-type">Typological Parallel</span>\n      <p>The <em>tebah</em> (basket/ark) used to save Moses is the same word used for Noah\'s Ark (Gen 6–8). Both are instruments of divine preservation amid the waters of judgment. Moses, saved from the waters, becomes the deliverer of Israel — who would also be saved "through the waters" at the sea crossing.</p>',
    1
)
out = out.replace(
    '<p>A filha do Faraó o encontrou, teve compaixão e o adotou. A própria mãe de Moisés, Joquebede, foi contratada como ama — um detalhe de ironia divina que o texto preserva com precisão.</p>',
    '<p>Pharaoh\'s daughter found him, had compassion, and adopted him. Moses\'s own mother, Jochebed, was hired as his nurse — a detail of divine irony that the text preserves with precision.</p>',
    1
)
out = out.replace(
    '<h2>Formação no Palácio — Êxodo 2.10; Atos 7.22</h2>\n    <p>Moisés foi "instruído em toda a sabedoria dos egípcios e era poderoso em palavras e obras" (At 7.22). Isso implica treinamento nas escolas de escribas egípcias (as <em>edubba</em>), que incluíam: literatura, astronomia, matemática, administração, lei, medicina e artes militares. Essa formação foi providencial — Moisés seria o autor do Pentateuco e o administrador de uma nação.</p>',
    '<h2>Formation in the Palace — Exodus 2:10; Acts 7:22</h2>\n    <p>Moses was "instructed in all the wisdom of the Egyptians and was mighty in his words and deeds" (Acts 7:22). This implies training in Egyptian scribal schools, which included: literature, astronomy, mathematics, administration, law, medicine, and military arts. This formation was providential — Moses would be the author of the Pentateuch and the administrator of a nation.</p>',
    1
)
out = out.replace(
    '<h2>O Homicídio e a Fuga — Êxodo 2.11–22</h2>\n    <p>Aos quarenta anos (At 7.23), ao ver um egípcio espancando um israelita, Moisés o matou. Quando o incidente foi exposto por um israelita ingrato, Moisés fugiu para Midiã. Este episódio revela: <strong>(1)</strong> sua identidade com o povo israelita, <strong>(2)</strong> seu impulso de justiça e <strong>(3)</strong> sua imaturidade — ainda não era o tempo de Deus (At 7.25 sugere que Moisés supôs que os israelitas entenderiam que Deus o usaria para libertá-los, mas eles não entenderam).</p>',
    '<h2>The Killing and Flight — Exodus 2:11–22</h2>\n    <p>At age forty (Acts 7:23), seeing an Egyptian beating an Israelite, Moses killed him. When the incident was exposed by an ungrateful Israelite, Moses fled to Midian. This episode reveals: <strong>(1)</strong> his identification with the Israelite people, <strong>(2)</strong> his impulse for justice, and <strong>(3)</strong> his immaturity — God\'s time had not yet come (Acts 7:25 suggests Moses assumed the Israelites would understand that God would use him to deliver them, but they did not).</p>',
    1
)
out = out.replace(
    '<h2>Midiã — A Escola do Deserto</h2>\n    <p>Quarenta anos de pastoreio foram a preparação para conduzir um povo pelo deserto. Moisés casou com <strong>Zípora</strong>, filha de Jetro (também chamado Reuel ou Hobabe), e teve dois filhos: <strong>Gérson</strong> ("sou estrangeiro aqui") e <strong>Eliezer</strong> ("meu Deus é socorro"). Cada nome revela a teologia existencial de Moisés no exílio.</p>',
    '<h2>Midian — The School of the Desert</h2>\n    <p>Forty years of shepherding were God\'s preparation for leading a people through the wilderness. Moses married <strong>Zipporah</strong>, daughter of Jethro (also called Reuel or Hobab), and had two sons: <strong>Gershom</strong> ("I am a sojourner here") and <strong>Eliezer</strong> ("my God is help"). Each name reveals Moses\'s existential theology in exile.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Passagem Central</span>\n      <p><strong>Êxodo 3.1 – 4.31</strong> é o texto primário. O evento ocorre no Monte Horebe (também chamado Sinai), enquanto Moisés pastoreia as ovelhas de seu sogro Jetro. Este é um dos mais longos e densos episódios de vocação profética em toda a Escritura — nenhum chamado divino no AT recebe tanto espaço narrativo quanto este.</p>',
    '<span class="callout-type">Central Passage</span>\n      <p><strong>Exodus 3:1 – 4:31</strong> is the primary text. The event occurs at Mount Horeb (also called Sinai), while Moses shepherds the flocks of his father-in-law Jethro. This is one of the longest and most theologically dense episodes of prophetic calling in all of Scripture — no other divine call in the OT receives as much narrative space as this one.</p>',
    1
)
out = out.replace(
    '<h3>Cena 1 — O Cenário e o Sinal (Êxodo 3.1–3)</h3>\n    <p>Moisés conduzia o rebanho pelo deserto e chegou a <strong>Horebe, o monte de Deus</strong> (Êx 3.1). O texto não explica por que aquele monte tinha esse nome — o narrador pressupõe que o leitor já sabe da santidade do lugar, ou talvez sinalize retrospectivamente que toda a história de Israel converge ali.</p>\n    <p>O que Moisés vê é descrito com precisão: <em>"uma sarça que ardia em fogo, mas a sarça não se consumia"</em> (Êx 3.2). A palavra hebraica para sarça é <strong>sneh</strong> (סְנֶה) — um arbusto espinhoso comum no deserto do Sinai, sem nenhuma majestade natural. O fogo que não consome é o paradoxo: fogo destrói, mas este não destrói. Presença divina que não aniquila.</p>\n    <p>Moisés raciocina consigo mesmo em voz alta no texto: <em>"Agora voltarei para ver esta grande visão — por que a sarça não se consome"</em> (Êx 3.3). É a curiosidade que o conduz — não uma visão imponente, não um exército angélico, mas um arbusto comum fazendo algo impossível. Deus usa o ordinário transformado para atrair o homem que vai transformar a história.</p>',
    '<h3>Scene 1 — The Setting and the Sign (Exodus 3:1–3)</h3>\n    <p>Moses was leading the flock through the wilderness and came to <strong>Horeb, the mountain of God</strong> (Exod 3:1). The text does not explain why that mountain already bore that name — the narrator assumes the reader already knows of the place\'s holiness, or perhaps signals retrospectively that all of Israel\'s history converges there.</p>\n    <p>What Moses sees is described with precision: <em>"a bush was burning, yet it was not consumed"</em> (Exod 3:2). The Hebrew word for bush is <strong>sneh</strong> (סְנֶה) — a common thorny shrub of the Sinai desert, possessing no natural majesty. The unconsuming fire is the paradox: fire destroys, but this fire does not. Divine presence that does not annihilate.</p>\n    <p>Moses reasons aloud in the text: <em>"I will turn aside to see this great sight, why the bush is not burned"</em> (Exod 3:3). It is curiosity that draws him — not an imposing vision, not an angelic army, but an ordinary bush doing something impossible. God uses the transformed ordinary to attract the man who will transform history.</p>',
    1
)
out = out.replace(
    '<h3>Cena 2 — A Teofania e o Chamado à Santidade (Êxodo 3.4–6)</h3>\n    <p>Quando YHWH vê que Moisés se voltou para olhar, <strong>chama-o pelo nome</strong>: <em>"Moisés, Moisés!"</em> A dupla repetição do nome (<em>Mosheh, Mosheh</em>) é uma marca de urgência e intimidade divina — a mesma forma usada com Abraão no sacrifício de Isaque (Gn 22.11), com Jacó em Peniel (Gn 46.2) e com Samuel (1Sm 3.10). Não é um chamado genérico: é pessoal, é histórico, é aliançado.</p>\n    <p>Moisés responde: <em>"Eis-me aqui"</em> (<em>hineni</em>, הִנֵּנִי) — a mesma palavra de disposição usada por Abraão (Gn 22.1), Jacó (Gn 31.11) e Samuel (1Sm 3.4). É a resposta do servo à voz do Soberano.</p>',
    '<h3>Scene 2 — The Theophany and the Call to Holiness (Exodus 3:4–6)</h3>\n    <p>When the Lord sees that Moses turned to look, he <strong>calls him by name</strong>: <em>"Moses, Moses!"</em> The double repetition of the name (<em>Mosheh, Mosheh</em>) is a mark of divine urgency and intimacy — the same form used with Abraham at the sacrifice of Isaac (Gen 22:11), with Jacob at Peniel (Gen 46:2), and with Samuel (1 Sam 3:10). This is not a generic call: it is personal, historical, and covenantal.</p>\n    <p>Moses answers: <em>"Here I am"</em> (<em>hineni</em>, הִנֵּנִי) — the same word of availability used by Abraham (Gen 22:1), Jacob (Gen 31:11), and Samuel (1 Sam 3:4). It is the servant\'s response to the voice of the Sovereign.</p>',
    1
)
out = out.replace(
    '<p>O primeiro comando divino é sobre a <strong>santidade do espaço</strong>: <em>"Não te chegues para cá; tira as sandálias dos pés, porque o lugar em que tu estás é terra santa"</em> (Êx 3.5). As sandálias separam o homem da terra — tirá-las é um ato de remoção da barreira, de contato direto com o sagrado. É a postura do ser humano diante da santidade de Deus: descalço, desarmado, sem proteção própria.</p>\n    <p>Deus então se <strong>identifica historicamente</strong>: <em>"Eu sou o Deus de teu pai, o Deus de Abraão, o Deus de Isaque, e o Deus de Jacó"</em> (Êx 3.6). Esta fórmula tripartite é decisiva: não é um deus genérico, não é uma nova divindade — é o mesmo Deus das promessas feitas séculos antes. A aliança abraâmica está em vigência. O Deus que fala não mudou.</p>\n    <p>A reação de Moisés é imediata: <em>"Moisés escondeu o rosto, porque teve medo de olhar para Deus"</em> (Êx 3.6). O mesmo homem que foi "instruído em toda a sabedoria dos egípcios" e que matou um egípcio sem hesitar agora esconde o rosto diante da presença divina. A santidade de Deus produz reverência genuína, não coragem presumida.</p>',
    '<p>The first divine command is about the <strong>holiness of space</strong>: <em>"Do not come near; take your sandals off your feet, for the place on which you are standing is holy ground"</em> (Exod 3:5). Sandals separate man from the earth — removing them is an act of barrier removal, of direct contact with the sacred. It is the posture of the human before the holiness of God: barefoot, unarmed, without self-protection.</p>\n    <p>God then <strong>identifies himself historically</strong>: <em>"I am the God of your father, the God of Abraham, the God of Isaac, and the God of Jacob"</em> (Exod 3:6). This tripartite formula is decisive: this is not a generic deity, not a new divinity — it is the same God of the promises made centuries before. The Abrahamic covenant is still in force. The God who speaks has not changed.</p>\n    <p>Moses\'s reaction is immediate: <em>"Moses hid his face, for he was afraid to look at God"</em> (Exod 3:6). The same man who was "instructed in all the wisdom of the Egyptians" and who killed an Egyptian without hesitation now hides his face before the divine presence. The holiness of God produces genuine reverence, not presumptuous courage.</p>',
    1
)
out = out.replace(
    '"Então disse: Não se aproxime! Tire as sandálias dos pés, pois o lugar em que você está é terra santa. Disse ainda: Eu sou o Deus de seu pai, o Deus de Abraão, o Deus de Isaque e o Deus de Jacó. Moisés então escondeu o rosto, porque teve medo de olhar para Deus."\n      <span class="scripture-ref">Êxodo 3.5–6 — NAA</span>',
    '"Then he said, \'Do not come near; take your sandals off your feet, for the place on which you are standing is holy ground.\' And he said, \'I am the God of your father, the God of Abraham, the God of Isaac, and the God of Jacob.\' And Moses hid his face, for he was afraid to look at God."\n      <span class="scripture-ref">Exodus 3:5–6 — ESV</span>',
    1
)
out = out.replace(
    '<h3>Cena 3 — Deus Ouviu, Deus Viu, Deus Desceu (Êxodo 3.7–10)</h3>\n    <p>O discurso divino que se segue é teologicamente revolucionário. YHWH descreve sua própria ação com três verbos que formam uma progressão desconcertante para qualquer leitor do mundo antigo:</p>',
    '<h3>Scene 3 — God Heard, God Saw, God Came Down (Exodus 3:7–10)</h3>\n    <p>The divine speech that follows is theologically revolutionary. YHWH describes his own action with three verbs that form a startling progression for any reader of the ancient world:</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Os Três Verbos Divinos — Êxodo 3.7–8</span>\n      <p><strong>"Certamente vi"</strong> (<em>ra\'oh ra\'iti</em>) — infinitivo absoluto em hebraico, enfatizando a completude e certeza da visão. Deus não apenas viu: <em>viu completamente</em>. Ele não estava distraído. Não ignorou. A opressão de Israel estava no campo de visão divino o tempo todo.<br><br>\n      <strong>"Ouvi o seu clamor"</strong> — O grito dos escravos subiu a Deus (Êx 2.23–25). Oração e sofrimento têm direção — eles chegam a algum lugar.<br><br>\n      <strong>"Desci para livrá-lo"</strong> — Este é o verbo mais surpreendente. O Deus transcendente <em>desce</em>. Esta é a lógica da Encarnação prefigurada no Sinai: a distância entre o Criador e a criatura é atravessada por iniciativa divina, não humana. João 1.14 é o eco perfeito: <em>"O Verbo se fez carne e habitou entre nós."</em></p>',
    '<span class="callout-type">The Three Divine Verbs — Exodus 3:7–8</span>\n      <p><strong>"I have surely seen"</strong> (<em>ra\'oh ra\'iti</em>) — the Hebrew infinitive absolute, emphasizing the completeness and certainty of the seeing. God did not merely see: he <em>saw completely</em>. He was not distracted. He did not ignore it. Israel\'s oppression was in the divine field of vision the entire time.<br><br>\n      <strong>"I have heard their cry"</strong> — The cry of the slaves ascended to God (Exod 2:23–25). Prayer and suffering have a direction — they arrive somewhere.<br><br>\n      <strong>"I have come down to deliver"</strong> — This is the most surprising verb. The transcendent God <em>comes down</em>. This is the logic of the Incarnation prefigured at Sinai: the distance between Creator and creature is crossed by divine initiative, not human effort. John 1:14 is the perfect echo: <em>"The Word became flesh and dwelt among us."</em></p>',
    1
)
out = out.replace(
    '<p>O mandato é claro: <em>"Vem agora, pois, e enviar-te-ei ao Faraó, para que tires o meu povo, os filhos de Israel, do Egito"</em> (Êx 3.10). Moisés, o exilado, o fugitivo, o pastor de ovelhas de outro homem — é enviado ao maior rei da terra.</p>',
    '<p>The mandate is clear: <em>"Come, I will send you to Pharaoh that you may bring my people, the children of Israel, out of Egypt"</em> (Exod 3:10). Moses, the exile, the fugitive, the shepherd of another man\'s flocks — is sent to the greatest king on earth.</p>',
    1
)
out = out.replace(
    '<h3>Cena 4 — As Cinco Objeções de Moisés (Êxodo 3.11–4.17)</h3>\n    <p>O que se segue é um dos diálogos mais humanos e honestos da Escritura. Moisés não aceita o chamado com entusiasmo — ele resiste, argumenta e recua, e cada objeção revela algo tanto de sua humanidade quanto do caráter de Deus:</p>',
    '<h3>Scene 4 — The Five Objections of Moses (Exodus 3:11–4:17)</h3>\n    <p>What follows is one of the most human and honest dialogues in all of Scripture. Moses does not accept the call with enthusiasm — he resists, argues, and retreats, and each objection reveals something both of his humanity and of God\'s character:</p>',
    1
)
# Five objections
out = out.replace(
    '<div class="timeline-period">Êxodo 3.11 — 1ª Objeção</div>\n        <div class="timeline-title">"Quem sou eu para ir ao Faraó?"</div>\n        <div class="timeline-text"><strong>A objeção:</strong> Inadequação pessoal. O homem que cresceu como príncipe egípcio agora não se sente apto. Quarenta anos no deserto como pastor de ovelhas de outro homem destruíram qualquer senso de status ou capacidade.<br><br>\n        <strong>A resposta divina:</strong> <em>"Eu serei contigo"</em> (Êx 3.12). Deus não refuta a autoavaliação de Moisés — ela pode até ser correta. Mas a questão não é a capacidade de Moisés; é a presença de Deus. O sinal dado é surpreendente: <em>"Quando tirares o povo do Egito, servireis a Deus neste monte."</em> É uma promessa futura dada como garantia presente — um sinal que só pode ser confirmado depois da obediência, não antes.</div>',
    '<div class="timeline-period">Exodus 3:11 — 1st Objection</div>\n        <div class="timeline-title">"Who am I to go to Pharaoh?"</div>\n        <div class="timeline-text"><strong>The objection:</strong> Personal inadequacy. The man who grew up as an Egyptian prince no longer feels capable. Forty years in the desert as another man\'s shepherd have destroyed any sense of status or ability.<br><br>\n        <strong>God\'s response:</strong> <em>"I will be with you"</em> (Exod 3:12). God does not refute Moses\'s self-assessment — it may even be correct. But the question is not Moses\'s capacity; it is God\'s presence. The sign given is surprising: <em>"When you have brought the people out of Egypt, you shall serve God on this mountain."</em> It is a future promise given as present guarantee — a sign that can only be confirmed after obedience, not before.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 3.13 — 2ª Objeção</div>\n        <div class="timeline-title">"Qual é o teu nome?"</div>\n        <div class="timeline-text"><strong>A objeção:</strong> Falta de credencial identificável. No mundo antigo, o nome divino era a chave do acesso e da autoridade. Israel precisaria saber qual deus os enviava.<br><br>\n        <strong>A resposta divina:</strong> <em>"EU SOU O QUE SOU"</em> — <strong>Ehyeh Asher Ehyeh</strong> (אֶהְיֶה אֲשֶׁר אֶהְיֶה) — Êxodo 3.14. A raiz verbal <em>hayah</em> (ser/existir) no imperfeito hebraico pode significar presente ou futuro: "Eu sou" ou "Eu serei". A ambiguidade é teológica: este Deus existe independentemente de qualquer coisa criada, e existirá ao longo de toda a história da redenção. Em seguida Deus instrui Moisés a usar o Nome completo: <strong>YHWH</strong> (יהוה), derivado da mesma raiz, na terceira pessoa: "Aquele que é / que será". Este é o Nome do pacto, o Nome que conecta Deus às promessas feitas aos patriarcas (Êx 3.15).</div>',
    '<div class="timeline-period">Exodus 3:13 — 2nd Objection</div>\n        <div class="timeline-title">"What is your name?"</div>\n        <div class="timeline-text"><strong>The objection:</strong> Lack of identifiable credentials. In the ancient world, the divine name was the key of access and authority. Israel would need to know which god was sending him.<br><br>\n        <strong>God\'s response:</strong> <em>"I AM WHO I AM"</em> — <strong>Ehyeh Asher Ehyeh</strong> (אֶהְיֶה אֲשֶׁר אֶהְיֶה) — Exodus 3:14. The verbal root <em>hayah</em> (to be/exist) in the Hebrew imperfect can mean present or future: "I am" or "I will be". The ambiguity is theological: this God exists independently of anything created, and will exist throughout all of redemptive history. God then instructs Moses to use the full Name: <strong>YHWH</strong> (יהוה), derived from the same root, in the third person: "He who is / who will be." This is the covenant Name, the Name that connects God to the promises made to the patriarchs (Exod 3:15).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 4.1 — 3ª Objeção</div>\n        <div class="timeline-title">"E se não me crerem?"</div>\n        <div class="timeline-text"><strong>A objeção:</strong> Falta de autoridade verificável. E se os anciões de Israel rejeitassem Moisés como mensageiro divino?<br><br>\n        <strong>A resposta divina:</strong> Deus concede três sinais milagrosos (Êx 4.2–9): (1) A vara que se torna serpente e retorna a vara quando Moisés a segura pela cauda — símbolo de autoridade sobre as forças da morte; (2) A mão que fica leprosa e é curada — símbolo de poder sobre a corrupção; (3) A água do Nilo transformada em sangue — o mesmo sinal que inaugurará a primeira praga. Os sinais não são truques: são antecipações do que Deus fará por Israel.</div>',
    '<div class="timeline-period">Exodus 4:1 — 3rd Objection</div>\n        <div class="timeline-title">"But suppose they will not believe me?"</div>\n        <div class="timeline-text"><strong>The objection:</strong> Lack of verifiable authority. What if the elders of Israel rejected Moses as a divine messenger?<br><br>\n        <strong>God\'s response:</strong> God grants three miraculous signs (Exod 4:2–9): (1) The staff that becomes a serpent and returns to a staff when Moses grabs its tail — symbol of authority over the forces of death; (2) The hand made leprous and healed — symbol of power over corruption; (3) Nile water turned to blood — the same sign that will inaugurate the first plague. The signs are not tricks: they are anticipations of what God will do for Israel.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 4.10 — 4ª Objeção</div>\n        <div class="timeline-title">"Não sou homem de fácil palavra"</div>\n        <div class="timeline-text"><strong>A objeção:</strong> Limitação de fala. Seja uma gagueira, um defeito de pronúncia ou simplesmente timidez retórica — Moisés alega ser incapaz de falar com eloquência. A ironia é que Atos 7.22 diz que ele era "poderoso em palavras" — talvez quarenta anos de solidão no deserto hajam embotado essa capacidade.<br><br>\n        <strong>A resposta divina:</strong> <em>"Quem fez a boca do homem? Ou quem faz o mudo, ou o surdo, ou o que vê, ou o cego? Não sou eu, o SENHOR?"</em> (Êx 4.11). Deus não promete curar a limitação — promete estar com a boca de Moisés e ensiná-lo o que dizer (Êx 4.12). O instrumento não precisa ser perfeito; precisa ser disponível.</div>',
    '<div class="timeline-period">Exodus 4:10 — 4th Objection</div>\n        <div class="timeline-title">"I am not eloquent"</div>\n        <div class="timeline-text"><strong>The objection:</strong> Limitation of speech. Whether a stutter, a speech defect, or simply rhetorical timidity — Moses claims he cannot speak with eloquence. The irony is that Acts 7:22 says he was "mighty in his words" — perhaps forty years of desert solitude had dulled that capacity.<br><br>\n        <strong>God\'s response:</strong> <em>"Who has made man\'s mouth? Who makes him mute, or deaf, or seeing, or blind? Is it not I, the Lord?"</em> (Exod 4:11). God does not promise to cure the limitation — he promises to be with Moses\'s mouth and teach him what to say (Exod 4:12). The instrument does not need to be perfect; it needs to be available.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 4.13 — 5ª Objeção</div>\n        <div class="timeline-title">"Envia, rogo-te, por mão de quem quiseres enviar"</div>\n        <div class="timeline-text"><strong>A objeção:</strong> Recusa velada. Após quatro objeções respondidas, Moisés ainda resiste. Esta última não tem argumento — é pura relutância. Ele simplesmente não quer ir.<br><br>\n        <strong>A resposta divina:</strong> <em>"E a ira do SENHOR se acendeu contra Moisés"</em> (Êx 4.14). Esta é a única vez em todo o episódio em que Deus demonstra ira. A paciência divina tem profundidade — mas a relutância persistente diante de uma vocação clara tem consequências. Deus, contudo, não retira o chamado: concede Aarão como porta-voz, mas Moisés continuará sendo o canal da palavra divina. A graça persiste mesmo na disciplina.</div>',
    '<div class="timeline-period">Exodus 4:13 — 5th Objection</div>\n        <div class="timeline-title">"Please send someone else"</div>\n        <div class="timeline-text"><strong>The objection:</strong> Veiled refusal. After four answered objections, Moses still resists. This last one has no argument — it is pure reluctance. He simply does not want to go.<br><br>\n        <strong>God\'s response:</strong> <em>"The anger of the Lord was kindled against Moses"</em> (Exod 4:14). This is the only moment in the entire episode where God demonstrates anger. Divine patience has depth — but persistent reluctance before a clear calling has consequences. God, however, does not withdraw the call: he grants Aaron as a spokesman, but Moses will remain the channel of the divine word. Grace persists even in discipline.</div>',
    1
)
out = out.replace(
    '<h3>Cena 5 — O Retorno ao Egito (Êxodo 4.18–31)</h3>\n    <p>Moisés retorna a Jetro, seu sogro, e pede licença para voltar ao Egito — com uma motivação discreta: <em>"para ver se ainda vivem meus irmãos"</em> (Êx 4.18). Não menciona a missão divina. Jetro o abençoa: <em>"Vai em paz."</em></p>\n    <p>Durante o caminho de volta ao Egito ocorre um episódio enigmático e perturbador (Êx 4.24–26): <em>"E no caminho, na estalagem, o SENHOR o encontrou e procurou matá-lo."</em> Deus que acabara de chamar Moisés agora ameaça sua vida. O motivo é inferido pelo que Zípora faz imediatamente: circuncida seu filho e toca os pés de Moisés com o prepúcio. O filho de Moisés não fora circuncidado — Moisés havia negligenciado o sinal da aliança abraâmica (Gn 17) em seu próprio lar. O mensageiro da aliança não podia liderar o povo da aliança sem honrar o sinal da aliança. Zípora, a midianita, salva Moisés da ira de Deus nesse momento.</p>\n    <p>Ao chegar ao Egito, Moisés e Aarão reúnem os anciões de Israel. Aarão repete as palavras divinas; Moisés realiza os sinais. O texto registra a resposta do povo com emoção contida: <em>"E o povo creu; e quando ouviram que o SENHOR havia visitado os filhos de Israel, e que havia visto a sua aflição, então se inclinaram e adoraram"</em> (Êx 4.31). A sarça no deserto moveu Israel à adoração.</p>',
    '<h3>Scene 5 — The Return to Egypt (Exodus 4:18–31)</h3>\n    <p>Moses returns to Jethro, his father-in-law, and asks permission to return to Egypt — with a discreet motivation: <em>"to see whether they are still alive"</em> (Exod 4:18). He does not mention the divine mission. Jethro blesses him: <em>"Go in peace."</em></p>\n    <p>On the way back to Egypt a cryptic and disturbing episode occurs (Exod 4:24–26): <em>"At a lodging place on the way the Lord met him and sought to put him to death."</em> The God who had just called Moses now threatens his life. The reason is inferred from what Zipporah immediately does: she circumcises their son and touches Moses\'s feet with the foreskin. Moses\'s son had not been circumcised — Moses had neglected the sign of the Abrahamic covenant (Gen 17) in his own household. The messenger of the covenant could not lead the covenant people without honoring the sign of the covenant. Zipporah, the Midianite, saves Moses from God\'s wrath in this moment.</p>\n    <p>Upon arriving in Egypt, Moses and Aaron gather the elders of Israel. Aaron repeats the divine words; Moses performs the signs. The text records the people\'s response with restrained emotion: <em>"And the people believed; and when they heard that the Lord had visited the people of Israel and that he had seen their affliction, they bowed their heads and worshiped"</em> (Exod 4:31). The bush in the desert had moved Israel to worship.</p>',
    1
)
out = out.replace(
    '<h2>O Nome Divino — YHWH</h2>\n    <p>A revelação do Nome divino em Êxodo 3.14 é o ponto teológico mais alto do chamado de Moisés:</p>',
    '<h2>The Divine Name — YHWH</h2>\n    <p>The revelation of the divine Name in Exodus 3:14 is the theological high point of Moses\'s calling:</p>',
    1
)
out = out.replace(
    '"Deus respondeu a Moisés: EU SOU O QUE SOU. E acrescentou: Assim você dirá aos israelitas: EU SOU me enviou a vocês."\n      <span class="scripture-ref">Êxodo 3.14 — NAA</span>',
    '"God said to Moses, \'I AM WHO I AM.\' And he said, \'Say this to the people of Israel: I AM has sent me to you.\'"\n      <span class="scripture-ref">Exodus 3:14 — ESV</span>',
    1
)
out = out.replace(
    '<p>O tetragrama <strong>יהוה</strong> (YHWH) deriva da raiz <em>hayah</em> — "ser, existir". As interpretações são múltiplas: <em>"Eu Sou o que Sou"</em> (aseidade — existência independente), <em>"Eu Serei o que Serei"</em> (fidelidade às promessas futuras), ou <em>"Eu faço ser o que faço ser"</em> (poder criador). O contexto favorece a dimensão de <strong>fidelidade da aliança</strong> — este é o Deus que cumprirá suas promessas a Abraão, Isaque e Jacó.</p>',
    '<p>The tetragrammaton <strong>יהוה</strong> (YHWH) derives from the root <em>hayah</em> — "to be, to exist." Interpretations are multiple: <em>"I Am Who I Am"</em> (aseity — independent existence), <em>"I Will Be What I Will Be"</em> (faithfulness to future promises), or <em>"I cause to be what I cause to be"</em> (creative power). The context favors the dimension of <strong>covenant faithfulness</strong> — this is the God who will fulfill his promises to Abraham, Isaac, and Jacob.</p>',
    1
)

# ══════════════════════════════════════════════════════════════════════════════
# Section: pragas
# ══════════════════════════════════════════════════════════════════════════════
out = out.replace(
    '<span class="section-tag">Libertação</span>\n      <h1 class="section-title">As Dez Pragas e o Êxodo</h1>\n      <p class="section-lead">O confronto entre YHWH e o Faraó — julgamento sobre os deuses do Egito e libertação do povo da aliança.</p>',
    '<span class="section-tag">Liberation</span>\n      <h1 class="section-title">The Ten Plagues and the Exodus</h1>\n      <p class="section-lead">The confrontation between YHWH and Pharaoh — judgment on the gods of Egypt and the liberation of the covenant people.</p>',
    1
)
out = out.replace(
    '<h2>Estrutura Teológica das Pragas</h2>\n    <p>As dez pragas (Êx 7–12) não são acidentes naturais ampliados — são atos de guerra teológica de YHWH contra o panteão egípcio. Êxodo 12.12 é explícito: <em>"Executarei juízos contra todos os deuses do Egito."</em> Cada praga tem correspondência com uma divindade específica do panteão egípcio.</p>',
    '<h2>Theological Structure of the Plagues</h2>\n    <p>The ten plagues (Exod 7–12) are not amplified natural disasters — they are acts of YHWH\'s theological warfare against the Egyptian pantheon. Exodus 12:12 is explicit: <em>"On all the gods of Egypt I will execute judgments."</em> Each plague corresponds to a specific deity of the Egyptian pantheon.</p>',
    1
)

# ══════════════════════════════════════════════════════════════════════════════
# Read the plague table section to translate it
# ══════════════════════════════════════════════════════════════════════════════

out = out.replace('<div class="plague-name">Águas em Sangue</div>\n          <div class="plague-ref">Êx 7.14–25 · Ataca Hápi (deus do Nilo)</div>',
                  '<div class="plague-name">Waters into Blood</div>\n          <div class="plague-ref">Exod 7:14–25 · Targets Hapi (god of the Nile)</div>', 1)
out = out.replace('<div class="plague-num">II</div>', '<div class="plague-num">II</div>', 1)  # no-op placeholder

# Read plague items from file
with open('at-pentateuco/index.html', encoding='utf-8') as f:
    src_orig = f.read()

# Extract all plague items and replace
plague_pt_en = [
    ('Rãs', 'Frogs', 'Êx 8.1–15 · Ataca Heqet (deusa das rãs)', 'Exod 8:1–15 · Targets Heqet (frog goddess)'),
    ('Piolhos / Mosquitos', 'Gnats / Lice', 'Êx 8.16–19 · Ataca Geb (deus da terra)', 'Exod 8:16–19 · Targets Geb (god of the earth)'),
    ('Moscas / Enxame', 'Flies / Swarms', 'Êx 8.20–32 · Ataca Khepri (deus-besouro)', 'Exod 8:20–32 · Targets Khepri (scarab god)'),
    ('Morte do Gado', 'Death of Livestock', 'Êx 9.1–7 · Ataca Ápis (touro sagrado)', 'Exod 9:1–7 · Targets Apis (sacred bull)'),
    ('Úlceras', 'Boils', 'Êx 9.8–12 · Ataca Sekhmet (deusa da medicina)', 'Exod 9:8–12 · Targets Sekhmet (goddess of medicine)'),
    ('Granizo', 'Hail', 'Êx 9.13–35 · Ataca Nut (deusa do céu)', 'Exod 9:13–35 · Targets Nut (sky goddess)'),
    ('Gafanhotos', 'Locusts', 'Êx 10.1–20 · Ataca Osiris (deus da vegetação)', 'Exod 10:1–20 · Targets Osiris (god of vegetation)'),
    ('Trevas', 'Darkness', 'Êx 10.21–29 · Ataca Rá (deus-sol)', 'Exod 10:21–29 · Targets Ra (sun god)'),
    ('Morte dos Primogênitos', 'Death of the Firstborn', 'Êx 12 · Ataca o próprio Faraó — filho de Rá', 'Exod 12 · Targets Pharaoh himself — son of Ra'),
]
for pt_name, en_name, pt_ref, en_ref in plague_pt_en:
    out = out.replace(
        f'<div class="plague-name">{pt_name}</div>\n          <div class="plague-ref">{pt_ref}</div>',
        f'<div class="plague-name">{en_name}</div>\n          <div class="plague-ref">{en_ref}</div>',
        1
    )


# ═══ pragas body ═══
out = out.replace(
    '<span class="callout-type">Padrão Estrutural</span>',
    '<span class="callout-type">Structural Pattern</span>',
    1
)
out = out.replace(
    'As pragas seguem um padrão triádico (1–3, 4–6, 7–9, + 10): nas primeiras de cada tríade, Moisés encontra o Faraó pela manhã; nas segundas, vai ao palácio; nas terceiras, não há aviso prévio. A escalada é progressiva, e a distinção entre Israel e Egito a partir da 4ª praga demonstra o caráter de eleição da ação divina.',
    'The plagues follow a triadic pattern (1–3, 4–6, 7–9, + 10): in the first of each triad, Moses meets Pharaoh in the morning; in the second, he goes to the palace; in the third, there is no prior warning. The escalation is progressive, and the distinction between Israel and Egypt from the 4th plague onward demonstrates the elective character of the divine action.',
    1
)
out = out.replace(
    '<h2>A Páscoa — Êxodo 12</h2>',
    '<h2>The Passover — Exodus 12</h2>',
    1
)

# ═══ sinai + golden calf ═══
out = out.replace(
    '<span class="section-tag">Revelação</span>\n      <h1 class="section-title">Sinai, a Aliança e a Lei</h1>\n      <p class="section-lead">A constituição da nação — Deus estabelece Israel como seu povo da aliança mediante lei, tabernáculo e sacrifício.</p>',
    '<span class="section-tag">Revelation</span>\n      <h1 class="section-title">Sinai, the Covenant, and the Law</h1>\n      <p class="section-lead">The constitution of the nation — God establishes Israel as his covenant people through law, tabernacle, and sacrifice.</p>',
    1
)
out = out.replace(
    '<h2>A Aliança do Sinai — Êxodo 19–24</h2>\n    <p>A Aliança do Sinai é uma aliança de lei (<em>berith</em>), estruturalmente similar aos tratados suzeranos hititas do segundo milênio a.C.: <strong>(1)</strong> preâmbulo identificando o soberano, <strong>(2)</strong> prólogo histórico das bênçãos passadas, <strong>(3)</strong> estipulações, <strong>(4)</strong> cláusula de depósito e leitura, <strong>(5)</strong> lista de testemunhas, <strong>(6)</strong> bênçãos e maldições. Êxodo 20 começa exatamente assim: "Eu sou o SENHOR teu Deus, que te tirei da terra do Egito..."</p>',
    '<h2>The Sinai Covenant — Exodus 19–24</h2>\n    <p>The Sinai Covenant is a law covenant (<em>berith</em>), structurally similar to Hittite suzerainty treaties of the second millennium BC: <strong>(1)</strong> preamble identifying the sovereign, <strong>(2)</strong> historical prologue of past blessings, <strong>(3)</strong> stipulations, <strong>(4)</strong> deposit and public reading clause, <strong>(5)</strong> list of witnesses, <strong>(6)</strong> blessings and curses. Exodus 20 begins exactly this way: "I am the Lord your God, who brought you out of the land of Egypt..."</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Graça Precede a Lei</span>\n      <p>A ordem é decisiva: Deus resgata Israel do Egito (graça) <em>antes</em> de dar a Lei. A obediência à Lei não é condição do resgate — é resposta ao resgate. Este é o fundamento reformado da teologia da aliança: a lei é resposta de gratidão ao evangelho da graça, não merecimento da salvação.</p>',
    '<span class="callout-type">Grace Precedes Law</span>\n      <p>The order is decisive: God rescues Israel from Egypt (grace) <em>before</em> giving the Law. Obedience to the Law is not the condition of rescue — it is the response to rescue. This is the Reformed foundation of covenant theology: the law is a grateful response to the gospel of grace, not a means of earning salvation.</p>',
    1
)
out = out.replace(
    '<h2>Os Dez Mandamentos — Êxodo 20 / Deuteronômio 5</h2>\n    <p>O Decálogo (<em>aseret hadevarim</em> — "as dez palavras") é a constituição moral de Israel e, segundo a tradição reformada, a lei moral de Deus aplicável a toda a humanidade. Estrutura-se em dois grupos: deveres para com Deus (mandamentos 1–4) e deveres para com o próximo (5–10), refletindo o resumo de Cristo: "amar a Deus e ao próximo" (Mc 12.29–31).</p>',
    '<h2>The Ten Commandments — Exodus 20 / Deuteronomy 5</h2>\n    <p>The Decalogue (<em>aseret hadevarim</em> — "the ten words") is the moral constitution of Israel and, according to the Reformed tradition, the moral law of God applicable to all humanity. It is structured in two groups: duties toward God (commandments 1–4) and duties toward neighbor (5–10), reflecting Christ\'s summary: "to love God and neighbor" (Mark 12:29–31).</p>',
    1
)
out = out.replace(
    '<h2>O Tabernáculo — Êxodo 25–40</h2>\n    <p>A construção do Tabernáculo (<em>mishkán</em>, מִשְׁכָּן — "morada, habitação") ocupa treze capítulos de Êxodo — mais espaço que qualquer outra instrução. Isso é significativo: a habitação de Deus entre seu povo é o objetivo central da aliança. O Tabernáculo era uma teologia visual — cada elemento apontava para Cristo:</p>',
    '<h2>The Tabernacle — Exodus 25–40</h2>\n    <p>The construction of the Tabernacle (<em>mishkan</em>, מִשְׁכָּן — "dwelling, habitation") occupies thirteen chapters of Exodus — more space than any other instruction. This is significant: God\'s dwelling among his people is the central goal of the covenant. The Tabernacle was a visual theology — every element pointed to Christ:</p>',
    1
)
out = out.replace(
    '<div class="card-title">Elementos do Tabernáculo e sua Tipologia</div>\n        <p>• <strong>Átrio externo:</strong> O altar de bronze — expiação pelos sacrifícios<br>\n        • <strong>Lugar Santo:</strong> Mesa dos pães da proposição, Candelabro, Altar de incenso<br>\n        • <strong>Santo dos Santos:</strong> Arca da Aliança com propiciatório (<em>kapporet</em>) — o trono de Deus, lugar do sangue expiatório<br>\n        • <strong>O Véu:</strong> Separação entre o homem e Deus — rasgado na morte de Cristo (Mc 15.38; Hb 9.8)</p>',
    '<div class="card-title">Tabernacle Elements and Their Typology</div>\n        <p>• <strong>Outer court:</strong> The bronze altar — atonement through sacrifices<br>\n        • <strong>Holy Place:</strong> Table of the bread of the Presence, Lampstand, Altar of incense<br>\n        • <strong>Holy of Holies:</strong> Ark of the Covenant with the mercy seat (<em>kapporet</em>) — God\'s throne, the place of atoning blood<br>\n        • <strong>The Veil:</strong> Separation between man and God — torn at Christ\'s death (Mark 15:38; Heb 9:8)</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Arca da Aliança</div>\n        <p>Continha: <strong>(1)</strong> as duas tábuas da Lei (Dt 10.5), <strong>(2)</strong> o vaso de maná (Êx 16.33–34; Hb 9.4), <strong>(3)</strong> a vara de Arão que floresceu (Nm 17; Hb 9.4). Simboliza: a lei (santidade divina), o maná (provisão), a vara (autoridade sacerdotal). Cristo é o cumprimento de todos os três: a lei personificada, o pão da vida, o Sumo Sacerdote.</p>',
    '<div class="card-title">The Ark of the Covenant</div>\n        <p>Contained: <strong>(1)</strong> the two stone tablets of the Law (Deut 10:5), <strong>(2)</strong> a jar of manna (Exod 16:33–34; Heb 9:4), <strong>(3)</strong> Aaron\'s staff that budded (Num 17; Heb 9:4). It symbolizes: the law (divine holiness), the manna (provision), the staff (priestly authority). Christ is the fulfillment of all three: the law personified, the bread of life, the High Priest.</p>',
    1
)
out = out.replace(
    '<h2>O Bezerro de Ouro — Êxodo 32–34</h2>',
    '<h2>The Golden Calf — Exodus 32–34</h2>',
    1
)
out = out.replace(
    '<span class="callout-type">Passagem Central</span>\n      <p><strong>Êxodo 32.1 – 34.35</strong> é o texto primário, com referências paralelas em Deuteronômio 9.7–10.11. Este episódio é narrado como a maior crise espiritual da história de Israel — ocorrida no momento mais sagrado: enquanto Deus entregava a Lei ao mediador no alto do monte, o povo quebrava aquela mesma lei ao pé do monte. O texto é estruturado em três movimentos: o pecado (cap. 32), a intercessão (32–33) e a restauração da aliança (cap. 34).</p>',
    '<span class="callout-type">Central Passage</span>\n      <p><strong>Exodus 32:1 – 34:35</strong> is the primary text, with parallel references in Deuteronomy 9:7–10:11. This episode is narrated as the greatest spiritual crisis in Israel\'s history — occurring at the most sacred moment: while God was delivering the Law to the mediator at the top of the mountain, the people were breaking that same law at its foot. The text is structured in three movements: the sin (ch. 32), the intercession (32–33), and the restoration of the covenant (ch. 34).</p>',
    1
)
out = out.replace(
    '<h3>Ato 1 — O Pecado: O Monte e o Vale (Êxodo 32.1–6)</h3>',
    '<h3>Act 1 — The Sin: The Mountain and the Valley (Exodus 32:1–6)</h3>',
    1
)
out = out.replace(
    'Moisés havia subido ao Monte Sinai para receber a Lei diretamente de Deus. O texto de Êxodo 24.18 registra: <em>"E Moisés entrou no meio da nuvem, e subiu ao monte; e esteve Moisés no monte quarenta dias e quarenta noites."</em> Quarenta dias de silêncio total — sem sinal, sem mensagem, sem retorno visível.',
    'Moses had ascended Mount Sinai to receive the Law directly from God. The text of Exodus 24:18 records: <em>"Moses entered the cloud and went up on the mountain. And Moses was on the mountain forty days and forty nights."</em> Forty days of total silence — no sign, no message, no visible return.',
    1
)
out = out.replace(
    'É esse vácuo que precipita a crise. <strong>Êxodo 32.1:</strong> <em>"Vendo o povo que Moisés tardava em descer do monte, ajuntou-se ao redor de Arão e disse-lhe: Levanta-te, faze-nos deuses que vão adiante de nós; porque não sabemos o que sucedeu a este Moisés, o homem que nos tirou da terra do Egito."</em>',
    'It is this vacuum that precipitates the crisis. <strong>Exodus 32:1:</strong> <em>"When the people saw that Moses delayed to come down from the mountain, the people gathered themselves together to Aaron and said to him, \'Up, make us gods who shall go before us. As for this Moses, the man who brought us up out of the land of Egypt, we do not know what has become of him.\'"</em>',
    1
)
out = out.replace(
    '<div class="card-title">A Impaciência como Raiz</div>\n        <p>O povo não espera nem quarenta dias por Moisés. Eles tinham acabado de comprometer-se solenemente à aliança (Êx 24.7: <em>"tudo o que o SENHOR falou faremos e obedeceremos"</em>). A tinta da aliança mal havia secado. A fé que não aguenta o silêncio de Deus busca um substituto visível.</p>',
    '<div class="card-title">Impatience as the Root</div>\n        <p>The people cannot wait even forty days for Moses. They had just solemnly committed themselves to the covenant (Exod 24:7: <em>"All that the Lord has spoken we will do, and we will be obedient"</em>). The ink of the covenant had barely dried. Faith that cannot endure God\'s silence seeks a visible substitute.</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Redefinição de Moisés</div>\n        <p>Note como o povo descreve Moisés: <em>"este Moisés, o homem que nos tirou da terra do Egito."</em> Não YHWH que os tirou — mas <em>Moisés</em>. Quando o mediador humano desaparece, o povo perde sua âncora. Isso revela que a fé deles estava em Moisés, não em YHWH.</p>',
    '<div class="card-title">The Redefinition of Moses</div>\n        <p>Note how the people describe Moses: <em>"this Moses, the man who brought us up out of the land of Egypt."</em> Not YHWH who brought them out — but <em>Moses</em>. When the human mediator disappears, the people lose their anchor. This reveals that their faith was in Moses, not in YHWH.</p>',
    1
)
out = out.replace(
    'Arão cede sem resistência. Pede os brincos de ouro das mulheres e filhos, os funde, esculpe e declara: <em>"Estes são os teus deuses, ó Israel, que te tiraram da terra do Egito"</em> (Êx 32.4). A mesma frase que o povo havia usado de Moisés, agora aplicada ao ídolo de ouro. Em seguida, Arão constrói um altar e declara: <em>"Amanhã será festa ao SENHOR"</em> (Êx 32.5) — como se o bezerro fosse uma representação de YHWH, não uma substituição.',
    'Aaron yields without resistance. He asks for the golden earrings of the women and children, melts them, shapes them, and declares: <em>"These are your gods, O Israel, who brought you up out of the land of Egypt"</em> (Exod 32:4). The same phrase the people had used of Moses, now applied to the golden idol. Then Aaron builds an altar and declares: <em>"Tomorrow shall be a feast to the Lord"</em> (Exod 32:5) — as if the calf were a representation of YHWH, not a replacement.',
    1
)
out = out.replace(
    '<span class="callout-type">O Bezerro no Contexto Egípcio</span>\n      <p>O touro/bezerro de ouro (<em>egel massekhah</em>, עֵגֶל מַסֵּכָה — "bezerro de metal fundido") não era uma invenção israelita. Na cultura egípcia, o touro Ápis era a encarnação do poder divino — adorado como deus em Mênfis. No Canaã, o deus El era representado como touro. Israel, recém-saída do Egito, recaiu numa forma de adoração familiar: visível, controlável, estático. Queriam um deus que pudesse ver, não um Deus que as nuvens ocultavam no monte.</p>',
    '<span class="callout-type">The Calf in Egyptian Context</span>\n      <p>The golden bull/calf (<em>egel massekhah</em>, עֵגֶל מַסֵּכָה — "cast metal calf") was not an Israelite invention. In Egyptian culture, the Apis bull was the incarnation of divine power — worshiped as a god in Memphis. In Canaan, the god El was represented as a bull. Israel, fresh out of Egypt, relapsed into a familiar form of worship: visible, controllable, static. They wanted a god they could see, not a God hidden by clouds on the mountain.</p>',
    1
)
out = out.replace(
    '<h3>Ato 2 — A Ira Divina e a Primeira Intercessão (Êxodo 32.7–14)</h3>',
    '<h3>Act 2 — Divine Wrath and the First Intercession (Exodus 32:7–14)</h3>',
    1
)
out = out.replace(
    'Deus interrompe a entrega da Lei para informar Moisés do que está acontecendo no vale. Sua linguagem é de distanciamento furioso: <em>"Desce, porque o teu povo, que tiraste da terra do Egito, se corrompeu"</em> (Êx 32.7). Repare: Deus não diz "meu povo" — diz <strong>"teu povo"</strong>. É uma linguagem de rejeição temporária, espelhando a que o povo havia usado de Moisés.',
    'God interrupts the giving of the Law to inform Moses of what is happening in the valley. His language is one of furious distancing: <em>"Go down, for your people, whom you brought up out of the land of Egypt, have corrupted themselves"</em> (Exod 32:7). Notice: God does not say "my people" — he says <strong>"your people."</strong> It is a language of temporary rejection, mirroring what the people had said about Moses.',
    1
)
out = out.replace(
    'O decreto divino é devastador: <em>"Agora, pois, deixa-me, para que a minha ira se acenda contra eles e os consuma; e de ti farei uma grande nação"</em> (Êx 32.10). Deus oferece a Moisés o que havia prometido a Abraão — fazer dele uma nação grande. É uma oferta extraordinária, e é uma prova: o que Moisés fará com ela?',
    'The divine decree is devastating: <em>"Now therefore let me alone, that my wrath may burn hot against them and I may consume them, in order that I may make a great nation of you"</em> (Exod 32:10). God offers Moses what he had promised Abraham — to make him a great nation. It is an extraordinary offer, and it is a test: what will Moses do with it?',
    1
)
out = out.replace(
    'Moisés recusa. Sua intercessão em Êxodo 32.11–13 é um dos discursos mais ousados da Bíblia inteira — Moisés <em>argumenta contra Deus</em> usando os próprios valores de Deus:',
    "Moses refuses. His intercession in Exodus 32:11–13 is one of the boldest speeches in all of Scripture — Moses <em>argues against God</em> using God's own values:",
    1
)
out = out.replace(
    '"Por que arderia a ira do <span style="font-variant:small-caps">Senhor</span> contra o seu povo, que você tirou do Egito com grande poder e com mão forte? Por que os egípcios diriam: Com más intenções ele os tirou, para matá-los nas montanhas e exterminá-los da face da terra? Abandone o ardor da sua ira e arrependa-se do mal contra o seu povo. Lembre-se de Abraão, Isaque e Israel, seus servos, aos quais você jurou por si mesmo..."\n      <span class="scripture-ref">Êxodo 32.11–13 — NAA</span>',
    '"O <span style="font-variant:small-caps">Lord</span>, why does your wrath burn hot against your people, whom you have brought out of the land of Egypt with great power and with a mighty hand? Why should the Egyptians say, \'With evil intent did he bring them out, to kill them in the mountains and to consume them from the face of the earth\'? Turn from your burning anger and relent from this disaster against your people. Remember Abraham, Isaac, and Israel, your servants, to whom you swore by your own self..."\n      <span class="scripture-ref">Exodus 32:11–13 — ESV</span>',
    1
)
out = out.replace(
    'Moisés usa <strong>três argumentos</strong>: (1) a reputação de Deus diante dos egípcios — "o que dirão as nações?"; (2) a natureza do próprio Deus como misericordioso; (3) as promessas aos patriarcas como fundamento inabalável da aliança. São os mesmos argumentos que qualquer advogado de defesa usaria — e funcionam. O texto registra: <em>"E o SENHOR se arrependeu do mal que dissera que havia de fazer ao seu povo"</em> (Êx 32.14).',
    'Moses uses <strong>three arguments</strong>: (1) God\'s reputation before the Egyptians — "what will the nations say?"; (2) the very nature of God as merciful; (3) the promises to the patriarchs as the unshakeable foundation of the covenant. These are the same arguments any defense attorney would use — and they work. The text records: <em>"And the Lord relented from the disaster that he had spoken of bringing on his people"</em> (Exod 32:14).',
    1
)
out = out.replace(
    '<h3>Ato 3 — A Descida do Monte e o Julgamento (Êxodo 32.15–29)</h3>',
    '<h3>Act 3 — Descent from the Mountain and Judgment (Exodus 32:15–29)</h3>',
    1
)
out = out.replace(
    'Moisés desce o monte carregando as duas tábuas de pedra — escritas "dos dois lados... e a escritura era escritura de Deus, gravada nas tábuas" (Êx 32.15–16). Josué, que havia esperado mais abaixo, ouve o barulho no acampamento e o interpreta como som de guerra. Moisés corrige: é canto, não batalha.',
    'Moses descends the mountain carrying the two stone tablets — written "on both sides... and the writing was the writing of God, engraved on the tablets" (Exod 32:15–16). Joshua, who had been waiting lower down, hears the noise in the camp and interprets it as the sound of war. Moses corrects him: it is singing, not battle.',
    1
)
out = out.replace(
    'Ao se aproximar e ver o bezerro e as danças, <strong>Moisés irou-se e atirou as tábuas</strong> da mão, quebrando-as ao pé do monte (Êx 32.19). O gesto é profundamente simbólico: a aliança foi quebrada primeiro pelo povo — Moisés apenas expressa visivelmente o que já acontecera espiritualmente. A Lei foi destruída antes mesmo de ser lida.',
    "As he draws near and sees the calf and the dancing, <strong>Moses's anger burned hot and he threw the tablets</strong> from his hands, breaking them at the foot of the mountain (Exod 32:19). The gesture is profoundly symbolic: the covenant was broken first by the people — Moses merely makes visible what had already happened spiritually. The Law was destroyed before it was even read.",
    1
)
out = out.replace(
    'Moisés então executa um julgamento triplo sobre o bezerro:',
    'Moses then executes a threefold judgment upon the calf:',
    1
)
out = out.replace(
    '<span class="callout-type">O Julgamento Sobre o Bezerro — Êxodo 32.20</span>\n      <p>Moisés <strong>(1) pegou o bezerro</strong> que fizeram, <strong>(2) queimou-o</strong> no fogo, <strong>(3) moeu-o</strong> até virar pó, <strong>(4) espalhou sobre as águas</strong> e <strong>(5) fez os israelitas beber</strong>. Este ritual de destruição tem paralelos com a lei das águas amargas de Números 5 (a mulher suspeita de adultério bebe as águas com o pó da maldição). Israel cometera adultério espiritual com seu deus; agora bebe as consequências da idolatria — literalmente. A aliança com YHWH era um casamento; o bezerro foi adultério.</p>',
    '<span class="callout-type">The Judgment on the Calf — Exodus 32:20</span>\n      <p>Moses <strong>(1) took the calf</strong> they had made, <strong>(2) burned it</strong> with fire, <strong>(3) ground it</strong> to powder, <strong>(4) scattered it on the water</strong>, and <strong>(5) made the Israelites drink it</strong>. This destruction ritual has parallels with the bitter water law of Numbers 5 (the woman suspected of adultery drinks the cursed water with the dust). Israel had committed spiritual adultery against their God; now they drink the consequences of idolatry — literally. The covenant with YHWH was a marriage; the calf was adultery.</p>',
    1
)
out = out.replace(
    'Moisés confronta Arão, que oferece uma das desculpas mais patéticas da Escritura: <em>"Eles me deram o ouro, e eu o lancei no fogo, e saiu este bezerro"</em> (Êx 32.24). Arão nega sua agência — o bezerro simplesmente <em>saiu</em> do fogo por conta própria. O líder que cedeu à pressão popular agora tenta se isentar da responsabilidade.',
    'Moses confronts Aaron, who offers one of the most pathetic excuses in Scripture: <em>"They gave me the gold, so I threw it into the fire, and out came this calf"</em> (Exod 32:24). Aaron denies his agency — the calf simply <em>came out</em> of the fire on its own. The leader who yielded to popular pressure now attempts to exempt himself from responsibility.',
    1
)
out = out.replace(
    'Moisés convoca os que estão com YHWH. Os levitas se apresentam. Por ordem de Moisés, percorrem o acampamento com espadas e matam cerca de três mil homens (Êx 32.28). O julgamento é severo e preciso: não toda a nação, mas os instigadores e os que persistiram na rebelião.',
    "Moses calls for those who are on the Lord's side. The Levites come forward. At Moses's command, they go through the camp with swords and kill about three thousand men (Exod 32:28). The judgment is severe and precise: not the entire nation, but the instigators and those who persisted in rebellion.",
    1
)
out = out.replace(
    '<h3>Ato 4 — A Segunda Intercessão: "Risca-me do Teu Livro" (Êxodo 32.30–35)</h3>',
    '<h3>Act 4 — The Second Intercession: "Blot Me Out of Your Book" (Exodus 32:30–35)</h3>',
    1
)
out = out.replace(
    'No dia seguinte, Moisés sobe novamente ao monte para fazer propiciação pelo pecado do povo. Sua intercessão atinge o ponto mais extremo possível:',
    "The next day, Moses goes up again to the mountain to make atonement for the people's sin. His intercession reaches the most extreme point possible:",
    1
)
out = out.replace(
    '"Mas agora, se você perdoar o pecado deles... Caso contrário, risque-me do livro que você escreveu."\n      <span class="scripture-ref">Êxodo 32.32 — NAA</span>',
    '"But now, if you will forgive their sin — but if not, please blot me out of your book that you have written."\n      <span class="scripture-ref">Exodus 32:32 — ESV</span>',
    1
)
out = out.replace(
    'Moisés oferece sua própria vida — sua existência no livro de Deus — como substituto pelo povo. Ele pede para ser riscado (<em>machah</em>, מְחֵה — apagar, obliterar) do livro divino se o povo não puder ser perdoado. Paulo usará linguagem quase idêntica em Romanos 9.3: <em>"porque eu mesmo desejaria ser anátema, separado de Cristo, por amor de meus irmãos."</em>',
    'Moses offers his own life — his existence in God\'s book — as a substitute for the people. He asks to be blotted out (<em>machah</em>, מְחֵה — to erase, obliterate) from the divine book if the people cannot be forgiven. Paul will use nearly identical language in Romans 9:3: <em>"For I could wish that I myself were accursed and cut off from Christ for the sake of my brothers."</em>',
    1
)
out = out.replace(
    'Mas Deus responde com um princípio inabalável: <em>"Quem pecou contra mim, a esse riscarei do meu livro"</em> (Êx 32.33). A substituição que Moisés propõe não é possível — não porque Deus é cruel, mas porque nenhum homem pecador pode ser o substituto expiatório de outro. A tipologia aqui aponta diretamente para Cristo: somente o Filho sem pecado poderia ser riscado <em>em lugar de</em> outros. O que Moisés desejou e não pôde fazer, Cristo fez.',
    'But God responds with an unshakeable principle: <em>"Whoever has sinned against me, I will blot out of my book"</em> (Exod 32:33). The substitution Moses proposes is not possible — not because God is cruel, but because no sinful man can be the atoning substitute for another. The typology here points directly to Christ: only the sinless Son could be blotted out <em>in place of</em> others. What Moses desired and could not do, Christ did.',
    1
)
out = out.replace(
    '<h3>Ato 5 — A Tenda da Congregação e o Rosto de Moisés (Êxodo 33–34)</h3>',
    '<h3>Act 5 — The Tent of Meeting and the Face of Moses (Exodus 33–34)</h3>',
    1
)
out = out.replace(
    'Após o pecado do bezerro, Deus anuncia que não subirá no meio do povo — pois os consumiria pelo caminho (Êx 33.3). É um momento de ruptura na presença divina. Moisés monta a <strong>Tenda da Congregação</strong> fora do acampamento — a presença de Deus se afastou para a periferia. Quando Moisés entrava na tenda, a coluna de nuvem descia (Êx 33.9), e o povo observava de longe, adorando cada um à porta de sua tenda.',
    "After the sin of the calf, God announces that he will not go up in the midst of the people — for he would consume them on the way (Exod 33:3). It is a moment of rupture in the divine presence. Moses pitches the <strong>Tent of Meeting</strong> outside the camp — God's presence has withdrawn to the periphery. When Moses entered the tent, the pillar of cloud would descend (Exod 33:9), and the people watched from a distance, each worshiping at his own tent door.",
    1
)
out = out.replace(
    'É nesse contexto — de distância divina após o maior pecado de Israel — que Moisés pede algo audacioso: <em>"Mostra-me, rogo-te, a tua glória"</em> (Êx 33.18). E Deus concede — não a visão direta da face divina (que nenhum homem pode ver e viver — Êx 33.20), mas a passagem da <em>bondade</em> de Deus diante de Moisés, e a proclamação do Nome.',
    'It is in this context — of divine distance after Israel\'s greatest sin — that Moses asks for something audacious: <em>"Please show me your glory"</em> (Exod 33:18). And God grants it — not the direct vision of the divine face (which no man can see and live — Exod 33:20), but the passing of God\'s <em>goodness</em> before Moses, and the proclamation of the Name.',
    1
)
out = out.replace(
    'A renovação da aliança em Êxodo 34 começa com Moisés talhando novas tábuas de pedra para substituir as que ele havia quebrado. O detalhe é teologicamente significativo: as primeiras tábuas foram feitas e escritas por Deus (Êx 32.16); as segundas também são escritas por Deus (Êx 34.1), mas <em>talhadas por Moisés</em>. Após o pecado, há cooperação humana no processo de restauração.',
    'The renewal of the covenant in Exodus 34 begins with Moses chiseling new stone tablets to replace those he had broken. The detail is theologically significant: the first tablets were made and written by God (Exod 32:16); the second are also written by God (Exod 34:1), but <em>chiseled by Moses</em>. After sin, there is human cooperation in the process of restoration.',
    1
)
out = out.replace(
    'Quando Moisés desce do monte pela segunda vez com as tábuas renovadas, ocorre o detalhe físico mais extraordinário da narrativa: <em>"a pele do seu rosto resplandecia"</em> (Êx 34.29–35, Hb: <em>qaran</em>, קָרַן — literalmente "irradiava raios"). A presença de Deus deixou uma marca visível no rosto de Moisés — tanto que os israelitas temiam se aproximar. Moisés precisou cobrir o rosto com um véu ao falar com o povo, removendo-o apenas para entrar na presença de Deus.',
    'When Moses descends the mountain a second time with the renewed tablets, the most extraordinary physical detail in the narrative occurs: <em>"the skin of his face shone"</em> (Exod 34:29–35, Heb: <em>qaran</em>, קָרַן — literally "sent out rays"). God\'s presence left a visible mark on Moses\'s face — so much so that the Israelites were afraid to come near him. Moses had to put a veil over his face when speaking to the people, removing it only when entering the presence of God.',
    1
)
out = out.replace(
    '<span class="callout-type">Paulo e o Véu — 2 Coríntios 3.7–18</span>\n      <p>Paulo usa o véu de Moisés como tipologia em 2 Coríntios 3. O véu não era para proteger o povo da glória — era para ocultar que a glória estava <em>desaparecendo</em> (3.13). O ministério da lei era glorioso, mas temporário. Em Cristo, o véu é removido (3.14–16), e nós contemplamos "a glória do Senhor a face descoberta" e somos transformados "de glória em glória" (3.18). O que Moisés experimentou parcialmente — e teve que ocultar — é o que os crentes possuem permanentemente em Cristo.</p>',
    '<span class="callout-type">Paul and the Veil — 2 Corinthians 3:7–18</span>\n      <p>Paul uses the veil of Moses as typology in 2 Corinthians 3. The veil was not to protect the people from the glory — it was to conceal that the glory was <em>fading</em> (3:13). The ministry of the law was glorious, but temporary. In Christ, the veil is removed (3:14–16), and we behold "the glory of the Lord with unveiled face" and are transformed "from one degree of glory to another" (3:18). What Moses experienced partially — and had to hide — is what believers possess permanently in Christ.</p>',
    1
)
out = out.replace(
    '<h2>A Teofania Plena — Êxodo 33–34</h2>\n    <p>Após a crise, Moisés pede ver a glória de Deus (Êx 33.18). Deus passa diante dele proclamando seu Nome — Êxodo 34.6–7 é a mais completa autodeclaração de Deus no AT:</p>',
    "<h2>The Full Theophany — Exodus 33–34</h2>\n    <p>After the crisis, Moses asks to see God's glory (Exod 33:18). God passes before him proclaiming his Name — Exodus 34:6–7 is the most complete self-declaration of God in the OT:</p>",
    1
)
out = out.replace(
    '"O <span style="font-variant:small-caps">Senhor</span>! O <span style="font-variant:small-caps">Senhor</span>! Deus compassivo e misericordioso, tardio em irar-se, transbordante de amor leal e de fidelidade, que mantém o amor leal por milhares, e perdoa a iniquidade, a transgressão e o pecado; que não absolve o culpado, e que pune a iniquidade dos pais nos filhos..."\n      <span class="scripture-ref">Êxodo 34.6–7 — NAA</span>',
    '"The <span style="font-variant:small-caps">Lord</span>, the <span style="font-variant:small-caps">Lord</span>, a God merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness, keeping steadfast love for thousands, forgiving iniquity and transgression and sin, but who will by no means clear the guilty, visiting the iniquity of the fathers on the children..."\n      <span class="scripture-ref">Exodus 34:6–7 — ESV</span>',
    1
)
out = out.replace(
    'Este texto (chamado pelos rabinos de <em>Shloshah Asar Middot</em> — as treze medidas divinas) é citado ou ecoado em pelo menos 15 passagens do AT (Nm 14.18; Sl 86.15; 103.8; 145.8; Jl 2.13; Jn 4.2; Mq 7.18 etc.) — demonstrando que é o credo teológico central de Israel sobre o caráter de Deus.',
    "This text (called by the rabbis the <em>Shloshah Asar Middot</em> — the thirteen divine attributes) is cited or echoed in at least 15 OT passages (Num 14:18; Ps 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2; Mic 7:18, etc.) — demonstrating that it is Israel's central theological creed about the character of God.",
    1
)

# ═══ deserto + teologia + nt + pentateuco ═══
out = out.replace(
    '<span class="section-tag">Peregrinação</span>\n      <h1 class="section-title">O Deserto, as Crises e a Morte de Moisés</h1>\n      <p class="section-lead">Quarenta anos de julgamento, fidelidade, falhas humanas e providência divina no deserto.</p>',
    '<span class="section-tag">Wilderness</span>\n      <h1 class="section-title">The Desert, the Crises, and the Death of Moses</h1>\n      <p class="section-lead">Forty years of judgment, faithfulness, human failure, and divine providence in the wilderness.</p>',
    1
)
out = out.replace(
    '<h2>A Estrutura de Números</h2>\n    <p>O livro de Números registra a geração condenada (capítulos 1–25) e a nova geração (capítulos 26–36). A tragédia central é a incredulidade em Cades-Barneia (Nm 13–14), que condena uma geração inteira a morrer no deserto. Hebreus 3–4 usa este evento como advertência escatológica: a incredulidade endurece o coração e impede a entrada no descanso de Deus.</p>',
    "<h2>The Structure of Numbers</h2>\n    <p>The book of Numbers records the condemned generation (chapters 1–25) and the new generation (chapters 26–36). The central tragedy is the unbelief at Kadesh-Barnea (Num 13–14), which condemns an entire generation to die in the wilderness. Hebrews 3–4 uses this event as an eschatological warning: unbelief hardens the heart and prevents entry into God's rest.</p>",
    1
)
out = out.replace(
    '<div class="timeline-period">Números 11</div>\n        <div class="timeline-title">Murmuração — O Desejo pela Carne</div>\n        <div class="timeline-text">Israel anseia pelos alimentos do Egito. YHWH envia codornizes em abundância — mas também uma praga. O lugar é chamado Quibrote-Taavá: "sepulcros da cobiça." O padrão é recorrente: ingratidão, queixa, juízo, misericórdia.</div>',
    '<div class="timeline-period">Numbers 11</div>\n        <div class="timeline-title">Grumbling — The Craving for Meat</div>\n        <div class="timeline-text">Israel craves the food of Egypt. YHWH sends quail in abundance — but also a plague. The place is called Kibroth-hattaavah: "graves of craving." The pattern is recurrent: ingratitude, complaint, judgment, mercy.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 12</div>\n        <div class="timeline-title">Rebelião de Aarão e Miriã</div>\n        <div class="timeline-text">A oposição ao casamento de Moisés com a mulher etíope e ao seu ministério exclusivo. YHWH defende Moisés, declarando-o único a quem fala "face a face, não por visões" (Nm 12.6–8). Miriã é castigada com lepra; Moisés intercede por ela.</div>',
    '<div class="timeline-period">Numbers 12</div>\n        <div class="timeline-title">The Rebellion of Aaron and Miriam</div>\n        <div class="timeline-text">Opposition to Moses\'s marriage to the Cushite woman and to his exclusive ministry. YHWH defends Moses, declaring him the only one to whom he speaks "face to face, not in riddles" (Num 12:6–8). Miriam is struck with leprosy; Moses intercedes for her.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 13–14</div>\n        <div class="timeline-title">Os Doze Espias — A Crise de Cades</div>\n        <div class="timeline-text">Dez espias trazem relatório negativo; apenas Calebe e Josué confiam em Deus. A incredulidade da congregação provoca o decreto divino: a geração adulta morrerá no deserto em quarenta anos. Nova intercessão de Moisés (Nm 14.13–19) apela ao caráter de Deus (Êx 34.6–7).</div>',
    '<div class="timeline-period">Numbers 13–14</div>\n        <div class="timeline-title">The Twelve Spies — The Crisis at Kadesh</div>\n        <div class="timeline-text">Ten spies bring a negative report; only Caleb and Joshua trust God. The congregation\'s unbelief triggers the divine decree: the adult generation will die in the wilderness over forty years. A new intercession by Moses (Num 14:13–19) appeals to God\'s character (Exod 34:6–7).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 16–17</div>\n        <div class="timeline-title">Rebelião de Coré, Datã e Abirão</div>\n        <div class="timeline-text">Rebelião sacerdotal e civil contra Moisés e Arão. A terra abre e engole os rebeldes; fogo consome os 250 oferentes de incenso. A vara de Arão que floresceu confirma o sacerdócio levítico. Hebreus 5 aplica esta tipologia ao sacerdócio de Cristo.</div>',
    '<div class="timeline-period">Numbers 16–17</div>\n        <div class="timeline-title">The Rebellion of Korah, Dathan, and Abiram</div>\n        <div class="timeline-text">Priestly and civil rebellion against Moses and Aaron. The earth opens and swallows the rebels; fire consumes the 250 incense-offering leaders. Aaron\'s staff that budded confirms the Levitical priesthood. Hebrews 5 applies this typology to Christ\'s priesthood.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 20</div>\n        <div class="timeline-title">O Pecado de Moisés em Meriba — Por Que Ele Não Entrou em Canaã</div>\n        <div class="timeline-text">Deus ordena falar à rocha para produzir água. Moisés, irritado, golpeia a rocha duas vezes dizendo "ouvi-nos, rebeldes!" — arrogando a si e a Arão o crédito do milagre ("nós vos daremos água"). O julgamento: Moisés não entrará em Canaã. Paulo (1Co 10.4) afirma que a rocha era Cristo.</div>',
    '<div class="timeline-period">Numbers 20</div>\n        <div class="timeline-title">Moses\'s Sin at Meribah — Why He Did Not Enter Canaan</div>\n        <div class="timeline-text">God commands speaking to the rock to produce water. Moses, angry, strikes the rock twice saying "Hear now, you rebels!" — arrogating to himself and Aaron the credit for the miracle ("shall we bring water for you?"). The judgment: Moses will not enter Canaan. Paul (1 Cor 10:4) states that the rock was Christ.</div>',
    1
)
out = out.replace(
    '<h2>Por Que Moisés Não Entrou na Terra Prometida — Análise Completa</h2>',
    '<h2>Why Moses Did Not Enter the Promised Land — Complete Analysis</h2>',
    1
)
out = out.replace(
    '<span class="callout-type">Passagem Central</span>\n      <p><strong>Números 20.1–13</strong> é o texto primário do pecado. O decreto de exclusão é confirmado em <strong>Números 20.12; 27.12–14</strong> e reiterado por Moisés em primeira pessoa em <strong>Deuteronômio 1.37; 3.23–28; 4.21–22; 32.48–52</strong>. A morte é narrada em <strong>Deuteronômio 34.1–8</strong>. Cada uma dessas passagens acrescenta uma camada diferente de perspectiva — exegética, teológica e pessoal.</p>',
    '<span class="callout-type">Central Passage</span>\n      <p><strong>Numbers 20:1–13</strong> is the primary text of the sin. The exclusion decree is confirmed in <strong>Numbers 20:12; 27:12–14</strong> and reiterated by Moses in the first person in <strong>Deuteronomy 1:37; 3:23–28; 4:21–22; 32:48–52</strong>. The death is narrated in <strong>Deuteronomy 34:1–8</strong>. Each of these passages adds a different layer of perspective — exegetical, theological, and personal.</p>',
    1
)
out = out.replace(
    '<h3>O Contexto Imediato — Números 20.1–13</h3>\n    <p>A cena ocorre em <strong>Cades</strong>, no deserto de Zim, no primeiro mês do quadragésimo ano da peregrinação (cf. Nm 33.38). O povo chegara ao mesmo lugar onde trinta e oito anos antes havia falhado com os espias — e agora murmura outra vez pela falta de água. Miriã havia morrido naquele mesmo lugar (Nm 20.1) — talvez contribuindo para o estado emocional de Moisés.</p>\n    <p>Deus ordena a Moisés com clareza: <em>"Toma a vara, e reúne a congregação, tu e Arão, teu irmão, e falai à rocha diante dos olhos deles, e ela dará a sua água"</em> (Nm 20.8). O comando é triplo e explícito: (1) toma a vara; (2) reúne o povo; (3) <strong>fala</strong> à rocha.</p>',
    '<h3>The Immediate Context — Numbers 20:1–13</h3>\n    <p>The scene takes place at <strong>Kadesh</strong>, in the wilderness of Zin, in the first month of the fortieth year of wandering (cf. Num 33:38). The people had arrived at the same place where thirty-eight years earlier they had failed with the spies — and now they grumble again for lack of water. Miriam had died in that same place (Num 20:1) — perhaps contributing to Moses\'s emotional state.</p>\n    <p>God commands Moses clearly: <em>"Take the staff, and assemble the congregation, you and Aaron your brother, and tell the rock before their eyes to yield its water"</em> (Num 20:8). The command is threefold and explicit: (1) take the staff; (2) assemble the people; (3) <strong>speak</strong> to the rock.</p>',
    1
)
out = out.replace(
    '<h3>O Que Moisés Fez de Errado — Uma Análise Precisa</h3>\n    <p>O texto de Números 20.10–11 registra exatamente o que aconteceu:</p>',
    '<h3>What Moses Did Wrong — A Precise Analysis</h3>\n    <p>The text of Numbers 20:10–11 records exactly what happened:</p>',
    1
)
out = out.replace(
    '"Moisés e Arão reuniram a assembleia diante da rocha; e ele lhes disse: Ouçam agora, rebeldes! Tiraremos água desta rocha para vocês? Então Moisés levantou a mão e feriu a rocha com a vara duas vezes; saiu muita água, e a assembleia e o seu gado beberam."\n      <span class="scripture-ref">Números 20.10–11 — NAA</span>',
    '"Moses and Aaron gathered the assembly together before the rock, and he said to them, \'Hear now, you rebels: shall we bring water for you out of this rock?\' And Moses lifted up his hand and struck the rock with his staff twice, and water came out abundantly, and the congregation and their livestock drank."\n      <span class="scripture-ref">Numbers 20:10–11 — ESV</span>',
    1
)
out = out.replace(
    'O texto identifica pelo menos <strong>quatro transgressões distintas</strong> nessa ação:',
    'The text identifies at least <strong>four distinct transgressions</strong> in this action:',
    1
)
out = out.replace(
    '<div class="timeline-period">Transgressão 1</div>\n        <div class="timeline-title">Golpeou em vez de Falar</div>\n        <div class="timeline-text">Deus mandou <em>falar</em> à rocha. Moisés <em>golpeou</em> com a vara — não uma, mas duas vezes. O golpe repetido sugere que na primeira vez a água não saiu, e Moisés bateu novamente com irritação crescente. Falar à rocha seria um ato de fé simples, dependente da palavra de Deus. Golpear era substituir a palavra pelo esforço físico — substituir a fé pelo método.</div>',
    '<div class="timeline-period">Transgression 1</div>\n        <div class="timeline-title">Struck Instead of Speaking</div>\n        <div class="timeline-text">God commanded Moses to <em>speak</em> to the rock. Moses <em>struck</em> it with the staff — not once, but twice. The repeated blow suggests that on the first strike the water did not come, and Moses struck again with growing irritation. Speaking to the rock would have been a simple act of faith, dependent on God\'s word. Striking it replaced the word with physical effort — replacing faith with method.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Transgressão 2</div>\n        <div class="timeline-title">Arrogou a Glória Divina</div>\n        <div class="timeline-text">"Acaso <strong>nós</strong> tiraremos água desta rocha para vós?" O pronome "nós" é devastador. Moisés e Arão colocaram-se como agentes do milagre — não como canais da ação divina. Quando Deus age por meio de um instrumento, o instrumento não pode reivindicar a autoria. A santificação de Deus diante do povo (Nm 20.12: "não me santificastes diante dos filhos de Israel") exige que a glória do milagre seja creditada ao único que pode produzi-la.</div>',
    '<div class="timeline-period">Transgression 2</div>\n        <div class="timeline-title">Arrogated Divine Glory</div>\n        <div class="timeline-text">"Shall <strong>we</strong> bring water for you out of this rock?" The pronoun "we" is devastating. Moses and Aaron placed themselves as agents of the miracle — not as channels of divine action. When God acts through an instrument, the instrument cannot claim authorship. The sanctification of God before the people (Num 20:12: "you did not believe in me, to uphold me as holy") requires that the glory of the miracle be credited to the only One who can produce it.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Transgressão 3</div>\n        <div class="timeline-title">Chamou o Povo de Rebeldes com Ira</div>\n        <div class="timeline-text">"Ouvi-me agora, <strong>rebeldes</strong>!" A palavra hebraica é <em>morim</em> (מֹרִים) — rebeldes, recalcitrantes. Embora o povo de fato estivesse murmurando, Moisés expressou essa palavra com raiva pessoal, não com a serena autoridade do mensageiro divino. O líder havia perdido o controle emocional — o homem que o texto descreve como "mui manso, mais do que todos os homens que havia sobre a face da terra" (Nm 12.3) agora explodia de fúria diante do povo.</div>',
    '<div class="timeline-period">Transgression 3</div>\n        <div class="timeline-title">Called the People Rebels in Anger</div>\n        <div class="timeline-text">"Hear now, you <strong>rebels</strong>!" The Hebrew word is <em>morim</em> (מֹרִים) — rebels, recalcitrant ones. Although the people were indeed grumbling, Moses expressed this word with personal anger, not with the calm authority of a divine messenger. The leader had lost emotional control — the man the text describes as "very meek, more than all people who were on the face of the earth" (Num 12:3) now erupted in fury before the people.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Transgressão 4</div>\n        <div class="timeline-title">Incredulidade — A Acusação Mais Profunda</div>\n        <div class="timeline-text">Números 20.12 diz: <em>"Porquanto não crastes em mim."</em> Esta é a acusação mais surpreendente — como pode Moisés, que falou com Deus "face a face", ser acusado de incredulidade? Deuteronômio 32.51 esclarece: "porque transgrediram contra mim... porque não me santificastes no meio dos filhos de Israel." A incredulidade de Moisés não era doutrinária — era funcional. No momento crítico, ele não confiou que a palavra de Deus fosse suficiente. Precisou <em>fazer algo</em> além do que Deus havia ordenado.</div>',
    '<div class="timeline-period">Transgression 4</div>\n        <div class="timeline-title">Unbelief — The Deepest Accusation</div>\n        <div class="timeline-text">Numbers 20:12 says: <em>"Because you did not believe in me."</em> This is the most surprising accusation — how can Moses, who spoke with God "face to face," be accused of unbelief? Deuteronomy 32:51 clarifies: "because you broke faith with me... because you did not treat me as holy in the midst of the people of Israel." Moses\'s unbelief was not doctrinal — it was functional. At the critical moment, he did not trust that God\'s word was sufficient. He needed to <em>do something</em> beyond what God had commanded.</div>',
    1
)
out = out.replace(
    '<span class="callout-type">A Tipologia da Rocha — 1 Coríntios 10.4</span>\n      <p>Paulo declara que "a rocha era Cristo" (1Co 10.4). Na primeira vez que a rocha foi golpeada (Êx 17.6), o comando era correto: a rocha deveria ser ferida. Isso tipificava a crucificação — Cristo seria golpeado uma vez, definitivamente, para produzir as águas vivas da salvação. Na segunda vez (Nm 20), a rocha deveria ser <em>falada</em> — não golpeada novamente. Golpear a rocha duas vezes desfazia a tipologia: sugeria que o sacrifício de Cristo precisaria ser repetido. Hebreus 9.28 responde: "Cristo foi oferecido uma vez para tirar os pecados de muitos." O erro litúrgico de Moisés era um erro tipológico de consequências eternas.</p>',
    '<span class="callout-type">The Typology of the Rock — 1 Corinthians 10:4</span>\n      <p>Paul declares that "the rock was Christ" (1 Cor 10:4). The first time the rock was struck (Exod 17:6), the command was correct: the rock was to be struck. This typified the crucifixion — Christ would be struck once, definitively, to produce the living waters of salvation. The second time (Num 20), the rock was to be <em>spoken to</em> — not struck again. Striking the rock a second time broke the typology: it suggested that Christ\'s sacrifice would need to be repeated. Hebrews 9:28 answers: "Christ, having been offered once to bear the sins of many." Moses\'s liturgical error was a typological error with eternal consequences.</p>',
    1
)
out = out.replace(
    '<h3>O Veredicto Divino — Números 20.12</h3>',
    '<h3>The Divine Verdict — Numbers 20:12</h3>',
    1
)
out = out.replace(
    '"O <span style="font-variant:small-caps">Senhor</span> disse a Moisés e a Arão: Porque vocês não confiaram em mim, para santificar-me diante dos israelitas, vocês não introduzirão esta assembleia na terra que lhes darei."\n      <span class="scripture-ref">Números 20.12 — NAA</span>',
    '"And the <span style="font-variant:small-caps">Lord</span> said to Moses and Aaron, \'Because you did not believe in me, to uphold me as holy in the eyes of the people of Israel, therefore you shall not bring this assembly into the land that I have given them.\'"\n      <span class="scripture-ref">Numbers 20:12 — ESV</span>',
    1
)
out = out.replace(
    'A sentença tem dois elementos: <strong>diagnóstico</strong> ("não crastes em mim, para me santificardes") e <strong>consequência</strong> ("não introduzireis esta congregação na terra"). Note que a consequência recai sobre ambos — Moisés <em>e</em> Arão. Arão morreu no Monte Hor pouco depois (Nm 20.22–29), igualmente excluído de Canaã.',
    'The sentence has two elements: <strong>diagnosis</strong> ("you did not believe in me, to uphold me as holy") and <strong>consequence</strong> ("you shall not bring this assembly into the land"). Note that the consequence falls on both — Moses <em>and</em> Aaron. Aaron died on Mount Hor shortly after (Num 20:22–29), equally excluded from Canaan.',
    1
)
out = out.replace(
    '<h3>Moisés Tenta Reverter a Sentença — Deuteronômio 3.23–28</h3>\n    <p>Em Deuteronômio 3, Moisés relata em primeira pessoa sua tentativa de apelar da sentença. Este é um dos momentos mais comoventes de toda a Bíblia:</p>',
    '<h3>Moses Tries to Reverse the Sentence — Deuteronomy 3:23–28</h3>\n    <p>In Deuteronomy 3, Moses recounts in the first person his attempt to appeal the sentence. This is one of the most moving moments in all of Scripture:</p>',
    1
)
out = out.replace(
    '"Naquele tempo supliquei ao <span style="font-variant:small-caps">Senhor</span>, dizendo: Senhor <span style="font-variant:small-caps">Deus</span>, você começou a mostrar ao seu servo a sua grandeza e a sua poderosa mão... Deixe-me passar e ver aquela boa terra que está além do Jordão, aquela bela região montanhosa e o Líbano. Mas o <span style="font-variant:small-caps">Senhor</span> estava irado comigo por causa de vocês e não me atendeu. O <span style="font-variant:small-caps">Senhor</span> me disse: Basta! Não me fale mais sobre este assunto."\n      <span class="scripture-ref">Deuteronômio 3.23–26 — NAA</span>',
    '"And I pleaded with the <span style="font-variant:small-caps">Lord</span> at that time, saying, \'O Lord God, you have only begun to show your servant your greatness and your mighty hand... Please let me go over and see the good land beyond the Jordan, that good hill country and Lebanon.\' But the <span style="font-variant:small-caps">Lord</span> was angry with me because of you and would not listen to me. And the <span style="font-variant:small-caps">Lord</span> said to me, \'Enough from you; do not speak to me of this matter again.\'"\n      <span class="scripture-ref">Deuteronomy 3:23–26 — ESV</span>',
    1
)
out = out.replace(
    'A expressão <em>"Basta"</em> (hebraico: <em>rav-lekha</em>, רַב-לְךָ — "suficiente para ti") é a resposta mais sóbria imaginável. Deus não debate, não negocia, não oferece condições. A porta está fechada. Moisés então recebe uma consolação parcial: poderá ver a terra do alto do monte Pisga, em todas as direções — mas não a cruzará (Dt 3.27).',
    'The expression <em>"Enough"</em> (Hebrew: <em>rav-lekha</em>, רַב-לְךָ — "it is enough for you") is the most sober response imaginable. God does not debate, negotiate, or offer conditions. The door is closed. Moses then receives a partial consolation: he will be able to see the land from the top of Mount Pisgah, in all directions — but he will not cross it (Deut 3:27).',
    1
)
out = out.replace(
    '<h3>Moisés Atribui Sua Exclusão ao Povo — Uma Perspectiva Complexa</h3>\n    <p>Em três passagens do Deuteronômio (1.37; 3.26; 4.21), Moisés afirma que foi excluído de Canaã <em>"por causa de vós"</em> — por causa do povo. Isso parece contradizer Números 20, que aponta o pecado do próprio Moisés. Como reconciliar?</p>',
    '<h3>Moses Attributes His Exclusion to the People — A Complex Perspective</h3>\n    <p>In three passages in Deuteronomy (1:37; 3:26; 4:21), Moses states that he was excluded from Canaan <em>"because of you"</em> — because of the people. This seems to contradict Numbers 20, which points to Moses\'s own sin. How to reconcile?</p>',
    1
)
out = out.replace(
    '<div class="card-title">Não há contradição — há camadas</div>\n        <p>O povo provocou a situação com suas murmurações (Nm 20.3–5). Sem a provocação do povo, Moisés não teria chegado àquele momento de pressão extrema. Há, portanto, um sentido legítimo em que o povo foi a causa ocasional do pecado de Moisés. Mas Moisés permanece responsável pela sua reação. A culpa não é transferida — ela é compartilhada em camadas distintas.</p>',
    '<div class="card-title">No contradiction — there are layers</div>\n        <p>The people provoked the situation with their grumbling (Num 20:3–5). Without the people\'s provocation, Moses would not have arrived at that moment of extreme pressure. There is, therefore, a legitimate sense in which the people were the occasional cause of Moses\'s sin. But Moses remains responsible for his reaction. The guilt is not transferred — it is shared in distinct layers.</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Dor Pessoal de Moisés</div>\n        <p>Deuteronômio 3.25 revela que Moisés genuinamente desejava entrar em Canaã. Não era indiferença — era uma perda profunda. O homem que passou quarenta anos conduzindo Israel em direção à Terra Prometida morreria no limiar, vendo-a de longe mas nunca pisando nela. A exclusão de Moisés é uma das cenas mais patéticas e comoventes da história bíblica.</p>',
    '<div class="card-title">Moses\'s Personal Grief</div>\n        <p>Deuteronomy 3:25 reveals that Moses genuinely desired to enter Canaan. It was not indifference — it was a deep loss. The man who spent forty years leading Israel toward the Promised Land would die at the threshold, seeing it from afar but never setting foot in it. Moses\'s exclusion is one of the most poignant and moving scenes in biblical history.</p>',
    1
)
out = out.replace(
    '<h3>A Vista do Monte Nebo — Deuteronômio 34.1–4</h3>\n    <p>Deus concede a Moisés uma visão panorâmica antes da morte. Do topo do Monte Nebo (Pisgá), Moisés pode ver:</p>',
    '<h3>The View from Mount Nebo — Deuteronomy 34:1–4</h3>\n    <p>God grants Moses a panoramic view before his death. From the top of Mount Nebo (Pisgah), Moses can see:</p>',
    1
)
out = out.replace(
    '<span class="name-tag">Gileade até Dã (norte)</span>\n      <span class="name-tag">Toda Naftali</span>\n      <span class="name-tag">Terra de Efraim e Manassés</span>\n      <span class="name-tag">Toda a terra de Judá até o Mar Ocidental (Mediterrâneo)</span>\n      <span class="name-tag">O Neguebe (sul)</span>\n      <span class="name-tag">O vale de Jericó, a Cidade das Palmeiras, até Zoar</span>',
    '<span class="name-tag">Gilead as far as Dan (north)</span>\n      <span class="name-tag">All of Naphtali</span>\n      <span class="name-tag">Land of Ephraim and Manasseh</span>\n      <span class="name-tag">All the land of Judah as far as the Western Sea (Mediterranean)</span>\n      <span class="name-tag">The Negev (south)</span>\n      <span class="name-tag">The Valley of Jericho, the City of Palm Trees, as far as Zoar</span>',
    1
)
out = out.replace(
    'Deus confirma: <em>"Esta é a terra que jurei dar a Abraão, a Isaque e a Jacó"</em> (Dt 34.4). A promessa patriarcal está sendo cumprida — Moisés a vê com seus próprios olhos. A consolação é real, mas a exclusão também. A graça e a justiça se tocam no mesmo momento, no mesmo monte.',
    'God confirms: <em>"This is the land of which I swore to Abraham, to Isaac, and to Jacob"</em> (Deut 34:4). The patriarchal promise is being fulfilled — Moses sees it with his own eyes. The consolation is real, but so is the exclusion. Grace and justice meet at the same moment, on the same mountain.',
    1
)
out = out.replace(
    '<span class="callout-type">Significado Teológico da Exclusão</span>\n      <p>A exclusão de Moisés de Canaã é, na hermenêutica reformada, parte do argumento tipológico do AT: a Lei (representada por Moisés) pode conduzir Israel até a fronteira da herança, mas não pode levá-la a entrar. Somente <strong>Josué</strong> — cujo nome em hebraico é <em>Yehoshua</em> (יְהוֹשֻׁעַ), a mesma raiz que <em>Yeshua</em> (Jesus) — conduziu o povo à terra. Paulo desenvolve essa lógica em Gálatas 3.23–25: "a lei nos serviu de aio para nos conduzir a Cristo." A lei guia até Cristo, mas não pode substituí-lo. Moisés morre na fronteira; Jesus entra.</p>',
    '<span class="callout-type">Theological Significance of the Exclusion</span>\n      <p>Moses\'s exclusion from Canaan is, in Reformed hermeneutics, part of the OT typological argument: the Law (represented by Moses) can lead Israel to the boundary of the inheritance, but cannot bring it in. Only <strong>Joshua</strong> — whose name in Hebrew is <em>Yehoshua</em> (יְהוֹשֻׁעַ), the same root as <em>Yeshua</em> (Jesus) — led the people into the land. Paul develops this logic in Galatians 3:23–25: "the law was our guardian until Christ came." The law guides to Christ, but cannot replace him. Moses dies at the border; Jesus enters.</p>',
    1
)
out = out.replace(
    '<h2>A Serpente de Bronze — João 3.14</h2>\n    <p>Em Números 21, cobras ardentes atacam o povo após nova murmuração. Deus ordena Moisés a fazer uma serpente de bronze e erguê-la num poste — quem olhasse para ela, viveria. Jesus usa este evento como tipologia direta de sua própria crucificação (Jo 3.14–15): "E como Moisés levantou a serpente no deserto, assim importa que o Filho do Homem seja levantado, para que todo aquele que nele crê tenha a vida eterna."</p>',
    '<h2>The Bronze Serpent — John 3:14</h2>\n    <p>In Numbers 21, fiery serpents attack the people after another episode of grumbling. God commands Moses to make a bronze serpent and lift it up on a pole — whoever looked at it would live. Jesus uses this event as a direct typology of his own crucifixion (John 3:14–15): "And as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life."</p>',
    1
)
out = out.replace(
    '<h2>Deuteronômio — O Sermão do Adeus</h2>\n    <p>Deuteronômio (grego: "segunda lei") é o discurso final de Moisés nas planícies de Moabe, endereçado à nova geração. É uma renovação da aliança — não uma nova lei, mas a lei reafirmada e aplicada à nova situação. Seu coração é o <em>Shemá</em> (Dt 6.4–9): <em>"Ouve, Israel: O SENHOR nosso Deus é o único SENHOR."</em></p>',
    '<h2>Deuteronomy — The Farewell Sermon</h2>\n    <p>Deuteronomy (Greek: "second law") is Moses\'s final discourse on the plains of Moab, addressed to the new generation. It is a covenant renewal — not a new law, but the law reaffirmed and applied to the new situation. Its heart is the <em>Shema</em> (Deut 6:4–9): <em>"Hear, O Israel: The Lord our God, the Lord is one."</em></p>',
    1
)
out = out.replace(
    '<h2>A Morte de Moisés — Deuteronômio 34</h2>\n    <p>Moisés sobe ao Monte Nebo (Pisgá), contempla toda a terra prometida — do Neguebe ao Hermom — e morre. Sua morte é narrada com sobriedade e mistério:</p>',
    '<h2>The Death of Moses — Deuteronomy 34</h2>\n    <p>Moses ascends Mount Nebo (Pisgah), surveys all the promised land — from the Negev to Hermon — and dies. His death is narrated with sobriety and mystery:</p>',
    1
)
out = out.replace(
    '<div class="card-title">Morreu com 120 anos</div>\n        <p>"Seus olhos não se tinham escurecido, nem perdera o viço" (Dt 34.7). A plenitude vital de Moisés até o fim contrasta com o destino ordinário da velhice — sinal da graça divina sobre seu servo.</p>',
    '<div class="card-title">Died at 120 years old</div>\n        <p>"His eye was undimmed, and his vigor unabated" (Deut 34:7). Moses\'s full vitality to the end contrasts with the ordinary fate of old age — a sign of divine grace upon his servant.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Sepultura Misteriosa</div>\n        <p>O SENHOR o sepultou num vale em Moabe, "e ninguém sabe onde fica o seu sepulcro até hoje" (Dt 34.6). Judas 9 revela que Miguel, o arcanjo, disputou com o diabo pelo corpo de Moisés — passagem enigmática relacionada à sua aparição na Transfiguração.</p>',
    '<div class="card-title">Mysterious Burial</div>\n        <p>The Lord buried him in a valley in Moab, "but no one knows the place of his burial to this day" (Deut 34:6). Jude 9 reveals that Michael the archangel disputed with the devil over the body of Moses — an enigmatic passage related to his appearance at the Transfiguration.</p>',
    1
)
out = out.replace(
    '<span class="section-tag">Teologia Sistemática</span>\n      <h1 class="section-title">A Teologia de Moisés</h1>\n      <p class="section-lead">As grandes contribuições teológicas do ministério mosaico ao cânone das Escrituras.</p>',
    '<span class="section-tag">Systematic Theology</span>\n      <h1 class="section-title">The Theology of Moses</h1>\n      <p class="section-lead">The major theological contributions of the Mosaic ministry to the biblical canon.</p>',
    1
)
out = out.replace(
    '<h2>1. Monoteísmo Radical</h2>\n    <p>O ministério de Moisés estabelece o monoteísmo exclusivo de Israel em contraste frontal com o politeísmo egípcio e cananeu. O Shemá (Dt 6.4) é a declaração mais clara: <em>"YHWH Elohenu YHWH Echad"</em> — YHWH é nosso Deus, YHWH é único. Não apenas que Israel deve adorar somente a YHWH (henoteísmo prático), mas que somente YHWH existe como Deus verdadeiro.</p>',
    '<h2>1. Radical Monotheism</h2>\n    <p>Moses\'s ministry establishes Israel\'s exclusive monotheism in direct contrast to Egyptian and Canaanite polytheism. The Shema (Deut 6:4) is the clearest declaration: <em>"YHWH Elohenu YHWH Echad"</em> — the Lord is our God, the Lord is one. Not merely that Israel must worship only YHWH (practical henotheism), but that only YHWH exists as the true God.</p>',
    1
)
out = out.replace(
    '<h2>2. Revelação do Nome Divino</h2>\n    <p>A revelação do Nome YHWH em Êxodo 3.14–15 e 6.2–3 é o evento epistemológico central do Pentateuco. O Nome não é apenas uma designação — é uma autodivulgação do caráter e ser de Deus. Êxodo 34.6–7 é a "definição" divina de si mesmo, e toda a teologia bíblica posterior é uma expansão desse núcleo.</p>',
    '<h2>2. Revelation of the Divine Name</h2>\n    <p>The revelation of the Name YHWH in Exodus 3:14–15 and 6:2–3 is the central epistemological event of the Pentateuch. The Name is not merely a designation — it is a self-disclosure of God\'s character and being. Exodus 34:6–7 is God\'s divine "definition" of himself, and all subsequent biblical theology is an expansion of this core.</p>',
    1
)
out = out.replace(
    '<h2>3. Teologia da Aliança</h2>\n    <p>Moisés é o mediador da aliança mais elaborada do AT. A Aliança Mosaica (também chamada Aliança Sinaítica ou Mosaica) tem estrutura tripartida: <strong>YHWH como Rei</strong>, <strong>Israel como povo da aliança</strong> e <strong>a Lei como constituição</strong>. Ela pressupõe e amplia as alianças abraâmica e noáica, e é cumprida e superada pela Nova Aliança em Cristo (Jr 31.31–34; Hb 8).</p>',
    '<h2>3. Covenant Theology</h2>\n    <p>Moses is the mediator of the most elaborate covenant in the OT. The Mosaic Covenant (also called the Sinaitic or Mosaic Covenant) has a tripartite structure: <strong>YHWH as King</strong>, <strong>Israel as covenant people</strong>, and <strong>the Law as constitution</strong>. It presupposes and amplifies the Abrahamic and Noahic covenants, and is fulfilled and surpassed by the New Covenant in Christ (Jer 31:31–34; Heb 8).</p>',
    1
)
out = out.replace(
    '<h2>4. Tipologia Sacerdotal</h2>\n    <p>O sistema levítico e o tabernáculo instituídos por Moisés formam um sistema tipológico completo que aponta para Cristo. Hebreus 8–10 desenvolve esta tipologia com detalhe: Cristo é o Sumo Sacerdote superior (Hb 4.14), o templo verdadeiro (Jo 2.21), o sacrifício definitivo (Hb 9.26), e o mediador da Nova Aliança (Hb 9.15).</p>',
    '<h2>4. Priestly Typology</h2>\n    <p>The Levitical system and tabernacle instituted by Moses form a complete typological system pointing to Christ. Hebrews 8–10 develops this typology in detail: Christ is the superior High Priest (Heb 4:14), the true temple (John 2:21), the definitive sacrifice (Heb 9:26), and the mediator of the New Covenant (Heb 9:15).</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Perspectiva Reformada-Calvinista</span>\n      <p>Na teologia da aliança reformada (Calvino, Westminster), a Lei Mosaica tem três usos: <strong>usus civilis</strong> (refrear o mal na sociedade), <strong>usus elenchticus</strong> (revelar o pecado e conduzir a Cristo — Gl 3.24) e <strong>usus didacticus / normativus</strong> (guia para a vida do crente regenerado). Os dez mandamentos permanecem como lei moral vinculante — não como caminho de salvação, mas como norma de vida nova.</p>',
    '<span class="callout-type">Reformed-Calvinist Perspective</span>\n      <p>In Reformed covenant theology (Calvin, Westminster), the Mosaic Law has three uses: <strong>usus civilis</strong> (restraining evil in society), <strong>usus elenchticus</strong> (revealing sin and driving to Christ — Gal 3:24), and <strong>usus didacticus / normativus</strong> (guide for the life of the regenerate believer). The ten commandments remain as binding moral law — not as a path of salvation, but as the norm of new life.</p>',
    1
)
out = out.replace(
    '<h2>5. A Esperança Escatológica</h2>\n    <p>Deuteronômio 18.15–18 é a promessa messiânica central de Moisés: Deus levantará um profeta <em>"semelhante a mim"</em> — que falará as palavras divinas. Pedro (At 3.22) e Estêvão (At 7.37) identificam explicitamente este profeta com Jesus. A grandeza de Moisés cria a categoria que somente o Filho de Deus poderia preencher.</p>',
    '<h2>5. Eschatological Hope</h2>\n    <p>Deuteronomy 18:15–18 is the central messianic promise of Moses: God will raise up a prophet <em>"like me"</em> — who will speak the divine words. Peter (Acts 3:22) and Stephen (Acts 7:37) explicitly identify this prophet with Jesus. The greatness of Moses creates the category that only the Son of God could fill.</p>',
    1
)
out = out.replace(
    '<h2>6. O Papel de Moisés na Teologia Bíblico-Sistemática</h2>',
    "<h2>6. Moses's Role in Biblical-Systematic Theology</h2>",
    1
)
out = out.replace(
    '<div class="card-title">Hermenêutica Cristológica</div>\n        <p>Jesus afirma em João 5.46: <em>"Se crêsseis em Moisés, creríeis em mim, porque ele escreveu de mim."</em> Lucas 24.27 registra que Cristo expôs "em todas as Escrituras as coisas que a ele se referiam, começando por Moisés." Ler Moisés corretamente é ler Cristo.</p>',
    '<div class="card-title">Christological Hermeneutics</div>\n        <p>Jesus states in John 5:46: <em>"If you believed Moses, you would believe me; for he wrote of me."</em> Luke 24:27 records that Christ expounded "in all the Scriptures the things concerning himself, beginning with Moses." To read Moses correctly is to read Christ.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Autoridade do Pentateuco</div>\n        <p>A autoria mosaica do Pentateuco é assumida consistentemente pelo NT (Mc 7.10; Jo 1.17; 7.19; At 3.22; Rm 10.5). Embora a crítica liberal (Wellhausen, JEPD) questione isso, a confirmação do próprio Cristo (Jo 5.45–47) é o argumento decisivo para a hermenêutica evangélica.</p>',
    '<div class="card-title">Authority of the Pentateuch</div>\n        <p>Mosaic authorship of the Pentateuch is consistently assumed by the NT (Mark 7:10; John 1:17; 7:19; Acts 3:22; Rom 10:5). Although liberal criticism (Wellhausen, JEPD) questions this, Christ\'s own confirmation (John 5:45–47) is the decisive argument for evangelical hermeneutics.</p>',
    1
)
out = out.replace(
    '<span class="section-tag">Cristologia e Novo Testamento</span>\n      <h1 class="section-title">Moisés no NT e os Tipos de Cristo</h1>\n      <p class="section-lead">Como o maior profeta de Israel aponta para Aquele que é maior que Moisés.</p>',
    '<span class="section-tag">Christology and New Testament</span>\n      <h1 class="section-title">Moses in the NT and the Types of Christ</h1>\n      <p class="section-lead">How the greatest prophet of Israel points to the One who is greater than Moses.</p>',
    1
)
out = out.replace(
    '<h2>Cristo, o Profeta Semelhante a Moisés</h2>\n    <p>Deuteronômio 18.15 é cumprido em Cristo de maneira plena. O paralelo é extenso e preciso:</p>',
    '<h2>Christ, the Prophet Like Moses</h2>\n    <p>Deuteronomy 18:15 is fulfilled in Christ in a complete way. The parallel is extensive and precise:</p>',
    1
)
out = out.replace(
    '<th>Aspecto</th>\n          <th>Moisés</th>\n          <th>Cristo — Cumprimento</th>',
    '<th>Aspect</th>\n          <th>Moses</th>\n          <th>Christ — Fulfillment</th>',
    1
)
out = out.replace(
    '<td>Ameaça na infância</td>\n          <td>Decreto de morte pelo Faraó (Êx 1)</td>\n          <td>Decreto de morte por Herodes (Mt 2)</td>',
    '<td>Childhood threat</td>\n          <td>Death decree by Pharaoh (Exod 1)</td>\n          <td>Death decree by Herod (Matt 2)</td>',
    1
)
out = out.replace(
    '<td>Saída do Egito</td>\n          <td>Éxodo de Israel (Êx 12–14)</td>\n          <td>"Do Egito chamei meu filho" (Mt 2.15; Os 11.1)</td>',
    '<td>Out of Egypt</td>\n          <td>Exodus of Israel (Exod 12–14)</td>\n          <td>"Out of Egypt I called my son" (Matt 2:15; Hos 11:1)</td>',
    1
)
out = out.replace(
    '<td>Travessia das águas</td>\n          <td>Mar Vermelho (Êx 14)</td>\n          <td>Batismo no Jordão (Mt 3)</td>',
    '<td>Crossing through water</td>\n          <td>Red Sea (Exod 14)</td>\n          <td>Baptism in the Jordan (Matt 3)</td>',
    1
)
out = out.replace(
    '<td>Quarenta dias/anos no deserto</td>\n          <td>40 anos de peregrinação</td>\n          <td>40 dias de tentação (Mt 4)</td>',
    '<td>Forty days/years in the desert</td>\n          <td>40 years of wandering</td>\n          <td>40 days of temptation (Matt 4)</td>',
    1
)
out = out.replace(
    '<td>Revelação no monte</td>\n          <td>Sinai — dez mandamentos</td>\n          <td>Sermão do Monte — "mas eu vos digo" (Mt 5–7)</td>',
    '<td>Revelation on a mountain</td>\n          <td>Sinai — ten commandments</td>\n          <td>Sermon on the Mount — "but I say to you" (Matt 5–7)</td>',
    1
)
out = out.replace(
    '<td>Mediador da Aliança</td>\n          <td>Aliança Sinaítica (Êx 24)</td>\n          <td>Nova Aliança no sangue (Lc 22.20; Hb 9.15)</td>',
    '<td>Mediator of the Covenant</td>\n          <td>Sinai Covenant (Exod 24)</td>\n          <td>New Covenant in his blood (Luke 22:20; Heb 9:15)</td>',
    1
)
out = out.replace(
    '<td>Pão do Céu</td>\n          <td>Maná no deserto (Êx 16)</td>\n          <td>"Eu sou o pão da vida" (Jo 6.35, 48–51)</td>',
    '<td>Bread from Heaven</td>\n          <td>Manna in the wilderness (Exod 16)</td>\n          <td>"I am the bread of life" (John 6:35, 48–51)</td>',
    1
)
out = out.replace(
    '<td>Água da rocha</td>\n          <td>Rocha em Horebe e Meriba</td>\n          <td>"A rocha era Cristo" (1Co 10.4)</td>',
    '<td>Water from the rock</td>\n          <td>Rock at Horeb and Meribah</td>\n          <td>"The rock was Christ" (1 Cor 10:4)</td>',
    1
)
out = out.replace(
    '<td>Intercessão sacrificial</td>\n          <td>"Risca-me do teu livro" (Êx 32.32)</td>\n          <td>Expiação substitutiva real (2Co 5.21)</td>',
    '<td>Sacrificial intercession</td>\n          <td>"Blot me out of your book" (Exod 32:32)</td>\n          <td>Real substitutionary atonement (2 Cor 5:21)</td>',
    1
)
out = out.replace(
    '<h2>A Transfiguração — Marcos 9.2–8</h2>\n    <p>Moisés aparece ao lado de Elias na Transfiguração — a Lei e os Profetas diante do próprio Cristo. Lucas 9.31 revela que eles falavam sobre o <em>êxodo</em> (<em>exodon</em>) de Jesus em Jerusalém — sua morte expiatória como o êxodo definitivo. A voz do Pai ordena: <em>"Este é o meu Filho amado; a ele ouvi."</em> — uma referência direta a Deuteronômio 18.15 ("a ele ouvireis").</p>',
    '<h2>The Transfiguration — Mark 9:2–8</h2>\n    <p>Moses appears alongside Elijah at the Transfiguration — the Law and the Prophets before Christ himself. Luke 9:31 reveals that they were speaking about the <em>exodus</em> (<em>exodon</em>) of Jesus in Jerusalem — his atoning death as the definitive Exodus. The Father\'s voice commands: <em>"This is my beloved Son; listen to him"</em> — a direct reference to Deuteronomy 18:15 ("you shall listen to him").</p>',
    1
)
out = out.replace(
    '<h2>Cristo Superior a Moisés — Hebreus 3.1–6</h2>\n    <p>Hebreus apresenta a comparação mais explícita: Moisés foi fiel como <strong>servo</strong> na casa de Deus (testemunhando o que viria); Cristo foi fiel como <strong>Filho</strong> sobre a casa de Deus. A honra de Cristo supera a de Moisés como o construtor supera a obra. O argumento é preciso: se Moisés merece tanta glória, quanto mais o Filho!</p>',
    "<h2>Christ Superior to Moses — Hebrews 3:1–6</h2>\n    <p>Hebrews presents the most explicit comparison: Moses was faithful as a <strong>servant</strong> in God's house (testifying to what was to come); Christ was faithful as a <strong>Son</strong> over God's house. Christ's honor surpasses Moses's as the builder surpasses the building. The argument is precise: if Moses deserves so much glory, how much more the Son!</p>",
    1
)
out = out.replace(
    '"Pois aquele que construiu a casa tem mais honra do que a própria casa... Moisés foi fiel em toda a casa de Deus como servo... mas Cristo é fiel como Filho sobre a própria casa de Deus."\n      <span class="scripture-ref">Hebreus 3.3–6 — NAA</span>',
    '"For Jesus has been counted worthy of more glory than Moses — as much more glory as the builder of a house has more honor than the house itself... Moses was faithful in all God\'s house as a servant... but Christ is faithful over God\'s house as a Son."\n      <span class="scripture-ref">Hebrews 3:3–6 — ESV</span>',
    1
)
out = out.replace(
    '<h2>A Nova Aliança Supera a Mosaica</h2>\n    <p>Hebreus 8 cita Jeremias 31.31–34 para demonstrar que a Aliança Mosaica era temporária e preparatória. O fato de Deus ter prometido uma <em>nova</em> aliança implica que a anterior era inadequada para realizar o propósito final — não pela fraqueza da Lei em si, mas pela fraqueza do povo (Hb 8.8). Cristo, o mediador da Nova Aliança, realiza o que a Lei apenas prometia: escreve a lei no coração, oferece perdão completo e proporciona o conhecimento direto de Deus.</p>',
    '<h2>The New Covenant Surpasses the Mosaic</h2>\n    <p>Hebrews 8 cites Jeremiah 31:31–34 to demonstrate that the Mosaic Covenant was temporary and preparatory. The fact that God promised a <em>new</em> covenant implies that the previous one was inadequate to achieve the final purpose — not because of weakness in the Law itself, but because of the weakness of the people (Heb 8:8). Christ, the mediator of the New Covenant, accomplishes what the Law only promised: writes the law on the heart, offers complete forgiveness, and provides direct knowledge of God.</p>',
    1
)
out = out.replace(
    '<h2>O Cântico de Moisés na Eternidade</h2>\n    <p>Apocalipse 15.3 descreve os remidos sobre o mar de vidro cantando "o cântico de Moisés, servo de Deus, e o cântico do Cordeiro." O Êxodo terreno encontra seu cumprimento no Êxodo celestial — o povo de Deus salvo das pragas do juízo final, glorificando o Deus que os libertou. A história de Moisés não termina no Monte Nebo — ela reverbera na eternidade.</p>',
    '<h2>The Song of Moses in Eternity</h2>\n    <p>Revelation 15:3 describes the redeemed on the sea of glass singing "the song of Moses, the servant of God, and the song of the Lamb." The earthly Exodus finds its fulfillment in the heavenly Exodus — the people of God saved from the plagues of final judgment, glorifying the God who delivered them. The story of Moses does not end at Mount Nebo — it reverberates in eternity.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Síntese Final</span>\n      <p>Moisés é o maior homem do Antigo Testamento — mas sua grandeza é precisamente sua função tipológica. Cada aspecto de seu ministério aponta além de si mesmo: seu nascimento aponta para a encarnação; sua libertação aponta para a redenção; sua mediação aponta para a intercessão de Cristo; sua lei aponta para o evangelho; sua morte aponta para o sacrifício; sua sepultura misteriosa aponta para a ressurreição. Ele não é o destino — é a seta que indica o destino. "A lei foi dada por Moisés; a graça e a verdade vieram por Jesus Cristo" (Jo 1.17).</p>',
    '<span class="callout-type">Final Synthesis</span>\n      <p>Moses is the greatest man of the Old Testament — but his greatness is precisely his typological function. Every aspect of his ministry points beyond itself: his birth points to the incarnation; his liberation points to redemption; his mediation points to Christ\'s intercession; his law points to the gospel; his death points to the sacrifice; his mysterious burial points to the resurrection. He is not the destination — he is the arrow that points to the destination. "The law was given through Moses; grace and truth came through Jesus Christ" (John 1:17).</p>',
    1
)
out = out.replace(
    '<span class="section-tag">Autoria e Cânon</span>\n      <h1 class="section-title">Moisés e o Pentateuco</h1>\n      <p class="section-lead">Os cinco primeiros livros da Bíblia — escritos por Moisés, fundamento de toda a revelação subsequente.</p>',
    '<span class="section-tag">Authorship and Canon</span>\n      <h1 class="section-title">Moses and the Pentateuch</h1>\n      <p class="section-lead">The first five books of the Bible — written by Moses, the foundation of all subsequent revelation.</p>',
    1
)
out = out.replace(
    'O Pentateuco (do grego <em>pentateuchos</em> — "os cinco rolos") é a base de toda a Escritura. Os judeus o chamam de <strong>Torah</strong> (תּוֹרָה — "instrução, lei"), e os próprios livros afirmam ou implicam autoria mosaica em dezenas de passagens. Jesus, os apóstolos e os autores do NT confirmam essa autoria consistentemente.',
    'The Pentateuch (from the Greek <em>pentateuchos</em> — "the five scrolls") is the foundation of all Scripture. Jews call it the <strong>Torah</strong> (תּוֹרָה — "instruction, law"), and the books themselves affirm or imply Mosaic authorship in dozens of passages. Jesus, the apostles, and the NT authors confirm this authorship consistently.',
    1
)
out = out.replace(
    '<h2>A Autoria Mosaica — Base Bíblica</h2>',
    '<h2>Mosaic Authorship — Biblical Basis</h2>',
    1
)
out = out.replace(
    '<span class="callout-type">Confirmação do Próprio Cristo</span>\n      <p>Jesus é o testemunho mais forte da autoria mosaica: "Se crêsseis em Moisés, creríeis em mim, porque <strong>ele escreveu de mim</strong>" (Jo 5.46). Em Lucas 24.27, o Cristo ressurreto expõe as Escrituras "começando por Moisés." Em Marcos 7.10 atribui explicitamente o quinto mandamento a Moisés. A confirmação de Cristo não pode ser descartada sem comprometer a autoridade de Jesus como mestre.</p>',
    '<span class="callout-type">Confirmed by Christ Himself</span>\n      <p>Jesus is the strongest witness for Mosaic authorship: "If you believed Moses, you would believe me; for <strong>he wrote of me</strong>" (John 5:46). In Luke 24:27, the risen Christ expounds the Scriptures "beginning with Moses." In Mark 7:10 he explicitly attributes the fifth commandment to Moses. Christ\'s confirmation cannot be dismissed without compromising Jesus\'s authority as teacher.</p>',
    1
)
out = out.replace(
    '<tr><td>"Moisés escreveu estas palavras"</td><td>Autotestemunho interno</td><td>Êx 24.4; 34.27; Nm 33.2; Dt 31.9, 22, 24</td></tr>',
    '<tr><td>"Moses wrote these words"</td><td>Internal self-testimony</td><td>Exod 24:4; 34:27; Num 33:2; Deut 31:9, 22, 24</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"No livro de Moisés está escrito"</td><td>Josué</td><td>Js 8.31–32; 23.6</td></tr>',
    '<tr><td>"In the book of Moses it is written"</td><td>Joshua</td><td>Josh 8:31–32; 23:6</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"Como está escrito na lei de Moisés"</td><td>1 Reis / Neemias</td><td>1Rs 2.3; Ne 8.1; Dn 9.13</td></tr>',
    '<tr><td>"As it is written in the law of Moses"</td><td>1 Kings / Nehemiah</td><td>1 Kgs 2:3; Neh 8:1; Dan 9:13</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"Moisés escreveu de mim"</td><td>Jesus</td><td>Jo 5.46–47</td></tr>',
    '<tr><td>"Moses wrote of me"</td><td>Jesus</td><td>John 5:46–47</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"A lei foi dada por Moisés"</td><td>João</td><td>Jo 1.17</td></tr>',
    '<tr><td>"The law was given through Moses"</td><td>John</td><td>John 1:17</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"Moisés disse..." (citando Deuteronômio)</td><td>Paulo</td><td>Rm 10.5; 1Co 9.9</td></tr>',
    '<tr><td>"Moses said..." (citing Deuteronomy)</td><td>Paul</td><td>Rom 10:5; 1 Cor 9:9</td></tr>',
    1
)
out = out.replace(
    '<tr><td>"No livro de Moisés" (citando Êxodo)</td><td>Marcos</td><td>Mc 12.26</td></tr>',
    '<tr><td>"In the book of Moses" (citing Exodus)</td><td>Mark</td><td>Mark 12:26</td></tr>',
    1
)
out = out.replace(
    '<h2>A Crítica Liberal — JEPD e a Resposta Evangélica</h2>\n    <p>No século XIX, Julius Wellhausen desenvolveu a <strong>Hipótese Documentária</strong> (teoria JEPD), propondo que o Pentateuco é uma compilação de quatro fontes independentes: <em>Jahvista (J), Eloísta (E), Deuteronomista (D)</em> e <em>Sacerdotal (P)</em>, compostas entre os séculos X e V a.C. — muito depois de Moisés. Esta hipótese dominou a teologia liberal por mais de um século.</p>',
    '<h2>Liberal Criticism — JEDP and the Evangelical Response</h2>\n    <p>In the 19th century, Julius Wellhausen developed the <strong>Documentary Hypothesis</strong> (JEDP theory), proposing that the Pentateuch is a compilation of four independent sources: <em>Yahwist (J), Elohist (E), Deuteronomist (D)</em>, and <em>Priestly (P)</em>, composed between the 10th and 5th centuries BC — long after Moses. This hypothesis dominated liberal theology for over a century.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Problemas com JEPD</div>\n        <p>• A alternância entre YHWH e Elohim (base da teoria) tem explicação literária interna<br>• Documentos hititas do 2º milênio a.C. confirmam o padrão de tratados de aliança de Êxodo<br>• Descobertas arqueológicas (Ebla, Ugarit, Mari) confirmam o contexto do 2º milênio<br>• A teoria não tem evidência manuscrita — nenhum fragmento J, E, D ou P jamais foi encontrado</p>',
    '<div class="card-title">Problems with JEDP</div>\n        <p>• The alternation between YHWH and Elohim (the theory\'s foundation) has an internal literary explanation<br>• Hittite documents from the 2nd millennium BC confirm the covenant treaty pattern of Exodus<br>• Archaeological discoveries (Ebla, Ugarit, Mari) confirm a 2nd millennium context<br>• The theory has no manuscript evidence — no fragment labeled J, E, D, or P has ever been found</p>',
    1
)
out = out.replace(
    '<div class="card-title">Posição Evangélica</div>\n        <p>A autoria mosaica é consistente com toda a evidência interna e com o testemunho do NT. Moisés era letrado (formado nas escolas egípcias), tinha acesso às tradições patriarcais orais e escritas, e viveu no século em que os eventos ocorreram. Isso não exclui a possibilidade de pequenas atualizações editoriais (ex: Dt 34, sobre a morte de Moisés — provavelmente de Josué).</p>',
    '<div class="card-title">Evangelical Position</div>\n        <p>Mosaic authorship is consistent with all internal evidence and the testimony of the NT. Moses was literate (trained in Egyptian scribal schools), had access to oral and written patriarchal traditions, and lived in the century when the events occurred. This does not exclude the possibility of minor editorial updates (e.g., Deut 34, about the death of Moses — probably by Joshua).</p>',
    1
)
out = out.replace(
    '<h2>Estrutura do Pentateuco como Unidade</h2>\n    <p>Os cinco livros formam uma narrativa progressiva com uma estrutura teológica coerente. Não são cinco documentos independentes — são cinco atos de uma única história:</p>',
    '<h2>The Pentateuch as a Unified Structure</h2>\n    <p>The five books form a progressive narrative with a coherent theological structure. They are not five independent documents — they are five acts of a single story:</p>',
    1
)
out = out.replace(
    '<div class="timeline-period">Livro 1</div>\n        <div class="timeline-title">Gênesis — As Origens</div>\n        <div class="timeline-text">Criação, queda, dilúvio, dispersão e as promessas patriarcais (Abraão, Isaque, Jacó, José). Estabelece o problema (pecado) e a solução prometida (aliança e bênção das nações).</div>',
    '<div class="timeline-period">Book 1</div>\n        <div class="timeline-title">Genesis — The Origins</div>\n        <div class="timeline-text">Creation, fall, flood, dispersion, and the patriarchal promises (Abraham, Isaac, Jacob, Joseph). Establishes the problem (sin) and the promised solution (covenant and blessing of the nations).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Livro 2</div>\n        <div class="timeline-title">Êxodo — A Libertação</div>\n        <div class="timeline-text">Opressão no Egito, chamado de Moisés, pragas, Páscoa, travessia do Mar, Sinai, Lei, Tabernáculo. Israel passa de escravos a povo da aliança.</div>',
    '<div class="timeline-period">Book 2</div>\n        <div class="timeline-title">Exodus — The Liberation</div>\n        <div class="timeline-text">Oppression in Egypt, calling of Moses, plagues, Passover, crossing of the Sea, Sinai, Law, Tabernacle. Israel passes from slaves to covenant people.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Livro 3</div>\n        <div class="timeline-title">Levítico — A Santidade</div>\n        <div class="timeline-text">Leis sacrificiais, sacerdócio, pureza, festas, Ano do Jubileu. Como o povo da aliança se aproxima e permanece diante de um Deus santo.</div>',
    '<div class="timeline-period">Book 3</div>\n        <div class="timeline-title">Leviticus — The Holiness</div>\n        <div class="timeline-text">Sacrificial laws, priesthood, purity, feasts, Year of Jubilee. How the covenant people draw near and remain before a holy God.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Livro 4</div>\n        <div class="timeline-title">Números — A Peregrinação</div>\n        <div class="timeline-text">Censo, jornada, rebeliões, julgamento da geração incrédula, formação da nova geração. O caminho entre a revelação e a herança.</div>',
    '<div class="timeline-period">Book 4</div>\n        <div class="timeline-title">Numbers — The Wandering</div>\n        <div class="timeline-text">Census, journey, rebellions, judgment of the unbelieving generation, formation of the new generation. The path between revelation and inheritance.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Livro 5</div>\n        <div class="timeline-title">Deuteronômio — A Renovação</div>\n        <div class="timeline-text">Discurso final de Moisés: recapitulação da lei, renovação da aliança, bênçãos e maldições, morte de Moisés. Israel na fronteira da herança, pronto para entrar.</div>',
    '<div class="timeline-period">Book 5</div>\n        <div class="timeline-title">Deuteronomy — The Renewal</div>\n        <div class="timeline-text">Moses\'s final discourse: recapitulation of the law, covenant renewal, blessings and curses, death of Moses. Israel at the boundary of the inheritance, ready to enter.</div>',
    1
)
out = out.replace(
    '<h2>O Pentateuco no Cânon</h2>\n    <p>No cânon hebraico, a Torah é a primeira das três divisões: <strong>Torah</strong> (Lei), <strong>Nevi\'im</strong> (Profetas) e <strong>Ketuvim</strong> (Escritos) — o chamado <em>TaNaK</em>. A Torah tem precedência hermenêutica: todos os outros livros são lidos à sua luz. Jesus resumiu o cânon como "a lei de Moisés, os profetas e os salmos" (Lc 24.44) — confirmando esta estrutura tripartite.</p>',
    '<h2>The Pentateuch in the Canon</h2>\n    <p>In the Hebrew canon, the Torah is the first of three divisions: <strong>Torah</strong> (Law), <strong>Nevi\'im</strong> (Prophets), and <strong>Ketuvim</strong> (Writings) — the so-called <em>TaNaK</em>. The Torah has hermeneutical precedence: all other books are read in its light. Jesus summarized the canon as "the Law of Moses, the Prophets, and the Psalms" (Luke 24:44) — confirming this tripartite structure.</p>',
    1
)

# ═══ genesis section ═══
out = out.replace(
    '<span class="section-tag">Pentateuco · Livro I</span>',
    '<span class="section-tag">Pentateuch · Book I</span>',
    1
)
out = out.replace(
    '<h1 class="section-title">Gênesis — O Livro das Origens</h1>',
    '<h1 class="section-title">Genesis — The Book of Origins</h1>',
    1
)
out = out.replace(
    '<p class="section-lead">No princípio — criação, queda, dilúvio, dispersão e as promessas que sustentam toda a história da redenção.</p>',
    '<p class="section-lead">In the beginning — creation, fall, flood, dispersion, and the promises that sustain all of redemptive history.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Dados Introdutórios</span>\n      <p><strong>Nome hebraico:</strong> <em>Bereshit</em> (בְּרֵאשִׁית) — "No princípio", da frase de abertura. <strong>Nome grego (LXX):</strong> <em>Genesis</em> — "origem, geração." <strong>Capítulos:</strong> 50. <strong>Período histórico abrangido:</strong> da criação até a morte de José no Egito (c. 1805 a.C.). <strong>Autor:</strong> Moisés (Jo 5.46–47; Mc 10.3–5). <strong>Versículo central:</strong> "No princípio criou Deus os céus e a terra." (1.1)</p>',
    '<span class="callout-type">Introductory Data</span>\n      <p><strong>Hebrew name:</strong> <em>Bereshit</em> (בְּרֵאשִׁית) — "In the beginning," from the opening phrase. <strong>Greek name (LXX):</strong> <em>Genesis</em> — "origin, generation." <strong>Chapters:</strong> 50. <strong>Historical period covered:</strong> from creation to the death of Joseph in Egypt (c. 1805 BC). <strong>Author:</strong> Moses (John 5:46–47; Mark 10:3–5). <strong>Key verse:</strong> "In the beginning, God created the heavens and the earth." (1:1)</p>',
    1
)
out = out.replace(
    '<div class="info-card-label">Extensão</div><div class="info-card-value">50 capítulos · da criação à morte de José no Egito (~1805 a.C.)</div>',
    '<div class="info-card-label">Extent</div><div class="info-card-value">50 chapters · from creation to the death of Joseph in Egypt (~1805 BC)</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Estrutura</div><div class="info-card-value">10 toledot ("gerações") como marcadores narrativos · História Primordial (1–11) e Patriarcal (12–50)</div>',
    '<div class="info-card-label">Structure</div><div class="info-card-value">10 toledot ("generations") as narrative markers · Primeval History (1–11) and Patriarchal History (12–50)</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Protoevangelium</div><div class="info-card-value">Gn 3.15 — primeira promessa messiânica da Bíblia · "este te ferirá a cabeça"</div>',
    '<div class="info-card-label">Protoevangelium</div><div class="info-card-value">Gen 3:15 — first messianic promise in the Bible · "he shall bruise your head"</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Aliança Abraâmica</div><div class="info-card-value">Gn 12.1–3 — pivot de toda a história bíblica: terra, descendência e bênção a todas as nações</div>',
    '<div class="info-card-label">Abrahamic Covenant</div><div class="info-card-value">Gen 12:1–3 — pivot of all biblical history: land, offspring, and blessing to all nations</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Citações no NT</div><div class="info-card-value">Mais de 200 alusões ao NT · livro mais referenciado do AT no Novo Testamento</div>',
    '<div class="info-card-label">NT Citations</div><div class="info-card-value">Over 200 NT allusions · most referenced OT book in the New Testament</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Imago Dei</div><div class="info-card-value">Gn 1.26–27 — fundamento da dignidade humana · Cristo é sua restauração plena (Cl 1.15; Rm 8.29)</div>',
    '<div class="info-card-label">Imago Dei</div><div class="info-card-value">Gen 1:26–27 — foundation of human dignity · Christ is its full restoration (Col 1:15; Rom 8:29)</div>',
    1
)
out = out.replace(
    '<h2 class="reveal">Estrutura do Livro — As Dez Toledot</h2>',
    '<h2 class="reveal">Structure of the Book — The Ten Toledot</h2>',
    1
)
out = out.replace(
    'A palavra estruturante de Gênesis é <em>toledot</em> (תּוֹלְדוֹת — "gerações, história, descendência"), que aparece dez vezes e funciona como marcador narrativo. O livro se divide em duas grandes seções: <strong>História Primordial</strong> (caps. 1–11) e <strong>História Patriarcal</strong> (caps. 12–50).',
    'The structuring word of Genesis is <em>toledot</em> (תּוֹלְדוֹת — "generations, history, lineage"), which appears ten times and functions as a narrative marker. The book divides into two major sections: <strong>Primeval History</strong> (chs. 1–11) and <strong>Patriarchal History</strong> (chs. 12–50).',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 1–2</div>\n        <div class="timeline-title">A Criação</div>\n        <div class="timeline-text">Criação em seis dias e descanso no sétimo. Deus cria por palavra (<em>fiat creation</em>). O homem (<em>adam</em>) é formado do pó e recebe o sopro de vida — único ser criado à imagem de Deus (<em>imago Dei</em>, 1.26–27). Eva é formada da costela de Adão. O jardim do Éden. O mandato cultural: cultivar e guardar (1.28; 2.15).</div>',
    '<div class="timeline-period">Genesis 1–2</div>\n        <div class="timeline-title">Creation</div>\n        <div class="timeline-text">Creation in six days and rest on the seventh. God creates by word (<em>fiat creation</em>). Man (<em>adam</em>) is formed from dust and receives the breath of life — the only being created in the image of God (<em>imago Dei</em>, 1:26–27). Eve is formed from Adam\'s rib. The garden of Eden. The cultural mandate: to till and keep it (1:28; 2:15).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 3</div>\n        <div class="timeline-title">A Queda — O Protoevangelium</div>\n        <div class="timeline-text">A serpente tenta Eva com a dúvida sobre a palavra de Deus (<em>"é verdade que Deus disse?"</em>). Adão e Eva comem o fruto proibido. O julgamento: maldição sobre a serpente, dor no parto, suor no trabalho, morte. O <em>Protoevangelium</em> (3.15): <em>"porei inimizade entre ti e a mulher, entre a tua descendência e o seu descendente; este te ferirá a cabeça, e tu lhe ferirás o calcanhar"</em> — a primeira promessa messiânica da Bíblia.</div>',
    '<div class="timeline-period">Genesis 3</div>\n        <div class="timeline-title">The Fall — The Protoevangelium</div>\n        <div class="timeline-text">The serpent tempts Eve with doubt about God\'s word (<em>"Did God actually say?"</em>). Adam and Eve eat the forbidden fruit. The judgment: curse on the serpent, pain in childbirth, toil in work, death. The <em>Protoevangelium</em> (3:15): <em>"I will put enmity between you and the woman, and between your offspring and her offspring; he shall bruise your head, and you shall bruise his heel"</em> — the first messianic promise in the Bible.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 4–11</div>\n        <div class="timeline-title">Queda, Dilúvio e Dispersão</div>\n        <div class="timeline-text">Caim mata Abel. A linhagem de Sete. O dilúvio (caps. 6–9): Noé acha graça diante de Deus; a Arca preserva a humanidade. Aliança noáica (arco-íris — 9.11–17). A Torre de Babel (cap. 11): dispersão das línguas e nações — o problema que a vocação de Abraão começará a resolver.</div>',
    '<div class="timeline-period">Genesis 4–11</div>\n        <div class="timeline-title">Fall, Flood, and Dispersion</div>\n        <div class="timeline-text">Cain kills Abel. The line of Seth. The flood (chs. 6–9): Noah finds grace before God; the Ark preserves humanity. Noahic covenant (rainbow — 9:11–17). The Tower of Babel (ch. 11): dispersion of languages and nations — the problem that Abraham\'s calling will begin to resolve.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 12–25</div>\n        <div class="timeline-title">Abraão — O Pai da Fé</div>\n        <div class="timeline-text">A vocação de Abrão (12.1–3): <em>"Vai... e eu te farei uma grande nação... e em ti serão benditas todas as famílias da terra."</em> As três dimensões da Promessa Abraâmica: terra, descendência e bênção universal. A Aliança de Abraão (cap. 15 — aliança unilateral, confirmada por Deus passando entre os animais cortados): incondicional e eterna. O sacrifício de Isaque (cap. 22 — <em>Akedá</em>): tipologia da morte substitutiva de Cristo.</div>',
    '<div class="timeline-period">Genesis 12–25</div>\n        <div class="timeline-title">Abraham — The Father of Faith</div>\n        <div class="timeline-text">The call of Abram (12:1–3): <em>"Go... and I will make of you a great nation... and in you all the families of the earth shall be blessed."</em> The three dimensions of the Abrahamic Promise: land, offspring, and universal blessing. The Abrahamic Covenant (ch. 15 — unilateral covenant, confirmed by God passing between the cut animals): unconditional and eternal. The sacrifice of Isaac (ch. 22 — <em>Akedah</em>): typology of Christ\'s substitutionary death.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 25–36</div>\n        <div class="timeline-title">Isaque e Jacó — A Aliança Transmitida</div>\n        <div class="timeline-text">Esaú e Jacó — a eleição soberana (25.23; Rm 9.10–13). Jacó engana Isaque e foge para Harã. A visão da escada ao céu em Betéis (28.10–22): YHWH confirma a aliança abraâmica a Jacó. A luta em Peniel (cap. 32): Jacó luta com Deus e recebe o nome Israel (<em>"aquele que luta com Deus"</em>). As doze tribos nascem de Jacó.</div>',
    '<div class="timeline-period">Genesis 25–36</div>\n        <div class="timeline-title">Isaac and Jacob — The Covenant Transmitted</div>\n        <div class="timeline-text">Esau and Jacob — sovereign election (25:23; Rom 9:10–13). Jacob deceives Isaac and flees to Haran. The vision of the stairway to heaven at Bethel (28:10–22): YHWH confirms the Abrahamic covenant to Jacob. The wrestling at Peniel (ch. 32): Jacob wrestles with God and receives the name Israel (<em>"one who strives with God"</em>). The twelve tribes are born from Jacob.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Gênesis 37–50</div>\n        <div class="timeline-title">José — Da Cova ao Trono</div>\n        <div class="timeline-text">José, filho amado de Jacó, vendido como escravo pelos irmãos invejosos. No Egito: casa de Potifar, prisão injusta, interpretação dos sonhos do Faraó. Exaltado como segundo do Faraó (41.40). A reconciliação com os irmãos: <em>"Não fostes vós que me vendestes para cá, mas Deus"</em> (45.5) — a providência divina operando através do mal humano. Os israelitas se estabelecem em Gósen. Morte de José aos 110 anos, com a profecia do Êxodo (50.24–25).</div>',
    '<div class="timeline-period">Genesis 37–50</div>\n        <div class="timeline-title">Joseph — From the Pit to the Throne</div>\n        <div class="timeline-text">Joseph, Jacob\'s beloved son, sold as a slave by his jealous brothers. In Egypt: Potiphar\'s house, unjust imprisonment, interpretation of Pharaoh\'s dreams. Exalted as second to Pharaoh (41:40). Reconciliation with his brothers: <em>"It was not you who sent me here, but God"</em> (45:5) — divine providence working through human evil. The Israelites settle in Goshen. Joseph dies at 110 years, with the prophecy of the Exodus (50:24–25).</div>',
    1
)
out = out.replace(
    '<h2 class="reveal">Os Grandes Temas Teológicos de Gênesis</h2>',
    '<h2 class="reveal">The Great Theological Themes of Genesis</h2>',
    1
)
out = out.replace(
    '<div class="card-title">A Imago Dei</div>\n        <p>O homem criado "à imagem e semelhança de Deus" (1.26–27) é o fundamento da dignidade humana. A queda distorce mas não destrói a imagem. Cristo é "a imagem do Deus invisível" (Cl 1.15) — a restauração plena da <em>imago Dei</em> é a meta da redenção (Rm 8.29).</p>',
    '<div class="card-title">The Imago Dei</div>\n        <p>Man created "in the image and likeness of God" (1:26–27) is the foundation of human dignity. The fall distorts but does not destroy the image. Christ is "the image of the invisible God" (Col 1:15) — the full restoration of the <em>imago Dei</em> is the goal of redemption (Rom 8:29).</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Aliança Abraâmica</div>\n        <p>A promessa de Gênesis 12.3 — <em>"em ti serão benditas todas as famílias da terra"</em> — é o eixo de toda a história bíblica. Paulo a chama de "evangelho pregado de antemão" (Gl 3.8). O cumprimento em Cristo: "as promessas foram feitas a Abraão e ao seu descendente" — Cristo (Gl 3.16).</p>',
    '<div class="card-title">The Abrahamic Covenant</div>\n        <p>The promise of Genesis 12:3 — <em>"in you all the families of the earth shall be blessed"</em> — is the axis of all biblical history. Paul calls it "the gospel preached beforehand" (Gal 3:8). Its fulfillment in Christ: "the promises were made to Abraham and to his offspring" — Christ (Gal 3:16).</p>',
    1
)
out = out.replace(
    '<div class="card-title">O Protoevangelium (3.15)</div>\n        <p>A primeira promessa messiânica da Escritura. A "inimizade" entre a descendência da serpente e a da mulher culmina em Cristo — que foi "ferido no calcanhar" (crucificação) mas "feriu a cabeça" da serpente (vitória sobre Satanás — Cl 2.15; Hb 2.14; Ap 12.9).</p>',
    '<div class="card-title">The Protoevangelium (3:15)</div>\n        <p>The first messianic promise in Scripture. The "enmity" between the offspring of the serpent and the woman\'s offspring culminates in Christ — who was "bruised on the heel" (crucifixion) but "bruised the head" of the serpent (victory over Satan — Col 2:15; Heb 2:14; Rev 12:9).</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Providência Soberana</div>\n        <p>A história de José é o exemplo mais elaborado de providência divina em Gênesis. Deus dirige os eventos humanos — incluindo o mal — para seus propósitos redentores. Paulo usa a mesma lógica em Rm 8.28: <em>"todas as coisas cooperam para o bem dos que amam a Deus."</em></p>',
    '<div class="card-title">Sovereign Providence</div>\n        <p>The story of Joseph is the most elaborate example of divine providence in Genesis. God directs human events — including evil — toward his redemptive purposes. Paul uses the same logic in Rom 8:28: <em>"all things work together for good for those who love God."</em></p>',
    1
)
out = out.replace(
    '<h2 class="reveal">O Protoevangelium — Gênesis 3.15 em Detalhe</h2>',
    '<h2 class="reveal">The Protoevangelium — Genesis 3:15 in Detail</h2>',
    1
)
out = out.replace(
    'Esta é a primeira promessa redentora da Bíblia — pronunciada no momento do julgamento pós-queda. YHWH Deus fala diretamente à serpente:',
    'This is the first redemptive promise in the Bible — pronounced at the moment of post-fall judgment. YHWH God speaks directly to the serpent:',
    1
)
out = out.replace(
    '"Porei inimizade entre você e a mulher, e entre a sua descendência e a descendência dela; esta lhe ferirá a cabeça, e você lhe ferirá o calcanhar."\n      <span class="scripture-ref">Gênesis 3.15 — NAA</span>',
    '"I will put enmity between you and the woman, and between your offspring and her offspring; he shall bruise your head, and you shall bruise his heel."\n      <span class="scripture-ref">Genesis 3:15 — ESV</span>',
    1
)
out = out.replace(
    'Três elementos exegéticos decisivos: <strong>(1) "Inimizade"</strong> — não paz, mas guerra entre o reino de Satanás e o reino de Deus; esta tensão percorre toda a história bíblica até Apocalipse 12. <strong>(2) "O seu descendente"</strong> (hebraico: <em>zera</em>, semente — singular) — Paulo em Gálatas 3.16 aplica este singular a Cristo. <strong>(3) "Ferirá a cabeça / ferirá o calcanhar"</strong> — ferimentos de intensidades opostas: a serpente inflige uma ferida dolorosa mas não fatal (a crucificação); o descendente da mulher inflige uma ferida mortal à cabeça da serpente (a vitória definitiva de Cristo sobre Satanás na cruz e na ressurreição).',
    'Three decisive exegetical elements: <strong>(1) "Enmity"</strong> — not peace, but war between Satan\'s kingdom and God\'s kingdom; this tension runs through all biblical history to Revelation 12. <strong>(2) "Her offspring"</strong> (Hebrew: <em>zera</em>, seed — singular) — Paul in Galatians 3:16 applies this singular to Christ. <strong>(3) "Bruise the head / bruise the heel"</strong> — wounds of opposing severity: the serpent inflicts a painful but non-fatal wound (the crucifixion); the woman\'s offspring inflicts a fatal wound to the serpent\'s head (Christ\'s definitive victory over Satan in the cross and resurrection).',
    1
)
out = out.replace(
    '<span class="callout-type">A Aliança Abraâmica — O Eixo de Toda a Bíblia</span>\n      <p>Gênesis 12.1–3 é o pivot da história bíblica. Tudo antes (caps. 1–11) é o problema: criação boa, queda, fragmentação, dispersão das nações em Babel. Tudo depois (Êxodo a Apocalipse) é a solução: como Deus cumprirá sua promessa a Abraão de abençoar <em>todas</em> as nações. O Novo Testamento começa com <em>"Livro da genealogia de Jesus Cristo, filho de Davi, filho de Abraão"</em> (Mt 1.1) — sinalizando que a história de Gênesis chegou ao seu cumprimento em Cristo.</p>',
    '<span class="callout-type">The Abrahamic Covenant — The Axis of the Entire Bible</span>\n      <p>Genesis 12:1–3 is the pivot of biblical history. Everything before (chs. 1–11) is the problem: good creation, fall, fragmentation, dispersion of nations at Babel. Everything after (Exodus to Revelation) is the solution: how God will fulfill his promise to Abraham to bless <em>all</em> nations. The New Testament begins with <em>"The book of the genealogy of Jesus Christ, the son of David, the son of Abraham"</em> (Matt 1:1) — signaling that the story of Genesis has reached its fulfillment in Christ.</p>',
    1
)
out = out.replace(
    '<h2 class="reveal">Gênesis no Novo Testamento</h2>\n    <p>Gênesis é citado ou aludido mais de 200 vezes no Novo Testamento. Os textos mais citados:</p>',
    '<h2 class="reveal">Genesis in the New Testament</h2>\n    <p>Genesis is cited or alluded to more than 200 times in the New Testament. The most frequently cited texts:</p>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 1.1 → Jo 1.1 ("No princípio era o Verbo")</span>',
    '<span class="name-tag">Gen 1:1 → John 1:1 ("In the beginning was the Word")</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 1.27 → Mc 10.6 (casamento)</span>',
    '<span class="name-tag">Gen 1:27 → Mark 10:6 (marriage)</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 2.24 → Ef 5.31 (marido e mulher)</span>',
    '<span class="name-tag">Gen 2:24 → Eph 5:31 (husband and wife)</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 3.15 → Gl 3.16; Rm 16.20</span>',
    '<span class="name-tag">Gen 3:15 → Gal 3:16; Rom 16:20</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 12.3 → Gl 3.8 (evangelho pregado a Abraão)</span>',
    '<span class="name-tag">Gen 12:3 → Gal 3:8 (gospel preached to Abraham)</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 15.6 → Rm 4.3 (fé de Abraão imputada como justiça)</span>',
    '<span class="name-tag">Gen 15:6 → Rom 4:3 (Abraham\'s faith credited as righteousness)</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 22 → Hb 11.17–19; Jo 3.16</span>',
    '<span class="name-tag">Gen 22 → Heb 11:17–19; John 3:16</span>',
    1
)
out = out.replace(
    '<span class="name-tag">Gn 50.20 → Rm 8.28</span>',
    '<span class="name-tag">Gen 50:20 → Rom 8:28</span>',
    1
)
out = out.replace(
    '<h2 class="reveal">Versículo-Chave</h2>\n    <div class="scripture reveal">\n      "No princípio, Deus criou os céus e a terra."\n      <span class="scripture-ref">Gênesis 1.1 — NAA · A declaração mais consequente da história humana.</span>\n    </div>\n  </section>',
    '<h2 class="reveal">Key Verse</h2>\n    <div class="scripture reveal">\n      "In the beginning, God created the heavens and the earth."\n      <span class="scripture-ref">Genesis 1:1 — ESV · The most consequential declaration in human history.</span>\n    </div>\n  </section>',
    1
)

# ═══ exodo-livro section ═══
out = out.replace(
    '<span class="section-tag">Pentateuco · Livro II</span>',
    '<span class="section-tag">Pentateuch · Book II</span>',
    1
)
out = out.replace(
    '<h1 class="section-title">Êxodo — O Livro da Libertação</h1>',
    '<h1 class="section-title">Exodus — The Book of Liberation</h1>',
    1
)
out = out.replace(
    '<p class="section-lead">Da escravidão à aliança — como YHWH resgatou seu povo e constituiu uma nação.</p>',
    '<p class="section-lead">From slavery to covenant — how YHWH rescued his people and constituted a nation.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Dados Introdutórios</span>\n      <p><strong>Nome hebraico:</strong> <em>Shemot</em> (שְׁמוֹת) — "Nomes", da frase de abertura "Estes são os nomes dos filhos de Israel." <strong>Nome grego (LXX):</strong> <em>Exodus</em> — "saída, partida." <strong>Capítulos:</strong> 40. <strong>Período histórico abrangido:</strong> c. 1526–1446 a.C. (do nascimento de Moisés ao erguimento do Tabernáculo). <strong>Autor:</strong> Moisés (confirmado em Êx 24.4; Mc 12.26).</p>',
    '<span class="callout-type">Introductory Data</span>\n      <p><strong>Hebrew name:</strong> <em>Shemot</em> (שְׁמוֹת) — "Names," from the opening phrase "These are the names of the sons of Israel." <strong>Greek name (LXX):</strong> <em>Exodus</em> — "departure, going out." <strong>Chapters:</strong> 40. <strong>Historical period covered:</strong> c. 1526–1446 BC (from the birth of Moses to the erection of the Tabernacle). <strong>Author:</strong> Moses (confirmed in Exod 24:4; Mark 12:26).</p>',
    1
)
out = out.replace(
    '<div class="info-card-label">Extensão</div><div class="info-card-value">40 capítulos · ~1526–1446 a.C. · do nascimento de Moisés ao Tabernáculo erguido</div>',
    '<div class="info-card-label">Extent</div><div class="info-card-value">40 chapters · ~1526–1446 BC · from the birth of Moses to the Tabernacle erected</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Nome de Deus</div><div class="info-card-value">YHWH revelado em Êx 3.14 ("EU SOU O QUE SOU") e 34.6–7 — as duas maiores revelações do caráter divino no AT</div>',
    '<div class="info-card-label">Name of God</div><div class="info-card-value">YHWH revealed in Exod 3:14 ("I AM WHO I AM") and 34:6–7 — the two greatest revelations of the divine character in the OT</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">As dez pragas</div><div class="info-card-value">Guerra teológica sistemática contra o panteão egípcio — cada praga ataca uma divindade específica</div>',
    '<div class="info-card-label">The ten plagues</div><div class="info-card-value">Systematic theological warfare against the Egyptian pantheon — each plague attacks a specific deity</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Aliança do Sinai</div><div class="info-card-value">Cap. 19–24: Decálogo + Código da Aliança + ratificação com sangue · a mais abrangente teofania do AT</div>',
    '<div class="info-card-label">Sinai Covenant</div><div class="info-card-value">Chs. 19–24: Decalogue + Book of the Covenant + blood ratification · the most comprehensive theophany in the OT</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Tipologia cristológica</div><div class="info-card-value">Cordeiro pascal, maná, rocha, sacerdote, tabernáculo, véu — um dos livros mais cristológicos do AT</div>',
    '<div class="info-card-label">Christological typology</div><div class="info-card-value">Passover lamb, manna, rock, priest, tabernacle, veil — one of the most christological books of the OT</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Meta do Êxodo</div><div class="info-card-value">Não é Canaã — é o Tabernáculo (cap. 40): Deus vem habitar no meio do povo libertado</div>',
    '<div class="info-card-label">Goal of Exodus</div><div class="info-card-value">Not Canaan — it is the Tabernacle (ch. 40): God comes to dwell among his liberated people</div>',
    1
)
out = out.replace(
    '<h2>Estrutura do Livro</h2>\n    <div class="timeline">\n      <div class="timeline-item">\n        <div class="timeline-period">Êxodo 1–2</div>',
    '<h2>Structure of the Book</h2>\n    <div class="timeline">\n      <div class="timeline-item">\n        <div class="timeline-period">Exodus 1–2</div>',
    1
)
out = out.replace(
    '<div class="timeline-title">A Opressão e o Nascimento de Moisés</div>\n        <div class="timeline-text">Israel multiplica-se no Egito; novo Faraó que "não conhecia José" (1.8) inaugura a escravidão. Decreto de morte dos meninos hebreus. Nascimento, preservação, formação e fuga de Moisés para Midiã.</div>',
    '<div class="timeline-title">The Oppression and the Birth of Moses</div>\n        <div class="timeline-text">Israel multiplies in Egypt; a new Pharaoh who "did not know Joseph" (1:8) inaugurates slavery. Decree of death for Hebrew boys. Birth, preservation, formation, and flight of Moses to Midian.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 3–6</div>\n        <div class="timeline-title">O Chamado de Moisés e as Primeiras Negociações</div>\n        <div class="timeline-text">A sarça ardente, a revelação de YHWH, as cinco objeções, o retorno ao Egito. As primeiras audiências com o Faraó resultam em piora das condições de Israel — a opressão aumenta antes de diminuir.</div>',
    '<div class="timeline-period">Exodus 3–6</div>\n        <div class="timeline-title">The Call of Moses and the First Negotiations</div>\n        <div class="timeline-text">The burning bush, the revelation of YHWH, the five objections, the return to Egypt. The first audiences with Pharaoh result in a worsening of Israel\'s conditions — the oppression increases before it diminishes.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 7–12</div>\n        <div class="timeline-title">As Dez Pragas</div>\n        <div class="timeline-text">Guerra teológica sistemática contra o panteão egípcio. Cada praga ataca uma divindade. O endurecimento do coração do Faraó (alternando entre ato de Deus e ato do próprio Faraó — Êx 4.21; 8.15). Clímax: a Páscoa e a morte dos primogênitos.</div>',
    '<div class="timeline-period">Exodus 7–12</div>\n        <div class="timeline-title">The Ten Plagues</div>\n        <div class="timeline-text">Systematic theological warfare against the Egyptian pantheon. Each plague attacks a deity. The hardening of Pharaoh\'s heart (alternating between God\'s act and Pharaoh\'s own act — Exod 4:21; 8:15). Climax: the Passover and the death of the firstborn.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 13–18</div>\n        <div class="timeline-title">A Travessia e a Jornada ao Sinai</div>\n        <div class="timeline-text">Saída do Egito pela coluna de nuvem e fogo. Travessia do Mar. O Cântico de Moisés (cap. 15) — primeiro hino de Israel. Maná e codornizes. Água na rocha em Horebe (cap. 17). Encontro com Jetro e reorganização judicial (cap. 18).</div>',
    '<div class="timeline-period">Exodus 13–18</div>\n        <div class="timeline-title">The Crossing and the Journey to Sinai</div>\n        <div class="timeline-text">Departure from Egypt by the pillar of cloud and fire. Crossing of the Sea. The Song of Moses (ch. 15) — Israel\'s first hymn. Manna and quail. Water from the rock at Horeb (ch. 17). Meeting with Jethro and judicial reorganization (ch. 18).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 19–24</div>\n        <div class="timeline-title">A Aliança do Sinai</div>\n        <div class="timeline-text">A teofania no Sinai (trovões, relâmpagos, nuvem, chifre soando). Os Dez Mandamentos (cap. 20). O Código da Aliança (cap. 21–23) — leis civis, criminais, sociais e litúrgicas. A ratificação da aliança com sangue (24.8) e a refeição dos líderes na presença de Deus (24.11).</div>',
    '<div class="timeline-period">Exodus 19–24</div>\n        <div class="timeline-title">The Sinai Covenant</div>\n        <div class="timeline-text">The theophany at Sinai (thunder, lightning, cloud, trumpet blast). The Ten Commandments (ch. 20). The Book of the Covenant (chs. 21–23) — civil, criminal, social, and liturgical laws. The blood ratification of the covenant (24:8) and the elders\' meal in God\'s presence (24:11).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 25–31</div>\n        <div class="timeline-title">As Instruções do Tabernáculo</div>\n        <div class="timeline-text">Deus entrega a Moisés os planos detalhados do Tabernáculo, todos os seus utensílios, as vestimentas sacerdotais, as ordenanças do sacerdócio, o incenso, o unguento sagrado e o Sabá. Bezalel e Aoliabe são nomeados como artesãos cheios do Espírito (31.1–11).</div>',
    '<div class="timeline-period">Exodus 25–31</div>\n        <div class="timeline-title">The Tabernacle Instructions</div>\n        <div class="timeline-text">God gives Moses the detailed plans for the Tabernacle, all its utensils, the priestly garments, the ordinances of the priesthood, the incense, the sacred anointing oil, and the Sabbath. Bezalel and Oholiab are appointed as Spirit-filled craftsmen (31:1–11).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 32–34</div>\n        <div class="timeline-title">O Bezerro de Ouro e a Renovação da Aliança</div>\n        <div class="timeline-text">A maior crise do Êxodo. Moisés intercede, julga, intercede novamente. Renovação da aliança; o rosto resplandecente de Moisés; a revelação de Êx 34.6–7.</div>',
    '<div class="timeline-period">Exodus 32–34</div>\n        <div class="timeline-title">The Golden Calf and the Renewal of the Covenant</div>\n        <div class="timeline-text">The greatest crisis of Exodus. Moses intercedes, judges, intercedes again. Renewal of the covenant; the radiant face of Moses; the revelation of Exod 34:6–7.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Êxodo 35–40</div>\n        <div class="timeline-title">A Construção do Tabernáculo</div>\n        <div class="timeline-text">Execução fiel de todas as instruções divinas. O livro culmina com a glória de YHWH enchendo o Tabernáculo (40.34–35) — a presença divina vem habitar no meio de seu povo. Moisés não consegue entrar por causa da glória.</div>',
    '<div class="timeline-period">Exodus 35–40</div>\n        <div class="timeline-title">The Construction of the Tabernacle</div>\n        <div class="timeline-text">Faithful execution of all the divine instructions. The book culminates with the glory of YHWH filling the Tabernacle (40:34–35) — the divine presence comes to dwell among his people. Moses cannot enter because of the glory.</div>',
    1
)
out = out.replace(
    '<h2>Temas Teológicos Centrais</h2>',
    '<h2>Central Theological Themes</h2>',
    1
)
out = out.replace(
    '<div class="card-title">Redenção pela Graça Soberana</div>\n        <p>Israel não foi resgatado por seus méritos, mas pelo amor de YHWH às promessas patriarcais (Êx 2.24). O Êxodo é o paradigma da salvação: iniciativa divina, poder divino, graça divina. Toda a teologia da redenção posterior pressupõe este modelo.</p>',
    '<div class="card-title">Redemption by Sovereign Grace</div>\n        <p>Israel was not rescued by its merits, but by YHWH\'s love for the patriarchal promises (Exod 2:24). The Exodus is the paradigm of salvation: divine initiative, divine power, divine grace. All subsequent theology of redemption presupposes this model.</p>',
    1
)
out = out.replace(
    '<div class="card-title">A Presença de Deus como Meta</div>\n        <p>O objetivo final do Êxodo não é Canaã — é o Tabernáculo. O livro começa com Deus "ouvindo o clamor" de longe e termina com Deus habitando no meio do povo. A proximidade divina é o coração do evangelho no Êxodo.</p>',
    '<div class="card-title">God\'s Presence as the Goal</div>\n        <p>The ultimate goal of the Exodus is not Canaan — it is the Tabernacle. The book begins with God "hearing the cry" from afar and ends with God dwelling among the people. Divine nearness is the heart of the gospel in Exodus.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Revelação do Caráter Divino</div>\n        <p>Êxodo contém as duas maiores revelações do Nome e do caráter de Deus no AT: o tetragrama em 3.14 e a proclamação de 34.6–7. Todo o AT faz eco a esses dois textos.</p>',
    '<div class="card-title">Revelation of the Divine Character</div>\n        <p>Exodus contains the two greatest revelations of God\'s Name and character in the OT: the tetragrammaton in 3:14 and the proclamation of 34:6–7. The entire OT echoes those two texts.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Tipologia Cristológica Densa</div>\n        <p>O cordeiro pascal (Jo 1.29; 1Co 5.7), o maná (Jo 6.35), a rocha (1Co 10.4), o sacerdote (Hb 4.14), o tabernáculo (Jo 1.14 — "habitou entre nós", <em>eskénosen</em>), o véu rasgado (Mc 15.38) — o livro de Êxodo é um dos mais cristológicos do AT.</p>',
    '<div class="card-title">Dense Christological Typology</div>\n        <p>The Passover lamb (John 1:29; 1 Cor 5:7), the manna (John 6:35), the rock (1 Cor 10:4), the priest (Heb 4:14), the tabernacle (John 1:14 — "dwelt among us," <em>eskēnōsen</em>), the torn veil (Mark 15:38) — the book of Exodus is one of the most christological in the OT.</p>',
    1
)
out = out.replace(
    '<h2>Versículo-Chave</h2>\n    <div class="scripture">\n      "Eu sou o <span style="font-variant:small-caps">Senhor</span>, o seu Deus, que o tirei da terra do Egito, da casa da escravidão."\n      <span class="scripture-ref">Êxodo 20.2 — NAA · A abertura do Decálogo</span>\n    </div>\n  </section>',
    '<h2>Key Verse</h2>\n    <div class="scripture">\n      "I am the <span style="font-variant:small-caps">Lord</span> your God, who brought you out of the land of Egypt, out of the house of slavery."\n      <span class="scripture-ref">Exodus 20:2 — ESV · The opening of the Decalogue</span>\n    </div>\n  </section>',
    1
)

# ═══ levitico section ═══
out = out.replace(
    '<span class="section-tag">Pentateuco · Livro III</span>',
    '<span class="section-tag">Pentateuch · Book III</span>',
    1
)
out = out.replace(
    '<h1 class="section-title">Levítico — O Livro da Santidade</h1>',
    '<h1 class="section-title">Leviticus — The Book of Holiness</h1>',
    1
)
out = out.replace(
    '<p class="section-lead">"Sede santos, porque eu, o SENHOR vosso Deus, sou santo." — A liturgia da aproximação ao Deus santo.</p>',
    '<p class="section-lead">"Be holy, for I the Lord your God am holy." — The liturgy of approaching the holy God.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Dados Introdutórios</span>\n      <p><strong>Nome hebraico:</strong> <em>Vayikra</em> (וַיִּקְרָא) — "E chamou", da frase de abertura. <strong>Nome grego (LXX):</strong> <em>Leuitikon</em> — "sobre os levitas" (embora o livro trate do sacerdócio aaronita, não apenas dos levitas). <strong>Capítulos:</strong> 27. <strong>Período histórico:</strong> c. 1446 a.C. — todo o livro se passa no Sinai, durante o primeiro mês após a erguida do Tabernáculo. <strong>Versículo central:</strong> "Sede santos, porque eu, o SENHOR vosso Deus, sou santo" (19.2).</p>',
    '<span class="callout-type">Introductory Data</span>\n      <p><strong>Hebrew name:</strong> <em>Vayikra</em> (וַיִּקְרָא) — "And he called," from the opening phrase. <strong>Greek name (LXX):</strong> <em>Leuitikon</em> — "concerning the Levites" (though the book deals with the Aaronic priesthood, not only the Levites). <strong>Chapters:</strong> 27. <strong>Historical period:</strong> c. 1446 BC — the entire book takes place at Sinai, during the first month after the Tabernacle was erected. <strong>Key verse:</strong> "Be holy, for I the Lord your God am holy" (19:2).</p>',
    1
)
out = out.replace(
    '<div class="info-card-label">Extensão</div><div class="info-card-value">27 capítulos · todo o livro se passa no Sinai · primeiro mês após o Tabernáculo erguido</div>',
    '<div class="info-card-label">Extent</div><div class="info-card-value">27 chapters · the entire book takes place at Sinai · first month after the Tabernacle erected</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">As 5 ofertas</div><div class="info-card-value">Holocausto, manjares, paz, pecado, culpa — cada uma expressa uma dimensão diferente da reconciliação com Deus</div>',
    '<div class="info-card-label">The 5 offerings</div><div class="info-card-value">Burnt offering, grain offering, peace offering, sin offering, guilt offering — each expresses a different dimension of reconciliation with God</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Yom Kippur</div><div class="info-card-value">Cap. 16 — dia mais sagrado: sangue no propiciatório + bode expiatório · fundamento de Hebreus 9–10</div>',
    '<div class="info-card-label">Yom Kippur</div><div class="info-card-value">Ch. 16 — holiest day: blood on the mercy seat + scapegoat · foundation of Hebrews 9–10</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Código de Santidade</div><div class="info-card-value">Caps. 17–27 — inclui amor ao próximo (19.18) citado por Jesus como o segundo maior mandamento</div>',
    '<div class="info-card-label">Holiness Code</div><div class="info-card-value">Chs. 17–27 — includes love of neighbor (19:18) cited by Jesus as the second greatest commandment</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Festas sagradas</div><div class="info-card-value">Cap. 23 — 7 festas de Israel · Páscoa, Pentecoste, Tabernáculos · todas com cumprimento cristológico</div>',
    '<div class="info-card-label">Sacred feasts</div><div class="info-card-value">Ch. 23 — 7 feasts of Israel · Passover, Pentecost, Tabernacles · all with christological fulfillment</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Jubileu</div><div class="info-card-value">Cap. 25 — a cada 50 anos: libertação de escravos, devolução de terras · Jesus cita Lv 25 em Lc 4.18–19</div>',
    '<div class="info-card-label">Jubilee</div><div class="info-card-value">Ch. 25 — every 50 years: liberation of slaves, return of lands · Jesus cites Lev 25 in Luke 4:18–19</div>',
    1
)
out = out.replace(
    '<h2>Estrutura do Livro</h2>\n    <div class="timeline">\n      <div class="timeline-item">\n        <div class="timeline-period">Levítico 1–7</div>',
    '<h2>Structure of the Book</h2>\n    <div class="timeline">\n      <div class="timeline-item">\n        <div class="timeline-period">Leviticus 1–7</div>',
    1
)
out = out.replace(
    '<div class="timeline-title">As Cinco Ofertas</div>\n        <div class="timeline-text"><strong>Holocausto</strong> (olah) — oferenda completamente queimada, simboliza consagração total a Deus. <strong>Oferta de manjares</strong> (minchah) — grãos e azeite, reconhecimento da provisão divina. <strong>Oferta de paz</strong> (shelamim) — comunhão e gratidão. <strong>Oferta pelo pecado</strong> (chattat) — expiação por pecados inadvertidos. <strong>Oferta pela culpa</strong> (asham) — reparação por transgressões específicas. Cada oferenda tem procedimentos distintos, mostrando a multiplicidade das dimensões do pecado e da reconciliação.</div>',
    '<div class="timeline-title">The Five Offerings</div>\n        <div class="timeline-text"><strong>Burnt offering</strong> (olah) — completely burned offering, symbolizes total consecration to God. <strong>Grain offering</strong> (minchah) — grain and oil, acknowledgment of divine provision. <strong>Peace offering</strong> (shelamim) — fellowship and gratitude. <strong>Sin offering</strong> (chattat) — atonement for inadvertent sins. <strong>Guilt offering</strong> (asham) — reparation for specific transgressions. Each offering has distinct procedures, showing the multiplicity of dimensions of sin and reconciliation.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Levítico 8–10</div>\n        <div class="timeline-title">A Ordenação do Sacerdócio e o Fogo Estranho</div>\n        <div class="timeline-text">Aarão e seus filhos são ungidos e ordenados em cerimônias de sete dias. No oitavo dia, ao oferecerem o primeiro sacrifício, fogo divino consome o holocausto — sinal de aceitação divina (9.24). Imediatamente depois, Nadabe e Abiú, filhos de Aarão, oferecem "fogo estranho" não ordenado por Deus (10.1) e são consumidos. A santidade do Tabernáculo exige obediência precisa — não criatividade religiosa.</div>',
    '<div class="timeline-period">Leviticus 8–10</div>\n        <div class="timeline-title">The Ordination of the Priesthood and the Strange Fire</div>\n        <div class="timeline-text">Aaron and his sons are anointed and ordained in seven-day ceremonies. On the eighth day, as they offer the first sacrifice, divine fire consumes the burnt offering — a sign of divine acceptance (9:24). Immediately after, Nadab and Abihu, sons of Aaron, offer "unauthorized fire" not commanded by God (10:1) and are consumed. The holiness of the Tabernacle demands precise obedience — not religious creativity.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Levítico 11–15</div>\n        <div class="timeline-title">Leis de Pureza — Alimentos, Partos, Doenças</div>\n        <div class="timeline-text">Distinção entre animais puros e impuros (cap. 11). Purificação após o parto (cap. 12). Diagnóstico e tratamento da <em>tsara\'at</em> (lepra/doenças de pele — cap. 13–14). Impurezas corporais (cap. 15). Essas leis ensinavam a Israel que o pecado gera impureza que deve ser tratada antes do acesso ao Tabernáculo.</div>',
    '<div class="timeline-period">Leviticus 11–15</div>\n        <div class="timeline-title">Purity Laws — Food, Childbirth, Disease</div>\n        <div class="timeline-text">Distinction between clean and unclean animals (ch. 11). Purification after childbirth (ch. 12). Diagnosis and treatment of <em>tsara\'at</em> (skin disease/leprosy — chs. 13–14). Bodily discharges (ch. 15). These laws taught Israel that sin produces impurity that must be addressed before access to the Tabernacle.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Levítico 16</div>\n        <div class="timeline-title">O Dia da Expiação — Yom Kippur</div>\n        <div class="timeline-text">O capítulo mais importante do livro. Uma vez ao ano, o Sumo Sacerdote entra no Santo dos Santos com o sangue expiatório. Dois bodes: um sacrificado pelo pecado do povo; o outro — o bode expiatório (<em>azazel</em>) — carrega simbolicamente os pecados de Israel para o deserto. Hebreus 9–10 dedica extenso espaço à interpretação cristológica deste capítulo: Cristo é o Sumo Sacerdote e o sacrifício ao mesmo tempo.</div>',
    '<div class="timeline-period">Leviticus 16</div>\n        <div class="timeline-title">The Day of Atonement — Yom Kippur</div>\n        <div class="timeline-text">The most important chapter in the book. Once a year, the High Priest enters the Holy of Holies with atoning blood. Two goats: one sacrificed for the sin of the people; the other — the scapegoat (<em>azazel</em>) — symbolically carries Israel\'s sins into the wilderness. Hebrews 9–10 devotes extensive space to the christological interpretation of this chapter: Christ is both High Priest and sacrifice.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Levítico 17–27</div>\n        <div class="timeline-title">O Código de Santidade</div>\n        <div class="timeline-text">A segunda metade do livro (chamada pelos estudiosos de "Código de Santidade" ou H) é organizada ao redor do imperativo: "Sede santos." Abrange: proibição de idolatria e práticas pagãs; lei do amor ao próximo (19.18 — citada por Jesus como o segundo maior mandamento); as festas sagradas (cap. 23 — Páscoa, Pentecoste, Tabernáculos etc.); o Ano Sabático e o Ano do Jubileu (cap. 25); bênçãos e maldições da aliança (cap. 26).</div>',
    '<div class="timeline-period">Leviticus 17–27</div>\n        <div class="timeline-title">The Holiness Code</div>\n        <div class="timeline-text">The second half of the book (called by scholars the "Holiness Code" or H) is organized around the imperative: "Be holy." It covers: prohibition of idolatry and pagan practices; the law of love for neighbor (19:18 — cited by Jesus as the second greatest commandment); the sacred feasts (ch. 23 — Passover, Pentecost, Tabernacles, etc.); the Sabbatical Year and the Year of Jubilee (ch. 25); covenant blessings and curses (ch. 26).</div>',
    1
)
out = out.replace(
    '<h2>O Yom Kippur em Detalhe — Levítico 16</h2>\n    <p>O Dia da Expiação é a instituição litúrgica mais importante do AT e a que recebe a interpretação mais extensa no NT (Hebreus 9–10). O ritual tem cinco elementos principais:</p>',
    '<h2>Yom Kippur in Detail — Leviticus 16</h2>\n    <p>The Day of Atonement is the most important liturgical institution in the OT and the one that receives the most extensive interpretation in the NT (Hebrews 9–10). The ritual has five main elements:</p>',
    1
)
out = out.replace(
    '<div class="card-title">O Sumo Sacerdote se Prepara</div>\n        <p>Arão banha-se e veste roupas de linho branco — não as vestimentas douradas normais. A entrada no Santo dos Santos exige humildade, não ostentação. Oferece primeiro um holocausto <em>por si mesmo</em> (Lv 16.6) — o mediador humano precisa de expiação antes de poder expiar pelo povo.</p>',
    '<div class="card-title">The High Priest Prepares</div>\n        <p>Aaron bathes and puts on white linen garments — not the usual golden vestments. Entry into the Holy of Holies requires humility, not ostentation. He first offers a burnt offering <em>for himself</em> (Lev 16:6) — the human mediator needs atonement before he can atone for the people.</p>',
    1
)
out = out.replace(
    '<div class="card-title">O Sangue no Propiciatório</div>\n        <p>O sangue do bode sacrificado é aspergido sobre o <em>kapporet</em> (propiciatório — literalmente "tampa da misericórdia") sete vezes. O sangue cobre a lei contida na Arca. Paulo usa essa linguagem em Rm 3.25: Cristo é o <em>hilastérion</em> — o propiciatório, o lugar da expiação.</p>',
    '<div class="card-title">The Blood on the Mercy Seat</div>\n        <p>The blood of the sacrificed goat is sprinkled on the <em>kapporet</em> (mercy seat — literally "covering of mercy") seven times. The blood covers the law contained in the Ark. Paul uses this language in Rom 3:25: Christ is the <em>hilastērion</em> — the mercy seat, the place of atonement.</p>',
    1
)
out = out.replace(
    '<div class="card-title">O Bode Expiatório</div>\n        <p>Arão confessa todos os pecados de Israel sobre a cabeça do segundo bode vivo, que é então enviado ao deserto por um homem designado. A imagem é vívida: os pecados são <em>carregados para longe</em>, não apenas cobertos. Isaías 53.6, 11–12 usa exatamente essa linguagem de transferência.</p>',
    '<div class="card-title">The Scapegoat</div>\n        <p>Aaron confesses all of Israel\'s sins over the head of the second live goat, which is then sent into the wilderness by a designated man. The image is vivid: sins are <em>carried away</em>, not merely covered. Isaiah 53:6, 11–12 uses exactly this language of transfer.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Limitações e Cumprimento em Cristo</div>\n        <p>O ritual precisava ser repetido anualmente — sinal de sua incompletude. Hb 10.1–4: "É impossível que o sangue de touros e bodes tire pecados." Cristo, ao contrário, "com uma só oferenda aperfeiçoou para sempre os que são santificados" (Hb 10.14). O Yom Kippur apontava para aquilo que apenas Cristo podia fazer.</p>',
    '<div class="card-title">Limitations and Fulfillment in Christ</div>\n        <p>The ritual had to be repeated annually — a sign of its incompleteness. Heb 10:1–4: "It is impossible for the blood of bulls and goats to take away sins." Christ, by contrast, "by a single offering has perfected for all time those who are being sanctified" (Heb 10:14). Yom Kippur pointed to what only Christ could accomplish.</p>',
    1
)
out = out.replace(
    '<h2>As Festas Sagradas de Israel — Levítico 23</h2>',
    '<h2>The Sacred Feasts of Israel — Leviticus 23</h2>',
    1
)
out = out.replace(
    '<thead><tr><th>Festa</th><th>Data (calendário hebraico)</th><th>Significado</th><th>Cumprimento em Cristo</th></tr></thead>',
    '<thead><tr><th>Feast</th><th>Date (Hebrew calendar)</th><th>Significance</th><th>Fulfillment in Christ</th></tr></thead>',
    1
)
out = out.replace(
    '<tr><td>Páscoa (Pessah)</td><td>14 Nisã</td><td>Libertação do Egito; sangue do cordeiro</td><td>Crucificação de Cristo (1Co 5.7)</td></tr>',
    '<tr><td>Passover (Pesach)</td><td>14 Nisan</td><td>Liberation from Egypt; blood of the lamb</td><td>Crucifixion of Christ (1 Cor 5:7)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Pães Ázimos</td><td>15–21 Nisã</td><td>Pressa da saída; sem fermento (símbolo de pecado)</td><td>Vida sem pecado; sepultura de Cristo</td></tr>',
    '<tr><td>Unleavened Bread</td><td>15–21 Nisan</td><td>Haste of the departure; no leaven (symbol of sin)</td><td>Sinless life; burial of Christ</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Primícias</td><td>16 Nisã</td><td>Primeira gavela da colheita oferecida</td><td>Ressurreição de Cristo — "primícias dos que dormem" (1Co 15.20)</td></tr>',
    '<tr><td>Firstfruits</td><td>16 Nisan</td><td>First sheaf of the harvest offered</td><td>Resurrection of Christ — "firstfruits of those who have fallen asleep" (1 Cor 15:20)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Pentecoste (Shavuot)</td><td>6 Sivã (50 dias depois)</td><td>Colheita do trigo; entrega da Lei no Sinai</td><td>Derramamento do Espírito Santo (At 2)</td></tr>',
    '<tr><td>Pentecost (Shavuot)</td><td>6 Sivan (50 days later)</td><td>Wheat harvest; giving of the Law at Sinai</td><td>Outpouring of the Holy Spirit (Acts 2)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Trombetas (Rosh Hashaná)</td><td>1 Tishri</td><td>Início do ano civil; chamado à preparação</td><td>Retorno de Cristo (1Ts 4.16)</td></tr>',
    '<tr><td>Trumpets (Rosh Hashanah)</td><td>1 Tishri</td><td>Beginning of the civil year; call to preparation</td><td>Return of Christ (1 Thess 4:16)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Dia da Expiação (Yom Kippur)</td><td>10 Tishri</td><td>Expiação nacional</td><td>Segunda Vinda e arrependimento de Israel (Zc 12.10; Rm 11.26)</td></tr>',
    '<tr><td>Day of Atonement (Yom Kippur)</td><td>10 Tishri</td><td>National atonement</td><td>Second Coming and repentance of Israel (Zech 12:10; Rom 11:26)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Tabernáculos (Sukkot)</td><td>15–21 Tishri</td><td>Habitação no deserto; colheita final</td><td>Reino Milenar; habitação de Deus com os homens (Ap 21.3)</td></tr>',
    '<tr><td>Tabernacles (Sukkot)</td><td>15–21 Tishri</td><td>Wilderness dwelling; final harvest</td><td>Millennial Kingdom; God dwelling with men (Rev 21:3)</td></tr>',
    1
)
out = out.replace(
    '<h2>Versículo-Chave</h2>\n    <div class="scripture">\n      "Pois a vida da carne está no sangue; e eu o dei a vocês sobre o altar para fazer expiação pelas suas vidas, pois é o sangue que faz expiação por meio da vida."\n      <span class="scripture-ref">Levítico 17.11 — NAA</span>\n    </div>\n  </section>',
    '<h2>Key Verse</h2>\n    <div class="scripture">\n      "For the life of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls, for it is the blood that makes atonement by the life."\n      <span class="scripture-ref">Leviticus 17:11 — ESV</span>\n    </div>\n  </section>',
    1
)

# ═══ numeros section ═══
out = out.replace(
    '<span class="section-tag">Pentateuco · Livro IV</span>',
    '<span class="section-tag">Pentateuch · Book IV</span>',
    1
)
out = out.replace(
    '<h1 class="section-title">Números — O Livro da Peregrinação</h1>',
    '<h1 class="section-title">Numbers — The Book of the Wilderness</h1>',
    1
)
out = out.replace(
    '<p class="section-lead">Da geração da incredulidade à geração da fé — quarenta anos entre a revelação e a herança.</p>',
    '<p class="section-lead">From the generation of unbelief to the generation of faith — forty years between revelation and inheritance.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Dados Introdutórios</span>\n      <p><strong>Nome hebraico:</strong> <em>Bamidbar</em> (בְּמִדְבַּר) — "No deserto", da frase de abertura. <strong>Nome grego (LXX):</strong> <em>Arithmoi</em> — "Números" (pelos dois censos do livro). <strong>Capítulos:</strong> 36. <strong>Período histórico abrangido:</strong> c. 1446–1406 a.C. — do Sinai às planícies de Moabe, quase 40 anos. <strong>Estrutura central:</strong> dois censos (cap. 1 e 26) enquadram a tragédia da geração perdida.</p>',
    '<span class="callout-type">Introductory Data</span>\n      <p><strong>Hebrew name:</strong> <em>Bamidbar</em> (בְּמִדְבַּר) — "In the wilderness," from the opening phrase. <strong>Greek name (LXX):</strong> <em>Arithmoi</em> — "Numbers" (from the two censuses in the book). <strong>Chapters:</strong> 36. <strong>Historical period covered:</strong> c. 1446–1406 BC — from Sinai to the plains of Moab, nearly 40 years. <strong>Central structure:</strong> two censuses (chs. 1 and 26) frame the tragedy of the lost generation.</p>',
    1
)
out = out.replace(
    '<div class="info-card-label">Extensão</div><div class="info-card-value">36 capítulos · ~1446–1406 a.C. · quase 40 anos de peregrinação no deserto</div>',
    '<div class="info-card-label">Extent</div><div class="info-card-value">36 chapters · ~1446–1406 BC · nearly 40 years of wilderness wandering</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Dois censos</div><div class="info-card-value">Cap. 1: 603.550 homens (1ª geração) · cap. 26: 601.730 (2ª geração) · estrutura teológica da substituição geracional</div>',
    '<div class="info-card-label">Two censuses</div><div class="info-card-value">Ch. 1: 603,550 men (1st generation) · ch. 26: 601,730 (2nd generation) · theological structure of generational replacement</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Cades-Barneia</div><div class="info-card-value">Caps. 13–14: 10 espias com relatório negativo → toda a geração condenada a morrer no deserto por incredulidade</div>',
    '<div class="info-card-label">Kadesh-Barnea</div><div class="info-card-value">Chs. 13–14: 10 spies with negative report → entire generation condemned to die in the wilderness for unbelief</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Bênção aaronita</div><div class="info-card-value">Nm 6.24–26 — encontrada em amuletos de prata do séc. VII a.C. em Ketef Hinom · texto bíblico mais antigo fora da Escritura</div>',
    '<div class="info-card-label">Aaronic blessing</div><div class="info-card-value">Num 6:24–26 — found on silver amulets from the 7th century BC at Ketef Hinnom · oldest biblical text found outside Scripture</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Serpente de bronze</div><div class="info-card-value">Nm 21.8–9 — tipologia da crucificação citada por Jesus em Jo 3.14: "assim também o Filho do Homem precisa ser levantado"</div>',
    '<div class="info-card-label">Bronze serpent</div><div class="info-card-value">Num 21:8–9 — typology of the crucifixion cited by Jesus in John 3:14: "so must the Son of Man be lifted up"</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Advertência no NT</div><div class="info-card-value">1Co 10.1–12: Paulo usa os eventos do deserto como "exemplos e advertência" para os crentes da nova aliança</div>',
    '<div class="info-card-label">NT Warning</div><div class="info-card-value">1 Cor 10:1–12: Paul uses the wilderness events as "examples and warnings" for believers of the new covenant</div>',
    1
)
out = out.replace(
    '<h2>Estrutura Bipartida — Dois Censos, Duas Gerações</h2>\n    <p>O livro é organizado em torno de dois recenseamentos militares. Entre eles, uma geração inteira perece no deserto por incredulidade. A estrutura é teológica, não apenas cronológica:</p>',
    '<h2>Bipartite Structure — Two Censuses, Two Generations</h2>\n    <p>The book is organized around two military censuses. Between them, an entire generation perishes in the wilderness because of unbelief. The structure is theological, not merely chronological:</p>',
    1
)
out = out.replace(
    '<div class="card-title">Primeira Geração (Capítulos 1–25)</div>\n        <p><strong>Censo 1 — Números 1:</strong> 603.550 homens de guerra. Esta geração havia visto as pragas, a Páscoa, a travessia do Mar, a teofania do Sinai. Tinham todo fundamento para confiar. Mas ao ser colocada diante da resistência (os espias), escolheu o medo. Toda essa geração morre no deserto — exceto Calebe e Josué.</p>',
    '<div class="card-title">First Generation (Chapters 1–25)</div>\n        <p><strong>Census 1 — Numbers 1:</strong> 603,550 fighting men. This generation had seen the plagues, the Passover, the crossing of the Sea, the theophany at Sinai. They had every foundation to trust. But when faced with resistance (the spies), they chose fear. The entire generation dies in the wilderness — except Caleb and Joshua.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Segunda Geração (Capítulos 26–36)</div>\n        <p><strong>Censo 2 — Números 26:</strong> 601.730 homens de guerra — quase o mesmo número, mas agora são pessoas completamente diferentes. Esta é a geração que entrará em Canaã. Os capítulos finais preparam essa geração: distribuição da terra, leis sobre heranças, cidades de refúgio.</p>',
    '<div class="card-title">Second Generation (Chapters 26–36)</div>\n        <p><strong>Census 2 — Numbers 26:</strong> 601,730 fighting men — almost the same number, but now completely different people. This is the generation that will enter Canaan. The final chapters prepare this generation: land distribution, inheritance laws, cities of refuge.</p>',
    1
)
out = out.replace(
    '<h2>Os Grandes Eventos de Números</h2>',
    '<h2>The Great Events of Numbers</h2>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 1–10</div>\n        <div class="timeline-title">Preparação para a Marcha</div>\n        <div class="timeline-text">Censo militar e organização do acampamento ao redor do Tabernáculo (cada tribo em posição específica — o Tabernáculo no centro). A consagração dos levitas. Os nazireus e a bênção aaronita (6.24–26): "O SENHOR te abençoe e te guarde; o SENHOR faça resplandecer o seu rosto sobre ti..." — a bênção mais repetida da Escritura. Israel parte do Sinai no décimo quinto mês após o Êxodo.</div>',
    '<div class="timeline-period">Numbers 1–10</div>\n        <div class="timeline-title">Preparation for the March</div>\n        <div class="timeline-text">Military census and organization of the camp around the Tabernacle (each tribe in a specific position — the Tabernacle at the center). The consecration of the Levites. The Nazirites and the Aaronic blessing (6:24–26): "The Lord bless you and keep you; the Lord make his face shine on you..." — the most repeated blessing in Scripture. Israel departs from Sinai in the fifteenth month after the Exodus.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 11–12</div>\n        <div class="timeline-title">As Primeiras Murmurações</div>\n        <div class="timeline-text">Queixa pelo fogo (Tabera). Queixa por carne (Quibrote-Taavá) — Deus envia codornizes e praga simultaneamente. Moisés recebe 70 anciãos ungidos com seu espírito (prefigurando o Espírito derramado em Pentecostes). Rebelião de Miriã e Aarão contra Moisés.</div>',
    '<div class="timeline-period">Numbers 11–12</div>\n        <div class="timeline-title">The First Complaints</div>\n        <div class="timeline-text">Complaint about fire (Taberah). Complaint for meat (Kibroth-hattaavah) — God sends quail and a plague simultaneously. Moses receives 70 elders anointed with his spirit (prefiguring the Spirit poured out at Pentecost). Rebellion of Miriam and Aaron against Moses.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 13–14</div>\n        <div class="timeline-title">Os Doze Espias — A Tragédia de Cades-Barneia</div>\n        <div class="timeline-text">Doze espias, um por tribo, exploram Canaã por quarenta dias. Dez trazem relatório do "impossível": "somos como gafanhotos aos olhos deles" (13.33). Dois — Calebe e Josué — creem que Deus pode conquistar a terra. O povo chora, murmura, ameaça lapidar Moisés e Josué, e deseja retornar ao Egito. O julgamento: 40 anos no deserto (um por dia de espionagem); a geração adulta morrerá sem entrar. Hebreus 3–4 usa este evento como advertência aos crentes de não endurecer o coração.</div>',
    '<div class="timeline-period">Numbers 13–14</div>\n        <div class="timeline-title">The Twelve Spies — The Tragedy of Kadesh-Barnea</div>\n        <div class="timeline-text">Twelve spies, one per tribe, explore Canaan for forty days. Ten bring back an "impossible" report: "we seemed to ourselves like grasshoppers" (13:33). Two — Caleb and Joshua — trust that God can conquer the land. The people weep, complain, threaten to stone Moses and Joshua, and desire to return to Egypt. The judgment: 40 years in the wilderness (one per day of spying); the adult generation will die without entering. Hebrews 3–4 uses this event as a warning to believers not to harden their hearts.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 16–17</div>\n        <div class="timeline-title">A Rebelião de Coré, Datã e Abirão</div>\n        <div class="timeline-text">Coré (levita) e 250 líderes civis contestam o sacerdócio exclusivo de Aarão: "Toda a congregação é santa" (16.3). O julgamento é dramático: a terra se abre e engole Coré e seus seguidores; fogo consome os 250. A vara de Aarão que floresceu (cap. 17) confirma diviniamente o sacerdócio aaronita.</div>',
    '<div class="timeline-period">Numbers 16–17</div>\n        <div class="timeline-title">The Rebellion of Korah, Dathan, and Abiram</div>\n        <div class="timeline-text">Korah (a Levite) and 250 civil leaders challenge Aaron\'s exclusive priesthood: "All the congregation is holy" (16:3). The judgment is dramatic: the earth opens and swallows Korah and his followers; fire consumes the 250. Aaron\'s staff that budded (ch. 17) divinely confirms the Aaronic priesthood.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 20–21</div>\n        <div class="timeline-title">Meriba, Morte de Arão, Serpente de Bronze</div>\n        <div class="timeline-text">Moisés golpeia a rocha (Meriba) — excluído de Canaã. Arão morre no Monte Hor; Eleazar assume o sacerdócio. Edom recusa passagem. Vitória sobre o rei Arade. Nova murmuração resulta em cobras ardentes; a serpente de bronze erguida é tipologia da crucificação (Jo 3.14). Vitórias sobre Siom (rei dos amorreus) e Ogue (rei de Basã).</div>',
    '<div class="timeline-period">Numbers 20–21</div>\n        <div class="timeline-title">Meribah, Death of Aaron, Bronze Serpent</div>\n        <div class="timeline-text">Moses strikes the rock (Meribah) — excluded from Canaan. Aaron dies at Mount Hor; Eleazar assumes the priesthood. Edom refuses passage. Victory over the king of Arad. New grumbling results in fiery serpents; the bronze serpent lifted up is a typology of the crucifixion (John 3:14). Victories over Sihon (king of the Amorites) and Og (king of Bashan).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 22–25</div>\n        <div class="timeline-title">Balaão e a Tentação de Moabe</div>\n        <div class="timeline-text">Balaque, rei de Moabe, contrata Balaão para amaldiçoar Israel. Deus impede a maldição — Balaão profere quatro bênçãos sobre Israel, incluindo a profecia messiânica da "estrela de Jacó" (24.17). No cap. 25, Israel peca sexualmente com mulheres de Moabe e adora Baal-Peor — 24.000 morrem na praga. Finéias (neto de Aarão) zela pela honra de Deus e detém a praga (25.11–13; citado em Sl 106.30–31).</td>',
    '<div class="timeline-period">Numbers 22–25</div>\n        <div class="timeline-title">Balaam and the Temptation of Moab</div>\n        <div class="timeline-text">Balak, king of Moab, hires Balaam to curse Israel. God prevents the curse — Balaam pronounces four blessings over Israel, including the messianic prophecy of the "star of Jacob" (24:17). In ch. 25, Israel commits sexual immorality with Moabite women and worships Baal-Peor — 24,000 die in the plague. Phinehas (grandson of Aaron) is zealous for God\'s honor and stops the plague (25:11–13; cited in Ps 106:30–31).</td>',
    1
)
out = out.replace(
    '<div class="timeline-period">Números 26–36</div>\n        <div class="timeline-title">A Nova Geração — Preparação para Canaã</div>\n        <div class="timeline-text">Segundo censo. Josué designado como sucessor de Moisés (27.12–23). Leis sobre ofertas, votos, guerra contra Midiã. As tribos de Rúben, Gade e meia tribo de Manassés pedem terras a leste do Jordão (cap. 32). Cidades de refúgio (cap. 35). Fronteiras da terra prometida.</div>',
    '<div class="timeline-period">Numbers 26–36</div>\n        <div class="timeline-title">The New Generation — Preparation for Canaan</div>\n        <div class="timeline-text">Second census. Joshua designated as Moses\'s successor (27:12–23). Laws on offerings, vows, war against Midian. The tribes of Reuben, Gad, and half of Manasseh request land east of the Jordan (ch. 32). Cities of refuge (ch. 35). Boundaries of the promised land.</div>',
    1
)
out = out.replace(
    '<h2>A Bênção Aaronita — Números 6.24–26</h2>',
    '<h2>The Aaronic Blessing — Numbers 6:24–26</h2>',
    1
)
out = out.replace(
    '"O <span style="font-variant:small-caps">Senhor</span> abençoe você e o proteja; o <span style="font-variant:small-caps">Senhor</span> faça resplandecer o seu rosto sobre você e lhe conceda graça; o <span style="font-variant:small-caps">Senhor</span> volte o seu rosto para você e lhe dê paz."\n      <span class="scripture-ref">Números 6.24–26 — NAA</span>',
    '"The <span style="font-variant:small-caps">Lord</span> bless you and keep you; the <span style="font-variant:small-caps">Lord</span> make his face shine on you and be gracious to you; the <span style="font-variant:small-caps">Lord</span> turn his face toward you and give you peace."\n      <span class="scripture-ref">Numbers 6:24–26 — ESV</span>',
    1
)
out = out.replace(
    'Esta bênção tripartite — descoberta em dois amuletos de prata no túmulo de Ketef Hinom (Jerusalém), datados do século VII a.C. — é o texto bíblico mais antigo jamais encontrado fora da Escritura. Cada uma das três petições intensifica a anterior: <em>guardar</em> → <em>ser gracioso</em> → <em>dar paz (shalom)</em>. O rosto de Deus que "resplandece" é a mesma linguagem do rosto de Moisés que resplandecia após a presença divina.',
    'This tripartite blessing — discovered on two silver amulets in the tomb of Ketef Hinnom (Jerusalem), dated to the 7th century BC — is the oldest biblical text ever found outside Scripture. Each of the three petitions intensifies the previous one: <em>keep</em> → <em>be gracious</em> → <em>give peace (shalom)</em>. The face of God that "shines" is the same language used for Moses\'s face which radiated after the divine presence.',
    1
)
out = out.replace(
    '<h2>Números no NT — Advertência e Esperança</h2>',
    '<h2>Numbers in the NT — Warning and Hope</h2>',
    1
)
out = out.replace(
    '<span class="callout-type">1 Coríntios 10.1–12 — Paulo e o Deserto</span>\n      <p>Paulo usa Números sistematicamente como espelho para a igreja de Corinto: "Estas coisas lhes sucederam como exemplos e foram escritas para advertência nossa" (1Co 10.11). Os quatro pecados que Paulo identifica são: idolatria (o bezerro de ouro), imoralidade sexual (Baal-Peor), tentação a Deus (cobras) e murmuração. O deserto de Israel é o manual de advertência para os crentes da nova aliança. Hebreus 3–4 faz o mesmo com a incredulidade de Cades.</p>',
    '<span class="callout-type">1 Corinthians 10:1–12 — Paul and the Wilderness</span>\n      <p>Paul uses Numbers systematically as a mirror for the church of Corinth: "These things happened to them as examples and were written down as warnings for us" (1 Cor 10:11). The four sins Paul identifies are: idolatry (the golden calf), sexual immorality (Baal-Peor), testing God (serpents), and grumbling. Israel\'s wilderness is the warning manual for new-covenant believers. Hebrews 3–4 does the same with the unbelief of Kadesh.</p>',
    1
)
out = out.replace(
    '<h2>Versículo-Chave</h2>\n    <div class="scripture">\n      "Assim como Moisés levantou a serpente no deserto, assim também o Filho do Homem precisa ser levantado, para que todo aquele que nele crê tenha a vida eterna."\n      <span class="scripture-ref">João 3.14–15 — NAA · Jesus citando Números 21</span>\n    </div>\n  </section>',
    '<h2>Key Verse</h2>\n    <div class="scripture">\n      "And as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life."\n      <span class="scripture-ref">John 3:14–15 — ESV · Jesus citing Numbers 21</span>\n    </div>\n  </section>',
    1
)

# ═══ deuteronomio section ═══
out = out.replace(
    '<span class="section-tag">Pentateuco · Livro V</span>',
    '<span class="section-tag">Pentateuch · Book V</span>',
    1
)
out = out.replace(
    '<h1 class="section-title">Deuteronômio — O Livro da Renovação</h1>',
    '<h1 class="section-title">Deuteronomy — The Book of Renewal</h1>',
    1
)
out = out.replace(
    '<p class="section-lead">O sermão do adeus — Moisés renova a aliança com a geração que entrará na terra.</p>',
    '<p class="section-lead">The farewell sermon — Moses renews the covenant with the generation that will enter the land.</p>',
    1
)
out = out.replace(
    '<span class="callout-type">Dados Introdutórios</span>\n      <p><strong>Nome hebraico:</strong> <em>Devarim</em> (דְּבָרִים) — "Palavras", da frase de abertura "Estas são as palavras que Moisés falou a todo o Israel." <strong>Nome grego (LXX):</strong> <em>Deuteronomion</em> — "segunda lei" (expressão retirada de Dt 17.18, onde o rei deve copiar <em>mishneh hatorah</em> — "uma cópia desta lei"). <strong>Capítulos:</strong> 34. <strong>Período histórico:</strong> planícies de Moabe, último mês antes da travessia do Jordão, c. 1406 a.C. <strong>Forma literária:</strong> tratado de aliança suzerano — o mais extenso do Pentateuco.</p>',
    '<span class="callout-type">Introductory Data</span>\n      <p><strong>Hebrew name:</strong> <em>Devarim</em> (דְּבָרִים) — "Words," from the opening phrase "These are the words that Moses spoke to all Israel." <strong>Greek name (LXX):</strong> <em>Deuteronomion</em> — "second law" (expression taken from Deut 17:18, where the king must copy <em>mishneh hatorah</em> — "a copy of this law"). <strong>Chapters:</strong> 34. <strong>Historical period:</strong> plains of Moab, last month before crossing the Jordan, c. 1406 BC. <strong>Literary form:</strong> suzerain-vassal covenant treaty — the most extensive in the Pentateuch.</p>',
    1
)
out = out.replace(
    '<div class="info-card-label">Extensão</div><div class="info-card-value">34 capítulos · planícies de Moabe · último mês antes da entrada em Canaã (~1406 a.C.)</div>',
    '<div class="info-card-label">Extent</div><div class="info-card-value">34 chapters · plains of Moab · last month before entering Canaan (~1406 BC)</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Forma literária</div><div class="info-card-value">Tratado de aliança suzerano-vassalo — paralelo estrutural aos tratados hititas do séc. XIV–XIII a.C.</div>',
    '<div class="info-card-label">Literary form</div><div class="info-card-value">Suzerain-vassal covenant treaty — structural parallel to Hittite treaties of the 14th–13th century BC</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Shemá</div><div class="info-card-value">Dt 6.4–5 — "Ouve, Israel: o Senhor é o nosso Deus, o único Senhor" · chamado pelo Jesus o maior mandamento</div>',
    '<div class="info-card-label">Shema</div><div class="info-card-value">Deut 6:4–5 — "Hear, O Israel: the Lord our God, the Lord is one" · called by Jesus the greatest commandment</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Profeta prometido</div><div class="info-card-value">Dt 18.15–18 — "o Senhor suscitará um profeta semelhante a mim" · citado em At 3.22 e Jo 6.14 como referência a Jesus</div>',
    '<div class="info-card-label">Promised prophet</div><div class="info-card-value">Deut 18:15–18 — "the Lord will raise up a prophet like me" · cited in Acts 3:22 and John 6:14 as a reference to Jesus</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Livro mais citado por Jesus</div><div class="info-card-value">Nas três tentações no deserto (Mt 4), Jesus cita Deuteronômio três vezes · o livro da obediência filial</div>',
    '<div class="info-card-label">Most cited OT book by Jesus</div><div class="info-card-value">In the three wilderness temptations (Matt 4), Jesus quotes Deuteronomy three times · the book of filial obedience</div>',
    1
)
out = out.replace(
    '<div class="info-card-label">Morte de Moisés</div><div class="info-card-value">Cap. 34: Moisés vê Canaã do Monte Nebo e morre sem entrar · "nunca mais se levantou em Israel profeta igual a Moisés" (34.10)</div>',
    '<div class="info-card-label">Death of Moses</div><div class="info-card-value">Ch. 34: Moses sees Canaan from Mount Nebo and dies without entering · "there has not arisen a prophet since in Israel like Moses" (34:10)</div>',
    1
)
out = out.replace(
    '<h2>Deuteronômio e os Tratados Hititas</h2>\n    <p>O linguista e arqueólogo George Mendenhall (1954) demonstrou que a estrutura de Deuteronômio corresponde precisamente aos tratados de suzerania hititas do segundo milênio a.C. Isso confirma a datação conservadora (mosaica) do livro — esses tratados não eram mais usados no primeiro milênio, época em que a crítica liberal situa a composição do livro.</p>',
    "<h2>Deuteronomy and the Hittite Treaties</h2>\n    <p>Linguist and archaeologist George Mendenhall (1954) demonstrated that the structure of Deuteronomy corresponds precisely to the Hittite suzerainty treaties of the second millennium BC. This confirms the conservative (Mosaic) dating of the book — these treaties were no longer in use in the first millennium, the period in which liberal criticism places the book's composition.</p>",
    1
)
out = out.replace(
    '<thead><tr><th>Elemento do Tratado Hitita</th><th>Correspondência em Deuteronômio</th></tr></thead>',
    '<thead><tr><th>Hittite Treaty Element</th><th>Correspondence in Deuteronomy</th></tr></thead>',
    1
)
out = out.replace(
    '<tr><td>Preâmbulo — identificação do soberano</td><td>"Estas são as palavras que Moisés falou" / YHWH como soberano (1.1–5)</td></tr>',
    '<tr><td>Preamble — identification of the sovereign</td><td>"These are the words that Moses spoke" / YHWH as sovereign (1:1–5)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Prólogo histórico — atos benevolentes</td><td>Recapitulação da história do Êxodo e deserto (1.6–3.29)</td></tr>',
    '<tr><td>Historical prologue — benevolent acts</td><td>Recapitulation of the Exodus and wilderness history (1:6–3:29)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Estipulações — obrigações do vassalo</td><td>Os mandamentos e leis (4.1–26.19)</td></tr>',
    '<tr><td>Stipulations — vassal obligations</td><td>The commandments and laws (4:1–26:19)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Cláusula de depósito e leitura pública</td><td>"Escreverás todas as palavras desta lei... lerás esta lei a todo Israel" (27.1–3; 31.9–13)</td></tr>',
    '<tr><td>Deposit and public reading clause</td><td>"You shall write all the words of this law... you shall read this law before all Israel" (27:1–3; 31:9–13)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Lista de testemunhas</td><td>Céu e terra como testemunhas (30.19; 31.28)</td></tr>',
    '<tr><td>Witness list</td><td>Heaven and earth as witnesses (30:19; 31:28)</td></tr>',
    1
)
out = out.replace(
    '<tr><td>Bênçãos e maldições</td><td>Bênçãos da obediência / maldições da desobediência (cap. 27–28)</td></tr>',
    '<tr><td>Blessings and curses</td><td>Blessings of obedience / curses of disobedience (chs. 27–28)</td></tr>',
    1
)
out = out.replace(
    '<h2>Estrutura do Livro — Três Discursos de Moisés</h2>',
    '<h2>Structure of the Book — Three Discourses of Moses</h2>',
    1
)
out = out.replace(
    '<div class="timeline-period">Deuteronômio 1–4</div>\n        <div class="timeline-title">Primeiro Discurso — Recapitulação Histórica</div>\n        <div class="timeline-text">Moisés recapitula a jornada do Sinai às planícies de Moabe: os espias, o julgamento no deserto, as vitórias sobre Siom e Ogue. O objetivo é teológico: que a nova geração entenda que o Deus que os conduz é o mesmo que agiu na história. O discurso culmina no apelo: "Sabe, pois, hoje, e considera no teu coração, que o SENHOR é Deus, em cima no céu e embaixo na terra; não há outro" (4.39).</div>',
    '<div class="timeline-period">Deuteronomy 1–4</div>\n        <div class="timeline-title">First Discourse — Historical Recapitulation</div>\n        <div class="timeline-text">Moses recapitulates the journey from Sinai to the plains of Moab: the spies, the judgment in the wilderness, the victories over Sihon and Og. The purpose is theological: that the new generation understand that the God leading them is the same who acted in history. The discourse culminates in the appeal: "Know therefore today, and lay it to your heart, that the Lord is God in heaven above and on the earth beneath; there is no other" (4:39).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Deuteronômio 5–26</div>\n        <div class="timeline-title">Segundo Discurso — A Lei Reafirmada e Expandida</div>\n        <div class="timeline-text">O coração do livro. Repetição dos Dez Mandamentos (cap. 5 — com diferença sutil no mandamento do Sábado: Êx 20 funda no descanso de Deus na criação; Dt 5 funda no Êxodo). O Shemá (6.4–9). O imperativo de não esquecer (cap. 8). Leis sobre o santuário central (cap. 12), profecia (cap. 18), rei, sacerdotes, cidades de refúgio, testemunhos, guerra santa e legislação social abrangente (cap. 12–25). A liturgia das primícias (26.1–11): confissão de fé histórica de Israel.</div>',
    '<div class="timeline-period">Deuteronomy 5–26</div>\n        <div class="timeline-title">Second Discourse — The Law Reaffirmed and Expanded</div>\n        <div class="timeline-text">The heart of the book. Repetition of the Ten Commandments (ch. 5 — with a subtle difference in the Sabbath commandment: Exod 20 grounds it in God\'s rest at creation; Deut 5 grounds it in the Exodus). The Shema (6:4–9). The imperative not to forget (ch. 8). Laws on the central sanctuary (ch. 12), prophecy (ch. 18), the king, priests, cities of refuge, witnesses, holy war, and comprehensive social legislation (chs. 12–25). The firstfruits liturgy (26:1–11): Israel\'s historical creed.</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Deuteronômio 27–30</div>\n        <div class="timeline-title">Bênçãos e Maldições — A Aliança em Vigor</div>\n        <div class="timeline-text">Cerimônia de renovação da aliança nos montes Gerizim e Ebal (instrução que Josué executará em Js 8). As bênçãos da obediência (28.1–14) e as maldições da desobediência (28.15–68 — o capítulo de juízo mais extenso do AT, com profecias que foram literalmente cumpridas na conquista assíria e babilônica). O chamado ao retorno e à restauração (cap. 30) — "Eu ponho diante de ti a vida e a morte... Escolhe, pois, a vida" (30.19).</div>',
    '<div class="timeline-period">Deuteronomy 27–30</div>\n        <div class="timeline-title">Blessings and Curses — The Covenant in Effect</div>\n        <div class="timeline-text">Covenant renewal ceremony at Mount Gerizim and Mount Ebal (the instruction Joshua will carry out in Josh 8). The blessings of obedience (28:1–14) and the curses of disobedience (28:15–68 — the most extensive judgment chapter in the OT, with prophecies that were literally fulfilled in the Assyrian and Babylonian conquests). The call to return and restoration (ch. 30) — "I have set before you life and death... therefore choose life" (30:19).</div>',
    1
)
out = out.replace(
    '<div class="timeline-period">Deuteronômio 31–34</div>\n        <div class="timeline-title">Terceiro Discurso — Despedida, Cântico e Morte</div>\n        <div class="timeline-text">Moisés designa Josué como sucessor (31.1–8). Entrega a lei aos sacerdotes para leitura a cada sete anos. O Cântico de Moisés (cap. 32 — poema didático sobre a fidelidade de YHWH e a infidelidade de Israel). A Bênção das Tribos (cap. 33 — paralela à bênção de Jacó em Gn 49). Morte de Moisés no Monte Nebo (cap. 34).</div>',
    '<div class="timeline-period">Deuteronomy 31–34</div>\n        <div class="timeline-title">Third Discourse — Farewell, Song, and Death</div>\n        <div class="timeline-text">Moses appoints Joshua as successor (31:1–8). Delivers the law to the priests for reading every seven years. The Song of Moses (ch. 32 — a didactic poem about YHWH\'s faithfulness and Israel\'s unfaithfulness). The Blessing of the Tribes (ch. 33 — parallel to Jacob\'s blessing in Gen 49). Death of Moses on Mount Nebo (ch. 34).</div>',
    1
)
out = out.replace(
    '<h2>O Shemá — Deuteronômio 6.4–9</h2>',
    '<h2>The Shema — Deuteronomy 6:4–9</h2>',
    1
)
out = out.replace(
    '"Ouça, Israel: O <span style="font-variant:small-caps">Senhor</span>, o nosso Deus, é o único <span style="font-variant:small-caps">Senhor</span>. Você amará o <span style="font-variant:small-caps">Senhor</span>, o seu Deus, de todo o coração, com toda a sua alma e com toda a sua força. Estas palavras que hoje lhe ordeno deverão estar no seu coração; você as ensinará diligentemente a seus filhos..."\n      <span class="scripture-ref">Deuteronômio 6.4–7 — NAA</span>',
    '"Hear, O Israel: The <span style="font-variant:small-caps">Lord</span> our God, the <span style="font-variant:small-caps">Lord</span> is one. You shall love the <span style="font-variant:small-caps">Lord</span> your God with all your heart and with all your soul and with all your might. And these words that I command you today shall be on your heart. You shall teach them diligently to your children..."\n      <span class="scripture-ref">Deuteronomy 6:4–7 — ESV</span>',
    1
)
out = out.replace(
    'O Shemá (<em>shema</em> = "ouve") é a oração central do judaísmo — recitada duas vezes ao dia desde a antiguidade. Jesus o citou como o "primeiro e maior mandamento" (Mc 12.29–30), fundindo-o com Levítico 19.18 ("amar ao próximo") em um resumo de toda a lei e os profetas (Mt 22.40).',
    'The Shema (<em>shema</em> = "hear") is the central prayer of Judaism — recited twice daily since antiquity. Jesus cited it as the "first and greatest commandment" (Mark 12:29–30), fusing it with Leviticus 19:18 ("love your neighbor") into a summary of all the law and the prophets (Matt 22:40).',
    1
)
out = out.replace(
    '<h2>O Capítulo 28 — Profecias Cumpridas</h2>\n    <p>Deuteronômio 28 contém a mais longa sequência de profecias condicionais do AT. As maldições da desobediência (vers. 15–68) descrevem com precisão eventos que ocorreram séculos depois:</p>',
    '<h2>Chapter 28 — Fulfilled Prophecies</h2>\n    <p>Deuteronomy 28 contains the longest sequence of conditional prophecies in the OT. The curses of disobedience (vv. 15–68) describe with precision events that occurred centuries later:</p>',
    1
)
out = out.replace(
    '<div class="card-title">Cumprimento Assírio (722 a.C.)</div>\n        <p>Deuteronômio 28.36 ("O SENHOR te levará a ti e ao teu rei a uma nação que não conheceste") e 28.64 ("O SENHOR te espalhará por todos os povos") — cumprido com a deportação das dez tribos do norte pela Assíria sob Salmaneser V e Sargão II.</p>',
    '<div class="card-title">Assyrian Fulfillment (722 BC)</div>\n        <p>Deuteronomy 28:36 ("The Lord will bring you and your king to a nation that neither you nor your fathers have known") and 28:64 ("The Lord will scatter you among all peoples") — fulfilled with the deportation of the ten northern tribes by Assyria under Shalmaneser V and Sargon II.</p>',
    1
)
out = out.replace(
    '<div class="card-title">Cumprimento Babilônico (586 a.C.) e Romano (70 d.C.)</div>\n        <p>Deuteronômio 28.49–52 (nação de longe como águia — a águia romana) e 28.53–57 (comer os próprios filhos durante o cerco — cumprido literalmente durante o cerco de Tito a Jerusalém, documentado por Josefo em "A Guerra Judaica").</p>',
    '<div class="card-title">Babylonian (586 BC) and Roman (70 AD) Fulfillment</div>\n        <p>Deuteronomy 28:49–52 (a nation from far away like an eagle — the Roman eagle) and 28:53–57 (eating their own children during the siege — fulfilled literally during Titus\'s siege of Jerusalem, documented by Josephus in "The Jewish War").</p>',
    1
)
out = out.replace(
    '<h2>Deuteronômio no NT — O Livro Mais Citado por Jesus</h2>',
    '<h2>Deuteronomy in the NT — The Book Most Cited by Jesus</h2>',
    1
)
out = out.replace(
    '<span class="callout-type">Jesus e Deuteronômio</span>\n      <p>Deuteronômio é o livro do AT mais citado por Jesus — especialmente durante a tentação no deserto (Mt 4.1–11). Cada uma das três respostas de Jesus ao diabo vem de Deuteronômio: "Nem só de pão viverá o homem" (Dt 8.3); "Não tentarás o Senhor teu Deus" (Dt 6.16); "Ao Senhor teu Deus adorarás" (Dt 6.13). O segundo Adão, tentado no deserto, vence citando o livro escrito para o povo que falhou no deserto. O que Israel não pôde fazer, Cristo fez.</p>',
    '<span class="callout-type">Jesus and Deuteronomy</span>\n      <p>Deuteronomy is the OT book most cited by Jesus — especially during the wilderness temptation (Matt 4:1–11). Each of Jesus\'s three responses to the devil comes from Deuteronomy: "Man shall not live by bread alone" (Deut 8:3); "You shall not put the Lord your God to the test" (Deut 6:16); "You shall worship the Lord your God" (Deut 6:13). The second Adam, tempted in the wilderness, conquers by quoting the book written for the people who failed in the wilderness. What Israel could not do, Christ did.</p>',
    1
)
out = out.replace(
    '<h2>O Profeta Prometido — Deuteronômio 18.15–18</h2>\n    <p>A profecia messiânica central do Pentateuco:</p>',
    '<h2>The Promised Prophet — Deuteronomy 18:15–18</h2>\n    <p>The central messianic prophecy of the Pentateuch:</p>',
    1
)
out = out.replace(
    '"O <span style="font-variant:small-caps">Senhor</span>, o seu Deus, levantará para você um profeta dentre os seus compatriotas, semelhante a mim; a ele vocês ouvirão... Levantarei para eles um profeta dentre seus compatriotas, semelhante a você; porei as minhas palavras na sua boca, e ele lhes dirá tudo o que eu lhe ordenar."\n      <span class="scripture-ref">Deuteronômio 18.15, 18 — NAA</span>',
    '"The <span style="font-variant:small-caps">Lord</span> your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen... I will raise up for them a prophet like you from among their brothers. And I will put my words in his mouth, and he shall speak to them all that I command him."\n      <span class="scripture-ref">Deuteronomy 18:15, 18 — ESV</span>',
    1
)
out = out.replace(
    'Pedro (At 3.22), Estêvão (At 7.37) e o próprio João (1.21, 45) identificam este profeta com Jesus. O critério de autenticação profética de Deuteronômio 18.21–22 ("se o profeta falar em nome do SENHOR, e a palavra não se cumprir") estabelece o padrão pelo qual toda profecia deve ser avaliada — um princípio de discernimento ainda aplicável.',
    'Peter (Acts 3:22), Stephen (Acts 7:37), and John himself (1:21, 45) identify this prophet with Jesus. The prophetic authentication criterion of Deuteronomy 18:21–22 ("if the prophet speaks in the name of the Lord and the word does not come to pass") establishes the standard by which all prophecy must be evaluated — a discernment principle still applicable today.',
    1
)
out = out.replace(
    '<h2>Versículo-Chave</h2>\n    <div class="scripture">\n      "Veja que hoje coloco diante de você a vida e o bem, a morte e o mal... Chamo o céu e a terra como testemunhas contra você hoje, de que coloquei diante de você a vida e a morte, a bênção e a maldição. Escolha, pois, a vida, para que você e os seus descendentes vivam."\n      <span class="scripture-ref">Deuteronômio 30.15, 19 — NAA</span>\n    </div>\n  </section>',
    '<h2>Key Verse</h2>\n    <div class="scripture">\n      "See, I have set before you today life and good, death and evil... I call heaven and earth to witness against you today, that I have set before you life and death, blessing and curse. Therefore choose life, that you and your offspring may live."\n      <span class="scripture-ref">Deuteronomy 30:15, 19 — ESV</span>\n    </div>\n  </section>',
    1
)

# ═══ plague fixes (correct refs) ═══
out = out.replace(
    '<div class="plague-name">Águas em Sangue</div>\n          <div class="plague-ref">Êx 7.14–25 · Ataca Hápi (deus do Nilo)</div>',
    '<div class="plague-name">Water to Blood</div>\n          <div class="plague-ref">Exod 7:14–25 · Targets Hapi (god of the Nile)</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Rãs</div>\n          <div class="plague-ref">Êx 8.1–15 · Ataca Heqet (deusa das rãs)</div>',
    '<div class="plague-name">Frogs</div>\n          <div class="plague-ref">Exod 8:1–15 · Targets Heqet (frog goddess)</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Piolhos / Mosquitos</div>\n          <div class="plague-ref">Êx 8.16–19 · Magos não reproduzem</div>',
    '<div class="plague-name">Gnats / Lice</div>\n          <div class="plague-ref">Exod 8:16–19 · Magicians cannot replicate</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Moscas</div>\n          <div class="plague-ref">Êx 8.20–32 · Distinção: Gósen preservada</div>',
    '<div class="plague-name">Flies</div>\n          <div class="plague-ref">Exod 8:20–32 · Distinction: Goshen preserved</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Peste no Gado</div>\n          <div class="plague-ref">Êx 9.1–7 · Ataca Ápis (touro sagrado)</div>',
    '<div class="plague-name">Livestock Disease</div>\n          <div class="plague-ref">Exod 9:1–7 · Targets Apis (sacred bull)</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Úlceras</div>\n          <div class="plague-ref">Êx 9.8–12 · Magos humilhados</div>',
    '<div class="plague-name">Boils</div>\n          <div class="plague-ref">Exod 9:8–12 · Magicians humiliated</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Granizo</div>\n          <div class="plague-ref">Êx 9.13–35 · Ataca Nut (céu) e Shu (ar)</div>',
    '<div class="plague-name">Hail</div>\n          <div class="plague-ref">Exod 9:13–35 · Targets Nut (sky) and Shu (air)</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Gafanhotos</div>\n          <div class="plague-ref">Êx 10.1–20 · Devastação agrícola total</div>',
    '<div class="plague-name">Locusts</div>\n          <div class="plague-ref">Exod 10:1–20 · Total agricultural devastation</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Trevas</div>\n          <div class="plague-ref">Êx 10.21–29 · Ataca Rá (deus-sol)</div>',
    '<div class="plague-name">Darkness</div>\n          <div class="plague-ref">Exod 10:21–29 · Targets Ra (sun god)</div>',
    1
)
out = out.replace(
    '<div class="plague-name">Morte dos Primogênitos</div>\n          <div class="plague-ref">Êx 11–12 · Ataca o próprio Faraó-deus</div>',
    '<div class="plague-name">Death of the Firstborn</div>\n          <div class="plague-ref">Exod 11–12 · Targets Pharaoh himself — son of Ra</div>',
    1
)

# ═══ script block replacement ═══
out = out.replace(
    "<script>\n  const _lang = localStorage.getItem('lang') || 'pt';\n\n  function applyLang(l) {\n    document.querySelectorAll('[data-pt]').forEach(el => {\n      el.innerHTML = l === 'en' ? el.dataset.en : el.dataset.pt;\n    });\n    document.getElementById('langLabel').textContent = l === 'en' ? 'PT' : 'EN';\n    document.documentElement.lang = l === 'en' ? 'en' : 'pt-BR';\n  }\n  function toggleLang() {\n    const next = localStorage.getItem('lang') === 'en' ? 'pt' : 'en';\n    localStorage.setItem('lang', next);\n    applyLang(next);\n  }\n\n  function showSection(id) {\n    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));\n    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));\n\n    const sec = document.getElementById(id);\n    if (sec) {\n      sec.classList.add('active');\n      sec.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));\n    }\n\n    document.querySelectorAll('.nav-item[data-section]').forEach(b => {\n      if (b.dataset.section === id) b.classList.add('active');\n    });\n\n    // On mobile: close sidebar after selection\n    const sidebar = document.getElementById('sidebar');\n    const overlay = document.getElementById('sidebarOverlay');\n    const toggle  = document.getElementById('menuToggle');\n    if (sidebar.classList.contains('open')) {\n      sidebar.classList.remove('open');\n      overlay.classList.remove('open');\n      toggle.setAttribute('aria-expanded', 'false');\n    }\n\n    window.scrollTo({ top: 0, behavior: 'smooth' });\n  }\n\n  // Mobile hamburger\n  const menuToggle     = document.getElementById('menuToggle');\n  const sidebar        = document.getElementById('sidebar');\n  const sidebarOverlay = document.getElementById('sidebarOverlay');\n\n  menuToggle.addEventListener('click', () => {\n    const open = sidebar.classList.toggle('open');\n    sidebarOverlay.classList.toggle('open', open);\n    menuToggle.setAttribute('aria-expanded', open);\n  });\n  sidebarOverlay.addEventListener('click', () => {\n    sidebar.classList.remove('open');\n    sidebarOverlay.classList.remove('open');\n    menuToggle.setAttribute('aria-expanded', 'false');\n  });\n\n  // Scroll reveal\n  const revealEls = document.querySelectorAll('.reveal');\n  const revealObs = new IntersectionObserver(entries => {\n    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });\n  }, { threshold: 0.12 });\n  revealEls.forEach(el => revealObs.observe(el));\n\n  // Back to top\n  const btt = document.getElementById('btt');\n  window.addEventListener('scroll', () => {\n    btt.classList.toggle('visible', window.scrollY > 400);\n  });\n\n  // Trigger reveals for the initially active section\n  document.querySelectorAll('.section.active .reveal').forEach(el => {\n    el.classList.add('visible');\n  });\n\n  if (_lang === 'en') applyLang('en');\n  else document.getElementById('langLabel').textContent = 'EN';\n</script>",
    "<script>\n  localStorage.setItem('lang', 'en');\n\n  function goToPt() {\n    localStorage.setItem('lang', 'pt');\n    window.location.href = '/pt/at-pentateuco';\n  }\n\n  function showSection(id) {\n    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));\n    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));\n\n    const sec = document.getElementById(id);\n    if (sec) {\n      sec.classList.add('active');\n      sec.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));\n    }\n\n    document.querySelectorAll('.nav-item[data-section]').forEach(b => {\n      if (b.dataset.section === id) b.classList.add('active');\n    });\n\n    const sidebar = document.getElementById('sidebar');\n    const overlay = document.getElementById('sidebarOverlay');\n    const toggle  = document.getElementById('menuToggle');\n    if (sidebar.classList.contains('open')) {\n      sidebar.classList.remove('open');\n      overlay.classList.remove('open');\n      toggle.setAttribute('aria-expanded', 'false');\n    }\n\n    window.scrollTo({ top: 0, behavior: 'smooth' });\n  }\n\n  const menuToggle     = document.getElementById('menuToggle');\n  const sidebar        = document.getElementById('sidebar');\n  const sidebarOverlay = document.getElementById('sidebarOverlay');\n\n  menuToggle.addEventListener('click', () => {\n    const open = sidebar.classList.toggle('open');\n    sidebarOverlay.classList.toggle('open', open);\n    menuToggle.setAttribute('aria-expanded', open);\n  });\n  sidebarOverlay.addEventListener('click', () => {\n    sidebar.classList.remove('open');\n    sidebarOverlay.classList.remove('open');\n    menuToggle.setAttribute('aria-expanded', 'false');\n  });\n\n  const revealEls = document.querySelectorAll('.reveal');\n  const revealObs = new IntersectionObserver(entries => {\n    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });\n  }, { threshold: 0.12 });\n  revealEls.forEach(el => revealObs.observe(el));\n\n  const btt = document.getElementById('btt');\n  window.addEventListener('scroll', () => {\n    btt.classList.toggle('visible', window.scrollY > 400);\n  });\n\n  document.querySelectorAll('.section.active .reveal').forEach(el => {\n    el.classList.add('visible');\n  });\n</script>",
    1
)

# ═══ lang button replacement ═══
out = out.replace(
    '<button class="lang-btn" id="langBtn" onclick="toggleLang()" aria-label="Switch language">\n  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>\n  <span id="langLabel">EN</span>\n</button>',
    '<button class="lang-btn" id="langBtn" onclick="goToPt()" aria-label="Switch to Portuguese">\n  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>\n  <span id="langLabel">PT</span>\n</button>',
    1
)

# ═══ footer replacement ═══
out = out.replace(
    'Estudo Bíblico Panorâmico · Moisés · Pentateuco · © Material de Estudo',
    'Panoramic Bible Study · Moses · Pentateuch · © Study Material',
    1
)

# ═══ fixes round 2 ═══
out = out.replace(
    '"Pois naquela noite passarei pelo Egito e ferirei todo primogênito... O sangue, porém, será o sinal nas casas onde vocês estiverem; quando eu vir o sangue, passarei por cima de vocês."\n      <span class="scripture-ref">Êxodo 12.12–13 — NAA</span>',
    '"For I will pass through the land of Egypt that night, and I will strike all the firstborn... The blood shall be a sign for you, on the houses where you are. And when I see the blood, I will pass over you."\n      <span class="scripture-ref">Exodus 12:12–13 — ESV</span>',
    1
)
out = out.replace(
    'A travessia do Mar (Êx 14) é o evento fundacional da identidade de Israel como nação resgatada. O exército egípcio — o maior poder militar da época — é destruído nas águas. Êxodo 15, o Cântico de Moisés, é uma das composições poéticas mais antigas da Bíblia e o primeiro hino litúrgico registrado de Israel. O mesmo cântico ressoa na eternidade — Apocalipse 15.3 descreve os remidos cantando "o cântico de Moisés e o cântico do Cordeiro."',
    'The crossing of the Sea (Exod 14) is the foundational event of Israel\'s identity as a redeemed nation. The Egyptian army — the greatest military power of the age — is destroyed in the waters. Exodus 15, the Song of Moses, is one of the oldest poetic compositions in the Bible and the first recorded liturgical hymn of Israel. The same song echoes in eternity — Revelation 15:3 describes the redeemed singing "the song of Moses, the servant of God, and the song of the Lamb."',
    1
)
out = out.replace(
    'A Páscoa (<em>Pessah</em>, פֶּסַח — "pular sobre, passar por cima") é a instituição central do Êxodo. Um cordeiro sem defeito, macho, de um ano, sacrificado ao entardecer; seu sangue aspergido nas ombreiras e na verga da porta; sua carne assada e comida com ervas amargas e pães ázimos, em posição de partida. É o mais antigo dos sacramentos de Israel e o protótipo tipológico da Ceia do Senhor (1Co 5.7: "Cristo, nosso Cordeiro pascal, foi sacrificado").',
    'The Passover (<em>Pesach</em>, פֶּסַח — "to pass over") is the central institution of the Exodus. An unblemished male lamb, one year old, sacrificed at twilight; its blood sprinkled on the doorposts and lintel; its flesh roasted and eaten with bitter herbs and unleavened bread, in a posture of readiness. It is the oldest of Israel\'s sacraments and the typological prototype of the Lord\'s Supper (1 Cor 5:7: "Christ, our Passover lamb, has been sacrificed").',
    1
)
out = out.replace(
    '<h2>A Sarça Ardente — Êxodo 3.1–4.31</h2>',
    '<h2>The Burning Bush — Exodus 3:1–4:31</h2>',
    1
)
out = out.replace(
    'ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação',
    'he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment',
    1
)

# ═══ fixes round 3 ═══
out = out.replace(
    'Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
    "Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwest Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who bought Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses's father-in-law, was a <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>",
    1
)

# ═══ fixes round 4 ═══
out = out.replace(
    '    <h2>Midiã — Contexto Geopolítico</h2>\n    <p>Os midianitas eram descendentes de Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
    "    <h2>Midian — Geopolitical Context</h2>\n    <p>The Midianites were descendants of Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwestern Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who purchased Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses's father-in-law, was <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>",
    1
)

# ═══ fixes round 5 ═══
out = out.replace(
    '<h2>Midiã — Contexto Geopolítico</h2>\n    <p>Os midianitas eram descendentes de Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerendo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
    "<h2>Midian — Geopolitical Context</h2>\n    <p>The Midianites were descendants of Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwestern Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who purchased Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses's father-in-law, was <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>",
    1
)

# ═══ final write ═══
import os
os.makedirs('at-pentateuco', exist_ok=True)
with open('at-pentateuco/index.en.html', 'w', encoding='utf-8') as f:
    f.write(out)
print('Written at-pentateuco/index.en.html')
