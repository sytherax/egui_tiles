with open("examples/advanced.rs", "r") as f:
    text = f.read()

import re

# find the conflict block
conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)
def repl(m):
    return """    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let (fps_instant, now) = ui.ctx().input(|i| {
            let dt = i.stable_dt;
            let fps = if dt > f32::EPSILON { 1.0 / dt } else { 0.0 };
            (fps, i.time)
        });
        if fps_instant.is_finite() && now.is_finite() {
            self.fps_history.add(now, fps_instant);
        }
        let fps_display = self
            .fps_history
            .average()
            .filter(|v| v.is_finite())
            .unwrap_or(fps_instant);

        egui::Panel::left("tree").show_inside(ui, |ui| {
"""

text = conflict_re.sub(repl, text)
with open("examples/advanced.rs", "w") as f:
    f.write(text)
