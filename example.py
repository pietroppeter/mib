import mib

nb = mib.Doc()

nb.text("# Example notebook\nusing [mib](https://github.com/pietroppeter/mib)")

# @nb.code
# def hello():
#    print("hello mib")
nb.add(mib.Code(code='print("hello mib")', output="hello mib"))

nb.save()
