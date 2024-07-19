# Neural networks from scratch

Repository for learning and experimenting.

Theory in chronological learning order here: [THEORY.md](THEORY.md)

## Dev

Install python or run these commands:

```bash
docker build -t python-container .
docker run -it -v "$(pwd)/scripts:/scripts" python-container
```

Then it's just python...

```bash
py hello.py
```

## Notes

 Black formatter extension really good for formatting python code. For VS Code go to settings Ctrl+, and search formatting and select the formatter and also click format on save.