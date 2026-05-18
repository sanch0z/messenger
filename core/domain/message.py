from optree.dataclasses import dataclass
from typing import Optional

@dataclass
class message:
    target:Optional[str]
    sender: Optional[str]
    text:str
    is_private:bool

