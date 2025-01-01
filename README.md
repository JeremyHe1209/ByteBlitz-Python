[Chinese](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README.md) | [English](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README-en.md)

## 码卡：一款充满 OI 元素的卡牌游戏

**码卡** 是一款富含 **OI**（信息学奥赛）元素的卡牌游戏，由两位中学生开发。这个项目正在积极开发中。

**想了解我们的进度？**

下载 [game.tldr](https://raw.githubusercontent.com/JeremyHe1209/ByteBlitz/main/game.tldr) 并使用 [tldraw](https://www.tldraw.com) 打开。这个文件详细展示了每个类的具体成员、类之间的关系以及我们目前的完成情况。（本文件更新较慢，对于新完成的类的介绍可能**并不准确**。）

**想正式加入我们？**

欢迎你给我们发邮件： ``heyicong.jeremy@gmail.com`` 或提 ``issue``。

**开源项目**

这个项目是完全开源的。任何人都可以在协议允许的范围内使用我们的代码。

### 为这个项目做出贡献

由于本游戏是卡牌游戏，需要大量的角色与卡牌。仅靠我们两个人的力量显然不可能，所以我们需要你的帮助！你的点点滴滴贡献都会被记录下来！

**可贡献的内容**

``CardPair`` 类（包含了 ``Card`` 类与 ``Minion`` 类）（暂未完成）

``Hero`` 类（已完成，可贡献）

**如何贡献**

对于 ``CardPair`` 类，暂未开放贡献。

对于 ``Hero`` 类，请参见 ``ByteBlitz/heroes/testhero`` 中的文件格式。假设英雄英文名为 ``{name}`` ，那么你需要**严格**按照以下规则命名：

```
ByteBlitz
    └── heroes
        └── {name}
            ├── {name}hero.py
            └── {name}heroskill.py
```

其中， ``{name}heroskill.py`` 是对英雄技能类（``Skill``）包括所有效果（``Effect``）的定义， ``{name}hero.py`` 是对英雄类的定义。

请在完成这两个文件后，**直接**在 ``issue`` 中发布代码（备注文件名以及文件位置）。我们审核后会将你的代码加入仓库并将你记录在贡献榜中。如果在编写途中遇到其他文件报错，请提 ``issue`` ，我们会尽快处理。

感谢您的贡献！

### 贡献榜

暂无。

---

_By [heyicong](https://www.luogu.com.cn/user/725640) & [JDScript0117](https://www.luogu.com.cn/user/910593)_
