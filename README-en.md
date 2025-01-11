[Chinese](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README.md) | [English](https://github.com/JeremyHe1209/ByteBlitz/blob/main/README-en.md)

## ByteBlitz: A Card Game with OI Elements

*Translate By [ChatGPT](https://chatgpt.com/)*

**ByteBlitz** is a card game rich in **OI** (Olympiad in Informatics) elements, developed by two middle school students. This project is currently under active development.

**Want to track our progress?**

Download [game.tldr](https://raw.githubusercontent.com/JeremyHe1209/ByteBlitz/main/game.tldr) and open it using [tldraw](https://www.tldraw.com). This file provides detailed information about each class, their relationships, and our current progress. (Note: This file is updated infrequently, so descriptions of newly completed classes may **not be accurate**.)

**Want to officially join us?**

Feel free to send us an email at: `heyicong.jeremy@gmail.com` or open an `issue`.

**Open Source Project**

This project is completely open source. Anyone can use our code within the limits of the license.

### Contribute to this Project

Since this is a card game, it requires a large number of characters and cards. It’s impossible for just the two of us to handle everything, so we need your help! Every small contribution you make will be recognized!

**Areas for Contribution**

The following classes need contributions:

- `CardPair` class (includes the `Card` and `Minion` classes) (not yet available for contribution)
- `Hero` class (completed and open for contributions)

**How to Contribute?**

For the `CardPair` class, contributions are currently not open.

For the `Hero` class, refer to the file structure in `ByteBlitz/heroes/testhero`. Assuming the hero's English name is `{name}`, you need to **strictly** follow the naming conventions below:

```
ByteBlitz
    └── heroes
        └── {name}
            ├── {name}hero.py
            ├── {name}heroskill1.py
            ├── {name}heroskill2.py
            ├── ...
            └── {name}heroskills.py
```

Here, files like `{name}heroskill1.py` define the hero's skills (`Skill`) and all effects (`Effect`), `{name}heroskills.py` serves as a container for all skills, and `{name}hero.py` defines the hero class.

Once these files are completed, **directly** submit your code in an `issue` (include the file names and locations). After review, we will add your code to the repository and credit you on the contributor list. If you encounter errors related to other files during development, please raise an `issue`, and we will address it as soon as possible.

Thank you for your contributions!

### Contributors

None yet.

---

_By [heyicong](https://www.luogu.com.cn/user/725640) & [JDScript0117](https://www.luogu.com.cn/user/910593)_
