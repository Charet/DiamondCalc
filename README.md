# 介绍

这是一个我的世界Java版1.16的钻石生成计算器

思路来源于B站:https://www.bilibili.com/video/BV1nU4y1E7Ja

打开后按提示分别输入地图种子,区块x与z坐标即可,层数无法计算,可以用猛男挖矿法来挖

人生建议:小心岩浆

python依赖包:numpy

原理大概就是up去看了源码发现一个区块只会生成一簇钻石,青金石也是.然后用他生成的算法计算就可以找到了.如果你算的坐标没有那就可能是压在基岩下或者生成洞穴岩浆等地形时刷掉了.

# 效果实验

![20210829100143](https://github.com/Charet/DiamondCalc/blob/master/img/20210829100143.png?raw=true)

什么嘛算~~(she)~~的还挺准的嘛

