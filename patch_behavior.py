with open("src/behavior.rs", "r") as f:
    text = f.read()

import re

conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)
def repl(m):
    return """    /// Can this tile be dragged?
    ///
    /// If `false`, the tile cannot be dragged by the user.
    /// This affects both tab dragging and pane dragging.
    ///
    /// Default: `true` (all tiles are draggable).
    fn is_tile_draggable(&self, _tiles: &Tiles<Pane>, _tile_id: TileId) -> bool {
        true
    }

    /// Can the children of this container be resized by dragging the separator?
    ///
    /// Only applies to [`crate::Linear`] and [`crate::Grid`] containers.
    ///
    /// Default: `true` (all containers are resizable).
    fn is_container_resizable(&self, _tiles: &Tiles<Pane>, _tile_id: TileId) -> bool {
        true
    }

    /// Allow creating tab layouts by dropping tiles into the tab area of other tiles.
    ///
    /// If `false`, dragging a tile over the tab area of another tile will not create a new tab layout.
    /// The tile will only be inserted as a horizontal or vertical split.
    fn allow_creating_tabs_on_drop(&self) -> bool {
        true
    }

"""

text = conflict_re.sub(repl, text)
with open("src/behavior.rs", "w") as f:
    f.write(text)
