from pydantic import BaseModel, RootModel
import json
import markdown
import os, inspect
from mib import theme

class Block(BaseModel):
    def to_json(self) -> str:
        return self.model_dump_json()


class Code(Block):
    code: str = ""
    output: str = ""

    def to_html(self) -> str:
        return f"""
<pre><code class="python">
{self.code}
</code></pre>
<pre>
{self.output}
</pre>
"""


class Text(Block):
    text: str = ""

    def to_html(self) -> str:
        return markdown.markdown(self.text)

def text(self: Block, text: str):
    self.add(Text(text=text))


class Doc(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_json(self) -> str:
        return json.dumps([blk.to_json() for blk in self.blocks])

    def to_html(self) -> str:
        head = theme.head
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        return f"""
<!DOCTYPE html>
<html lang="en-us">
{head}
<body>
<main>
{blocks}
</main>
</body>
</html>
"""

    def save(self):
        filename = inspect.stack()[1].filename.replace(".py", ".html")
        with open(filename, "w") as f:
            f.write(self.to_html())


Doc.text = text