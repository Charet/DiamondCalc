# 这是一个我的世界钻石计算器,游戏适用版本为1.16.5 java版
# 思路来源于B站up主一只冰迷的视频https://www.bilibili.com/video/BV1nU4y1E7Ja
import numpy as np

mul = 25214903917
mask = (1 << 48) - 1


def mulandmask(a):
    return a * mul + 11 & mask


def clac(mapseed, blockx, blockz):
    temp = mapseed ^ mul & mask

    first = mulandmask(temp)
    second = mulandmask(first)
    i = (np.left_shift(np.right_shift(first, 16), 32) + np.right_shift(np.left_shift(second, 16), 32)) | 1

    third = mulandmask(second)
    fourth = mulandmask(third)
    j = (np.left_shift(np.right_shift(third, 16), 32) + np.right_shift(np.left_shift(fourth, 16), 32)) | 1

    temp = ((((16 * blockx * i + 16 * blockz * j) ^ mapseed) + 60009) ^ mul) & mask
    print(temp)
    relativex = np.right_shift(mulandmask(temp), 44)
    relativez = np.right_shift(mulandmask(mulandmask(temp)), 44)

    diamondx = relativex + 16 * blockx
    diamondz = relativez + 16 * blockz

    return diamondx, diamondz


if __name__ == '__main__':
    seed = int(input("Please input map seed:"))
    x = int(input("Please input x for Block:"))
    z = int(input("Please input z for Block:"))
    print(clac(seed, x, z))
