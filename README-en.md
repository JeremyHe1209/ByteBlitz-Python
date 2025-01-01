[Chinese](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README.md) | [English](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README-en.md)

## ByteBlitz: A card game full of OI elements

_Translate By [Google](https://translate.google.com)_

**ByteBlitz** is a card game full of **OI** (Olympiad in Informatics) elements, developed by two middle school students. This project is under active development.

**Want to know our progress?**

Download [game.tldr](https://raw.githubusercontent.com/JeremyHe1209/ByteBlitz/main/game.tldr) and open it with [tldraw](https://www.tldraw.com). This file shows in detail the specific members of each class, the relationship between classes, and our current completion status. (This file is updated slowly, and the introduction of the newly completed class may not be accurate.)

**Want to join us officially?**

You are welcome to send us an email: ``heyicong.jeremy@gmail.com`` or raise an ``issue``.

**Open Source Project**

This project is completely open source. Anyone can use our code within the scope permitted by the agreement.

### Contribute to this project

Since this game is a card game, it requires a large number of characters and cards. It is obviously impossible for the two of us to do it alone, so we need your help! Your contributions will be recorded!

**Contributions**

``CardPair`` class (including ``Card`` class and ``Minion`` class) (not yet completed)

``Hero`` class (completed, can be contributed)

**How ​​to contribute**

For the ``CardPair`` class, contributions are not open yet.

For the ``Hero`` class, see the file format in ``ByteBlitz/heroes/testhero``. Assuming the hero's English name is ``{name}``, you need to **strictly** follow the following naming rules:

```
ByteBlitz
    └── heroes
        └── {name}
            ├── {name}hero.py
            └── {name}heroskill.py
```

Among them, ``{name}heroskill.py`` is the definition of the hero skill class (``Skill``) including all effects (``Effect``), and ``{name}hero.py`` is the definition of the hero class.

After completing these two files, please **directly** publish the code in ``issue`` (note the file name and file location). After review, we will add your code to the repository and record you in the contribution list. If you encounter other file errors during the writing process, please raise ``issue`` and we will handle it as soon as possible.

Thank you for your contribution!

### Contribution list

None yet.

--- _By [heyicong](https://www.luogu.com.cn/user/725640) & [JDScript0117](https://www.luogu.com.cn/user/910593)_