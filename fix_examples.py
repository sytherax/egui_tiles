with open("examples/advanced.rs", "r") as f:
    text = f.read()
text = text.replace("ctx.request_repaint();", "ui.ctx().request_repaint();")
with open("examples/advanced.rs", "w") as f:
    f.write(text)

with open("examples/simple.rs", "r") as f:
    text = f.read()
text = text.replace(
    "fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {",
    "fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {",
)
text = text.replace("ctx.input(|i|", "ui.ctx().input(|i|")
text = text.replace(
    "egui::CentralPanel::default().show(ctx, |ui| {",
    "egui::CentralPanel::default().show_inside(ui, |ui| {",
)
text = text.replace("ctx.request_repaint();", "ui.ctx().request_repaint();")
with open("examples/simple.rs", "w") as f:
    f.write(text)

with open("tests/floating_positions.rs", "r") as f:
    text = f.read()
text = text.replace(
    "egui::CentralPanel::default().show(ctx, |ui| {",
    "egui::CentralPanel::default().show_inside(ui, |ui| {",
)
with open("tests/floating_positions.rs", "w") as f:
    f.write(text)
