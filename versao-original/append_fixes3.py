# -*- coding: utf-8 -*-
additions = [
    (
        'Midiã, filho de Abraão e Quetura (Gn 25.2). Habitavam o noroeste da Arábia, sul de Canaã e partes do Sinai. Eram comerciantes (cf. os midianitas que compraram José — Gn 37.28) e seminômades. Jetro/Reuel, sogro de Moisés, era <em>sacerdote de Midiã</em> — sua identidade religiosa é significativa: ele sacrifica a Deus após o Êxodo (Êx 18.12), sugerindo conhecimento do YHWH ou reconhecimento pós-revelação.</p>',
        'Midian, son of Abraham and Keturah (Gen 25:2). They inhabited northwest Arabia, southern Canaan, and parts of Sinai. They were traders (cf. the Midianites who bought Joseph — Gen 37:28) and semi-nomads. Jethro/Reuel, Moses\'s father-in-law, was a <em>priest of Midian</em> — his religious identity is significant: he sacrifices to God after the Exodus (Exod 18:12), suggesting prior knowledge of YHWH or post-revelation acknowledgment.</p>',
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

insert_text = '\n# ═══ fixes round 3 ═══\n' + ''.join(lines)
new_content = content[:write_idx] + insert_text + content[write_idx:]

with open('gen_en_pentateuco.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f'Inserted {len(additions)} fix(es) before write block')
