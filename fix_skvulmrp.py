import re

with open("examples/simple.rs", "r") as f:
    text = f.read()


def repl1(m):
    return """        if self.show_sidebar {
            egui::SidePanel::left("tree_sidebar_simple").show_inside(ui, |ui| {
                if ui.button("Reset").clicked() { *self = SimpleApp::new(); }
                if ui.button("Toggle Sidebar").clicked() { self.show_sidebar = !self.show_sidebar; }
                ui.checkbox(&mut self.show_tabs, "Show Tabs for all panes");
                self.behavior.simplification_options.all_panes_must_have_tabs = self.show_tabs;
                self.behavior.ui(ui);
                if ui.button("Add pane to root").clicked() { self.add_pane_to_root(); }
                ui.label(format!("FPS: {:.1}", fps_display));
                ui.checkbox(&mut self.continuous_render, "Continuous render");
                let mut floating = self.tree.floating;
                if ui.checkbox(&mut floating, "Floating mode").changed() { self.tree.set_floating(floating); }
                ui.label(if self.tree.floating {"Floating Mode"} else {"Tiled Mode"});
                ui.separator();
                ui.collapsing("Active tiles", |ui| {
                    let active = self.tree.active_tiles();
                    for tile_id in active { use egui_tiles::Behavior as _; let name = self.behavior.tab_title_for_tile(&self.tree.tiles, tile_id); ui.label(format!("{} - {tile_id:?}", name.text())); }
                });
                ui.separator();
                if let Some(root) = self.tree.root() { tree_ui(ui, &mut self.behavior, &mut self.tree.tiles, root); }
                if let Some(parent) = self.behavior.add_child_to.take() { self.add_pane_to_tabs(parent); }
            });
        } else {
            egui::TopBottomPanel::top("top_controls_simple").show_inside(ui, |ui| {
                ui.horizontal(|ui| {
                    if ui.button("Show Sidebar").clicked() { self.show_sidebar = true; }
                    ui.checkbox(&mut self.show_tabs, "Show Tabs for all panes");
                    self.behavior.simplification_options.all_panes_must_have_tabs = self.show_tabs;
                    if ui.button("Add Pane").clicked() { self.add_pane_to_root(); }
                    ui.label(format!("FPS: {:.1}", fps_display));
                    ui.checkbox(&mut self.continuous_render, "Continuous render");
                });
            });
        }

        egui::CentralPanel::default().show_inside(ui, |ui| {"""


text = re.sub(
    r"<<<<<<< conflict 1 of 2.*?>>>>>>> conflict 1 of 2 ends",
    repl1,
    text,
    flags=re.DOTALL,
)


def repl2(m):
    return """        if self.continuous_render { ui.ctx().request_repaint(); }
    }

    fn save(&mut self, storage: &mut dyn eframe::Storage) {
        #[cfg(feature = "serde")]
        eframe::set_value(storage, eframe::APP_KEY, &self);"""


text = re.sub(
    r"<<<<<<< conflict 2 of 2.*?>>>>>>> conflict 2 of 2 ends",
    repl2,
    text,
    flags=re.DOTALL,
)

with open("examples/simple.rs", "w") as f:
    f.write(text)
