from sticker_factory import StickerFactory
from album import Album
from decimal import Decimal
import argparse


def simulate_completions(stickers_factory: StickerFactory, n_completions: int) -> Decimal:
    album = Album(stickers_factory)
    money_spent = []
    for i in range(n_completions):
        album.fill_album()
        money_spent.append(album.get_money_spent())
        album.reset()

    return Decimal(sum(money_spent)) / n_completions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('total_stickers', type=int)
    parser.add_argument('stickers_in_pack', type=int)
    parser.add_argument('pack_price', type=float)
    parser.add_argument('-sim', '--simulations', type=int, default=20)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    world_cup = StickerFactory(args.total_stickers, args.stickers_in_pack, args.pack_price)
    x = simulate_completions(world_cup, args.simulations)
    print(f"{x:.2f}")
