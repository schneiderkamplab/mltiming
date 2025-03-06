#!/usr/bin/env python
from contextlib import contextmanager
from dataclasses import dataclass
from time import monotonic, sleep

__all__ = ["timing", "TimingResult"]

@dataclass
class TimingResult:
    key: str = None
    start: float = None
    end: float = None

    @property
    def elapsed(self):
        return None if self.start is None or self.end is None else self.end-self.start

    @property
    def dict(self):
        return {self.key: self.elapsed}

@contextmanager
def timing(
    message=None,
    key=None,
    format="{result.elapsed:.2f}s",
):
    if message is not None:
        print(message, end=" ... ", flush=True)
    start = monotonic()
    result = TimingResult(key=key, start=start)
    try:
        yield result
    finally:
        result.end = monotonic()
        if message:
            print(format.format(**vars()), flush=True)
