# phys_sim

A 2D physics simulator built with Python and pygame-ce. Currently simulates a rod hanging from a pivot point that you can move left and right.

## Controls

| Key | Action |
|-----|--------|
| A / ← | Move pivot left |
| D / → | Move pivot right |
| Escape | Quit |

## Installation (Windows)

### 1. Install Python

Download and install Python 3.11 or later from [python.org](https://www.python.org/downloads/windows/).

> During installation, check **"Add python.exe to PATH"**.

### 2. Download this repository

Click the green **Code** button on this page and choose **Download ZIP**, then extract it to a folder of your choice.

Or if you have Git installed:

```
git clone https://github.com/Mikecoward/phys_sim.git
cd phys_sim
```

### 3. Create a virtual environment

Open a terminal in the project folder (Shift+right-click → "Open in Terminal") and run:

```
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run

```
python main.py
```
