def get_variance(box_id):
    d = dict.fromkeys(set(box_id), 0)
    for c in box_id:
        d[c] += 1
    return d


def get_checksum(box_ids):
    twice, thrice = (0, 0)
    for box_id in box_ids:
        frequencies = get_variance(box_id).values()
        if 2 in frequencies:
            twice += 1
        if 3 in frequencies:
            thrice += 1
    return twice * thrice


def get_common_letters(box_ids):
    for i, a in enumerate(box_ids):
        for b in box_ids[i+1:]:
            common = []
            for j in range(len(a)):
                if a[j] == b[j]:
                    common.append(a[j])
            if len(a) - len(common) == 1:
                return "".join(common)
    return None


if __name__ == "__main__":
    lines = [line.strip() for line in open("day02.txt", "r")]

    print('checksum:', get_checksum(lines[:]))
    print('common letters:', get_common_letters(lines[:]))
