IP_ADDRESS = "192.168.1.151"
PORT = 9990
TIMEOUT_SECONDS = 5

ROUTING = {
    "streaming": {
        "OUTPUT_CHANNELS": [11],
        "INPUT_CHANNELS": [4, 5, 8, 9],
        "INTERVAL_SECONDS": 31
    },
    "portrait": {
        "OUTPUT_CHANNELS": [6, 7],
        "INPUT_CHANNELS": [6, 7],
        "INTERVAL_SECONDS": 23
    },
    "landscape": {
        "OUTPUT_CHANNELS": [4, 5, 8],
        "INPUT_CHANNELS": [4, 5, 8, 9],
        "INTERVAL_SECONDS": 47
    }
}
