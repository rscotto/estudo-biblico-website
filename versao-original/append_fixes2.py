# -*- coding: utf-8 -*-
# Fix remaining PT passages that were missed or had wrong source text

additions = [
    # Passover scripture - correct source has "primogênito" not "primênascio"
    (
        '"Pois naquela noite passarei pelo Egito e ferirei todo primogênito... O sangue, porém, será o sinal nas casas onde vocês estiverem; quando eu vir o sangue, passarei por cima de vocês."\n      <span class="scripture-ref">Êxodo 12.12–13 — NAA</span>',
        '"For I will pass through the land of Egypt that night, and I will strike all the firstborn... The blood shall be a sign for you, on the houses where you are. And when I see the blood, I will pass over you."\n      <span class="scripture-ref">Exodus 12:12–13 — ESV</span>',
    ),
    # Sea crossing paragraph (was removed by repair, needs proper replacement)
    (
        'A travessia do Mar (Êx 14) é o evento fundacional da identidade de Israel como nação resgatada. O exército egípcio — o maior poder militar da época — é destruído nas águas. Êxodo 15, o Cântico de Moisés, é uma das composições poéticas mais antigas da Bíblia e o primeiro hino litúrgico registrado de Israel. O mesmo cântico ressoa na eternidade — Apocalipse 15.3 descreve os remidos cantando "o cântico de Moisés e o cântico do Cordeiro."',
        'The crossing of the Sea (Exod 14) is the foundational event of Israel\'s identity as a redeemed nation. The Egyptian army — the greatest military power of the age — is destroyed in the waters. Exodus 15, the Song of Moses, is one of the oldest poetic compositions in the Bible and the first recorded liturgical hymn of Israel. The same song echoes in eternity — Revelation 15:3 describes the redeemed singing "the song of Moses, the servant of God, and the song of the Lamb."',
    ),
    # Passover body paragraph (Israel's - was broken before)
    (
        'A Páscoa (<em>Pessah</em>, פֶּסַח — "pular sobre, passar por cima") é a instituição central do Êxodo. Um cordeiro sem defeito, macho, de um ano, sacrificado ao entardecer; seu sangue aspergido nas ombreiras e na verga da porta; sua carne assada e comida com ervas amargas e pães ázimos, em posição de partida. É o mais antigo dos sacramentos de Israel e o protótipo tipológico da Ceia do Senhor (1Co 5.7: "Cristo, nosso Cordeiro pascal, foi sacrificado").',
        'The Passover (<em>Pesach</em>, פֶּסַח — "to pass over") is the central institution of the Exodus. An unblemished male lamb, one year old, sacrificed at twilight; its blood sprinkled on the doorposts and lintel; its flesh roasted and eaten with bitter herbs and unleavened bread, in a posture of readiness. It is the oldest of Israel\'s sacraments and the typological prototype of the Lord\'s Supper (1 Cor 5:7: "Christ, our Passover lamb, has been sacrificed").',
    ),
    # Sarça Ardente section title (still in PT)
    (
        '<h2>A Sarça Ardente — Êxodo 3.1–4.31</h2>',
        '<h2>The Burning Bush — Exodus 3:1–4:31</h2>',
    ),
    # Jethro paragraph with Êxodo reference
    (
        'ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação',
        'he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment',
    ),
]

lines = []
for pt, en in additions:
    lines.append(f'out = out.replace(\n    {repr(pt)},\n    {repr(en)},\n    1\n)\n')

with open('gen_en_pentateuco.py', 'a', encoding='utf-8') as f:
    f.write('\n# ═══ fixes round 2 ═══\n')
    f.writelines(lines)

print(f'Appended {len(additions)} fixes')
