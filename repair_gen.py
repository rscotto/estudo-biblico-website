# -*- coding: utf-8 -*-
"""Remove broken lines 484-562 from gen_en_pentateuco.py (raw multiline/apostrophe issues).
The correct versions already exist at lines 565+.
"""
with open('gen_en_pentateuco.py', encoding='utf-8') as f:
    lines = f.readlines()

# Lines are 0-indexed. We want to remove lines 483-561 (0-indexed) = lines 484-562 (1-indexed)
# But we must be careful not to remove the line 503 comment separator and line 504 blank line.
# Actually let's find the boundaries by content.

content = ''.join(lines)

# The broken section starts at: out = out.replace(\n    'A Páscoa
# and ends before: \n# ═══ sinai + golden calf ═══
start_marker = "out = out.replace(\n    'A Páscoa (<em>Pessah</em>"
end_marker = "\n# ═══ sinai + golden calf ═══\n"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1:
    print('Start marker not found!')
elif end_idx == -1:
    print('End marker not found!')
else:
    # Also check there's a comment before the broken section to keep
    # Find the '# ═══ pragas body ═══' marker to know where the good part ends
    # We want to keep everything up to (not including) start_marker
    new_content = content[:start_idx] + content[end_idx:]
    with open('gen_en_pentateuco.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    removed_chars = end_idx - start_idx
    print(f'Removed {removed_chars} chars (broken section). File updated.')
