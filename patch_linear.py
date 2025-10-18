with open("src/container/linear.rs", "r") as f:
    text = f.read()

import re

conflict_re = re.compile(r"<<<<<<<.*?\n(.*?)>>>>>>> conflict \d+ of \d+ ends\n", re.DOTALL)

def repl(m):
    block = m.group(1)
    # The block contains %%%%%%%, \\\\\\\, +++++++
    # Let's extract the part after +++++++
    parts = block.split("+++++++")
    rebased_part = parts[1].split("\n", 1)[1] # remove the branch info line
    # replace #[allow(...)] with #[expect(...)] at the very end
    rebased_part = rebased_part.replace("#[allow(clippy::too_many_arguments)]", "#[expect(clippy::too_many_arguments)]")
    return rebased_part

text = conflict_re.sub(repl, text)
with open("src/container/linear.rs", "w") as f:
    f.write(text)
