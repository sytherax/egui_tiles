with open("src/behavior.rs", "r") as f:
    text = f.read()

import re

# Remove the floating_pane_border stuff
text = re.sub(
    r"\s+/// Are floating panes bordered\?.*?fn floating_pane_border_enabled.*?true\s+\}",
    "",
    text,
    flags=re.DOTALL,
)
text = re.sub(
    r"\s+/// The stroke for borders around floating panes.*?fn floating_pane_border_stroke.*?\}\s*",
    "\n",
    text,
    flags=re.DOTALL,
)
text = re.sub(
    r"\s+/// The rounding for borders around floating panes.*?fn floating_pane_border_rounding.*?\}\s*",
    "\n",
    text,
    flags=re.DOTALL,
)

# Fix paint_corner_hint
text = text.replace(
    "fn paint_corner_hint(&self, _ui: &mut Ui, _response: &Response, _corner_rect: Rect) {",
    "fn paint_corner_hint(&self, _ui: &egui::Ui, _response: &egui::Response, _corner_rect: egui::Rect) {",
)

with open("src/behavior.rs", "w") as f:
    f.write(text)
