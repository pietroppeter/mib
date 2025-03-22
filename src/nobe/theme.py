head = """
<head>
  <title>a nobe document</title>
  
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22>🐳</text></svg>">
  
  <meta content="text/html; charset=utf-8" http-equiv="content-type">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="nobe-literate" name="generator">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/light.min.css">
  <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/pietroppeter/nimib/assets/atom-one-light.css'>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script>hljs.highlightAll();</script>
</head>
"""

doc = """
<!DOCTYPE html>
<html lang="en-us">
{head}
<body>
<main>
{blocks}
</main>
</body>
</html>
"""

code = """
<pre><code class="python">{source}</code></pre>
<pre>{stdout}</pre>
"""

image = """
<img src="{url}", alt="{alt}">
"""
