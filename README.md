# Discord-Fetch-DMs

Discord-Fetch-DMs is a Python script that allows you to scrape direct messages (DMs) from a specified user on Discord. The script logs into your Discord account using a token, fetches the DMs from the specified user, and saves the messages and attachments to your local machine.

## Requirements

- Python 3.6+
- `discord.py-self` library

## Installation

1. Clone the repository or download the script files.
2. Install the required Python packages using `pip`:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python main.py
    ```

2. If you don't have a [token.txt](https://github.com/2034/Discord-Fetch-DMs/blob/main/token.txt) file, the script will prompt you to enter your Discord token. The token will be saved in [token.txt](https://github.com/2034/Discord-Fetch-DMs/blob/main/token.txt) for future use.
3. Enter the Discord ID of the user whose DMs you want to scrape when prompted.
4. The script will fetch the DMs and save the messages and attachments to a folder named after the user's Discord ID.

## Files

- [main.py](https://github.com/2034/Discord-Fetch-DMs/blob/main/main.py): The main script file.
- `requirements.txt`: The file containing the required Python packages.

## Example

```sh
python main.py
