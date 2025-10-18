with open("src/tree.rs", "r") as f:
    text = f.read()

import re

# We can replace the conflict 1
conflict_1_re = re.compile(r"<<<<<<< conflict 1 of 2\n.*?>>>>>>> conflict 1 of 2 ends\n", re.DOTALL)

def repl1(m):
    return """                    if behavior.pane_ui(ui, tile_id, pane) == UiResponse::DragStarted
                        && behavior.is_tile_draggable(&self.tiles, tile_id) 
                    {
                        let allow_drag = if self.floating {
                            self.tiles.parent_of(tile_id).map_or(false, |parent_id| {
                                matches!(
                                    self.tiles.get(parent_id),
                                    Some(Tile::Container(Container::Tabs(_)))
                                )
                            })
                        } else {
                            true
                        };

                        if allow_drag {
                            ui.set_dragged_id(tile_id.egui_id(self.id));
                        }
                    }
"""

text = conflict_1_re.sub(repl1, text)

conflict_2_re = re.compile(r"<<<<<<< conflict 2 of 2\n.*?>>>>>>> conflict 2 of 2 ends\n", re.DOTALL)

def repl2(m):
    return """                if preview_rect.width() > 32.0
                    && preview_rect.height() > 32.0
                    && let Some(Tile::Pane(pane)) = self.tiles.get_mut(dragged_tile_id)
                {
                    // Intentionally ignore the response, since the user cannot possibly
                    // begin a drag on the preview pane.
                    let ui_builder = egui::UiBuilder::new()
                        .max_rect(preview_rect)
                        .sizing_pass()
                        .invisible();
                    let _ignored: UiResponse = behavior.pane_ui(
                        &mut ui.new_child(ui_builder),
                        dragged_tile_id,
                        pane,
                    );
                }
"""

text = conflict_2_re.sub(repl2, text)

with open("src/tree.rs", "w") as f:
    f.write(text)
