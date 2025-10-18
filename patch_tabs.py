with open("src/container/tabs.rs", "r") as f:
    text = f.read()

import re

conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)

def repl(m):
    return """                        if !tree.is_root(tile_id)
                            && !tree.floating
                            && behavior.is_tile_draggable(&tree.tiles, tile_id)
                        {
"""

text = conflict_re.sub(repl, text)
with open("src/container/tabs.rs", "w") as f:
    f.write(text)
