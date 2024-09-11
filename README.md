# Quantum Computing and Machine Learning

2024 spring/summer/autumn.

Repository for self learning QC and QML to prepare for bachelor thesis and/or including myself in the work of Vilnius University quantum computing study group, masters studies and in general out of interest. 

## Content

Resource: [Quantum Soar channel on YouTube](https://www.youtube.com/@quantum-soar). Cheatsheet: [LaTex](./QuantumSoar-cheatsheet.tex) and [PDF](./QuantumSoar-cheatsheet.pdf)


## Coding setup

Install python or run on docker:

```bash
docker build -t python-container .
docker run -it -v "$(pwd)/scripts:/scripts" python-container
```

Then it's just python...

```bash
py hello.py
```

Black formatter extension really good for formatting python code. For VS Code go to settings Ctrl+, and search formatting and select the formatter and also check format on save.
