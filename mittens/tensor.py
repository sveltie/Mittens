from __future__ import annotations
import copy
from dataclasses import dataclass
from typing import List, Optional, Union


class Tensor:
    def __init__(self, component: List, dtype: Optional[Union[int, float]]) -> None:
        self.component = component
        self.dtype = dtype

    def __str__(self) -> str:
        return str(self.component)

    def __repr__(self) -> str:
        return f"Tensor.{self.dtype}.{self.component}"

    def __copy__(self) -> Tensor:
        return Tensor(self.component, self.dtype)

    def __deepcopy__(self) -> Tensor:
        return Tensor(copy.deepcopy(self.component, self.dtype))

    def __len__(self) -> int:
        return len(self.component)


class tensor(Tensor):
    pass
