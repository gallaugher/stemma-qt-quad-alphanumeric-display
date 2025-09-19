import time
import board
import busio
from adafruit_ht16k33.segments import Seg14x4

# Create I2C connection
i2c = busio.I2C(board.SCL, board.SDA)
display = Seg14x4(i2c)

def scroll_text(text, speed=0.3, loops=1, padding=True):
    """
    Scroll text across the 4-character display

    Args:
        text (str): The text to scroll
        speed (float): Delay between scroll steps in seconds (default: 0.3)
        loops (int): Number of times to repeat the scroll (default: 1)
        padding (bool): Add spaces at start/end for smoother scrolling (default: True)
    """
    if padding:
        # Add spaces so text scrolls in and out smoothly
        padded_text = "    " + text + "    "
    else:
        padded_text = text

    # If text is 4 characters or less, just display it
    if len(padded_text) <= 4:
        display.print(padded_text.ljust(4))
        time.sleep(speed * 3)  # Display longer since no scrolling
        return

    # Scroll the text
    for loop in range(loops):
        for i in range(len(padded_text) - 3):
            display.print(padded_text[i:i + 4])
            time.sleep(speed)


def scroll_text_continuous(text, speed=0.3):
    """
    Scroll text continuously until interrupted
    Press Ctrl+C to stop

    Args:
        text (str): The text to scroll
        speed (float): Delay between scroll steps in seconds
    """
    padded_text = "    " + text + "    "

    print(f"Scrolling '{text}' continuously...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            for i in range(len(padded_text) - 3):
                display.print(padded_text[i:i + 4])
                time.sleep(speed)
    except KeyboardInterrupt:
        print("\nScrolling stopped!")

display.brightness = 0.8

# Change this string to whatever you want to scroll!
my_message = "HEY THERE, LEGEND. THIS IS THE STEMMA-QT RED 0.54 INCH QUAD ALPHANUMERIC DISPLAY"
# Try some other messages
messages = [
    "DEMO TEXT",
    "1234567890",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "COOL, RIGHT?"
]

print("Scrolling display running!")
while True:
    # Basic scroll - change the text here!
    scroll_text(my_message)
    # Different speeds and repetitions
    scroll_text("FAST", speed=0.1, loops=2)
    scroll_text("SLOW", speed=0.8, loops=1)

    for message in messages:
        scroll_text(message, speed=0.3, loops=1)


