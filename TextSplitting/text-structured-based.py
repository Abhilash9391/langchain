from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Trading is the process of buying and selling financial assets such as stocks, currencies, commodities, or cryptocurrencies with the aim of making a profit from price movements. Traders analyze market trends using technical indicators, charts, and economic news to make informed decisions. Trading can be short-term, such as day trading and swing trading, or long-term, such as position trading. While trading offers opportunities for financial growth, it also involves significant risk due to market volatility. Successful trading requires discipline, risk management, continuous learning, and a well-defined strategy rather than relying on emotions or speculation alone.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)