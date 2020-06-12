from functools import partial

from ...core import components
from ...utils import func_factory, make_identifier
from . import defaults

__all__ = (
    "submit",
    "next",
    "back",
    "reset",
)


_make_identifier = partial(make_identifier, suffixes=["buttons"])

submit = func_factory(defaults.submit, components.ButtonComponent, _make_identifier)
next = func_factory(defaults.next, components.ButtonComponent, _make_identifier)
back = func_factory(defaults.back, components.ButtonComponent, _make_identifier)
reset = func_factory(defaults.reset, components.ButtonComponent, _make_identifier)
