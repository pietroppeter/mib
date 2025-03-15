import mib

nb = mib.Doc()

#nb.text("# Example notebook\nusing [mib]()")
nb.add(mib.Text(text="# Example notebook\nusing [mib]()"))

#@nb.code
#def hello():
#    print("hello mib")
nb.add(mib.Code(code="print(\"hello mib\")", output="hello mib"))


print(nb.to_json())
# print(nb.to_html())
