# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the simulator
python main.py
```

## Architecture

Single-file pygame app (`main.py`). The simulation loop runs at 60 FPS using `clock.tick(FPS)` and accumulates elapsed time `t` to drive all motion.

**Pivot motion** is driven by held keyboard input (A/D or left/right arrows). `PIVOT_SPEED` (pixels/sec) controls how fast it moves. The pivot is clamped to the window bounds each frame.

**Rod** currently hangs rigidly straight down from the pivot. Pendulum swing physics (angle, angular velocity, torque) will be added later, at which point the rod endpoint will be computed from the pivot position plus a unit vector in the direction of the rod angle.

Constants at the top of the file control all tunable parameters (amplitude, frequency, rod length, colors).
