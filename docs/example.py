import nobe

nb = nobe.Doc()

nb.text("# Example notebook\nmade with [nobe](https://github.com/pietroppeter/nobe)🐳")

nb.code(lambda: print("hi"))


@nb.code
def _():
    print("hello")


nb.save()
