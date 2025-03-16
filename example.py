import mib

nb = mib.Doc()

nb.text("# Example notebook\nusing [mib](https://github.com/pietroppeter/mib)")

nb.code(lambda: print("hi"))


@nb.code
def _():
    print("hello")


nb.save()
