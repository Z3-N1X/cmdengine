# 🎮 CMD Game Engine

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

</div>

<p align="center">
  <img src="https://i.imgur.com/placeholder.png" alt="CMD Game Engine Logo" width="200"/>
</p>

> A lightweight, powerful command-line game engine built with Python, bringing retro-style gaming to your terminal! 🚀

## ✨ Features

- 🎯 **Component-Based Architecture** - Flexible and modular game object system
- 🎨 **ASCII Graphics Engine** - Create beautiful text-based visuals
- 🔄 **Real-time Rendering** - Smooth display updates and animations
- 📐 **Transform System** - Easy object positioning and movement
- 🎭 **Custom Sprite Support** - Design your own ASCII characters
- 🖥️ **Windows Console Optimization** - Perfect window sizing and display

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/gameEngine.git

# Navigate to the project directory
cd gameEngine

# Install dependencies
pip install pywin32
```

## 🎮 Usage Example

```python
from engine.modules import Object
from engine.modules.components.transform import Transform
from engine.varTypes.Vector2 import Vector2

# Create a game object
player = Object('Player', '@')
player_transform = Transform()
player_transform.position = Vector2(10, 5)
player.components.append(player_transform)
```

## 🏗️ Architecture

The engine is built on a component-based architecture:

- **Objects**: Base entities in the game world
- **Components**: Modular pieces that add functionality
  - `Transform`: Handles position and movement
  - More components coming soon!
- **Vector2**: 2D vector implementation for positions and movements

## 🔧 Configuration

Customize your game window by adjusting these parameters in `engine/main.py`:

```python
TEXT_WIDTH = 100    # Width in characters
TEXT_HEIGHT = 10    # Height in characters
CHAR_WIDTH = 12.6   # Pixels per character
CHAR_HEIGHT = 30    # Pixels per line
```

## 🎨 Creating Game Objects

1. Create an object with a sprite character
2. Add a Transform component
3. Set the position
4. Add to the game loop

## 🛣️ Roadmap

- [ ] Collision detection system
- [ ] Input handling
- [ ] Sound effects support
- [ ] Scene management
- [ ] Particle systems
- [ ] UI components

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
  Made with ❤️ and ☕ by Your Name
</div>
