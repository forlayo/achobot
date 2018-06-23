# Acho-bot
> Auto aim bot using neural network.

It uses OpenCV 3.3 dnn module + petrained MobileNetSSD caffemodel to detect entities with person form on screen and then moves the cursor over them and does click. It's a playground idea to create an auto-aim bot for games like Fornite.

## Getting Started

### Prerequisites

- Python3

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

## Built With

- [PyCharm](https://www.jetbrains.com/pycharm/) as IDE
- [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) to struggling with libraries per project.

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us. 

## License

This project is licensed under the Apache License - see the [LICENSE](./LICENSE) file for details 

## Acknowledgments

- **Aniruddh Chandratre** - Works are based on his repository: https://github.com/C-Aniruddh/realtime_object_recognition