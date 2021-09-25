# 这是一个我的世界钻石计算器,游戏适用版本为1.16/1.17 java版
# 思路来源于B站up主一只冰迷的视频https://www.bilibili.com/video/BV1nU4y1E7Ja
import numpy as np

mul = 25214903917
mask = (1 << 48) - 1


def mulandmask(a):
    return a * mul + 11 & mask


def diamondclac(mapseed, blockx, blockz, ver):
    temp = mapseed ^ mul & mask

    first = mulandmask(temp)
    second = mulandmask(first)
    i = (np.left_shift(np.right_shift(first, 16), 32) + np.right_shift(np.left_shift(second, 16), 32)) | 1

    third = mulandmask(second)
    fourth = mulandmask(third)
    j = (np.left_shift(np.right_shift(third, 16), 32) + np.right_shift(np.left_shift(fourth, 16), 32)) | 1

    temp = ((((16 * blockx * i + 16 * blockz * j) ^ mapseed) + ver) ^ mul) & mask
    relativex = np.right_shift(mulandmask(temp), 44)
    relativez = np.right_shift(mulandmask(mulandmask(temp)), 44)

    diamondx = relativex + 16 * blockx
    diamondz = relativez + 16 * blockz

    return diamondx, diamondz


def lazulicalc(seed, blockx, blockz, ver):
    lazulix, diamondz = diamondclac(seed, blockx, blockz, ver)
    if diamondz % 16 < 4:
        lazuliz = diamondz + 16 - 4 + (diamondz % 16)
    else:
        lazuliz = diamondz - 4
    return lazulix, lazuliz


if __name__ == '__main__':
    while True:
        version = float(input("Please input game version:"))
        if version == 1.16:
            ver = 60009
            break
        elif version == 1.17:
            ver = 60011
            break
        else:
            print("[Error]:Please input 1.16 or 1.17.")
    seed = int(input("Please input map seed:"))
    x = int(input("Please input x:"))
    blockx = int(x / 16)
    z = int(input("Please input z:"))
    blockz = int(z / 16)
    print("Diamond:", diamondclac(seed, blockx, blockz, int(ver)))
    print("Lazuli:", lazulicalc(seed, blockx, blockz, int(ver)))
    input("按Enter退出...")
