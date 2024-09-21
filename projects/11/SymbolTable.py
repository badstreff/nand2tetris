from enum import StrEnum, auto


class IdentifierKind(StrEnum):
    STATIC = auto()
    FIELD = auto()
    ARG = auto()
    VAR = auto()

class SymbolTable(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self._table = {
            IdentifierKind.STATIC: [],
            IdentifierKind.FIELD: [],
            IdentifierKind.ARG: [],
            IdentifierKind.VAR: []
        }
    def define(self, name: str, type: str, kind: IdentifierKind):
        self._table[kind].append({"name": name, "type": type})
    def var_count(self, kind: IdentifierKind) -> int:
        return len(self._table[kind])
    def kind_of(self, name: str) -> IdentifierKind | None:
        for k, v in self._table.items():
            for sym in v:
                if sym["name"] == name:
                    return k
        raise Exception(f"SymbolNotFound - {name}")
    def type_of(self, name: str) -> str:
        for _, v in self._table.items():
            for sym in v:
                if sym["name"] == name:
                    return sym["type"]
        raise Exception(f"SymbolNotFound - {name}")
    def index_of(self, name: str) -> int:
        for _, v in self._table.items():
            for i, sym in enumerate(v):
                if sym["name"] == name:
                    return i
        raise Exception(f"SymbolNotFound - {name}")