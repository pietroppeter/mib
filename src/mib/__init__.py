from pydantic import BaseModel, RootModel
import json

class Block(BaseModel):
    
    def to_json(self) -> str:
        return self.model_dump_json()


class Code(Block):
    code: str = ""
    output: str = ""


class Text(Block):
    text: str = ""


class Doc(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_json(self) -> str:
        return json.dumps([blk.to_json() for blk in self.blocks])
