# Acho-bot
Auto aim bot using neural network, done in python.

It uses OpenCV 3.3 dnn module + petrained MobileNetSSD caffemodel to detect entities with person form on screen and then moves the cursor over them and does click. It's a playground idea to create an auto-aim bot for games like Fornite.

## Getting Started

### Prerequisites

- Python3

### Recommendations

- PyCharm as IDE
- Virtualenv

### Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 achobot.py
```

A window will appear that's doing screengrabs, and over these screen grabs are looking for persons. While a person is found then it clicked it. You can even check it opening a photo or so with a guy into.  

**Note:** To quit, having the bot window focused, press 'q'. 

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us. 

## Acknowledgments

- **Aniruddh Chandratre** - Works are based on his repository: https://github.com/C-Aniruddh/realtime_object_recognition