# -*- coding: utf-8 -*-
# Fix: source uses 'sugerendo' not 'sugerindo'
# Also uses correct h2 tag starting with <h2> (no leading spaces in the replacement key)

additions = [
    (
        '<h2>Midiã — Contexto Geopolítico</h2>\n    <p>Os midianitas eram descendentes de Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerendo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
        '<h2>Midian — Geopolitical Context</h2>\n    <p>The Midianites were descendants of Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwestern Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who purchased Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses\'s father-in-law, was <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>',
    ),
]

lines = []
for pt, en in additions:
    lines.append(f'out = out.replace(\n    {repr(pt)},\n    {repr(en)},\n    1\n)\n')

# Insert before the final write block
with open('gen_en_pentateuco.py', encoding='utf-8') as f:
    content = f.read()

write_marker = '\n# ═══ final write ═══\n'
write_idx = content.find(write_marker)

insert_text = '\n# ═══ fixes round 5 ═══\n' + ''.join(lines)
new_content = content[:write_idx] + insert_text + content[write_idx:]

with open('gen_en_pentateuco.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Inserted fix5 before write block')
