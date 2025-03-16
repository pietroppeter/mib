import inspect
import io
import json
import sys
from typing import Callable, Optional

import markdown
from pydantic import BaseModel

from mib import source
from mib import theme


class Block(BaseModel):
    def to_json(self) -> str:
        return self.model_dump_json()


class Doc(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_json(self) -> str:
        return json.dumps([blk.to_json() for blk in self.blocks])

    def to_html(self) -> str:
        head = theme.head
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        return theme.doc.format(head=head, blocks=blocks)

    def save(self):
        filename = inspect.stack()[1].filename.replace(".py", ".html")
        with open(filename, "w") as f:
            f.write(self.to_html())


class Text(Block):
    text: str = ""

    def to_html(self) -> str:
        return markdown.markdown(self.text)


def text(doc: Doc, text: str):
    doc.add(Text(text=text))


Doc.text = text


class Code(Block):
    callable: Optional[Callable] = None
    source: str = ""
    stdout: str = ""

    def to_html(self) -> str:
        return theme.code.format(source=self.source, stdout=self.stdout)


def code(doc: Doc, callable: Callable):
    blk = Code(callable=callable)
    blk.source = source.getsource(callable)

    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    blk.callable()

    blk.stdout = sys.stdout.getvalue()
    sys.stdout = _stdout

    doc.add(blk)


Doc.code = code
