#!/usr/bin/env python3
"""Append sinai/golden-calf translations to gen_en_pentateuco.py"""

additions = [
    # sinai section header
    (
        '<span class="section-tag">Revelação</span>\n      <h1 class="section-title">Sinai, a Aliança e a Lei</h1>\n      <p class="section-lead">A constituição da nação — Deus estabelece Israel como seu povo da aliança mediante lei, tabernáculo e sacrifício.</p>',
        '<span class="section-tag">Revelation</span>\n      <h1 class="section-title">Sinai, the Covenant, and the Law</h1>\n      <p class="section-lead">The constitution of the nation — God establishes Israel as his covenant people through law, tabernacle, and sacrifice.</p>'
    ),
    (
        '<h2>A Aliança do Sinai — Êxodo 19–24</h2>\n    <p>A Aliança do Sinai é uma aliança de lei (<em>berith</em>), estruturalmente similar aos tratados suzeranos hititas do segundo milênio a.C.: <strong>(1)</strong> preâmbulo identificando o soberano, <strong>(2)</strong> prólogo histórico das bênçãos passadas, <strong>(3)</strong> estipulações, <strong>(4)</strong> cláusula de depósito e leitura, <strong>(5)</strong> lista de testemunhas, <strong>(6)</strong> bênçãos e maldições. Êxodo 20 começa exatamente assim: "Eu sou o SENHOR teu Deus, que te tirei da terra do Egito..."</p>',
        '<h2>The Sinai Covenant — Exodus 19–24</h2>\n    <p>The Sinai Covenant is a law covenant (<em>berith</em>), structurally similar to Hittite suzerainty treaties of the second millennium BC: <strong>(1)</strong> preamble identifying the sovereign, <strong>(2)</strong> historical prologue of past blessings, <strong>(3)</strong> stipulations, <strong>(4)</strong> deposit and public reading clause, <strong>(5)</strong> list of witnesses, <strong>(6)</strong> blessings and curses. Exodus 20 begins exactly this way: "I am the Lord your God, who brought you out of the land of Egypt..."</p>'
    ),
    (
        '<span class="callout-type">Graça Precede a Lei</span>\n      <p>A ordem é decisiva: Deus resgata Israel do Egito (graça) <em>antes</em> de dar a Lei. A obediência à Lei não é condição do resgate — é resposta ao resgate. Este é o fundamento reformado da teologia da aliança: a lei é resposta de gratidão ao evangelho da graça, não merecimento da salvação.</p>',
        '<span class="callout-type">Grace Precedes Law</span>\n      <p>The order is decisive: God rescues Israel from Egypt (grace) <em>before</em> giving the Law. Obedience to the Law is not the condition of rescue — it is the response to rescue. This is the Reformed foundation of covenant theology: the law is a grateful response to the gospel of grace, not a means of earning salvation.</p>'
    ),
    (
        '<h2>Os Dez Mandamentos — Êxodo 20 / Deuteronômio 5</h2>\n    <p>O Decálogo (<em>aseret hadevarim</em> — "as dez palavras") é a constituição moral de Israel e, segundo a tradição reformada, a lei moral de Deus aplicável a toda a humanidade. Estrutura-se em dois grupos: deveres para com Deus (mandamentos 1–4) e deveres para com o próximo (5–10), refletindo o resumo de Cristo: "amar a Deus e ao próximo" (Mc 12.29–31).</p>',
        '<h2>The Ten Commandments — Exodus 20 / Deuteronomy 5</h2>\n    <p>The Decalogue (<em>aseret hadevarim</em> — "the ten words") is the moral constitution of Israel and, according to the Reformed tradition, the moral law of God applicable to all humanity. It is structured in two groups: duties toward God (commandments 1–4) and duties toward neighbor (5–10), reflecting Christ\'s summary: "to love God and neighbor" (Mark 12:29–31).</p>'
    ),
    (
        '<h2>O Tabernáculo — Êxodo 25–40</h2>\n    <p>A construção do Tabernáculo (<em>mishkán</em>, מִשְׁכָּן — "morada, habitação") ocupa treze capítulos de Êxodo — mais espaço que qualquer outra instrução. Isso é significativo: a habitação de Deus entre seu povo é o objetivo central da aliança. O Tabernáculo era uma teologia visual — cada elemento apontava para Cristo:</p>',
        '<h2>The Tabernacle — Exodus 25–40</h2>\n    <p>The construction of the Tabernacle (<em>mishkan</em>, מִשְׁכָּן — "dwelling, habitation") occupies thirteen chapters of Exodus — more space than any other instruction. This is significant: God\'s dwelling among his people is the central goal of the covenant. The Tabernacle was a visual theology — every element pointed to Christ:</p>'
    ),
    (
        '<div class="card-title">Elementos do Tabernáculo e sua Tipologia</div>\n        <p>• <strong>Átrio externo:</strong> O altar de bronze — expiação pelos sacrifícios<br>\n        • <strong>Lugar Santo:</strong> Mesa dos pães da proposição, Candelabro, Altar de incenso<br>\n        • <strong>Santo dos Santos:</strong> Arca da Aliança com propiciatório (<em>kapporet</em>) — o trono de Deus, lugar do sangue expiatório<br>\n        • <strong>O Véu:</strong> Separação entre o homem e Deus — rasgado na morte de Cristo (Mc 15.38; Hb 9.8)</p>',
        '<div class="card-title">Tabernacle Elements and Their Typology</div>\n        <p>• <strong>Outer court:</strong> The bronze altar — atonement through sacrifices<br>\n        • <strong>Holy Place:</strong> Table of the bread of the Presence, Lampstand, Altar of incense<br>\n        • <strong>Holy of Holies:</strong> Ark of the Covenant with the mercy seat (<em>kapporet</em>) — God\'s throne, the place of atoning blood<br>\n        • <strong>The Veil:</strong> Separation between man and God — torn at Christ\'s death (Mark 15:38; Heb 9:8)</p>'
    ),
    (
        '<div class="card-title">A Arca da Aliança</div>\n        <p>Continha: <strong>(1)</strong> as duas tábuas da Lei (Dt 10.5), <strong>(2)</strong> o vaso de maná (Êx 16.33–34; Hb 9.4), <strong>(3)</strong> a vara de Arão que floresceu (Nm 17; Hb 9.4). Simboliza: a lei (santidade divina), o maná (provisão), a vara (autoridade sacerdotal). Cristo é o cumprimento de todos os três: a lei personificada, o pão da vida, o Sumo Sacerdote.</p>',
        '<div class="card-title">The Ark of the Covenant</div>\n        <p>Contained: <strong>(1)</strong> the two stone tablets of the Law (Deut 10:5), <strong>(2)</strong> a jar of manna (Exod 16:33–34; Heb 9:4), <strong>(3)</strong> Aaron\'s staff that budded (Num 17; Heb 9:4). It symbolizes: the law (divine holiness), the manna (provision), the staff (priestly authority). Christ is the fulfillment of all three: the law personified, the bread of life, the High Priest.</p>'
    ),
    # golden calf
    ('<h2>O Bezerro de Ouro — Êxodo 32–34</h2>', '<h2>The Golden Calf — Exodus 32–34</h2>'),
    (
        '<span class="callout-type">Passagem Central</span>\n      <p><strong>Êxodo 32.1 – 34.35</strong> é o texto primário, com referências paralelas em Deuteronômio 9.7–10.11. Este episódio é narrado como a maior crise espiritual da história de Israel — ocorrida no momento mais sagrado: enquanto Deus entregava a Lei ao mediador no alto do monte, o povo quebrava aquela mesma lei ao pé do monte. O texto é estruturado em três movimentos: o pecado (cap. 32), a intercessão (32–33) e a restauração da aliança (cap. 34).</p>',
        '<span class="callout-type">Central Passage</span>\n      <p><strong>Exodus 32:1 – 34:35</strong> is the primary text, with parallel references in Deuteronomy 9:7–10:11. This episode is narrated as the greatest spiritual crisis in Israel\'s history — occurring at the most sacred moment: while God was delivering the Law to the mediator at the top of the mountain, the people were breaking that same law at its foot. The text is structured in three movements: the sin (ch. 32), the intercession (32–33), and the restoration of the covenant (ch. 34).</p>'
    ),
    ('<h3>Ato 1 — O Pecado: O Monte e o Vale (Êxodo 32.1–6)</h3>', '<h3>Act 1 — The Sin: The Mountain and the Valley (Exodus 32:1–6)</h3>'),
    (
        'Moisés havia subido ao Monte Sinai para receber a Lei diretamente de Deus. O texto de Êxodo 24.18 registra: <em>"E Moisés entrou no meio da nuvem, e subiu ao monte; e esteve Moisés no monte quarenta dias e quarenta noites."</em> Quarenta dias de silêncio total — sem sinal, sem mensagem, sem retorno visível.',
        'Moses had ascended Mount Sinai to receive the Law directly from God. The text of Exodus 24:18 records: <em>"Moses entered the cloud and went up on the mountain. And Moses was on the mountain forty days and forty nights."</em> Forty days of total silence — no sign, no message, no visible return.'
    ),
    (
        'É esse vácuo que precipita a crise. <strong>Êxodo 32.1:</strong> <em>"Vendo o povo que Moisés tardava em descer do monte, ajuntou-se ao redor de Arão e disse-lhe: Levanta-te, faze-nos deuses que vão adiante de nós; porque não sabemos o que sucedeu a este Moisés, o homem que nos tirou da terra do Egito."</em>',
        'It is this vacuum that precipitates the crisis. <strong>Exodus 32:1:</strong> <em>"When the people saw that Moses delayed to come down from the mountain, the people gathered themselves together to Aaron and said to him, \'Up, make us gods who shall go before us. As for this Moses, the man who brought us up out of the land of Egypt, we do not know what has become of him.\'"</em>'
    ),
    (
        '<div class="card-title">A Impaciência como Raiz</div>\n        <p>O povo não espera nem quarenta dias por Moisés. Eles tinham acabado de comprometer-se solenemente à aliança (Êx 24.7: <em>"tudo o que o SENHOR falou faremos e obedeceremos"</em>). A tinta da aliança mal havia secado. A fé que não aguenta o silêncio de Deus busca um substituto visível.</p>',
        '<div class="card-title">Impatience as the Root</div>\n        <p>The people cannot wait even forty days for Moses. They had just solemnly committed themselves to the covenant (Exod 24:7: <em>"All that the Lord has spoken we will do, and we will be obedient"</em>). The ink of the covenant had barely dried. Faith that cannot endure God\'s silence seeks a visible substitute.</p>'
    ),
    (
        '<div class="card-title">A Redefinição de Moisés</div>\n        <p>Note como o povo descreve Moisés: <em>"este Moisés, o homem que nos tirou da terra do Egito."</em> Não YHWH que os tirou — mas <em>Moisés</em>. Quando o mediador humano desaparece, o povo perde sua âncora. Isso revela que a fé deles estava em Moisés, não em YHWH.</p>',
        '<div class="card-title">The Redefinition of Moses</div>\n        <p>Note how the people describe Moses: <em>"this Moses, the man who brought us up out of the land of Egypt."</em> Not YHWH who brought them out — but <em>Moses</em>. When the human mediator disappears, the people lose their anchor. This reveals that their faith was in Moses, not in YHWH.</p>'
    ),
    (
        'Arão cede sem resistência. Pede os brincos de ouro das mulheres e filhos, os funde, esculpe e declara: <em>"Estes são os teus deuses, ó Israel, que te tiraram da terra do Egito"</em> (Êx 32.4). A mesma frase que o povo havia usado de Moisés, agora aplicada ao ídolo de ouro. Em seguida, Arão constrói um altar e declara: <em>"Amanhã será festa ao SENHOR"</em> (Êx 32.5) — como se o bezerro fosse uma representação de YHWH, não uma substituição.',
        'Aaron yields without resistance. He asks for the golden earrings of the women and children, melts them, shapes them, and declares: <em>"These are your gods, O Israel, who brought you up out of the land of Egypt"</em> (Exod 32:4). The same phrase the people had used of Moses, now applied to the golden idol. Then Aaron builds an altar and declares: <em>"Tomorrow shall be a feast to the Lord"</em> (Exod 32:5) — as if the calf were a representation of YHWH, not a replacement.'
    ),
    (
        '<span class="callout-type">O Bezerro no Contexto Egípcio</span>\n      <p>O touro/bezerro de ouro (<em>egel massekhah</em>, עֵגֶל מַסֵּכָה — "bezerro de metal fundido") não era uma invenção israelita. Na cultura egípcia, o touro Ápis era a encarnação do poder divino — adorado como deus em Mênfis. No Canaã, o deus El era representado como touro. Israel, recém-saída do Egito, recaiu numa forma de adoração familiar: visível, controlável, estático. Queriam um deus que pudesse ver, não um Deus que as nuvens ocultavam no monte.</p>',
        '<span class="callout-type">The Calf in Egyptian Context</span>\n      <p>The golden bull/calf (<em>egel massekhah</em>, עֵגֶל מַסֵּכָה — "cast metal calf") was not an Israelite invention. In Egyptian culture, the Apis bull was the incarnation of divine power — worshiped as a god in Memphis. In Canaan, the god El was represented as a bull. Israel, fresh out of Egypt, relapsed into a familiar form of worship: visible, controllable, static. They wanted a god they could see, not a God hidden by clouds on the mountain.</p>'
    ),
    ('<h3>Ato 2 — A Ira Divina e a Primeira Intercessão (Êxodo 32.7–14)</h3>', '<h3>Act 2 — Divine Wrath and the First Intercession (Exodus 32:7–14)</h3>'),
    (
        'Deus interrompe a entrega da Lei para informar Moisés do que está acontecendo no vale. Sua linguagem é de distanciamento furioso: <em>"Desce, porque o teu povo, que tiraste da terra do Egito, se corrompeu"</em> (Êx 32.7). Repare: Deus não diz "meu povo" — diz <strong>"teu povo"</strong>. É uma linguagem de rejeição temporária, espelhando a que o povo havia usado de Moisés.',
        'God interrupts the giving of the Law to inform Moses of what is happening in the valley. His language is one of furious distancing: <em>"Go down, for your people, whom you brought up out of the land of Egypt, have corrupted themselves"</em> (Exod 32:7). Notice: God does not say "my people" — he says <strong>"your people."</strong> It is a language of temporary rejection, mirroring what the people had said about Moses.'
    ),
    (
        'O decreto divino é devastador: <em>"Agora, pois, deixa-me, para que a minha ira se acenda contra eles e os consuma; e de ti farei uma grande nação"</em> (Êx 32.10). Deus oferece a Moisés o que havia prometido a Abraão — fazer dele uma nação grande. É uma oferta extraordinária, e é uma prova: o que Moisés fará com ela?',
        'The divine decree is devastating: <em>"Now therefore let me alone, that my wrath may burn hot against them and I may consume them, in order that I may make a great nation of you"</em> (Exod 32:10). God offers Moses what he had promised Abraham — to make him a great nation. It is an extraordinary offer, and it is a test: what will Moses do with it?'
    ),
    (
        'Moisés recusa. Sua intercessão em Êxodo 32.11–13 é um dos discursos mais ousados da Bíblia inteira — Moisés <em>argumenta contra Deus</em> usando os próprios valores de Deus:',
        'Moses refuses. His intercession in Exodus 32:11–13 is one of the boldest speeches in all of Scripture — Moses <em>argues against God</em> using God\'s own values:'
    ),
    (
        '"Por que arderia a ira do <span style="font-variant:small-caps">Senhor</span> contra o seu povo, que você tirou do Egito com grande poder e com mão forte? Por que os egípcios diriam: Com más intenções ele os tirou, para matá-los nas montanhas e exterminá-los da face da terra? Abandone o ardor da sua ira e arrependa-se do mal contra o seu povo. Lembre-se de Abraão, Isaque e Israel, seus servos, aos quais você jurou por si mesmo..."\n      <span class="scripture-ref">Êxodo 32.11–13 — NAA</span>',
        '"O <span style="font-variant:small-caps">Lord</span>, why does your wrath burn hot against your people, whom you have brought out of the land of Egypt with great power and with a mighty hand? Why should the Egyptians say, \'With evil intent did he bring them out, to kill them in the mountains and to consume them from the face of the earth\'? Turn from your burning anger and relent from this disaster against your people. Remember Abraham, Isaac, and Israel, your servants, to whom you swore by your own self..."\n      <span class="scripture-ref">Exodus 32:11–13 — ESV</span>'
    ),
    (
        'Moisés usa <strong>três argumentos</strong>: (1) a reputação de Deus diante dos egípcios — "o que dirão as nações?"; (2) a natureza do próprio Deus como misericordioso; (3) as promessas aos patriarcas como fundamento inabalável da aliança. São os mesmos argumentos que qualquer advogado de defesa usaria — e funcionam. O texto registra: <em>"E o SENHOR se arrependeu do mal que dissera que havia de fazer ao seu povo"</em> (Êx 32.14).',
        'Moses uses <strong>three arguments</strong>: (1) God\'s reputation before the Egyptians — "what will the nations say?"; (2) the very nature of God as merciful; (3) the promises to the patriarchs as the unshakeable foundation of the covenant. These are the same arguments any defense attorney would use — and they work. The text records: <em>"And the Lord relented from the disaster that he had spoken of bringing on his people"</em> (Exod 32:14).'
    ),
    ('<h3>Ato 3 — A Descida do Monte e o Julgamento (Êxodo 32.15–29)</h3>', '<h3>Act 3 — Descent from the Mountain and Judgment (Exodus 32:15–29)</h3>'),
    (
        'Moisés desce o monte carregando as duas tábuas de pedra — escritas "dos dois lados... e a escritura era escritura de Deus, gravada nas tábuas" (Êx 32.15–16). Josué, que havia esperado mais abaixo, ouve o barulho no acampamento e o interpreta como som de guerra. Moisés corrige: é canto, não batalha.',
        'Moses descends the mountain carrying the two stone tablets — written "on both sides... and the writing was the writing of God, engraved on the tablets" (Exod 32:15–16). Joshua, who had been waiting lower down, hears the noise in the camp and interprets it as the sound of war. Moses corrects him: it is singing, not battle.'
    ),
    (
        'Ao se aproximar e ver o bezerro e as danças, <strong>Moisés irou-se e atirou as tábuas</strong> da mão, quebrando-as ao pé do monte (Êx 32.19). O gesto é profundamente simbólico: a aliança foi quebrada primeiro pelo povo — Moisés apenas expressa visivelmente o que já acontecera espiritualmente. A Lei foi destruída antes mesmo de ser lida.',
        'As he draws near and sees the calf and the dancing, <strong>Moses\'s anger burned hot and he threw the tablets</strong> from his hands, breaking them at the foot of the mountain (Exod 32:19). The gesture is profoundly symbolic: the covenant was broken first by the people — Moses merely makes visible what had already happened spiritually. The Law was destroyed before it was even read.'
    ),
    ('Moisés então executa um julgamento triplo sobre o bezerro:', 'Moses then executes a threefold judgment upon the calf:'),
    (
        '<span class="callout-type">O Julgamento Sobre o Bezerro — Êxodo 32.20</span>\n      <p>Moisés <strong>(1) pegou o bezerro</strong> que fizeram, <strong>(2) queimou-o</strong> no fogo, <strong>(3) moeu-o</strong> até virar pó, <strong>(4) espalhou sobre as águas</strong> e <strong>(5) fez os israelitas beber</strong>. Este ritual de destruição tem paralelos com a lei das águas amargas de Números 5 (a mulher suspeita de adultério bebe as águas com o pó da maldição). Israel cometera adultério espiritual com seu deus; agora bebe as consequências da idolatria — literalmente. A aliança com YHWH era um casamento; o bezerro foi adultério.</p>',
        '<span class="callout-type">The Judgment on the Calf — Exodus 32:20</span>\n      <p>Moses <strong>(1) took the calf</strong> they had made, <strong>(2) burned it</strong> with fire, <strong>(3) ground it</strong> to powder, <strong>(4) scattered it on the water</strong>, and <strong>(5) made the Israelites drink it</strong>. This destruction ritual has parallels with the bitter water law of Numbers 5 (the woman suspected of adultery drinks the cursed water with the dust). Israel had committed spiritual adultery against their God; now they drink the consequences of idolatry — literally. The covenant with YHWH was a marriage; the calf was adultery.</p>'
    ),
    (
        'Moisés confronta Arão, que oferece uma das desculpas mais patéticas da Escritura: <em>"Eles me deram o ouro, e eu o lancei no fogo, e saiu este bezerro"</em> (Êx 32.24). Arão nega sua agência — o bezerro simplesmente <em>saiu</em> do fogo por conta própria. O líder que cedeu à pressão popular agora tenta se isentar da responsabilidade.',
        'Moses confronts Aaron, who offers one of the most pathetic excuses in Scripture: <em>"They gave me the gold, so I threw it into the fire, and out came this calf"</em> (Exod 32:24). Aaron denies his agency — the calf simply <em>came out</em> of the fire on its own. The leader who yielded to popular pressure now attempts to exempt himself from responsibility.'
    ),
    (
        'Moisés convoca os que estão com YHWH. Os levitas se apresentam. Por ordem de Moisés, percorrem o acampamento com espadas e matam cerca de três mil homens (Êx 32.28). O julgamento é severo e preciso: não toda a nação, mas os instigadores e os que persistiram na rebelião.',
        'Moses calls for those who are on the Lord\'s side. The Levites come forward. At Moses\'s command, they go through the camp with swords and kill about three thousand men (Exod 32:28). The judgment is severe and precise: not the entire nation, but the instigators and those who persisted in rebellion.'
    ),
    ('<h3>Ato 4 — A Segunda Intercessão: "Risca-me do Teu Livro" (Êxodo 32.30–35)</h3>', '<h3>Act 4 — The Second Intercession: "Blot Me Out of Your Book" (Exodus 32:30–35)</h3>'),
    (
        'No dia seguinte, Moisés sobe novamente ao monte para fazer propiciação pelo pecado do povo. Sua intercessão atinge o ponto mais extremo possível:',
        'The next day, Moses goes up again to the mountain to make atonement for the people\'s sin. His intercession reaches the most extreme point possible:'
    ),
    (
        '"Mas agora, se você perdoar o pecado deles... Caso contrário, risque-me do livro que você escreveu."\n      <span class="scripture-ref">Êxodo 32.32 — NAA</span>',
        '"But now, if you will forgive their sin — but if not, please blot me out of your book that you have written."\n      <span class="scripture-ref">Exodus 32:32 — ESV</span>'
    ),
    (
        'Moisés oferece sua própria vida — sua existência no livro de Deus — como substituto pelo povo. Ele pede para ser riscado (<em>machah</em>, מְחֵה — apagar, obliterar) do livro divino se o povo não puder ser perdoado. Paulo usará linguagem quase idêntica em Romanos 9.3: <em>"porque eu mesmo desejaria ser anátema, separado de Cristo, por amor de meus irmãos."</em>',
        'Moses offers his own life — his existence in God\'s book — as a substitute for the people. He asks to be blotted out (<em>machah</em>, מְחֵה — to erase, obliterate) from the divine book if the people cannot be forgiven. Paul will use nearly identical language in Romans 9:3: <em>"For I could wish that I myself were accursed and cut off from Christ for the sake of my brothers."</em>'
    ),
    (
        'Mas Deus responde com um princípio inabalável: <em>"Quem pecou contra mim, a esse riscarei do meu livro"</em> (Êx 32.33). A substituição que Moisés propõe não é possível — não porque Deus é cruel, mas porque nenhum homem pecador pode ser o substituto expiatório de outro. A tipologia aqui aponta diretamente para Cristo: somente o Filho sem pecado poderia ser riscado <em>em lugar de</em> outros. O que Moisés desejou e não pôde fazer, Cristo fez.',
        'But God responds with an unshakeable principle: <em>"Whoever has sinned against me, I will blot out of my book"</em> (Exod 32:33). The substitution Moses proposes is not possible — not because God is cruel, but because no sinful man can be the atoning substitute for another. The typology here points directly to Christ: only the sinless Son could be blotted out <em>in place of</em> others. What Moses desired and could not do, Christ did.'
    ),
    ('<h3>Ato 5 — A Tenda da Congregação e o Rosto de Moisés (Êxodo 33–34)</h3>', '<h3>Act 5 — The Tent of Meeting and the Face of Moses (Exodus 33–34)</h3>'),
    (
        'Após o pecado do bezerro, Deus anuncia que não subirá no meio do povo — pois os consumiria pelo caminho (Êx 33.3). É um momento de ruptura na presença divina. Moisés monta a <strong>Tenda da Congregação</strong> fora do acampamento — a presença de Deus se afastou para a periferia. Quando Moisés entrava na tenda, a coluna de nuvem descia (Êx 33.9), e o povo observava de longe, adorando cada um à porta de sua tenda.',
        'After the sin of the calf, God announces that he will not go up in the midst of the people — for he would consume them on the way (Exod 33:3). It is a moment of rupture in the divine presence. Moses pitches the <strong>Tent of Meeting</strong> outside the camp — God\'s presence has withdrawn to the periphery. When Moses entered the tent, the pillar of cloud would descend (Exod 33:9), and the people watched from a distance, each worshiping at his own tent door.'
    ),
    (
        'É nesse contexto — de distância divina após o maior pecado de Israel — que Moisés pede algo audacioso: <em>"Mostra-me, rogo-te, a tua glória"</em> (Êx 33.18). E Deus concede — não a visão direta da face divina (que nenhum homem pode ver e viver — Êx 33.20), mas a passagem da <em>bondade</em> de Deus diante de Moisés, e a proclamação do Nome.',
        'It is in this context — of divine distance after Israel\'s greatest sin — that Moses asks for something audacious: <em>"Please show me your glory"</em> (Exod 33:18). And God grants it — not the direct vision of the divine face (which no man can see and live — Exod 33:20), but the passing of God\'s <em>goodness</em> before Moses, and the proclamation of the Name.'
    ),
    (
        'A renovação da aliança em Êxodo 34 começa com Moisés talhando novas tábuas de pedra para substituir as que ele havia quebrado. O detalhe é teologicamente significativo: as primeiras tábuas foram feitas e escritas por Deus (Êx 32.16); as segundas também são escritas por Deus (Êx 34.1), mas <em>talhadas por Moisés</em>. Após o pecado, há cooperação humana no processo de restauração.',
        'The renewal of the covenant in Exodus 34 begins with Moses chiseling new stone tablets to replace those he had broken. The detail is theologically significant: the first tablets were made and written by God (Exod 32:16); the second are also written by God (Exod 34:1), but <em>chiseled by Moses</em>. After sin, there is human cooperation in the process of restoration.'
    ),
    (
        'Quando Moisés desce do monte pela segunda vez com as tábuas renovadas, ocorre o detalhe físico mais extraordinário da narrativa: <em>"a pele do seu rosto resplandecia"</em> (Êx 34.29–35, Hb: <em>qaran</em>, קָרַן — literalmente "irradiava raios"). A presença de Deus deixou uma marca visível no rosto de Moisés — tanto que os israelitas temiam se aproximar. Moisés precisou cobrir o rosto com um véu ao falar com o povo, removendo-o apenas para entrar na presença de Deus.',
        'When Moses descends the mountain a second time with the renewed tablets, the most extraordinary physical detail in the narrative occurs: <em>"the skin of his face shone"</em> (Exod 34:29–35, Heb: <em>qaran</em>, קָרַן — literally "sent out rays"). God\'s presence left a visible mark on Moses\'s face — so much so that the Israelites were afraid to come near him. Moses had to put a veil over his face when speaking to the people, removing it only when entering the presence of God.'
    ),
    (
        '<span class="callout-type">Paulo e o Véu — 2 Coríntios 3.7–18</span>\n      <p>Paulo usa o véu de Moisés como tipologia em 2 Coríntios 3. O véu não era para proteger o povo da glória — era para ocultar que a glória estava <em>desaparecendo</em> (3.13). O ministério da lei era glorioso, mas temporário. Em Cristo, o véu é removido (3.14–16), e nós contemplamos "a glória do Senhor a face descoberta" e somos transformados "de glória em glória" (3.18). O que Moisés experimentou parcialmente — e teve que ocultar — é o que os crentes possuem permanentemente em Cristo.</p>',
        '<span class="callout-type">Paul and the Veil — 2 Corinthians 3:7–18</span>\n      <p>Paul uses the veil of Moses as typology in 2 Corinthians 3. The veil was not to protect the people from the glory — it was to conceal that the glory was <em>fading</em> (3:13). The ministry of the law was glorious, but temporary. In Christ, the veil is removed (3:14–16), and we behold "the glory of the Lord with unveiled face" and are transformed "from one degree of glory to another" (3:18). What Moses experienced partially — and had to hide — is what believers possess permanently in Christ.</p>'
    ),
    (
        '<h2>A Teofania Plena — Êxodo 33–34</h2>\n    <p>Após a crise, Moisés pede ver a glória de Deus (Êx 33.18). Deus passa diante dele proclamando seu Nome — Êxodo 34.6–7 é a mais completa autodeclaração de Deus no AT:</p>',
        '<h2>The Full Theophany — Exodus 33–34</h2>\n    <p>After the crisis, Moses asks to see God\'s glory (Exod 33:18). God passes before him proclaiming his Name — Exodus 34:6–7 is the most complete self-declaration of God in the OT:</p>'
    ),
    (
        '"O <span style="font-variant:small-caps">Senhor</span>! O <span style="font-variant:small-caps">Senhor</span>! Deus compassivo e misericordioso, tardio em irar-se, transbordante de amor leal e de fidelidade, que mantém o amor leal por milhares, e perdoa a iniquidade, a transgressão e o pecado; que não absolve o culpado, e que pune a iniquidade dos pais nos filhos..."\n      <span class="scripture-ref">Êxodo 34.6–7 — NAA</span>',
        '"The <span style="font-variant:small-caps">Lord</span>, the <span style="font-variant:small-caps">Lord</span>, a God merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness, keeping steadfast love for thousands, forgiving iniquity and transgression and sin, but who will by no means clear the guilty, visiting the iniquity of the fathers on the children..."\n      <span class="scripture-ref">Exodus 34:6–7 — ESV</span>'
    ),
    (
        'Este texto (chamado pelos rabinos de <em>Shloshah Asar Middot</em> — as treze medidas divinas) é citado ou ecoado em pelo menos 15 passagens do AT (Nm 14.18; Sl 86.15; 103.8; 145.8; Jl 2.13; Jn 4.2; Mq 7.18 etc.) — demonstrando que é o credo teológico central de Israel sobre o caráter de Deus.',
        'This text (called by the rabbis the <em>Shloshah Asar Middot</em> — the thirteen divine attributes) is cited or echoed in at least 15 OT passages (Num 14:18; Ps 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2; Mic 7:18, etc.) — demonstrating that it is Israel\'s central theological creed about the character of God.'
    ),
]

lines = []
for pt, en in additions:
    lines.append(f'out = out.replace(\n    {repr(pt)},\n    {repr(en)},\n    1\n)\n')

with open('gen_en_pentateuco.py', 'a', encoding='utf-8') as f:
    f.write('\n# ═══ sinai + golden calf ═══\n')
    f.writelines(lines)

print(f'Appended {len(lines)} replacements')
