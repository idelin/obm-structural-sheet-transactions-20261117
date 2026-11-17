from dataclasses import dataclass,field
@dataclass
class Sheet:
    name:str
    cells:dict=field(default_factory=dict)
