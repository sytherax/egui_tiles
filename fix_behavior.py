with open("src/behavior.rs", "r") as f:
    text = f.read()

to_insert = """
    /// Does the behavior allow for resizing the window diagonally?
    fn allow_diagonal_resize(&self) -> bool {
        true
    }

    /// Are floating panes bordered?
    fn floating_pane_border_enabled(&self) -> bool {
        true
    }

    /// The stroke for borders around floating panes
    fn floating_pane_border_stroke(&self, _visuals: &Visuals) -> Stroke {
        Stroke::new(1.0, Color32::from_gray(128))
    }

    /// The rounding for borders around floating panes
    fn floating_pane_border_rounding(&self) -> GuiRounding {
        GuiRounding::ZERO
    }

    /// Paint a hint at the corners when hovering them to drag a floating window diagonally.
    fn paint_corner_hint(&self, _ui: &mut Ui, _response: &Response, _corner_rect: Rect) {
    }
"""

text = text.replace(
    "    fn allow_creating_tabs_on_drop(&self) -> bool {\n        true\n    }\n",
    "    fn allow_creating_tabs_on_drop(&self) -> bool {\n        true\n    }\n"
    + to_insert,
)

with open("src/behavior.rs", "w") as f:
    f.write(text)
