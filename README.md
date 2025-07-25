# simrender 🎬

A Python package for easily rendering robotic simulation environments to a web-ready (GLTF) format, including animated episodes for visualization and analysis. It also supports easy rendering to notebook cells in Jupyter and Marimo.

## Features

- 🎯 **GLB Export**: Export static scenes and animated sequences to industry-standard GLB format
- 🎮 **Gymnasium Integration**: Automatic support for Gymnasium environments with `InteractiveRenderWrapper`
- 📊 **Animation Recording**: Capture animated episodes with configurable capture frame rates
- 📕 **Notebook Support**: Rendering wrapper classes can be displayed in Jupyter/Marimo notebooks out of the box

### Simulator Support

- [x] MuJoCo
- [ ] MJX/MuJoCo Warp
- [ ] Newton
- [ ] Isaac Sim
- [ ] Isaac Gym (legacy)

## Installation

```bash
pip install simrender
```

## Usage

### Gymnasium Environments

Wrap any Gymnasium environment to enable GLB export:

```python
import gymnasium as gym
from simrender.gym import InteractiveRenderWrapper

# Create and wrap environment
env = gym.make("Ant-v5")
env = InteractiveRenderWrapper(env)

# Record an animated episode
with env.animation(fps=30):
    obs, _ = env.reset(seed=42)
    for _ in range(1000):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        if terminated or truncated:
            break

# Save to GLB file
env.save("episode.glb")

# or, display it if running in a notebook cell
env
```

### MuJoCo Models

For direct MuJoCo model rendering:

```python
import mujoco
from simrender.mujoco import MujocoRender

# Load MuJoCo model
model = mujoco.MjModel.from_xml_file("scene.xml")
data = mujoco.MjData(model)

# Create renderer
render = MujocoRender(model)

# Single frame render
mujoco.mj_step(model, data)
render.render(data)
render.save("single_frame.glb")

# Animated sequence
with render.animation(fps=10):
    for i in range(3000):
        mujoco.mj_step(model, data)
        render.render(data)

render.save("animated_sequence.glb")

# or, display it if running in a notebook cell
render
```

## File Format

The exported GLB files are compatible with:
- 🌐 Web browsers (Three.js, Babylon.js)
- 🎨 3D modeling software (Blender, Maya, 3ds Max)
- 🎮 Game engines (Unity, Unreal Engine)
- 📱 AR/VR applications
- Anything that supports GLTF/GLB

## License

This project is dual-licensed under MIT and Apache 2.0 licenses. You may choose either license for your use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

