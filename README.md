# mib-notebook

Mib is a literate programming tool to publish static html notebooks from python code.

Install it (`pip install` or `uv add`) as `mib-notebook`, import it as `mib`.

You put your code in a file like [docs/example.py](docs/example.py),
you run it like a normal python script (e.g. `uv run python example.py`)
and you get out [example.html](https://pietroppeter.github.io/mib/example.html).

One way to try this out is:

```
curl -O https://raw.githubusercontent.com/pietroppeter/mib/refs/heads/main/docs/example.py
uv run --with mib example.py
open example.html
```

It is [nimib.py] without [nim].

The goal is to experiment with a [nimib]-like python api.

[nimib]: https://github.com/pietroppeter/nimib
[nimib.py]: https://github.com/nimib-land/nimib.py
[nim]: https://nim-lang.org/
