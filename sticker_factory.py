from decimal import Decimal
from typing import List
from random import randint


class StickerFactory:
    def __init__(self, total_stickers: int, stickers_in_pack: int, pack_price: float,
                 same_stickers_in_pack: bool = False):
        self.total_stickers = total_stickers
        self.stickers_in_pack = stickers_in_pack
        self.pack_price = Decimal(pack_price)
        self.same_stickers_in_pack = same_stickers_in_pack

    def get_total_stickers(self) -> int:
        return self.total_stickers

    def get_pack_price(self) -> Decimal:
        return self.pack_price

    def get_stickers_in_pack(self) -> int:
        return self.stickers_in_pack

    def make_pack(self) -> List[int]:
        pack = []
        for _ in range(self.stickers_in_pack):
            sticker = self.random_sticker()
            if not self.same_stickers_in_pack:
                while sticker in pack:
                    sticker = self.random_sticker()
                pack.append(sticker)
            else:
                pack.append(sticker)

        return pack

    def random_sticker(self) -> int:
        return randint(0, self.total_stickers - 1)
