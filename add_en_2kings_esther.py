#!/usr/bin/env python3
"""Adds EN data-lang blocks for 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther."""

with open('at-historicos/index.html', encoding='utf-8') as f:
    src = f.read()

def wrap(book_id, pt_eyebrow, en_eyebrow, pt_title, en_title,
         pt_meta, en_meta, pt_verse, en_verse,
         pt_ctx, en_ctx, pt_geo, en_geo, pt_study, en_study):
    """Replace the pure-PT sections of a book with bilingual data-lang wrappers."""

    # ── header ──
    old_hdr = f'''        <div class="book-eyebrow">{pt_eyebrow}</div>
        <h2 class="book-title"><span>{pt_title}</span></h2>
        <div class="book-meta">
{pt_meta}
        </div>
        <div class="book-verse">{pt_verse}</div>'''

    new_hdr = f'''        <div class="lang-content" data-lang="pt"><div class="book-eyebrow">{pt_eyebrow}</div></div>
        <div class="lang-content" data-lang="en" style="display:none"><div class="book-eyebrow">{en_eyebrow}</div></div>
        <div class="lang-content" data-lang="pt"><h2 class="book-title"><span>{pt_title}</span></h2></div>
        <div class="lang-content" data-lang="en" style="display:none"><h2 class="book-title"><span>{en_title}</span></h2></div>
        <div class="lang-content" data-lang="pt">
        <div class="book-meta">
{pt_meta}
        </div>
        </div>
        <div class="lang-content" data-lang="en" style="display:none">
        <div class="book-meta">
{en_meta}
        </div>
        </div>
        <div class="lang-content" data-lang="pt"><div class="book-verse">{pt_verse}</div></div>
        <div class="lang-content" data-lang="en" style="display:none"><div class="book-verse">{en_verse}</div></div>'''

    src2 = src.replace(old_hdr, new_hdr, 1)
    if src2 == src:
        print(f'WARNING: header not replaced for {book_id}')

    # ── ctx tab ──
    old_ctx = f'      <div class="tab-panel active" id="{book_id}-ctx">\n{pt_ctx}\n      </div>'
    new_ctx = (f'      <div class="tab-panel active" id="{book_id}-ctx">\n'
               f'        <div class="lang-content" data-lang="pt">\n{pt_ctx}\n        </div>\n'
               f'        <div class="lang-content" data-lang="en" style="display:none">\n{en_ctx}\n        </div>\n'
               f'      </div>')
    src3 = src2.replace(old_ctx, new_ctx, 1)
    if src3 == src2:
        print(f'WARNING: ctx not replaced for {book_id}')

    # ── geo tab ──
    old_geo = f'      <div class="tab-panel" id="{book_id}-geo">\n{pt_geo}\n      </div>'
    new_geo = (f'      <div class="tab-panel" id="{book_id}-geo">\n'
               f'        <div class="lang-content" data-lang="pt">\n{pt_geo}\n        </div>\n'
               f'        <div class="lang-content" data-lang="en" style="display:none">\n{en_geo}\n        </div>\n'
               f'      </div>')
    src4 = src3.replace(old_geo, new_geo, 1)
    if src4 == src3:
        print(f'WARNING: geo not replaced for {book_id}')

    # ── study tab ──
    old_study = f'      <div class="tab-panel" id="{book_id}-study">\n{pt_study}\n      </div>'
    new_study = (f'      <div class="tab-panel" id="{book_id}-study">\n'
                 f'        <div class="lang-content" data-lang="pt">\n{pt_study}\n        </div>\n'
                 f'        <div class="lang-content" data-lang="en" style="display:none">\n{en_study}\n        </div>\n'
                 f'      </div>')
    src5 = src4.replace(old_study, new_study, 1)
    if src5 == src4:
        print(f'WARNING: study not replaced for {book_id}')

    return src5

# ════════════════════════════ 2 KINGS ════════════════════════════════════════

src = wrap(
    book_id='reis2',
    pt_eyebrow='Livro 12 · Históricos · Antigo Testamento',
    en_eyebrow='Book 12 · Historical · Old Testament',
    pt_title='2 Reis',
    en_title='2 Kings',
    pt_meta='''\
          <span class="book-tag">~853–586 a.C.</span>
          <span class="book-tag">Exílio Assírio e Babilônico</span>
          <span class="book-tag">25 capítulos</span>
          <span class="book-tag">Autor: Jeremias (tradição)</span>''',
    en_meta='''\
          <span class="book-tag">~853–586 BC</span>
          <span class="book-tag">Assyrian and Babylonian Exile</span>
          <span class="book-tag">25 chapters</span>
          <span class="book-tag">Author: Jeremiah (tradition)</span>''',
    pt_verse='"Não tema, pois os que estão conosco são mais do que os que estão com eles."<cite>2 Reis 6.16 — NAA</cite>',
    en_verse='"Do not be afraid, for those who are with us are more than those who are with them."<cite>2 Kings 6:16 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">25 capítulos · ~853–586 a.C. · fim dos dois reinos</div></div>
            <div class="info-card"><div class="info-card-label">Queda do norte</div><div class="info-card-value">Israel cai para a Assíria em 722/721 a.C. · 10 tribos deportadas e substituídas → origem dos samaritanos</div></div>
            <div class="info-card"><div class="info-card-label">Queda do sul</div><div class="info-card-value">Judá cai para Babilônia · 3 deportações (605, 597, 586 a.C.) · Templo de Salomão destruído em 586 a.C.</div></div>
            <div class="info-card"><div class="info-card-label">Eliseu</div><div class="info-card-value">Milagres domésticos · cura de Naamã o sírio (cap. 5) · citado por Jesus em Lc 4.27 como exemplo da graça universal</div></div>
            <div class="info-card"><div class="info-card-label">Ezequias</div><div class="info-card-value">Cerco de Senaqueribe: 185.000 soldados aniquilados numa noite · confirmado no Prisma de Taylor (artefato assírio)</div></div>
            <div class="info-card"><div class="info-card-label">Josias</div><div class="info-card-value">Descobre o Livro da Lei (~621 a.C.) · reforma radical · mas texto nota: tarde demais para reverter o julgamento por Manassés</div></div>
          </div>
        </div>

        <div class="study-block">
          <div class="block-title">O Colapso dos Dois Reinos</div>
          <div class="block-body">
            <p>2 Reis documenta o declínio e fim dos dois reinos. O <strong>reino do norte (Israel)</strong> cai para a <strong>Assíria</strong> em 722/721 a.C. sob Sargão II. As dez tribos são deportadas e substituídas por povos estrangeiros — o início dos "samaritanos" como grupo étnico misto. O <strong>reino do sul (Judá)</strong> sobrevive mais 136 anos, mas cai para a <strong>Babilônia</strong> sob Nabucodonosor: três deportações (605, 597, 586 a.C.), culminando com a destruição do Templo de Salomão.</p>
            <p>O contexto é a ascensão dos grandes impérios mesopotâmicos: a Assíria domina do século IX ao final do VII; depois a coalizão medo-babilônica destrói Nínive em 612 a.C. e a Babilônia de Nabucodonosor herda o domínio regional.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">Book Overview</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Scope</div><div class="info-card-value">25 chapters · ~853–586 BC · end of both kingdoms</div></div>
            <div class="info-card"><div class="info-card-label">Fall of the north</div><div class="info-card-value">Israel falls to Assyria in 722/721 BC · 10 tribes deported and replaced → origin of the Samaritans</div></div>
            <div class="info-card"><div class="info-card-label">Fall of the south</div><div class="info-card-value">Judah falls to Babylon · 3 deportations (605, 597, 586 BC) · Solomon's Temple destroyed 586 BC</div></div>
            <div class="info-card"><div class="info-card-label">Elisha</div><div class="info-card-value">Domestic miracles · healing of Naaman the Syrian (ch. 5) · cited by Jesus in Luke 4:27 as example of universal grace</div></div>
            <div class="info-card"><div class="info-card-label">Hezekiah</div><div class="info-card-value">Sennacherib's siege: 185,000 soldiers destroyed in one night · confirmed in Taylor Prism (Assyrian artifact)</div></div>
            <div class="info-card"><div class="info-card-label">Josiah</div><div class="info-card-value">Finds the Book of the Law (~621 BC) · radical reform · but text notes: too late to reverse judgment decreed for Manasseh</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Collapse of Both Kingdoms</div>
          <div class="block-body">
            <p>2 Kings documents the decline and fall of both kingdoms. The <strong>northern kingdom (Israel)</strong> falls to <strong>Assyria</strong> in 722/721 BC under Sargon II. The ten tribes are deported and replaced by foreign peoples — the beginning of the "Samaritans" as a mixed ethnic group. The <strong>southern kingdom (Judah)</strong> survives another 136 years, but falls to <strong>Babylon</strong> under Nebuchadnezzar: three deportations (605, 597, 586 BC), culminating in the destruction of Solomon's Temple.</p>
            <p>The backdrop is the rise of the great Mesopotamian empires: Assyria dominates from the 9th century through the late 7th; then the Medo-Babylonian coalition destroys Nineveh in 612 BC and Nebuchadnezzar's Babylon inherits regional supremacy.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">Das Margens do Jordão à Babilônia</div>
          <div class="geo-box">
            <p>O arco geográfico de 2 Reis é imenso: da <strong>Samaria</strong> (destruída em 722 a.C.) à <strong>Nínive</strong> assíria (norte do Iraque atual) e à <strong>Babilônia</strong> (90 km ao sul de Bagdá). Jerusalém é sitiada três vezes. O Templo de Salomão, no Monte Moriá, é incendiado em 586 a.C. — evento que traumatiza o judaísmo para sempre e é lamentado em Lamentações.</p>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">From the Jordan River to Babylon</div>
          <div class="geo-box">
            <p>The geographical sweep of 2 Kings is vast: from <strong>Samaria</strong> (destroyed 722 BC) to <strong>Nineveh</strong> in Assyria (northern Iraq) and <strong>Babylon</strong> (90 km south of Baghdad). Jerusalem is besieged three times. Solomon's Temple on Mount Moriah is burned in 586 BC — an event that traumatizes Judaism permanently and is lamented in the book of Lamentations.</p>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">Eliseu — O Profeta dos Milagres</div>
          <div class="block-body">
            <p>Os primeiros capítulos de 2 Reis são dominados por <strong>Eliseu</strong>, sucessor de Elias. Enquanto Elias é figura solitária e de fogo, Eliseu opera em comunidade e seus milagres são notavelmente domésticos: purifica águas, multiplica azeite para uma viúva, ressuscita o filho da sunamita, cura a lepra de <strong>Naamã o sírio</strong>. A cura de Naamã (cap. 5) é especialmente significativa — um general estrangeiro e inimigo recebe a graça de Deus — e é citada por Jesus em Lucas 4.27 como exemplo do alcance universal da graça.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Ezequias e Josias — Os Reis da Reforma</div>
          <div class="block-body">
            <p><strong>Ezequias (caps. 18–20):</strong> O rei mais elogiado de Judá depois de Davi. Quando a Assíria de Senaqueribe cerca Jerusalém, Ezequias ora e o anjo do Senhor aniquila 185.000 soldados assírios numa noite. O Prisma de Taylor (texto assírio) confirma o cerco mas registra a retirada de forma evasiva — confirma historicidade sem explicar o milagre.</p>
            <p><strong>Josias (caps. 22–23):</strong> Descobre o Livro da Lei durante a reforma do Templo (~621 a.C.) e implementa a reforma mais radical da história de Judá, destruindo todos os altares pagãos de Dan a Berseba. Mas o texto registra com tristeza que tudo isso não bastou para reverter o julgamento já decretado por causa de Manassés.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">O Carro de Fogo de Elias — Elevação sem Morte</div>
          <div class="block-body">
            <p>A transição entre 1 e 2 Reis é marcada por um dos episódios mais extraordinários da Bíblia: a <strong>elevação de Elias</strong> (2Rs 2). Elias não morre — é arrebatado em um redemoinho, com um carro de fogo e cavalos de fogo separando-o de Eliseu. Eliseu rasga suas vestes (sinal de luto) e exclama: "Pai meu! Pai meu! Carros de Israel e sua cavalaria!" — reconhecendo que Elias era mais valioso para Israel do que todo o exército nacional.</p>
            <p>Eliseu pede uma "porção dobrada" do espírito de Elias — não o dobro de poder, mas a parte do primogênito (Dt 21.17): ele quer ser reconhecido como o herdeiro legítimo. A prova é o manto de Elias: ao golpear as águas, elas se abrem, como fizeram no Jordão para Moisés e Josué. O manto representa continuidade de autoridade profética. No NT, Elias retorna na Transfiguração (Mc 9) e é identificado com João Batista (Mt 17.12–13) — o precursor que prepara o caminho.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Israel e Judá — Duas Trajetórias Paralelas</div>
          <div class="block-body">
            <p>2 Reis alterna sistematicamente entre os reis dos dois reinos, criando uma narrativa paralela que pode confundir. O padrão editorial é consistente: cada rei é apresentado com (1) ano de início em relação ao rei paralelo, (2) duração do reinado, (3) capital, (4) julgamento moral ("fez o que era mau/bom aos olhos do Senhor"), (5) fonte de referência ("Anais dos Reis de Israel/Judá"), e (6) morte e sucessão.</p>
            <p>O resultado é assimétrico: <strong>Israel (norte)</strong> tem 19 reis em ~210 anos — nenhum recebe elogio; todos "andaram nos pecados de Jeroboão". <strong>Judá (sul)</strong> tem 20 reis em ~345 anos — oito recebem algum elogio, dois (Ezequias e Josias) recebem elogios extraordinários. A diferença é estrutural: Israel nunca teve o Templo em Jerusalém, nunca teve continuidade dinástica (9 golpes de estado), nunca teve um profeta que acompanhasse a dinastia regularmente como Elias/Eliseu. A avaliação do texto é que Israel nasceu sob o pecado institucional de Jeroboão e nunca se recuperou.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Não tema, pois os que estão conosco são mais do que os que estão com eles."</p>
          <cite>2 Reis 6.16 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">Elisha — The Prophet of Miracles</div>
          <div class="block-body">
            <p>The opening chapters of 2 Kings are dominated by <strong>Elisha</strong>, Elijah's successor. Where Elijah is a solitary, fiery figure, Elisha operates in community and his miracles are notably domestic: he purifies water, multiplies oil for a widow, raises the Shunammite's son, and heals the leprosy of <strong>Naaman the Syrian</strong>. Naaman's healing (ch. 5) is especially significant — a foreign enemy general receives God's grace — and is cited by Jesus in Luke 4:27 as an example of grace's universal reach.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Hezekiah and Josiah — Kings of Reform</div>
          <div class="block-body">
            <p><strong>Hezekiah (chs. 18–20):</strong> The most praised king of Judah after David. When Sennacherib's Assyria besieges Jerusalem, Hezekiah prays and the angel of the LORD strikes down 185,000 Assyrian soldiers in one night. The Taylor Prism (an Assyrian text) confirms the siege but records the withdrawal evasively — confirming historicity without explaining the miracle.</p>
            <p><strong>Josiah (chs. 22–23):</strong> Finds the Book of the Law during Temple repairs (~621 BC) and implements the most radical reform in Judah's history, destroying every pagan altar from Dan to Beersheba. But the text records with sorrow that even this was not enough to reverse the judgment already decreed because of Manasseh.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Elijah's Chariot of Fire — Translation without Death</div>
          <div class="block-body">
            <p>The transition from 1 Kings to 2 Kings is marked by one of the Bible's most extraordinary episodes: <strong>Elijah's translation</strong> (2 Kgs 2). Elijah does not die — he is taken up in a whirlwind, with a chariot of fire and horses of fire separating him from Elisha. Elisha tears his clothes (a sign of mourning) and cries out: "My father, my father! The chariots of Israel and its horsemen!" — recognizing that Elijah was worth more to Israel than its entire army.</p>
            <p>Elisha asks for a "double portion" of Elijah's spirit — not twice the power, but the firstborn's share (Deut 21:17): he wants to be recognized as the rightful heir. The proof is Elijah's cloak: when he strikes the waters, they part, as they did at the Jordan for Moses and Joshua. In the NT, Elijah appears at the Transfiguration (Mark 9) and is identified with John the Baptist (Matt 17:12–13) — the forerunner who prepares the way.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Israel and Judah — Two Parallel Trajectories</div>
          <div class="block-body">
            <p>2 Kings systematically alternates between the kings of both kingdoms in a parallel narrative. The editorial pattern is consistent: each king is introduced with (1) accession year relative to the parallel king, (2) length of reign, (3) capital, (4) moral verdict ("did what was evil/good in the sight of the LORD"), (5) source reference ("Annals of the Kings of Israel/Judah"), and (6) death and succession.</p>
            <p>The result is asymmetric: <strong>Israel (north)</strong> has 19 kings over ~210 years — none receives praise; all "walked in the sin of Jeroboam." <strong>Judah (south)</strong> has 20 kings over ~345 years — eight receive some praise, two (Hezekiah and Josiah) extraordinary praise. The difference is structural: Israel never had the Temple in Jerusalem, never had dynastic continuity (9 coups), and never had a prophet who regularly accompanied the dynasty as Elijah/Elisha did Ahab's line. The text's verdict is that Israel was born under Jeroboam's institutional sin and never recovered.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Do not be afraid, for those who are with us are more than those who are with them."</p>
          <cite>2 Kings 6:16 — ESV</cite>
        </div>'''
)

# ════════════════════════════ 1 CHRONICLES ═══════════════════════════════════

src = wrap(
    book_id='cronicas1',
    pt_eyebrow='Livro 13 · Históricos · Antigo Testamento',
    en_eyebrow='Book 13 · Historical · Old Testament',
    pt_title='1 Crônicas',
    en_title='1 Chronicles',
    pt_meta='''\
          <span class="book-tag">~450–400 a.C. (composição)</span>
          <span class="book-tag">Releitura Pós-Exílica</span>
          <span class="book-tag">29 capítulos</span>
          <span class="book-tag">Autor: O Cronista (Esdras?)</span>''',
    en_meta='''\
          <span class="book-tag">~450–400 BC (composition)</span>
          <span class="book-tag">Post-Exilic Rereading</span>
          <span class="book-tag">29 chapters</span>
          <span class="book-tag">Author: The Chronicler (Ezra?)</span>''',
    pt_verse='"Teus, <span style="font-variant:small-caps">Senhor</span>, são a grandeza, o poder, a glória, a vitória e a majestade; pois teus são todos os seres que estão nos céus e na terra."<cite>1 Crônicas 29.11 — NAA</cite>',
    en_verse='"Yours, O <span style="font-variant:small-caps">Lord</span>, is the greatness and the power and the glory and the victory and the majesty, for all that is in the heavens and in the earth is yours."<cite>1 Chronicles 29:11 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">29 capítulos · composição ~450–400 a.C. · perspectiva pós-exílica</div></div>
            <div class="info-card"><div class="info-card-label">Autor</div><div class="info-card-value">O Cronista — provavelmente o mesmo redator de Esdras e Neemias</div></div>
            <div class="info-card"><div class="info-card-label">Genealogias</div><div class="info-card-value">Caps. 1–9: de Adão aos retornados do exílio · situam Israel desde a criação no plano divino</div></div>
            <div class="info-card"><div class="info-card-label">Davi no Cronista</div><div class="info-card-value">Pecados omitidos · apresentado quase exclusivamente como organizador do culto e planejador do Templo</div></div>
            <div class="info-card"><div class="info-card-label">Jabez</div><div class="info-card-value">1Cr 4.9–10 — oração audaciosa no meio de lista de nomes esquecidos: "se me abençoasses e alargasses o meu território"</div></div>
            <div class="info-card"><div class="info-card-label">Satanás</div><div class="info-card-value">1Cr 21.1 vs 2Sm 24.1 — mesmo evento: Cronista nomeia o agente intermediário, refletindo desenvolvimento teológico pós-exílico</div></div>
          </div>
        </div>

        <div class="study-block">
          <div class="block-title">A Teologia do Recomeço</div>
          <div class="block-body">
            <p>1 e 2 Crônicas foram compostos após o retorno do exílio babilônico (~450–400 a.C.), provavelmente pelo mesmo autor de Esdras e Neemias — o chamado "Cronista". O contexto é o da <strong>comunidade pós-exílica</strong> tentando reconstruir a identidade nacional em torno do Templo, do sacerdócio e da aliança davídica, sem um rei no trono.</p>
            <p>O Cronista relê a mesma história de Samuel e Reis, mas com ênfases radicalmente diferentes: omite a maioria dos pecados de Davi (o episódio de Bate-Seba não aparece), omite todo o reino do norte (Israel), e foca quase obsessivamente no Templo, na música litúrgica e no sacerdócio. É história teológica para uma geração que precisa de esperança e identidade.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">Book Overview</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Scope</div><div class="info-card-value">29 chapters · composed ~450–400 BC · post-exilic perspective</div></div>
            <div class="info-card"><div class="info-card-label">Author</div><div class="info-card-value">The Chronicler — likely the same editor as Ezra and Nehemiah</div></div>
            <div class="info-card"><div class="info-card-label">Genealogies</div><div class="info-card-value">Chs. 1–9: from Adam to the exiles who returned · situate Israel within God's plan from creation</div></div>
            <div class="info-card"><div class="info-card-label">David in Chronicles</div><div class="info-card-value">Sins omitted · presented almost exclusively as organizer of worship and planner of the Temple</div></div>
            <div class="info-card"><div class="info-card-label">Jabez</div><div class="info-card-value">1 Chr 4:9–10 — bold prayer amid a list of forgotten names: "Oh that you would bless me and enlarge my border"</div></div>
            <div class="info-card"><div class="info-card-label">Satan</div><div class="info-card-value">1 Chr 21:1 vs 2 Sam 24:1 — same event: Chronicler names the intermediary agent, reflecting post-exilic theological development</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Theology of New Beginnings</div>
          <div class="block-body">
            <p>1 and 2 Chronicles were composed after the return from Babylonian exile (~450–400 BC), probably by the same author as Ezra and Nehemiah — known as "the Chronicler." The context is the <strong>post-exilic community</strong> attempting to rebuild national identity around the Temple, the priesthood, and the Davidic covenant, with no king on the throne.</p>
            <p>The Chronicler retells the same history as Samuel and Kings, but with radically different emphases: he omits most of David's sins (the Bathsheba episode does not appear), omits the entire northern kingdom of Israel, and focuses almost obsessively on the Temple, liturgical music, and the priesthood. It is theological history for a generation that desperately needs hope and identity.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">De Adão a Davi</div>
          <div class="geo-box">
            <p>Os primeiros 9 capítulos de 1 Crônicas são genealogias — de Adão até os retornados do exílio. O projeto genealógico do Cronista situa Israel no tempo e no espaço: desde a criação, passando pelos patriarcas e as tribos, até o retorno. <strong>Jerusalém</strong> é o centro geográfico e teológico absoluto de toda a narrativa — a cidade onde Deus habita e para onde todo o culto converge.</p>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">From Adam to David</div>
          <div class="geo-box">
            <p>The first nine chapters of 1 Chronicles consist of genealogies — from Adam to those who returned from exile. The Chronicler's genealogical project situates Israel in time and space: from creation, through the patriarchs and the tribes, to the return. <strong>Jerusalem</strong> is the absolute geographical and theological center of the entire narrative — the city where God dwells and toward which all worship converges.</p>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">Davi — O Rei do Culto</div>
          <div class="block-body">
            <p>Em 1 Crônicas, Davi é apresentado quase exclusivamente como organizador do culto e planejador do Templo. Ele organiza os sacerdotes em 24 turnos (cap. 24), os levitas em funções (cap. 23), os músicos (cap. 25 — incluindo os "profetas musicais": filhos de Asafe, Hemã e Jedutum), os porteiros e tesoureiros (cap. 26).</p>
            <p>Davi não pode construir o Templo porque "derramou muito sangue" (22.8), mas prepara tudo — materiais, planos, recursos humanos — e entrega a Salomão. O Cronista vê Davi como o verdadeiro arquiteto espiritual do Templo, mesmo que Salomão seja o construtor físico.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">As Genealogias como Teologia</div>
          <div class="block-body">
            <p>Os primeiros nove capítulos de 1 Crônicas são genealogias — de Adão até os retornados do exílio. Para o leitor moderno, são o trecho mais árido da Bíblia; para o leitor pós-exílico, eram literalmente o mais vital. Após décadas na Babilônia, a questão prática era: <em>quem somos?</em> Quem é sacerdote legítimo? Quem tem direito a que território? Quem pode servir no Templo?</p>
            <p>Mas o Cronista vai além do registro civil. As genealogias começam em <strong>Adão</strong> (1.1) — não em Abraão. Israel não é apenas um povo entre outros: é a continuação do projeto divino desde a criação. A lista passa por Sem, Abraão, Isaque, Jacó — e então explode nas doze tribos, com Judá e Levi recebendo tratamento especial por razões messiânicas e sacerdotais. Nomes estranhos e obscuros salpicam a lista — como a oração de <strong>Jabez</strong> (4.9-10), brevíssima mas intensa: "Oh! Se me abençoasses e alargasses o meu território!" — um modelo de oração audaciosa no meio de uma lista de nomes esquecidos.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">O Censo de Davi — A Diferença entre os Dois Relatos</div>
          <div class="block-body">
            <p>O censo de Davi em 1 Crônicas 21 é o mesmo episódio de 2 Samuel 24 — mas com uma diferença chocante: enquanto em Samuel "o furor do Senhor se acendeu contra Israel e instigou Davi" (2Sm 24.1), em Crônicas "Satanás se levantou contra Israel e instigou Davi" (1Cr 21.1). Esta variação não é contradição — é teologia complementar. Deus é soberano sobre tudo, incluindo Satanás; em Samuel a soberania divina abrange tudo, em Crônicas o agente intermediário é explicitado.</p>
            <p>A diferença reflete o desenvolvimento teológico do período pós-exílico, quando a angelologia e a figura do Adversário (<em>satan</em> = acusador/adversário) foram articuladas de forma mais explícita — influência que alguns estudiosos associam ao contato com a teologia persa zoroastriana, embora o conceito já esteja em embrião em Jó 1–2. O Cronista usa o termo para proteger a imagem de um Deus que "tenta" ao mal — distinção que o NT tornará doutrina explícita (Tg 1.13: "Deus não é tentado pelo mal e a ninguém tenta").</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Teus, <span style="font-variant:small-caps">Senhor</span>, são a grandeza, o poder, a glória, a vitória e a majestade; pois teus são todos os seres que estão nos céus e na terra."</p>
          <cite>1 Crônicas 29.11 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">David — The King of Worship</div>
          <div class="block-body">
            <p>In 1 Chronicles, David is presented almost exclusively as the organizer of worship and planner of the Temple. He arranges the priests into 24 divisions (ch. 24), assigns the Levites their duties (ch. 23), organizes the musicians (ch. 25 — including the "musical prophets": sons of Asaph, Heman, and Jeduthun), and appoints gatekeepers and treasurers (ch. 26).</p>
            <p>David cannot build the Temple because he "shed much blood" (22:8), but he prepares everything — materials, blueprints, personnel — and hands it all to Solomon. The Chronicler views David as the true spiritual architect of the Temple, even though Solomon is its physical builder.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Genealogies as Theology</div>
          <div class="block-body">
            <p>The first nine chapters of 1 Chronicles are genealogies — from Adam to those who returned from exile. For the modern reader they are the Bible's driest stretch; for the post-exilic reader they were literally the most urgent. After decades in Babylon, the pressing questions were: <em>Who are we?</em> Who is a legitimate priest? Who has a claim to which territory? Who may serve in the Temple?</p>
            <p>But the Chronicler goes beyond a civic register. The genealogies begin with <strong>Adam</strong> (1:1) — not Abraham. Israel is not merely one nation among others: it is the continuation of God's project from creation. The list runs through Shem, Abraham, Isaac, Jacob — then fans out into the twelve tribes, with Judah and Levi receiving special treatment for messianic and priestly reasons. Obscure names dot the list — like the prayer of <strong>Jabez</strong> (4:9-10), brief but intense: "Oh that you would bless me and enlarge my border!" — a model of bold prayer nestled amid a list of forgotten names.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">David's Census — The Difference Between the Two Accounts</div>
          <div class="block-body">
            <p>David's census in 1 Chronicles 21 is the same episode as 2 Samuel 24 — but with a striking difference: in Samuel "the anger of the LORD was kindled against Israel, and he incited David" (2 Sam 24:1), while in Chronicles "Satan stood against Israel and incited David" (1 Chr 21:1). This variation is not a contradiction — it is complementary theology. God is sovereign over all, including Satan; Samuel emphasizes divine sovereignty encompassing everything, while Chronicles names the intermediary agent.</p>
            <p>The difference reflects the theological development of the post-exilic period, when angelology and the figure of the Adversary (<em>satan</em> = accuser/adversary) were articulated more explicitly. The Chronicler uses the term to protect the image of a God who does not tempt anyone to evil — a distinction the NT makes explicit doctrine (Jas 1:13: "God cannot be tempted with evil, and he himself tempts no one").</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Yours, O <span style="font-variant:small-caps">Lord</span>, is the greatness and the power and the glory and the victory and the majesty, for all that is in the heavens and in the earth is yours."</p>
          <cite>1 Chronicles 29:11 — ESV</cite>
        </div>'''
)

# ════════════════════════════ 2 CHRONICLES ═══════════════════════════════════

src = wrap(
    book_id='cronicas2',
    pt_eyebrow='Livro 14 · Históricos · Antigo Testamento',
    en_eyebrow='Book 14 · Historical · Old Testament',
    pt_title='2 Crônicas',
    en_title='2 Chronicles',
    pt_meta='''\
          <span class="book-tag">~970–586 a.C. (eventos)</span>
          <span class="book-tag">Salomão ao Exílio</span>
          <span class="book-tag">36 capítulos</span>
          <span class="book-tag">Autor: O Cronista</span>''',
    en_meta='''\
          <span class="book-tag">~970–586 BC (events)</span>
          <span class="book-tag">Solomon to the Exile</span>
          <span class="book-tag">36 chapters</span>
          <span class="book-tag">Author: The Chronicler</span>''',
    pt_verse='"Se o meu povo, que se chama pelo meu nome, se humilhar, orar, buscar a minha face e se converter dos seus maus caminhos, então eu ouvirei do céu, perdoarei os seus pecados e restaurarei a sua terra."<cite>2 Crônicas 7.14 — NAA</cite>',
    en_verse='"If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land."<cite>2 Chronicles 7:14 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">36 capítulos · de Salomão ao exílio · foco exclusivo em Judá (norte ignorado)</div></div>
            <div class="info-card"><div class="info-card-label">Versículo central</div><div class="info-card-value">2Cr 7.14 — condições da restauração: humilhar, orar, buscar, converter-se · promessa tripla de Deus</div></div>
            <div class="info-card"><div class="info-card-label">Grandes reformadores</div><div class="info-card-value">Asa, Josafá, Ezequias, Josias — ciclos de reforma e apostasia analisados com tese teológica explícita</div></div>
            <div class="info-card"><div class="info-card-label">Manassés</div><div class="info-card-value">Cap. 33 — conversão em exílio babilônico: ausente em 2 Reis, presente aqui · argumento pós-exílico de esperança para Israel</div></div>
            <div class="info-card"><div class="info-card-label">Edito de Ciro</div><div class="info-card-value">Versículo final (36.22–23) quase idêntico ao início de Esdras — obra originalmente unificada</div></div>
            <div class="info-card"><div class="info-card-label">Tese do exílio</div><div class="info-card-value">36.15–16: "zombaram dos mensageiros de Deus, desprezaram as suas palavras, escarneceram dos seus profetas"</div></div>
          </div>
        </div>

        <div class="study-block">
          <div class="block-title">O Padrão da Reforma e do Esquecimento</div>
          <div class="block-body">
            <p>2 Crônicas cobre de Salomão ao exílio — com foco nos ciclos de reforma e apostasia em Judá. Os grandes reformadores são <strong>Asa, Josafá, Ezequias e Josias</strong>. O Cronista interpreta cada crise como resultado direto de fidelidade ou infidelidade: quando o rei busca a Deus, há vitória; quando abandona, há derrota. Esta tese teológica é mais explícita do que em Reis — o Cronista escreve para uma comunidade que precisa entender por que o exílio aconteceu.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">Book Overview</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Scope</div><div class="info-card-value">36 chapters · from Solomon to the exile · exclusive focus on Judah (north ignored)</div></div>
            <div class="info-card"><div class="info-card-label">Central verse</div><div class="info-card-value">2 Chr 7:14 — conditions of restoration: humble, pray, seek, turn · God's threefold promise</div></div>
            <div class="info-card"><div class="info-card-label">Great reformers</div><div class="info-card-value">Asa, Jehoshaphat, Hezekiah, Josiah — cycles of reform and apostasy analyzed with explicit theological thesis</div></div>
            <div class="info-card"><div class="info-card-label">Manasseh</div><div class="info-card-value">Ch. 33 — conversion in Babylonian exile: absent in 2 Kings, present here · post-exilic argument of hope for Israel</div></div>
            <div class="info-card"><div class="info-card-label">Edict of Cyrus</div><div class="info-card-value">Final verse (36:22–23) nearly identical to the opening of Ezra — originally a unified work</div></div>
            <div class="info-card"><div class="info-card-label">Thesis of the exile</div><div class="info-card-value">36:15–16: "they kept mocking the messengers of God, despising his words and scoffing at his prophets"</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Cycle of Reform and Forgetting</div>
          <div class="block-body">
            <p>2 Chronicles covers Solomon through the exile — focusing on Judah's cycles of reform and apostasy. The great reformers are <strong>Asa, Jehoshaphat, Hezekiah, and Josiah</strong>. The Chronicler interprets each crisis as a direct result of faithfulness or unfaithfulness: when the king seeks God, there is victory; when he abandons God, there is defeat. This theological thesis is more explicit than in Kings — the Chronicler writes for a community that needs to understand why the exile happened.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">Judá Sozinha no Mapa</div>
          <div class="geo-box">
            <p>2 Crônicas foca exclusivamente em <strong>Judá</strong> — o reino do sul. O norte simplesmente não existe para o Cronista após a divisão. O território de Judá, de Berseba ao norte de Jerusalém, é o palco de toda a narrativa. Cidades importantes: <strong>Laquis</strong> (fortaleza sul — sitiada por Senaqueribe), <strong>Hebrom</strong> e o deserto da Judeia onde reis fugiam.</p>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">Judah Alone on the Map</div>
          <div class="geo-box">
            <p>2 Chronicles focuses exclusively on <strong>Judah</strong> — the southern kingdom. The north simply does not exist for the Chronicler after the division. Judah's territory, from Beersheba to north of Jerusalem, is the stage for the entire narrative. Key cities: <strong>Lachish</strong> (southern fortress — besieged by Sennacherib), <strong>Hebron</strong>, and the Judean wilderness where kings fled.</p>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">2 Cr 7.14 — A Promessa da Restauração</div>
          <div class="block-body">
            <p>A resposta divina a Salomão após a dedicação do Templo tornou-se um dos versículos mais invocados em contextos de avivamento e oração nacional. O texto estabelece quatro condições: <strong>humilhar-se, orar, buscar a face de Deus e converter-se dos maus caminhos</strong>. A promessa é tripla: Deus ouvirá do céu, perdoará o pecado e sará a terra. O versículo foi escrito para Israel — mas o Cronista o apresenta como princípio universal que transcende épocas.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Manassés — A Conversão Mais Surpreendente</div>
          <div class="block-body">
            <p>2 Crônicas registra um episódio ausente em 2 Reis: a <strong>conversão de Manassés</strong> (cap. 33). Em Reis, Manassés é o pior rei de Judá — culpado pelo exílio. Mas Crônicas adiciona: levado cativo para a Babilônia pelos assírios, Manassés se humilhou diante de Deus em angústia, foi ouvido e restaurado ao trono. Esta adição é teologicamente explosiva: até o pior pecador pode ser restaurado pela humilhação genuína. O Cronista a preserva porque sua audiência pós-exílica precisa ouvir que o perdão é possível para Israel.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Josafá e Asa — Reforma Incompleta e Aliança Perigosa</div>
          <div class="block-body">
            <p><strong>Asa</strong> (caps. 14–16) é um dos reis mais promissores de Judá: derrota um exército etíope de um milhão de homens confiando no Senhor (14.11), reforma o culto e remove a rainha-mãe Maacá por causa de um ídolo pornográfico. Mas no final alia-se com a Síria contra Israel pagando com o ouro do Templo — e quando o profeta Hanani o repreende, Asa o aprisionou e oprimiu parte do povo. O Cronista registra: nos anos seguintes, quando Asa adoeceu gravemente dos pés, "não buscou ao Senhor, mas aos médicos" (16.12). A frase não condena a medicina — condena a exclusividade: Asa buscou os médicos em vez de Deus, não junto com Deus.</p>
            <p><strong>Josafá</strong> (caps. 17–20), filho de Asa, ensina a Lei em todo Judá (17.7-9 — proto-sistema de educação religiosa), mas alia-se perigosamente com Acabe do norte (cap. 18) — aliança que o profeta Jeú condena: "Dás ajuda ao ímpio e amas os que odeiam ao Senhor?" (19.2). O ponto alto é a batalha de 2Cr 20: cercado por moabitas, amonitas e outros, Josafá ora, e Deus diz "a batalha não é vossa, mas de Deus" (20.15). Os adoradores vão à frente do exército cantando — e os inimigos se destroem mutuamente.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">O Exílio como Consequência — A Tese Teológica do Cronista</div>
          <div class="block-body">
            <p>O versículo final de 2 Crônicas (36.22-23) — o Edito de Ciro — é quase idêntico ao versículo inicial de Esdras. Os dois livros foram originalmente um só. O Cronista encerra sua obra não com o incêndio do Templo, mas com o decreto de restauração — porque sua teologia é de esperança, não de julgamento final.</p>
            <p>Mas o Cronista é claro sobre por que o exílio aconteceu: "O Senhor, Deus de seus pais, enviou continuamente mensageiros a eles, porque tinha misericórdia de seu povo e de sua habitação. Mas eles zombavam dos mensageiros de Deus, desprezavam as suas palavras e escarneçam dos seus profetas" (36.15-16). Três verbos — zombar, desprezar, escarnecer — resumem séculos de rejeição profética. O exílio não foi acidente histórico: foi consequência direta e específica de uma padrão repetido de rejeição da Palavra. A audiência pós-exílica do Cronista precisa entender isso para não repetir o ciclo.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Se o meu povo, que se chama pelo meu nome, se humilhar, orar, buscar a minha face e se converter dos seus maus caminhos, então eu ouvirei do céu, perdoarei os seus pecados e restaurarei a sua terra."</p>
          <cite>2 Crônicas 7.14 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">2 Chronicles 7:14 — The Promise of Restoration</div>
          <div class="block-body">
            <p>God's answer to Solomon after the Temple dedication has become one of the most invoked verses in revival and national prayer contexts. The text establishes four conditions: <strong>humble themselves, pray, seek God's face, and turn from their wicked ways</strong>. The promise is threefold: God will hear from heaven, forgive their sin, and heal their land. The verse was written for Israel — but the Chronicler presents it as a universal principle transcending every era.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Manasseh — The Most Surprising Conversion</div>
          <div class="block-body">
            <p>2 Chronicles records an episode absent from 2 Kings: the <strong>conversion of Manasseh</strong> (ch. 33). In Kings, Manasseh is Judah's worst king — held responsible for the exile. But Chronicles adds: taken captive to Babylon by the Assyrians, Manasseh humbled himself before God in distress, was heard, and was restored to his throne. This addition is theologically explosive: even the worst sinner can be restored through genuine humility. The Chronicler preserves it because his post-exilic audience needs to hear that forgiveness is possible for Israel.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Jehoshaphat and Asa — Incomplete Reform and Dangerous Alliance</div>
          <div class="block-body">
            <p><strong>Asa</strong> (chs. 14–16) is one of Judah's most promising kings: he defeats a million-man Ethiopian army by trusting the LORD (14:11), reforms worship, and removes his grandmother Maacah from her position because of an obscene idol. But he ultimately allies with Syria against Israel, paying with Temple gold — and when the prophet Hanani rebukes him, Asa imprisons him and oppresses part of the people. The Chronicler records that in later years, when Asa suffered a severe foot disease, "he did not seek the LORD, but sought help from physicians" (16:12). The phrase does not condemn medicine — it condemns exclusivity: Asa sought physicians instead of God, not alongside God.</p>
            <p><strong>Jehoshaphat</strong> (chs. 17–20), Asa's son, teaches the Law throughout Judah (17:7-9 — a proto-religious education system), but dangerously allies with Ahab of the north (ch. 18) — an alliance the prophet Jehu condemns: "Should you help the wicked and love those who hate the LORD?" (19:2). The climax is the battle of 2 Chr 20: surrounded by Moabites, Ammonites, and others, Jehoshaphat prays, and God says "the battle is not yours but God's" (20:15). The worshipers lead the army singing — and the enemies destroy one another.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Exile as Consequence — The Chronicler's Theological Thesis</div>
          <div class="block-body">
            <p>The final verse of 2 Chronicles (36:22-23) — the Edict of Cyrus — is nearly identical to the opening verse of Ezra. The two books were originally one. The Chronicler closes his work not with the burning of the Temple, but with the decree of restoration — because his theology is one of hope, not final judgment.</p>
            <p>But the Chronicler is clear about why the exile happened: "The LORD, the God of their fathers, sent persistently to them by his messengers, because he had compassion on his people and on his dwelling place. But they kept mocking the messengers of God, despising his words and scoffing at his prophets" (36:15-16). Three verbs — mock, despise, scoff — summarize centuries of prophetic rejection. The exile was not a historical accident: it was the direct and specific consequence of a repeated pattern of rejecting the Word. The Chronicler's post-exilic audience must understand this in order not to repeat the cycle.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land."</p>
          <cite>2 Chronicles 7:14 — ESV</cite>
        </div>'''
)

# ════════════════════════════ EZRA ═══════════════════════════════════════════

src = wrap(
    book_id='esdras',
    pt_eyebrow='Livro 15 · Históricos · Antigo Testamento',
    en_eyebrow='Book 15 · Historical · Old Testament',
    pt_title='Esdras',
    en_title='Ezra',
    pt_meta='''\
          <span class="book-tag">~538–458 a.C.</span>
          <span class="book-tag">Retorno do Exílio</span>
          <span class="book-tag">10 capítulos</span>
          <span class="book-tag">Autor: Esdras</span>''',
    en_meta='''\
          <span class="book-tag">~538–458 BC</span>
          <span class="book-tag">Return from Exile</span>
          <span class="book-tag">10 chapters</span>
          <span class="book-tag">Author: Ezra</span>''',
    pt_verse='"Pois Esdras havia dedicado o seu coração a estudar a lei do <span style="font-variant:small-caps">Senhor</span>, a praticá-la e a ensinar os seus preceitos e ordenanças em Israel."<cite>Esdras 7.10 — NAA</cite>',
    en_verse='"For Ezra had set his heart to study the Law of the <span style="font-variant:small-caps">Lord</span>, and to do it and to teach his statutes and rules in Israel."<cite>Ezra 7:10 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">10 capítulos · ~538–458 a.C. · dois retornos do exílio</div></div>
            <div class="info-card"><div class="info-card-label">Edito de Ciro</div><div class="info-card-value">539 a.C. — Cilindro de Ciro (British Museum) confirma a política persa de tolerância religiosa</div></div>
            <div class="info-card"><div class="info-card-label">Segundo Templo</div><div class="info-card-value">Concluído em 516 a.C. — 70 anos após destruição do primeiro (Jeremias 25.11), mobilizado por Ageu e Zacarias</div></div>
            <div class="info-card"><div class="info-card-label">Esdras</div><div class="info-card-value">Sacerdote e escriba · chamado "segundo Moisés" pela tradição · chega em 458 a.C. com mandato de Artaxerxes I</div></div>
            <div class="info-card"><div class="info-card-label">Documentos aramaicos</div><div class="info-card-value">Esd 4.8–6.18 e 7.12–26 em aramaico — cartas oficiais persas preservadas no idioma original · autenticidade arqueológica</div></div>
            <div class="info-card"><div class="info-card-label">Crise final</div><div class="info-card-value">Caps. 9–10: casamentos mistos com "povos da terra" · solução drástica de dissolução — lida como sobrevivência espiritual da comunidade frágil</div></div>
          </div>
        </div>

        <div class="study-block">
          <div class="block-title">O Edito de Ciro e o Novo Êxodo</div>
          <div class="block-body">
            <p>Em 539 a.C., Ciro II da Pérsia conquista a Babilônia. No ano seguinte (538 a.C.), emite o famoso <strong>Edito de Ciro</strong> permitindo que os povos deportados retornassem a suas terras e reconstruíssem seus templos — política de tolerância radicalmente diferente da assíria. O <strong>Cilindro de Ciro</strong> (encontrado em 1879, no British Museum) confirma historicamente essa política. Para Israel, é percebido como milagre: Isaías havia profetizado Ciro pelo nome 150 anos antes (Is 44.28–45.1).</p>
            <p>O <strong>Império Persa</strong> (~550–330 a.C.) governa através de sátrapas e permite autonomia religiosa e cultural local — o que torna possível a reconstrução judaica. A <em>Pax Persica</em> é o ambiente em que o judaísmo pós-exílico se consolida.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">Book Overview</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Scope</div><div class="info-card-value">10 chapters · ~538–458 BC · two returns from exile</div></div>
            <div class="info-card"><div class="info-card-label">Edict of Cyrus</div><div class="info-card-value">539 BC — Cyrus Cylinder (British Museum) confirms the Persian policy of religious tolerance</div></div>
            <div class="info-card"><div class="info-card-label">Second Temple</div><div class="info-card-value">Completed 516 BC — 70 years after the first was destroyed (Jeremiah 25:11), spurred by Haggai and Zechariah</div></div>
            <div class="info-card"><div class="info-card-label">Ezra</div><div class="info-card-value">Priest and scribe · called "second Moses" by tradition · arrives 458 BC with a commission from Artaxerxes I</div></div>
            <div class="info-card"><div class="info-card-label">Aramaic documents</div><div class="info-card-value">Ezra 4:8–6:18 and 7:12–26 in Aramaic — official Persian letters preserved in the original language · archaeological authenticity</div></div>
            <div class="info-card"><div class="info-card-label">Final crisis</div><div class="info-card-value">Chs. 9–10: intermarriage with "peoples of the land" · drastic dissolution — read as spiritual survival of a fragile community</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Edict of Cyrus and the New Exodus</div>
          <div class="block-body">
            <p>In 539 BC, Cyrus II of Persia conquers Babylon. The following year (538 BC), he issues the famous <strong>Edict of Cyrus</strong> permitting deported peoples to return to their lands and rebuild their temples — a policy of tolerance radically different from Assyria's. The <strong>Cyrus Cylinder</strong> (discovered in 1879, now in the British Museum) historically confirms this policy. For Israel it is perceived as a miracle: Isaiah had prophesied Cyrus by name 150 years earlier (Isa 44:28–45:1).</p>
            <p>The <strong>Persian Empire</strong> (~550–330 BC) governs through satraps and allows local religious and cultural autonomy — which makes the Jewish restoration possible. The <em>Pax Persica</em> is the environment in which post-exilic Judaism consolidates itself.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">Babilônia a Jerusalém — 1.600 km</div>
          <div class="geo-box">
            <p>A jornada dos exilados da <strong>Babilônia</strong> (sul do Iraque) a <strong>Jerusalém</strong> era de ~1.600 km pelas rotas comerciais — uma caminhada de 3 a 4 meses. Esdras relata dois retornos: o primeiro sob <strong>Zorobabel</strong> (~538 a.C., ~50.000 pessoas) e o segundo sob o próprio <strong>Esdras</strong> (~458 a.C., ~1.700 homens além de mulheres e crianças). Jerusalém em ruínas — muros destruídos, Templo incendiado — era espetáculo desolador para quem retornava.</p>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">Babylon to Jerusalem — 1,600 km</div>
          <div class="geo-box">
            <p>The journey of the exiles from <strong>Babylon</strong> (southern Iraq) to <strong>Jerusalem</strong> was approximately 1,600 km along trade routes — a walk of three to four months. Ezra records two returns: the first under <strong>Zerubbabel</strong> (~538 BC, ~50,000 people) and the second under <strong>Ezra</strong> himself (~458 BC, ~1,700 men plus women and children). Jerusalem in ruins — walls demolished, Temple burned — was a desolate sight for those returning.</p>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">A Reconstrução do Templo</div>
          <div class="block-body">
            <p>A reconstrução do Templo (caps. 1–6) enfrenta resistência dos <strong>povos da terra</strong> — os samaritanos e outros grupos que habitavam Canaã durante o exílio. Eles primeiro se oferecem para ajudar (4.1–2) e são recusados; depois sabotam a obra por anos enviando cartas acusatórias aos reis persas. A reconstrução para por 16 anos (536–520 a.C.) — até que os profetas <strong>Ageu e Zacarias</strong> mobilizam o povo e Dario I confirma o Edito de Ciro. O segundo Templo é concluído em 516 a.C. — 70 anos após a destruição do primeiro, cumprindo a profecia de Jeremias.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Esdras — O Pai do Judaísmo Rabínico</div>
          <div class="block-body">
            <p>Esdras, sacerdote e escriba (<em>sofer</em>) perito na Lei de Moisés, chega a Jerusalém em 458 a.C. com mandato do rei Artaxerxes I para ensinar a Lei e administrar a comunidade. A tradição judaica o chama de "segundo Moisés" e o credita com a canonização do Pentateuco, a introdução do alfabeto hebraico quadrado (substituindo o paleo-hebraico), e a fundação da Grande Sinagoga — o proto-corpo rabínico. Sua oração de confissão (cap. 9) é um dos textos mais tocantes de intercessão do AT: ele intercede pelos pecados do povo como se fossem seus próprios.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Os Casamentos Mistos — Crise de Identidade e Separação</div>
          <div class="block-body">
            <p>O episódio mais perturbador de Esdras é o capítulo final (caps. 9–10): Esdras descobre que sacerdotes, levitas e líderes haviam casado com mulheres das "nações da terra" (9.2). Sua reação é de prostração: rasga as vestes, arranca os cabelos da barba e fica sentado em choque até o sacrifício da tarde. Sua oração de confissão (cap. 9) intercede pelos pecados do povo como se fossem seus próprios — usando "nós" e "nossos" embora ele pessoalmente não estivesse envolvido.</p>
            <p>A solução adotada é drástica: dissolver os casamentos e enviar as mulheres estrangeiras com seus filhos. Para a sensibilidade moderna, é profundamente perturbador — mulheres e crianças pagando o preço de decisões dos homens. O texto não comenta a questão moral da perspectiva das mulheres. A preocupação de Esdras é teológica: a mistura de cultos — não de raças — havia destruído Israel antes (como Salomão demonstrou). O contexto é extremo: a comunidade pós-exílica é minúscula, frágil, ainda sem muros, rodeada de culturas que a absorveriam. A ação brutal de Esdras é, na sua própria lógica, ato de sobrevivência espiritual de uma comunidade à beira do desaparecimento.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Os Documentos Aramaicos — Janela Histórica Única</div>
          <div class="block-body">
            <p>Esdras 4.8–6.18 e 7.12-26 estão escritos em <strong>aramaico</strong> — não em hebraico. O aramaico era a língua diplomática do Império Persa, equivalente ao latim medieval ou ao inglês atual nas relações internacionais. O Cronista preservou documentos oficiais no idioma original sem tradução — uma decisão editorial que demonstra intenção de autenticidade histórica.</p>
            <p>Esses documentos incluem cartas ao rei Artaxerxes acusando os judeus de rebeldia (4.11-16), a resposta real ordenando que a obra pare (4.17-22), a carta de Tatenai ao rei Dario questionando a autorização (5.6-17), a resposta de Dario confirmando o Edito de Ciro e ordenando que deixem os judeus construir (6.1-12). Arqueólogos encontraram documentos persas do mesmo período que confirmam o estilo e o vocabulário das cartas — o que convenceu muitos céticos do século XIX da autenticidade dos textos de Esdras.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Pois Esdras havia dedicado o seu coração a estudar a lei do <span style="font-variant:small-caps">Senhor</span>, a praticá-la e a ensinar os seus preceitos e ordenanças em Israel."</p>
          <cite>Esdras 7.10 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">Rebuilding the Temple</div>
          <div class="block-body">
            <p>The reconstruction of the Temple (chs. 1–6) faces opposition from the <strong>peoples of the land</strong> — the Samaritans and other groups that had inhabited Canaan during the exile. They first offer to help (4:1–2) and are refused; then they sabotage the work for years by sending accusatory letters to Persian kings. Construction halts for 16 years (536–520 BC) — until the prophets <strong>Haggai and Zechariah</strong> mobilize the people and Darius I confirms the Edict of Cyrus. The Second Temple is completed in 516 BC — 70 years after the first was destroyed, fulfilling Jeremiah's prophecy.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Ezra — Father of Rabbinic Judaism</div>
          <div class="block-body">
            <p>Ezra, a priest and scribe (<em>sofer</em>) skilled in the Law of Moses, arrives in Jerusalem in 458 BC with a commission from King Artaxerxes I to teach the Law and govern the community. Jewish tradition calls him "the second Moses" and credits him with canonizing the Pentateuch, introducing the square Hebrew script (replacing the paleo-Hebrew script), and founding the Great Assembly — the proto-rabbinic body. His prayer of confession (ch. 9) is one of the OT's most moving intercessory texts: he intercedes for the people's sins as if they were his own.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Mixed Marriages — Identity Crisis and Separation</div>
          <div class="block-body">
            <p>The most disturbing episode in Ezra is the final section (chs. 9–10): Ezra discovers that priests, Levites, and leaders had married women from "the peoples of the land" (9:2). His reaction is prostration: he tears his garments, pulls hair from his beard, and sits in shock until the evening sacrifice. His prayer of confession (ch. 9) intercedes for the people's sins as if they were his own — using "we" and "our" though he personally was not involved.</p>
            <p>The adopted solution is drastic: dissolve the marriages and send the foreign women away with their children. To modern sensibility this is deeply disturbing — women and children paying the price for decisions made by men. The text does not comment on the moral question from the women's perspective. Ezra's concern is theological: the mixing of worship systems — not of races — had destroyed Israel before (as Solomon demonstrated). The context is extreme: the post-exilic community is tiny, fragile, still without walls, surrounded by cultures that would absorb it. Ezra's brutal action is, by its own logic, an act of spiritual survival for a community on the verge of disappearing.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Aramaic Documents — A Unique Historical Window</div>
          <div class="block-body">
            <p>Ezra 4:8–6:18 and 7:12–26 are written in <strong>Aramaic</strong> — not Hebrew. Aramaic was the diplomatic language of the Persian Empire, equivalent to medieval Latin or modern English in international relations. The Chronicler preserved official documents in the original language without translation — an editorial decision that demonstrates an intention of historical authenticity.</p>
            <p>These documents include letters to King Artaxerxes accusing the Jews of rebellion (4:11-16), the royal reply ordering the work to stop (4:17-22), Tattenai's letter to King Darius questioning the authorization (5:6-17), and Darius's reply confirming the Edict of Cyrus and ordering that the Jews be allowed to build (6:1-12). Archaeologists have found Persian documents from the same period that confirm the style and vocabulary of these letters — which convinced many 19th-century skeptics of the authenticity of the Ezra texts.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"For Ezra had set his heart to study the Law of the <span style="font-variant:small-caps">Lord</span>, and to do it and to teach his statutes and rules in Israel."</p>
          <cite>Ezra 7:10 — ESV</cite>
        </div>'''
)

# ════════════════════════════ NEHEMIAH ═══════════════════════════════════════

src = wrap(
    book_id='neemias',
    pt_eyebrow='Livro 16 · Históricos · Antigo Testamento',
    en_eyebrow='Book 16 · Historical · Old Testament',
    pt_title='Neemias',
    en_title='Nehemiah',
    pt_meta='''\
          <span class="book-tag">~445–430 a.C.</span>
          <span class="book-tag">Reconstrução dos Muros</span>
          <span class="book-tag">13 capítulos</span>
          <span class="book-tag">Autor: Neemias / Redator</span>''',
    en_meta='''\
          <span class="book-tag">~445–430 BC</span>
          <span class="book-tag">Rebuilding the Walls</span>
          <span class="book-tag">13 chapters</span>
          <span class="book-tag">Author: Nehemiah / Editor</span>''',
    pt_verse='"O Deus do céu nos concederá sucesso; nós, seus servos, nos levantaremos e construiremos."<cite>Neemias 2.20 — NAA</cite>',
    en_verse='"The God of heaven will make us prosper, and we his servants will arise and build."<cite>Nehemiah 2:20 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">O Copeiro do Rei</div>
          <div class="block-body">
            <p>Neemias é copeiro do rei Artaxerxes I em <strong>Susa</strong> — cargo de extrema confiança (o copeiro provava o vinho do rei para detectar veneno). Quando recebe notícia das condições de Jerusalém — muros destruídos, povo em desgraça — ele chora, jejua e ora por dias. Sua oração (cap. 1) combina adoração, confissão histórica citando Deuteronômio e petição específica. Depois pede ao rei permissão para reconstruir — com ousadia e preparação: já tem em mente o que precisa pedir (madeira, cartas de passagem). O rei concede.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">The King's Cupbearer</div>
          <div class="block-body">
            <p>Nehemiah is the cupbearer of King Artaxerxes I in <strong>Susa</strong> — a position of extreme trust (the cupbearer tasted the king's wine to detect poison). When he receives news about Jerusalem's condition — walls demolished, people in disgrace — he weeps, fasts, and prays for days. His prayer (ch. 1) combines adoration, historical confession citing Deuteronomy, and specific petition. He then boldly asks the king for permission to rebuild — with preparation: he already knows exactly what he needs to request (timber, letters of safe passage). The king grants it.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">Os Muros de Jerusalém</div>
          <div class="geo-box">
            <p>Neemias inspeciona os muros de Jerusalém à noite (2.12-16) — para não revelar seus planos antes de estar pronto. O livro inclui a descrição detalhada de quais grupos reconstruíram quais seções (cap. 3): a <strong>Porta do Peixe, Porta Velha, Porta do Vale, Porta do Esterco, Porta da Fonte, Porta das Águas, Porta dos Cavalos, Porta do Leste, Porta da Guarda</strong> — uma topografia de Jerusalém do século V a.C. de valor arqueológico imenso.</p>
          </div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Duração da obra</div><div class="info-card-value">52 dias (Neemias 6.15) — recorde de gestão</div></div>
            <div class="info-card"><div class="info-card-label">Principal oposição</div><div class="info-card-value">Sambalate (Samaria) e Tobias (Amom)</div></div>
            <div class="info-card"><div class="info-card-label">Ponto mais vulnerável</div><div class="info-card-value">Porta do Esterco — setor mais danificado</div></div>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">The Walls of Jerusalem</div>
          <div class="geo-box">
            <p>Nehemiah inspects Jerusalem's walls by night (2:12-16) — so as not to reveal his plans before he is ready. The book includes a detailed description of which groups rebuilt which sections (ch. 3): the <strong>Fish Gate, Old Gate, Valley Gate, Dung Gate, Fountain Gate, Water Gate, Horse Gate, East Gate, Guard Gate</strong> — a 5th-century BC topography of Jerusalem of immense archaeological value.</p>
          </div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Duration of work</div><div class="info-card-value">52 days (Nehemiah 6:15) — a management record</div></div>
            <div class="info-card"><div class="info-card-label">Main opposition</div><div class="info-card-value">Sanballat (Samaria) and Tobiah (Ammon)</div></div>
            <div class="info-card"><div class="info-card-label">Most vulnerable section</div><div class="info-card-value">Dung Gate — most heavily damaged sector</div></div>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">52 Dias — Liderança Sob Pressão</div>
          <div class="block-body">
            <p>A reconstrução dos muros em apenas <strong>52 dias</strong> (6.15) é um dos feitos de gestão mais notáveis do AT. Neemias enfrenta três tipos de oposição: <strong>ridicularização</strong> ("uma raposa subiria e derrubaria o muro" — 4.3), <strong>ameaça de ataque armado</strong> (os trabalhadores constroem com uma mão e seguram armas com a outra — 4.17), e <strong>pressão interna</strong> (usura entre os judeus — cap. 5). A cada ameaça, Neemias responde com oração imediata e ação prática — nunca só oração, nunca só ação.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">A Alegria do Senhor como Força</div>
          <div class="block-body">
            <p>O capítulo 8 é o clímax espiritual: Esdras lê a Lei de Moisés em praça pública por horas, os levitas explicam o sentido ao povo (proto-homilética), o povo chora ao ouvir as palavras. A resposta é surpreendente: "Não pranteeis nem choreis... A alegria do Senhor é a vossa força" (8.9–10). O luto é transformado em celebração. A Festa dos Tabernáculos é celebrada pela primeira vez desde os dias de Josué (8.17) — 1.000 anos depois.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">A Reforma Social — Neemias e a Justiça Econômica</div>
          <div class="block-body">
            <p>No capítulo 5, em meio à crise da construção, Neemias descobre que judeus ricos estão <strong>cobrando juros de irmãos judeus</strong> que venderam campos e filhos como escravos para sobreviver. É a desigualdade interna enquanto o muro ainda não está concluído. Neemias convoca uma grande assembleia — e a resolução é imediata e radical: os credores restituirão tudo — campos, casas, dinheiro, juros — imediatamente.</p>
            <p>Para dar o exemplo, Neemias revela que nunca exigiu o salário de governador ao qual tinha direito — alimentando sua própria casa e 150 funcionários do próprio bolso. Sua pergunta retórica é poderosa: "O que vocês estão fazendo não é bom. Não devemos andar no temor do nosso Deus?" (5.9). A liderança moral precede a exigência moral. O texto é um dos mais explícitos do AT sobre a incompatibilidade entre devoção religiosa e exploração econômica dentro da comunidade de fé.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">O Pacto Renovado — Cap. 10 e a Reforma Comunitária</div>
          <div class="block-body">
            <p>Após a leitura pública da Lei (cap. 8) e a grande oração de confissão histórica (cap. 9 — uma das mais longas da Bíblia, percorrendo toda a história de Israel do Êxodo ao exílio), o povo firma um pacto escrito (cap. 10) com comprometimentos específicos e práticos: <strong>não casarão com os povos da terra; guardarão o sábado; observarão o ano sabático para as dívidas; contribuirão para a manutenção do Templo; trarão os primogênitos, as primícias, os dízimos.</strong></p>
            <p>O pacto de Neemias 10 é notável por sua especificidade: não é vaga promessa de "seguir a Deus", mas compromissos jurídicos detalhados. O NT chama isso de "obrigação" (<em>anáthema</em> — comprometer-se formalmente). O Cronista registra os nomes dos signatários — sacerdotes, levitas, líderes, povo. A renovação da aliança é ato público, comunitário, registrado, verificável. A fé bíblica sempre produziu comunidade estruturada, não apenas experiência interior.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"O Deus do céu nos concederá sucesso; nós, seus servos, nos levantaremos e construiremos."</p>
          <cite>Neemias 2.20 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">52 Days — Leadership Under Pressure</div>
          <div class="block-body">
            <p>Rebuilding the walls in just <strong>52 days</strong> (6:15) is one of the OT's most remarkable feats of leadership. Nehemiah faces three types of opposition: <strong>ridicule</strong> ("even a fox going up on it would break down their stone wall" — 4:3), <strong>threat of armed attack</strong> (workers build with one hand and hold a weapon with the other — 4:17), and <strong>internal pressure</strong> (usury among the Jews — ch. 5). To each threat Nehemiah responds with immediate prayer and practical action — never prayer alone, never action alone.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Joy of the LORD Is Your Strength</div>
          <div class="block-body">
            <p>Chapter 8 is the spiritual climax: Ezra reads the Law of Moses in the public square for hours, the Levites explain the meaning to the people (proto-homiletics), and the people weep as they hear the words. The response is surprising: "Do not mourn or weep... the joy of the LORD is your strength" (8:9–10). Mourning is transformed into celebration. The Feast of Tabernacles is celebrated for the first time since the days of Joshua (8:17) — a thousand years later.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Social Reform — Nehemiah and Economic Justice</div>
          <div class="block-body">
            <p>In chapter 5, in the midst of the construction crisis, Nehemiah discovers that wealthy Jews are <strong>charging interest from fellow Jews</strong> who had sold their fields and even their children into servitude to survive. This is internal inequality while the wall is still unfinished. Nehemiah convenes a great assembly — and the resolution is immediate and radical: the creditors will restore everything — fields, houses, money, interest — at once.</p>
            <p>To set the example, Nehemiah reveals that he never claimed the governor's salary to which he was entitled — feeding his household and 150 officials from his own resources. His rhetorical question is powerful: "The thing that you are doing is not good. Ought you not to walk in the fear of our God?" (5:9). Moral leadership precedes moral demands. The text is one of the OT's most explicit statements on the incompatibility of religious devotion with economic exploitation within the community of faith.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Renewed Covenant — Ch. 10 and Community Reform</div>
          <div class="block-body">
            <p>After the public reading of the Law (ch. 8) and the great historical prayer of confession (ch. 9 — one of the Bible's longest, tracing Israel's entire history from the Exodus to the exile), the people enter a written covenant (ch. 10) with specific, practical commitments: <strong>they will not intermarry with the peoples of the land; they will keep the Sabbath; they will observe the sabbatical year for debts; they will contribute to Temple maintenance; they will bring firstfruits, firstborn, and tithes.</strong></p>
            <p>Nehemiah 10's covenant is remarkable for its specificity: it is not a vague promise to "follow God" but detailed legal commitments. The renewal of the covenant is a public, communal, recorded, verifiable act. Biblical faith has always produced structured community, not merely interior experience.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"The God of heaven will make us prosper, and we his servants will arise and build."</p>
          <cite>Nehemiah 2:20 — ESV</cite>
        </div>'''
)

# ════════════════════════════ ESTHER ═════════════════════════════════════════

src = wrap(
    book_id='ester',
    pt_eyebrow='Livro 17 · Históricos · Antigo Testamento',
    en_eyebrow='Book 17 · Historical · Old Testament',
    pt_title='Ester',
    en_title='Esther',
    pt_meta='''\
          <span class="book-tag">~483–473 a.C.</span>
          <span class="book-tag">Diáspora Persa</span>
          <span class="book-tag">10 capítulos</span>
          <span class="book-tag">Autor: Mardoqueu (tradição)</span>''',
    en_meta='''\
          <span class="book-tag">~483–473 BC</span>
          <span class="book-tag">Persian Diaspora</span>
          <span class="book-tag">10 chapters</span>
          <span class="book-tag">Author: Mordecai (tradition)</span>''',
    pt_verse='"Quem sabe se você não chegou à posição de rainha precisamente para um momento como este?"<cite>Ester 4.14 — NAA</cite>',
    en_verse='"And who knows whether you have not come to the kingdom for such a time as this?"<cite>Esther 4:14 — ESV</cite>',
    pt_ctx='''\
        <div class="study-block">
          <div class="block-title">O Palácio de Susa e a Ameaça do Genocídio</div>
          <div class="block-body">
            <p>Ester se passa na corte persa de <strong>Xerxes I</strong> (Assuero — ~486–465 a.C.) em Susa. É o único livro bíblico que se passa inteiramente fora da terra de Israel e que não menciona o nome de Deus em nenhum momento — na versão hebraica masorética. Apesar da ausência do nome divino, a providência permeia cada detalhe da narrativa.</p>
            <p>O contexto é a diáspora: judeus que não retornaram com Zorobabel permaneceram no Império Persa. Hamã, o agagita — provável descendente de Agague, rei dos amalecitas que Saul não matou (1Sm 15) — planeja um genocídio de todos os judeus do império como represália ao desrespeito de Mardoqueu. O Palácio de Susa (Shush, Irã atual) foi escavado por arqueólogos franceses no século XIX — confirmando muitos detalhes arquitetônicos do livro.</p>
          </div>
        </div>''',
    en_ctx='''\
        <div class="study-block">
          <div class="block-title">The Palace of Susa and the Threat of Genocide</div>
          <div class="block-body">
            <p>Esther is set in the Persian court of <strong>Xerxes I</strong> (Ahasuerus — ~486–465 BC) at Susa. It is the only biblical book set entirely outside the land of Israel and the only one that never mentions the name of God — in the Hebrew Masoretic text. Despite the divine name's absence, providence permeates every detail of the narrative.</p>
            <p>The context is the diaspora: Jews who had not returned with Zerubbabel remained in the Persian Empire. Haman the Agagite — likely a descendant of Agag, king of the Amalekites whom Saul failed to kill (1 Sam 15) — plans the genocide of all the Jews of the empire in retaliation for Mordecai's refusal to bow. The Palace of Susa (Shush, modern Iran) was excavated by French archaeologists in the 19th century — confirming many architectural details of the book.</p>
          </div>
        </div>''',
    pt_geo='''\
        <div class="study-block">
          <div class="block-title">Susa — Capital do Poder Persa</div>
          <div class="geo-box">
            <p><strong>Susa</strong> (Shush, sudoeste do Irã atual) era uma das quatro capitais do Império Persa aqueménida, usada como residência de inverno. O palácio de Xerxes — identificado arqueologicamente — tinha a <em>apadana</em> (salão das audiências) com 72 colunas de 20 metros, pátios de mármore e jardins irrigados. O "pátio interior" onde Ester aguarda a convocação (4.11; 5.1) é arqueologicamente identificável.</p>
          </div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Susa</div><div class="info-card-value">Atual Shush, sudoeste do Irã · capital persa de inverno</div></div>
            <div class="info-card"><div class="info-card-label">Extensão do Império</div><div class="info-card-value">Da Índia à Etiópia · 127 províncias (Est 1.1)</div></div>
            <div class="info-card"><div class="info-card-label">Distância a Jerusalém</div><div class="info-card-value">~2.200 km · outro mundo para os judeus da diáspora</div></div>
          </div>
        </div>''',
    en_geo='''\
        <div class="study-block">
          <div class="block-title">Susa — Capital of Persian Power</div>
          <div class="geo-box">
            <p><strong>Susa</strong> (Shush, southwestern Iran) was one of the four capitals of the Achaemenid Persian Empire, used as a winter residence. Xerxes' palace — archaeologically identified — featured the <em>apadana</em> (audience hall) with 72 columns 20 meters tall, marble courtyards, and irrigated gardens. The "inner court" where Esther waits to be summoned (4:11; 5:1) is archaeologically identifiable.</p>
          </div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Susa</div><div class="info-card-value">Modern Shush, southwestern Iran · Persian winter capital</div></div>
            <div class="info-card"><div class="info-card-label">Empire's extent</div><div class="info-card-value">From India to Ethiopia · 127 provinces (Esth 1:1)</div></div>
            <div class="info-card"><div class="info-card-label">Distance to Jerusalem</div><div class="info-card-value">~2,200 km · another world for diaspora Jews</div></div>
          </div>
        </div>''',
    pt_study='''\
        <div class="study-block">
          <div class="block-title">A Providência Oculta</div>
          <div class="block-body">
            <p>A ausência do nome de Deus em Ester é tão significativa quanto sua presença em outros livros. O texto convida o leitor a ver a providência divina através de coincidências impossíveis: Ester torna-se rainha <em>exatamente</em> quando a ameaça surge. Mardoqueu descobre a conspiração contra Xerxes <em>exatamente</em> no tempo certo. O rei tem insônia na noite crucial e manda ler os anais, que <em>exatamente</em> registram o serviço de Mardoqueu ainda não recompensado. Hamã chega ao palácio <em>exatamente</em> quando o rei decide honrar Mardoqueu. A providência age através do natural, não do milagroso.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Para um Momento Como Este</div>
          <div class="block-body">
            <p>A frase de Mardoqueu (4.14) é um dos versículos mais teologicamente densos do AT sem mencionar Deus: "Se te calares neste tempo, de algum outro lugar virá alívio e livramento para os judeus, mas tu e a casa de teu pai perecereis. E quem sabe se para um momento como este chegaste a ser rainha?" A premissa é clara: Deus agirá de qualquer forma — a questão é se Ester participará do plano.</p>
            <p>A resposta de Ester — "se perecer, perecerei" (4.16) — é ato de coragem absoluta: entrar sem convocação ante o rei era punível de morte. A <strong>festa do Purim</strong> (14–15 de Adar) celebra esses eventos até hoje — a festa mais alegre do calendário judaico, onde Ester é lido em voz alta com gritos e chocalhos toda vez que o nome de Hamã é mencionado.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Hamã como Tipo do Anticristo — A Teologia da Perseguição</div>
          <div class="block-body">
            <p>Hamã o agagita (3.1) carrega um sobrenome que o leitor atento reconhece imediatamente: é descendente de <strong>Agague, rei dos amalecitas</strong> — o rei que Saul deveria ter destruído e não o fez (1Sm 15). A perseguição de Hamã contra os judeus é, na lógica narrativa da Bíblia, o reaparecimento de uma hostilidade que atravessa gerações. Mardoqueu, benjaminita (como Saul), desta vez não recua.</p>
            <p>Hamã é apresentado como figura que concentra poder absoluto e usa-o para destruição total: obtém do rei o anel de selar (3.10 — símbolo de autoridade delegada ilimitada), lança o pur (sorte — daí "Purim") para determinar o dia do genocídio, paga 10.000 talentos de prata pela autorização (3.9). Seu orgulho é tão frágil que um único homem que não se prostra (Mardoqueu) o precipita ao genocídio de uma nação inteira. A queda de Hamã é enfaticamente irónica: o poste que mandou construir para enforcar Mardoqueu (5.14) torna-se o instrumento de sua própria execução (7.10). A Bíblia chama isso de retribuição poética — Deus "faz cair o ímpio em suas próprias redes" (Sl 141.10).</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">A Estrutura Quiástica — Arte Literária de Ester</div>
          <div class="block-body">
            <p>Ester é uma das obras literariamente mais sofisticadas do AT. O livro tem estrutura de <strong>quiasma</strong> — espelho invertido onde os eventos se correspondem em ordem reversa. O centro do quiasma (caps. 6–7) é a noite de insônia de Xerxes e o honor de Mardoqueu — o ponto de virada onde o destino se inverte. Em torno desse centro, os festins correspondem-se: os dois banquetes iniciais (Xerxes e Vasti; a festa dos 180 dias) espelham os dois banquetes finais de Ester (caps. 5 e 7). Os éditos correspondem-se: o édito de extermínio (cap. 3) é espelhado pelo édito de defesa (cap. 8). As elevações: Hamã elevado (3.1) e depois executado; Mardoqueu humilhado (3.2-4) e depois exaltado (8.2).</p>
            <p>Esta estrutura não é coincidência — é composição intencional de um escritor de talento extraordinário. O livro pode ser lido como relato histórico e como obra literária ao mesmo tempo; ambas as leituras são ricas. O judaísmo reconheceu essa qualidade: Ester é o único livro bíblico para o qual os rabinos permitiram que fosse copiado por qualquer pessoa, não apenas por escribas — tal era seu valor pedagógico e literário.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">O Jejum de Ester — Arma Espiritual sem Nome Divino</div>
          <div class="block-body">
            <p>Quando Ester decide agir, sua primeira ação não é política mas espiritual: "Vai, reúne todos os judeus que se encontram em Susã, e jejuai por mim; não comais nem bebais por três dias, nem de noite nem de dia. Eu também jejuarei" (4.16). O jejum coletivo de três dias — sem que o nome de Deus seja mencionado — é a oração mais intensa que o livro registra. A ausência do nome divino é eloquente: quando não há palavras, o jejum fala.</p>
            <p>O detalhe do <strong>cetro estendido</strong> (5.2; 8.4) revela a tensão máxima da narrativa: a lei persa que punia de morte quem entrasse sem convocação ante o rei era real (verificada em documentos históricos persas). Ester não entra simplesmente como rainha — entra literalmente arriscando a vida. A coragem de Ester é tanto espiritual quanto física. A Igreja antiga viu em Ester intercedendo ante o rei um tipo de Cristo intercedendo ante o Pai — entrando onde não podia, para salvar quem não podia se salvar.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Quem sabe se você não chegou à posição de rainha precisamente para um momento como este?"</p>
          <cite>Ester 4.14 — NAA</cite>
        </div>''',
    en_study='''\
        <div class="study-block">
          <div class="block-title">Hidden Providence</div>
          <div class="block-body">
            <p>The absence of God's name in Esther is as significant as its presence in other books. The text invites the reader to see divine providence through impossible coincidences: Esther becomes queen <em>exactly</em> when the threat arises. Mordecai discovers the conspiracy against Xerxes <em>exactly</em> at the right moment. The king has insomnia on the crucial night and orders the royal chronicles to be read, which <em>exactly</em> record Mordecai's unrewarded service. Haman arrives at the palace <em>exactly</em> when the king has decided to honor Mordecai. Providence works through the natural, not the miraculous.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">For Such a Time as This</div>
          <div class="block-body">
            <p>Mordecai's words (4:14) are among the OT's most theologically dense without mentioning God: "For if you keep silent at this time, relief and deliverance will rise for the Jews from another place, but you and your father's house will perish. And who knows whether you have not come to the kingdom for such a time as this?" The premise is clear: God will act regardless — the question is whether Esther will participate in the plan.</p>
            <p>Esther's answer — "if I perish, I perish" (4:16) — is an act of absolute courage: appearing before the king unsummoned was punishable by death. The <strong>festival of Purim</strong> (14–15 Adar) celebrates these events to this day — the most joyful festival in the Jewish calendar, where Esther is read aloud with shouts and noisemakers every time Haman's name is mentioned.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Haman as Antichrist Type — The Theology of Persecution</div>
          <div class="block-body">
            <p>Haman the Agagite (3:1) bears a surname the attentive reader immediately recognizes: he is a descendant of <strong>Agag, king of the Amalekites</strong> — the king Saul was supposed to destroy and did not (1 Sam 15). Haman's persecution of the Jews is, in the Bible's narrative logic, the reappearance of a hostility that spans generations. Mordecai, a Benjaminite (like Saul), this time does not back down.</p>
            <p>Haman is presented as a figure who concentrates absolute power and uses it for total destruction: he obtains the king's signet ring (3:10 — symbol of unlimited delegated authority), casts the pur (lot — hence "Purim") to determine the day of genocide, and pays 10,000 talents of silver for authorization (3:9). His pride is so fragile that a single man who refuses to bow (Mordecai) precipitates him into the genocide of an entire nation. Haman's fall is emphatically ironic: the gallows he had built to hang Mordecai (5:14) becomes the instrument of his own execution (7:10). The Bible calls this poetic justice — God "lets the wicked fall into their own nets" (Ps 141:10).</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Chiastic Structure — Literary Art in Esther</div>
          <div class="block-body">
            <p>Esther is one of the OT's most literarily sophisticated works. The book has a <strong>chiastic</strong> structure — an inverted mirror in which events correspond in reverse order. The center of the chiasm (chs. 6–7) is Xerxes' sleepless night and the honoring of Mordecai — the turning point where destiny reverses. Around this center, the banquets correspond: the two opening feasts (Xerxes and Vashti; the 180-day celebration) mirror Esther's two final banquets (chs. 5 and 7). The edicts correspond: the edict of extermination (ch. 3) is mirrored by the edict of defense (ch. 8). The reversals: Haman exalted (3:1) then executed; Mordecai humiliated (3:2-4) then exalted (8:2).</p>
            <p>This structure is not coincidence — it is the intentional composition of a writer of extraordinary talent. The book can be read simultaneously as historical account and as literary art; both readings are rich.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Esther's Fast — Spiritual Weapon Without the Divine Name</div>
          <div class="block-body">
            <p>When Esther decides to act, her first action is not political but spiritual: "Go, gather all the Jews to be found in Susa, and hold a fast on my behalf, and do not eat or drink for three days, night or day. I and my young women will also fast as you do" (4:16). The three-day collective fast — without the name of God being mentioned — is the most intense prayer the book records. The absence of the divine name is eloquent: when there are no words, fasting speaks.</p>
            <p>The detail of the <strong>extended scepter</strong> (5:2; 8:4) reveals the narrative's maximum tension: the Persian law that punished with death anyone who entered the king's presence unsummoned was real (verified in Persian historical documents). Esther does not simply enter as queen — she literally enters risking her life. The ancient Church saw in Esther interceding before the king a type of Christ interceding before the Father — entering where she could not go, to save those who could not save themselves.</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"And who knows whether you have not come to the kingdom for such a time as this?"</p>
          <cite>Esther 4:14 — ESV</cite>
        </div>'''
)

with open('at-historicos/index.html', 'w', encoding='utf-8') as f:
    f.write(src)

lang_count = src.count('data-lang=')
print(f'Done. Total data-lang attributes: {lang_count}')
