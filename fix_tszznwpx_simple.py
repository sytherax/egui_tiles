import re

with open("examples/simple.rs", "r") as f:
    text = f.read()


def repl1(m):
    return """            egui::SidePanel::left("tree_sidebar_simple").show_inside(ui, |ui| {
                if ui.button("Reset").clicked() {
                    *self = SimpleApp::new();
                }
                if ui.button("Toggle Sidebar").clicked() {
                    self.show_sidebar = !self.show_sidebar;
                }"""


text = re.sub(
    r"<<<<<<< conflict 1 of 2.*?>>>>>>> conflict 1 of 2 ends",
    repl1,
    text,
    flags=re.DOTALL,
)


def repl2(m):
    return """        if self.continuous_render {
            ui.ctx().request_repaint();
        }"""


text = re.sub(
    r"<<<<<<< conflict 2 of 2.*?>>>>>>> conflict 2 of 2 ends",
    repl2,
    text,
    flags=re.DOTALL,
)

with open("examples/simple.rs", "w") as f:
    f.write(text)
