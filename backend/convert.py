from enum import Enum
from dataclasses import dataclass
from typing import Callable

from annotated_types import IsNotFinite
from fastapi import Form


class Format(Enum):
    ogg = ("ogg",)
    mp3 = "mp3"


@dataclass(frozen=True)
class Conversion:
    IN: Format
    OUT: Format


class Convertor:
    conversions = {}

    
    def ogg_to_mp3(self, file):
        pass

    
    def mp3_to_ogg(self, file):
        pass

    @classmethod
    def convert(cls, IN:Format, OUT:Format, file )



Convertor.convert(Format.ogg, Format.mp3, "file.ogg")
