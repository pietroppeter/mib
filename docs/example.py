import nobe

nb = nobe.Doc()

nb.text("# Example document\nmade with [nobe](https://github.com/pietroppeter/nobe)🐳")

nb.text("## Capture output")
nb.text(
    "Output of commands is captured (two ways to declare a code block, check in source code)"
)

nb.code(lambda: print("hi"))


@nb.code
def _():
    print("hello")


nb.text("## Accessing variables in blocks")

nb.text("Declare a variable in one block")


@nb.code
def _():
    global x
    x = 0


nb.text("change it in another block and print it")


@nb.code
def _():
    global x
    x += 1
    print(x)


nb.text("do it 3 times (look for the loop in source code)")

for _ in range(3):

    @nb.code
    def _():
        global x
        x += 1
        print(x)


nb.text(
    "You have to know Python scoping in functions and use global keyword to do the above"
)

nb.text("## Image")

nb.code(
    lambda: nb.image(
        url="https://images.unsplash.com/photo-1565374587194-89003eaebb5b?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        alt="Mountain background in the dolomites with a small hut and two out of focus cyclists climbing on a road",
    )
)

nb.text("Photo from [unsplash](https://unsplash.com/it/foto/casa-sullerba-verde-vicino-a-brown-mountain-88Pbp37FjSs).")

nb.text(f"""## Source code

This is the source code for this document:
        
```py
{nb.source.replace("```", "````")}
```
                
""")

nb.save()
