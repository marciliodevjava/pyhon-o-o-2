# abstract base classes
from abc import ABC
from collections.abc import MutableSequence
from numbers import Complex
from typing import Any


class Numero(Complex):

    def __getitem__(self, item):
        super().__getitem__(item)

    def __abs__(self):
        super().__abs__()

    def __add__(self, other):
        super().__add__(other)

    def __complex__(self):
        super().__complex__()

    def __eq__(self, other):
        super().__eq__(other)

    def __pow__(self, power, modulo=None):
        super().__pow__(power)

    def __mul__(self, other):
        super().__mul__(other)

    def __neg__(self):
        super().__neg__()

    def __pos__(self):
        super().__pos__()

    def __radd__(self, other):
        super().__radd__(other)

    def __rmul__(self, other):
        super().__rmul__(other)

    def __rpow__(self, other):
        super().__rpow__(other)

    def __rtruediv__(self, other):
        super().__rtruediv__(other)

    def __truediv__(self, other):
        super().__truediv__(other)

    def conjugate(self) -> Any:
        return super().conjugate()

    def imag(self) -> Any:
        return super().imag()
    
    def real(self) -> Any:
        super().real()

filmes = Numero()
