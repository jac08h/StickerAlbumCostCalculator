from objects.sticker_factory import StickerFactory
from decimal import Decimal


class Album:
    def __init__(self, sticker_factory: StickerFactory):
        self.sticker_factory = sticker_factory

        self.album = [False] * self.sticker_factory.get_total_stickers()  # empty album
        self.stickers_bought = 0

    def buy_pack(self):
        pack = self.sticker_factory.make_pack()
        for sticker in pack:
            self.album[sticker] = True
        self.stickers_bought += self.sticker_factory.get_stickers_in_pack()

    def fill_album(self):
        while self.get_fill_percentage() < 100:
            self.buy_pack()

    def get_money_spent(self) -> Decimal:
        packs_bought = Decimal(self.stickers_bought / self.sticker_factory.get_stickers_in_pack())
        return packs_bought * self.sticker_factory.get_pack_price()

    def get_fill_percentage(self) -> Decimal:
        collected_stickers = sum([int(i) for i in self.album])
        return Decimal(collected_stickers) / len(self.album) * 100

    def summary(self):
        print(
            f"{self.get_fill_percentage()}% filled with {self.stickers_bought} stickers for {self.get_money_spent()}€")

    def reset(self):
        self.album = [False] * self.sticker_factory.get_total_stickers()  # empty album
        self.stickers_bought = 0
