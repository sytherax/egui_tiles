with open("src/container/grid.rs", "r") as f:
    text = f.read()

import re

conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)
def repl(m):
    return """        let visible_children_and_holes = self.visible_children_and_holes(&tree.tiles);

        for &child in &visible_children_and_holes {
            if let Some(child) = child {
                tree.tile_ui(behavior, drop_context, ui, child);
                crate::cover_tile_if_dragged(tree, behavior, ui, child);
"""

text = conflict_re.sub(repl, text)
with open("src/container/grid.rs", "w") as f:
    f.write(text)
