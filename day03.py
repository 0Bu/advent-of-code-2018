import re


def get_overlapping_claims(rectangles):
    coordinates = {}
    for r in rectangles:
        index, x, y, width, height = [int(a) for a in re.findall(r'\d+', r)]
        for y_ in range(y, y + height):
            for x_ in range(x, x + width):
                if (x_, y_) in coordinates:
                    coordinates[(x_, y_)] += 1
                else:
                    coordinates[(x_, y_)] = 1
    return sum(v > 1 for v in coordinates.values())


def get_nonoverlapping_claim_ids(rectangles):
    coordinates = dict()
    ids = set()
    for r in rectangles:
        index, x, y, width, height = [int(a) for a in re.findall(r'\d+', r)]
        ids.add(index)
        for y_ in range(y, y + height):
            for x_ in range(x, x + width):
                coordinates.setdefault((x_, y_), set()).add(index)

    for c in coordinates.values():
        if len(c) > 1:
            ids -= c

    return ids


if __name__ == "__main__":
    lines = [line.strip() for line in open("day03.txt", "r")]

    print('overlapped claims:', get_overlapping_claims(lines[:]))
    print('nonoverlapping claim ids:', get_nonoverlapping_claim_ids(lines[:]))
