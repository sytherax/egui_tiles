with open("examples/simple.rs", "r") as f:
    text = f.read()

import re

# find the conflict block
conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)
def repl(m):
    return """    eframe::run_native(
        "My egui App",
        options,
        Box::new(|_cc| Ok(Box::new(SimpleApp::new()))),
    )
"""

text = conflict_re.sub(repl, text)
with open("examples/simple.rs", "w") as f:
    f.write(text)
