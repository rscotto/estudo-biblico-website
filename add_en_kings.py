#!/usr/bin/env python3
"""
Wraps the untranslated books (1 Kings through Esther) in at-historicos/index.html
with data-lang="pt" / data-lang="en" blocks, identical to the Joshua-2Samuel pattern.
"""

with open('at-historicos/index.html', encoding='utf-8') as f:
    src = f.read()

# ── 1 KINGS ──────────────────────────────────────────────────────────────────

old_1kgs_header = '''        <div class="book-eyebrow">Livro 11 · Históricos · Antigo Testamento</div>
        <h2 class="book-title"><span>1 Reis</span></h2>
        <div class="book-meta">
          <span class="book-tag">~970–853 a.C.</span>
          <span class="book-tag">Salomão · Divisão do Reino</span>
          <span class="book-tag">22 capítulos</span>
          <span class="book-tag">Autor: Jeremias (tradição)</span>
        </div>
        <div class="book-verse">"Dá ao teu servo um coração que ouça, para que eu possa governar o teu povo e discernir entre o bem e o mal."<cite>1 Reis 3.9 — NAA</cite></div>'''

new_1kgs_header = '''        <div class="lang-content" data-lang="pt"><div class="book-eyebrow">Livro 11 · Históricos · Antigo Testamento</div></div>
        <div class="lang-content" data-lang="en" style="display:none"><div class="book-eyebrow">Book 11 · Historical · Old Testament</div></div>
        <div class="lang-content" data-lang="pt"><h2 class="book-title"><span>1 Reis</span></h2></div>
        <div class="lang-content" data-lang="en" style="display:none"><h2 class="book-title"><span>1 Kings</span></h2></div>
        <div class="lang-content" data-lang="pt">
        <div class="book-meta">
          <span class="book-tag">~970–853 a.C.</span>
          <span class="book-tag">Salomão · Divisão do Reino</span>
          <span class="book-tag">22 capítulos</span>
          <span class="book-tag">Autor: Jeremias (tradição)</span>
        </div>
        </div>
        <div class="lang-content" data-lang="en" style="display:none">
        <div class="book-meta">
          <span class="book-tag">~970–853 BC</span>
          <span class="book-tag">Solomon · Division of the Kingdom</span>
          <span class="book-tag">22 chapters</span>
          <span class="book-tag">Author: Jeremiah (tradition)</span>
        </div>
        </div>
        <div class="lang-content" data-lang="pt"><div class="book-verse">"Dá ao teu servo um coração que ouça, para que eu possa governar o teu povo e discernir entre o bem e o mal."<cite>1 Reis 3.9 — NAA</cite></div></div>
        <div class="lang-content" data-lang="en" style="display:none"><div class="book-verse">"Give your servant therefore an understanding mind to govern your people, that I may discern between good and evil."<cite>1 Kings 3:9 — ESV</cite></div></div>'''

src = src.replace(old_1kgs_header, new_1kgs_header, 1)

# 1 Kings ctx block
old_1kgs_ctx = '''      <div class="tab-panel active" id="reis1-ctx">
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">22 capítulos · ~970–853 a.C. · Salomão e a divisão do reino</div></div>
            <div class="info-card"><div class="info-card-label">Templo de Salomão</div><div class="info-card-value">Construído em 7 anos (~966–959 a.C.) · cedros do Líbano · ouro de Ofir · destruído em 586 a.C.</div></div>
            <div class="info-card"><div class="info-card-label">Divisão do reino</div><div class="info-card-value">930 a.C. — Judá (sul) e Israel (norte · 10 tribos) se separam permanentemente por causa da apostasia de Salomão</div></div>
            <div class="info-card"><div class="info-card-label">Elias Tisbita</div><div class="info-card-value">Surge sem genealogia (17.1) · duelo do Carmelo contra 450 profetas de Baal · "voz mansa e delicada" no Sinai (19.12)</div></div>
            <div class="info-card"><div class="info-card-label">Jezabel</div><div class="info-card-value">Financia 850 profetas pagãos, mata profetas do Senhor e manda assassinar Nabot para expropriar sua vinha</div></div>
            <div class="info-card"><div class="info-card-label">Critério editorial</div><div class="info-card-value">Cada rei avaliado pela fidelidade a Deus e centralização do culto em Jerusalém · nenhum rei do norte recebe elogio</div></div>
          </div>
        </div>

        <div class="study-block">
          <div class="block-title">Glória e Ruptura</div>
          <div class="block-body">
            <p>1 Reis narra a trajetória de Israel do apogeu ao colapso. O reinado de Salomão (~970–930 a.C.) é o pico da civilização israelita: paz, prosperidade, o Templo de Jerusalém, fama internacional. Mas o livro mostra como as sementes da destruição foram plantadas no próprio auge. A divisão do reino em 930 a.C. é a maior catástrofe política da história israelita — consequência direta da apostasia de Salomão.</p>
            <p>A segunda metade do livro alterna entre os reis de Israel (norte) e Judá (sul), avaliando cada rei pelo critério de fidelidade a Deus e à centralização do culto em Jerusalém. O norte nunca tem um rei "bom" por esse critério.</p>
          </div>
        </div>
      </div>'''

new_1kgs_ctx = '''      <div class="tab-panel active" id="reis1-ctx">
        <div class="lang-content" data-lang="pt">
        <div class="study-block">
          <div class="block-title">Dados do Livro</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Extensão</div><div class="info-card-value">22 capítulos · ~970–853 a.C. · Salomão e a divisão do reino</div></div>
            <div class="info-card"><div class="info-card-label">Templo de Salomão</div><div class="info-card-value">Construído em 7 anos (~966–959 a.C.) · cedros do Líbano · ouro de Ofir · destruído em 586 a.C.</div></div>
            <div class="info-card"><div class="info-card-label">Divisão do reino</div><div class="info-card-value">930 a.C. — Judá (sul) e Israel (norte · 10 tribos) se separam permanentemente por causa da apostasia de Salomão</div></div>
            <div class="info-card"><div class="info-card-label">Elias Tisbita</div><div class="info-card-value">Surge sem genealogia (17.1) · duelo do Carmelo contra 450 profetas de Baal · "voz mansa e delicada" no Sinai (19.12)</div></div>
            <div class="info-card"><div class="info-card-label">Jezabel</div><div class="info-card-value">Financia 850 profetas pagãos, mata profetas do Senhor e manda assassinar Nabot para expropriar sua vinha</div></div>
            <div class="info-card"><div class="info-card-label">Critério editorial</div><div class="info-card-value">Cada rei avaliado pela fidelidade a Deus e centralização do culto em Jerusalém · nenhum rei do norte recebe elogio</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Glória e Ruptura</div>
          <div class="block-body">
            <p>1 Reis narra a trajetória de Israel do apogeu ao colapso. O reinado de Salomão (~970–930 a.C.) é o pico da civilização israelita: paz, prosperidade, o Templo de Jerusalém, fama internacional. Mas o livro mostra como as sementes da destruição foram plantadas no próprio auge. A divisão do reino em 930 a.C. é a maior catástrofe política da história israelita — consequência direta da apostasia de Salomão.</p>
            <p>A segunda metade do livro alterna entre os reis de Israel (norte) e Judá (sul), avaliando cada rei pelo critério de fidelidade a Deus e à centralização do culto em Jerusalém. O norte nunca tem um rei "bom" por esse critério.</p>
          </div>
        </div>
        </div>
        <div class="lang-content" data-lang="en" style="display:none">
        <div class="study-block">
          <div class="block-title">Book Overview</div>
          <div class="info-grid">
            <div class="info-card"><div class="info-card-label">Scope</div><div class="info-card-value">22 chapters · ~970–853 BC · Solomon and the division of the kingdom</div></div>
            <div class="info-card"><div class="info-card-label">Solomon's Temple</div><div class="info-card-value">Built in 7 years (~966–959 BC) · cedars of Lebanon · gold of Ophir · destroyed 586 BC</div></div>
            <div class="info-card"><div class="info-card-label">Kingdom divided</div><div class="info-card-value">930 BC — Judah (south) and Israel (north · 10 tribes) split permanently due to Solomon's apostasy</div></div>
            <div class="info-card"><div class="info-card-label">Elijah the Tishbite</div><div class="info-card-value">Appears without genealogy (17:1) · Mount Carmel contest against 450 Baal prophets · "still small voice" at Sinai (19:12)</div></div>
            <div class="info-card"><div class="info-card-label">Jezebel</div><div class="info-card-value">Funds 850 pagan prophets, murders the LORD's prophets, and has Naboth killed to seize his vineyard</div></div>
            <div class="info-card"><div class="info-card-label">Editorial criterion</div><div class="info-card-value">Each king evaluated by faithfulness to God and centralized worship in Jerusalem · no northern king receives praise</div></div>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Glory and Rupture</div>
          <div class="block-body">
            <p>1 Kings traces Israel's trajectory from its zenith to collapse. Solomon's reign (~970–930 BC) represents the peak of Israelite civilization: peace, prosperity, the Temple in Jerusalem, international renown. Yet the book shows how the seeds of destruction were sown at the very height of glory. The division of the kingdom in 930 BC is the greatest political catastrophe in Israelite history — a direct consequence of Solomon's apostasy.</p>
            <p>The second half alternates between the kings of Israel (north) and Judah (south), evaluating each by faithfulness to God and centralized worship in Jerusalem. No northern king ever meets this standard.</p>
          </div>
        </div>
        </div>
      </div>'''

src = src.replace(old_1kgs_ctx, new_1kgs_ctx, 1)

# 1 Kings geo block
old_1kgs_geo = '''      <div class="tab-panel" id="reis1-geo">
        <div class="study-block">
          <div class="block-title">O Templo e os Dois Reinos</div>
          <div class="geo-box">
            <p>O <strong>Monte Moriá</strong> — onde Abraão quase sacrificou Isaque e onde Davi comprou a eira de Araúna — é o local do Templo de Salomão. O Templo foi construído em 7 anos (~966–959 a.C.) com cedros do Líbano e ouro de Ofir. Com a divisão, <strong>Judá</strong> (sul: Judá + Benjamim, capital Jerusalém) e <strong>Israel</strong> (norte: 10 tribos, capital inicial Siquém, depois Tirsa e depois Samaria) se separam permanentemente.</p>
          </div>
        </div>
      </div>'''

new_1kgs_geo = '''      <div class="tab-panel" id="reis1-geo">
        <div class="lang-content" data-lang="pt">
        <div class="study-block">
          <div class="block-title">O Templo e os Dois Reinos</div>
          <div class="geo-box">
            <p>O <strong>Monte Moriá</strong> — onde Abraão quase sacrificou Isaque e onde Davi comprou a eira de Araúna — é o local do Templo de Salomão. O Templo foi construído em 7 anos (~966–959 a.C.) com cedros do Líbano e ouro de Ofir. Com a divisão, <strong>Judá</strong> (sul: Judá + Benjamim, capital Jerusalém) e <strong>Israel</strong> (norte: 10 tribos, capital inicial Siquém, depois Tirsa e depois Samaria) se separam permanentemente.</p>
          </div>
        </div>
        </div>
        <div class="lang-content" data-lang="en" style="display:none">
        <div class="study-block">
          <div class="block-title">The Temple and the Two Kingdoms</div>
          <div class="geo-box">
            <p><strong>Mount Moriah</strong> — where Abraham nearly sacrificed Isaac and where David bought Araunah's threshing floor — is the site of Solomon's Temple. Built over 7 years (~966–959 BC) with cedars from Lebanon and gold from Ophir. After the division, <strong>Judah</strong> (south: Judah + Benjamin, capital Jerusalem) and <strong>Israel</strong> (north: 10 tribes, capitals Shechem, then Tirzah, then Samaria) split permanently.</p>
          </div>
        </div>
        </div>
      </div>'''

src = src.replace(old_1kgs_geo, new_1kgs_geo, 1)

# 1 Kings study block
old_1kgs_study = '''      <div class="tab-panel" id="reis1-study">
        <div class="study-block">
          <div class="block-title">Salomão — Sabedoria e Apostasia</div>
          <div class="block-body">
            <p>O pedido de Salomão em Gibeom (cap. 3) — sabedoria em vez de riqueza ou longevidade — é o ponto alto de sua vida espiritual. O julgamento entre as duas mães (3.16-28) demonstra essa sabedoria imediatamente. A construção e dedicação do Templo (caps. 5–8) é o ápice da narrativa — o discurso de Salomão na dedicação (cap. 8) é uma das maiores orações da Bíblia, incluindo a notável oração pelo estrangeiro (8.41-43).</p>
            <p>Mas Salomão tem <strong>700 esposas e 300 concubinas</strong> (11.3) — representando alianças políticas com cada nação vizinha. O resultado: "suas mulheres lhe perverteram o coração" (11.3). Ele constrói altares para Quemós, Moloque e Astarte. A punição é a divisão do reino — adiada uma geração por causa de Davi.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Elias — A Voz Mansa e Delicada</div>
          <div class="block-body">
            <p>A segunda metade de 1 Reis é dominada por <strong>Elias Tisbita</strong> — o maior profeta do reino do norte. Surge abruptamente sem genealogia (17.1) e enfrenta Acabe e Jezabel, o casal real mais ímpio da história israelita. O <strong>Monte Carmelo</strong> (cap. 18) é o duelo definidor: Elias versus 450 profetas de Baal, terminando com fogo descendo do céu. Mas logo depois, ameaçado por Jezabel, Elias foge ao Sinai em colapso emocional — e Deus o encontra não no fogo nem no vento, mas na "<strong>voz mansa e delicada</strong>" (19.12). É a mais bela teofania do AT após o Monte Sinai.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">A Rainha de Sabá — Sabedoria que Atravessa Fronteiras</div>
          <div class="block-body">
            <p>A visita da <strong>Rainha de Sabá</strong> (cap. 10) é um dos episódios mais celebrados de 1 Reis. A Sabá era provavelmente o reino do atual Iêmen — a 2.000 km de Jerusalém. A rainha viajou com "caravana muito grande, com camelos carregados de especiarias" para testar Salomão com questões difíceis. Quando viu sua sabedoria, seu palácio, sua mesa e seu culto, "não havia mais espírito nela" (10.5) — ficou sem fôlego de admiração.</p>
            <p>Jesus cita este episódio em Mateus 12.42: "A Rainha do Sul se levantará no juízo contra esta geração e a condenará; porque ela veio dos confins da terra para ouvir a sabedoria de Salomão, e eis aqui algo maior do que Salomão." O episódio funciona no texto como símbolo do alcance universal da sabedoria dada por Deus — e também como ironia amarga: uma rainha pagã busca sabedoria com fervor que os próprios israelitas não demonstram.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Jezabel — O Poder do Paganismo Institucionalizado</div>
          <div class="block-body">
            <p><strong>Jezabel</strong>, filha do rei de Sidom e esposa de Acabe, é a figura mais ativa e ameaçadora do reino do norte. Não se trata apenas de apostasia religiosa pessoal — Jezabel financia 450 profetas de Baal e 400 de Aserá à custa do tesouro real (18.19), persegue e mata os profetas do Senhor (18.4), e após a derrota no Carmelo escreve cartas em nome do rei ordenando o assassinato de Nabot para que Acabe tome sua vinha (cap. 21).</p>
            <p>A morte de Nabot é expropriação estatal legitimada por falso testemunho — a fusão do poder real com a injustiça econômica que todos os profetas do AT denunciarão. A confrontação de Elias com Acabe ("Encontraste-me, ó meu inimigo?" — 21.20) e a sentença sobre Jezabel ("Os cães comerão Jezabel no campo de Jezreel") são cumpridas literalmente em 2 Reis 9. O nome "Jezabel" tornou-se sinônimo de perversão religiosa no NT (Ap 2.20).</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Dá ao teu servo um coração que ouça, para que eu possa governar o teu povo e discernir entre o bem e o mal."</p>
          <cite>1 Reis 3.9 — NAA</cite>
        </div>
      </div>'''

new_1kgs_study = '''      <div class="tab-panel" id="reis1-study">
        <div class="lang-content" data-lang="pt">
        <div class="study-block">
          <div class="block-title">Salomão — Sabedoria e Apostasia</div>
          <div class="block-body">
            <p>O pedido de Salomão em Gibeom (cap. 3) — sabedoria em vez de riqueza ou longevidade — é o ponto alto de sua vida espiritual. O julgamento entre as duas mães (3.16-28) demonstra essa sabedoria imediatamente. A construção e dedicação do Templo (caps. 5–8) é o ápice da narrativa — o discurso de Salomão na dedicação (cap. 8) é uma das maiores orações da Bíblia, incluindo a notável oração pelo estrangeiro (8.41-43).</p>
            <p>Mas Salomão tem <strong>700 esposas e 300 concubinas</strong> (11.3) — representando alianças políticas com cada nação vizinha. O resultado: "suas mulheres lhe perverteram o coração" (11.3). Ele constrói altares para Quemós, Moloque e Astarte. A punição é a divisão do reino — adiada uma geração por causa de Davi.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Elias — A Voz Mansa e Delicada</div>
          <div class="block-body">
            <p>A segunda metade de 1 Reis é dominada por <strong>Elias Tisbita</strong> — o maior profeta do reino do norte. Surge abruptamente sem genealogia (17.1) e enfrenta Acabe e Jezabel, o casal real mais ímpio da história israelita. O <strong>Monte Carmelo</strong> (cap. 18) é o duelo definidor: Elias versus 450 profetas de Baal, terminando com fogo descendo do céu. Mas logo depois, ameaçado por Jezabel, Elias foge ao Sinai em colapso emocional — e Deus o encontra não no fogo nem no vento, mas na "<strong>voz mansa e delicada</strong>" (19.12). É a mais bela teofania do AT após o Monte Sinai.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">A Rainha de Sabá — Sabedoria que Atravessa Fronteiras</div>
          <div class="block-body">
            <p>A visita da <strong>Rainha de Sabá</strong> (cap. 10) é um dos episódios mais celebrados de 1 Reis. A Sabá era provavelmente o reino do atual Iêmen — a 2.000 km de Jerusalém. A rainha viajou com "caravana muito grande, com camelos carregados de especiarias" para testar Salomão com questões difíceis. Quando viu sua sabedoria, seu palácio, sua mesa e seu culto, "não havia mais espírito nela" (10.5) — ficou sem fôlego de admiração.</p>
            <p>Jesus cita este episódio em Mateus 12.42: "A Rainha do Sul se levantará no juízo contra esta geração e a condenará; porque ela veio dos confins da terra para ouvir a sabedoria de Salomão, e eis aqui algo maior do que Salomão." O episódio funciona no texto como símbolo do alcance universal da sabedoria dada por Deus — e também como ironia amarga: uma rainha pagã busca sabedoria com fervor que os próprios israelitas não demonstram.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Jezabel — O Poder do Paganismo Institucionalizado</div>
          <div class="block-body">
            <p><strong>Jezabel</strong>, filha do rei de Sidom e esposa de Acabe, é a figura mais ativa e ameaçadora do reino do norte. Não se trata apenas de apostasia religiosa pessoal — Jezabel financia 450 profetas de Baal e 400 de Aserá à custa do tesouro real (18.19), persegue e mata os profetas do Senhor (18.4), e após a derrota no Carmelo escreve cartas em nome do rei ordenando o assassinato de Nabot para que Acabe tome sua vinha (cap. 21).</p>
            <p>A morte de Nabot é expropriação estatal legitimada por falso testemunho — a fusão do poder real com a injustiça econômica que todos os profetas do AT denunciarão. A confrontação de Elias com Acabe ("Encontraste-me, ó meu inimigo?" — 21.20) e a sentença sobre Jezabel ("Os cães comerão Jezabel no campo de Jezreel") são cumpridas literalmente em 2 Reis 9. O nome "Jezabel" tornou-se sinônimo de perversão religiosa no NT (Ap 2.20).</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Dá ao teu servo um coração que ouça, para que eu possa governar o teu povo e discernir entre o bem e o mal."</p>
          <cite>1 Reis 3.9 — NAA</cite>
        </div>
        </div>
        <div class="lang-content" data-lang="en" style="display:none">
        <div class="study-block">
          <div class="block-title">Solomon — Wisdom and Apostasy</div>
          <div class="block-body">
            <p>Solomon's request at Gibeon (ch. 3) — wisdom rather than wealth or long life — is the high point of his spiritual life. The judgment between the two mothers (3:16-28) immediately demonstrates that wisdom. The construction and dedication of the Temple (chs. 5–8) is the narrative's climax — Solomon's prayer at the dedication (ch. 8) is one of the greatest prayers in the Bible, including the remarkable prayer for the foreigner (8:41-43).</p>
            <p>But Solomon takes <strong>700 wives and 300 concubines</strong> (11:3) — each representing a political alliance with a neighboring nation. The result: "his wives turned away his heart" (11:3). He builds altars for Chemosh, Molech, and Ashtoreth. The punishment is the division of the kingdom — delayed one generation for David's sake.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Elijah — The Still Small Voice</div>
          <div class="block-body">
            <p>The second half of 1 Kings is dominated by <strong>Elijah the Tishbite</strong> — the greatest prophet of the northern kingdom. He appears abruptly without genealogy (17:1) and confronts Ahab and Jezebel, the most wicked royal couple in Israelite history. <strong>Mount Carmel</strong> (ch. 18) is the defining contest: Elijah versus 450 Baal prophets, ending with fire falling from heaven. But immediately afterward, threatened by Jezebel, Elijah flees to Sinai in emotional collapse — and God meets him not in the fire or the wind, but in a "<strong>still small voice</strong>" (19:12 ESV). It is the most beautiful theophany in the OT after Mount Sinai.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">The Queen of Sheba — Wisdom Crossing Borders</div>
          <div class="block-body">
            <p>The visit of the <strong>Queen of Sheba</strong> (ch. 10) is one of 1 Kings' most celebrated episodes. Sheba was likely the kingdom of modern Yemen — some 2,000 km from Jerusalem. She came with "a very great retinue, with camels bearing spices" to test Solomon with hard questions. When she witnessed his wisdom, his palace, his table, and his worship, "there was no more breath in her" (10:5) — she was overwhelmed with admiration.</p>
            <p>Jesus cites this episode in Matthew 12:42: "The queen of the South will rise at the judgment with this generation and condemn it, for she came from the ends of the earth to hear the wisdom of Solomon, and behold, something greater than Solomon is here." The episode stands as a symbol of the universal reach of God-given wisdom — and as bitter irony: a pagan queen seeks wisdom with a fervor Israel's own people never show.</p>
          </div>
        </div>
        <div class="study-block">
          <div class="block-title">Jezebel — The Power of Institutionalized Paganism</div>
          <div class="block-body">
            <p><strong>Jezebel</strong>, daughter of the king of Sidon and wife of Ahab, is the most active and threatening figure in the northern kingdom. This goes beyond personal religious apostasy — Jezebel funds 450 Baal prophets and 400 Asherah prophets at royal expense (18:19), hunts down and kills the LORD's prophets (18:4), and after the Carmel defeat writes letters in the king's name ordering Naboth's murder so Ahab can seize his vineyard (ch. 21).</p>
            <p>Naboth's death is state expropriation legitimized by false testimony — the fusion of royal power and economic injustice that every OT prophet will denounce. Elijah's confrontation of Ahab ("Have you found me, O my enemy?" — 21:20) and the sentence on Jezebel ("The dogs shall eat Jezebel in the territory of Jezreel") are literally fulfilled in 2 Kings 9. The name "Jezebel" became a synonym for religious corruption in the NT (Rev 2:20).</p>
          </div>
        </div>
        <div class="key-verse">
          <p>"Give your servant therefore an understanding mind to govern your people, that I may discern between good and evil."</p>
          <cite>1 Kings 3:9 — ESV</cite>
        </div>
        </div>
      </div>'''

src = src.replace(old_1kgs_study, new_1kgs_study, 1)

with open('at-historicos/index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print('1 Kings done.')
