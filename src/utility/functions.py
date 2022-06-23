from utility.constants import N_OF_CELL


def get_init() -> tuple:
    return (0, 0, 0, 0) if N_OF_CELL == 4 else (0, 0, 0, 0, 0, 0, 0, 0)