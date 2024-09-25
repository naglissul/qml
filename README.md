# Quantum Computing and Machine Learning

2024 spring/summer/autumn.

Repository for self learning QC and QML to prepare for bachelor thesis and/or including myself in the work of Vilnius University quantum computing study group, masters studies and in general out of interest.

## Tech

- Python
- Qiskit

HSI classification: spectral scikit-learn numpy

## Content

Resources: [Quantum Soar channel on YouTube](https://www.youtube.com/@quantum-soar), Chuand and Nielsen Quantum Computation adn QUantum Information.

Cheatsheet: [LaTex](./QuantumSoar-cheatsheet.tex) and [PDF](./QuantumSoar-cheatsheet.pdf)

HSI examples from Harvard: https://vision.seas.harvard.edu/hyperspec/download.html

HSI from gov: https://earthexplorer.usgs.gov/

https://github.com/spectralpython/sample-data/

http://www.spectralpython.net/index.html

## Coding setup

Install python with packages mentioned in Dockerfile or run on docker:

```bash
docker build -t python-container .
docker run -it -v "$(pwd)/scripts:/scripts" python-container
```

Then it's just python...

```bash
py qiskit/hello.py
```

Black formatter extension really good for formatting python code. For VS Code go to settings Ctrl+, and search formatting and select the formatter and also check format on save.
