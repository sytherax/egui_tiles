import re

with open("src/behavior.rs", "r") as f:
    text = f.read()


def repl(m):
    return """    /// Whether floating panes should have borders.
    ///
    /// Return `true` to enable borders for floating panes.
    fn floating_pane_border_enabled(&self) -> bool {
        false
    }

    /// The stroke used for floating pane borders.
    ///
    /// Only used if [`Self::floating_pane_border_enabled`] returns `true`.
    fn floating_pane_border_stroke(&self, visuals: &Visuals) -> Stroke {
        Stroke::new(1.0, visuals.widgets.noninteractive.bg_stroke.color)
    }

    /// The rounding used for floating pane borders.
    ///
    /// Only used if [`Self::floating_pane_border_enabled`] returns `true`.
    fn floating_pane_border_rounding(&self, _visuals: &Visuals) -> f32 {
        4.0
    }

    /// Paint a hint in the corner of grid tiles that can be used for resizing.
    ///
    /// The default implementation paints diagonal lines in the bottom-right corner.
    fn paint_corner_hint(&self, ui: &egui::Ui, response: &egui::Response, rect: Rect) {
        let style_stroke = ui.style().interact(response).fg_stroke;
        let painter = ui.painter();
        let corner = egui::Align2::RIGHT_BOTTOM;
        let corner_pos = corner
            .pos_in_rect(&rect)
            .round_to_pixels(ui.pixels_per_point());

        let mut w = 2.0;
        let stroke = egui::Stroke {
            width: 1.0,
            color: style_stroke.color,
        };

        while w <= rect.width() && w <= rect.height() {
            let x_dir = corner.x().to_sign();
            let y_dir = corner.y().to_sign();
            painter.line_segment(
                [
                    egui::pos2(corner_pos.x - w * x_dir, corner_pos.y),
                    egui::pos2(corner_pos.x, corner_pos.y - w * y_dir),
                ],
                stroke,
            );
            w += 4.0;
        }"""


text = re.sub(
    r"<<<<<<< conflict 1 of 1.*?>>>>>>> conflict 1 of 1 ends",
    repl,
    text,
    flags=re.DOTALL,
)

with open("src/behavior.rs", "w") as f:
    f.write(text)
