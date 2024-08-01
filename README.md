# XT-TradeBot 🤖🌐

Welcome to the XT-TradeBot repository! This project is a bilingual Telegram bot that enables users to trade on the XT.com exchange based on user signals. 🚀

## Features ✨

- **Bilingual Support**: The bot supports both English 🇺🇸 and Persian 🇮🇷 languages.
- **Real-time Trading**: Execute buy and sell orders on XT.com using user-provided signals.
- **Secure**: Utilizes the XT.com API for secure trading.

## Installation 🛠️

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/XT-TradeBot.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd XT-TradeBot
    ```
3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration ⚙️

1. **Set up your environment variables**:
    - `API_KEY`: Your XT.com API key.
    - `SECRET_KEY`: Your XT.com API secret key.
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.

2. **Create a `.env` file in the project directory** and add your keys:
    ```env
    API_KEY=your_xt_api_key
    SECRET_KEY=your_xt_secret_key
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    ```

## Usage 🚀

1. **Start the bot**:
    ```sh
    python bot.py
    ```

2. **Interact with the bot on Telegram**:
    - **/start**: The bot will greet you and allow you to choose your language.
    - **Enter your trading signal**: Follow the format to provide signals, e.g., `BINANCE_BTCUSDT LONG Limit $58000 Lev 4 Value 85 SL 54000 TP 66000`.

   ### Example Signal Structure 📊
   ```
   BINANCE_BTCUSDT
   LONG Limit
   $58000
   Lev 4
   Value 85
   SL 54000
   TP 66000
   ```

   - **Symbols**: Start with the market symbol like `BINANCE_BTCUSDT`.
   - **Direction & Order Type**: Mention if it's `LONG` or `SHORT` and `Limit` or `Market`.
   - **Price**: Specify the price (e.g., `$58000`).
   - **Leverage**: Define the leverage (e.g., `Lev 4`).
   - **Value**: State the value in USD (e.g., `Value 85`).
   - **Stop Loss (SL)** and **Take Profit (TP)**: Set these as needed (e.g., `SL 54000`, `TP 66000`).

## Contributing 🤝

We welcome contributions! Feel free to open issues, suggest features, and submit pull requests. Let's enhance trading experiences together! 💪

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- A big thank you to the developers of `pyxt` and `python-telegram-bot` for their excellent libraries!
- Special thanks to the XT.com team for providing a comprehensive API for trading.

## Contact 📬

For any queries or issues, please contact us at [your.email@example.com](mailto:your.email@example.com).

---

### Important Notes 🚨

1. **Security**: Ensure your API keys are kept secure and not exposed publicly.
2. **Testing**: Always test your bot thoroughly in a safe environment before using it with real funds.
3. **Compliance**: Make sure your use of the bot complies with all relevant regulations and exchange policies.

Happy Trading! 📈📉