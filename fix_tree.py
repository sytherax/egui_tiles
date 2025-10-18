with open("src/tree.rs", "r") as f:
    text = f.read()

text = text.replace(
    "for &child in container.active_children() {",
    "for child in container.active_children(&self.tiles) {",
)

text = text.replace(
    """            let mut visible_children = container
                .active_children()
                .filter(|child| self.is_visible(**child))
                .copied();""",
    """            let mut visible_children = container
                .active_children(&self.tiles)
                .filter(|child| self.is_visible(*child));""",
)

with open("src/tree.rs", "w") as f:
    f.write(text)
