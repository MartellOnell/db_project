import string
import random


def string_generator(
    size: int = 6,
    chars: str = string.ascii_uppercase + string.digits
) -> str:
    return ''.join(random.choice(chars) for _ in range(size))