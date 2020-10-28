from typing import List
from random import randint
from decimal import Decimal


class StickersFactory:
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


class AlbumEdition:
    def __init__(self, sticker_factory: StickersFactory):
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


def simulate_completions(stickers_factory: StickersFactory, n_completions: int) -> Decimal:
    album = AlbumEdition(stickers_factory)
    money_spent = []
    for i in range(n_completions):
        album.fill_album()
        money_spent.append(album.get_money_spent())
        album.reset()

    return Decimal(sum(money_spent)) / n_completions


if __name__ == '__main__':
    world_cup = StickersFactory(682, 5, 0.8)
    x = simulate_completions(world_cup, 100)
    print(f"{x:.2f}")
