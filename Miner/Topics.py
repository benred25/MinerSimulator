from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class Topics(QVBoxLayout):
    """
    Topics objects will be related to the glossary and hold links to the material
    """

    def __init__(self):
        super(Topics, self).__init__()
        self.layout = QVBoxLayout()

        self.definition = QLabel("After you search a term, info will appear here")
        self.definition.setFixedHeight(200)
        self.definition.setWordWrap(True)
        self.addWidget(self.definition)
        self.setAlignment(Qt.AlignTop)

    def getTopic(self, topic):
        """
        Takes in a topic and returns the info for that topic (a URL).
        :param topic: a String of a topic title
        :return: a list of info on the topic???
        """
        topics_dict = {
              "agent": ["https://www.investopedia.com/terms/a/agent.asp", "youtube-link"],
              "assets": ["https://www.investopedia.com/terms/s/stock.asp", "youtube-link"],
              "symbol": ["https://www.investopedia.com/terms/s/stocksymbol.asp", "youtube-link"],
              "volume": ["https://www.fool.com/knowledge-center/what-is-volume-in-stock-trading.aspx", "youtube-link"],
              "day range": ["https://www.investopedia.com/terms/r/range.asp", "youtube-link"],
              "52 week range": ["https://www.investopedia.com/terms/1/52-week-range.asp", "youtube-link"],
              "dividend": ["https://www.investopedia.com/terms/s/stockdividend.asp", "youtube-link"],
              "yield": ["https://www.fool.com/knowledge-center/dividend-yield.aspx", "youtube-link"],
              "closing price": ["https://www.investopedia.com/terms/c/closingprice.asp", "youtube-link"],
              "open price": ["https://www.investopedia.com/terms/o/openingprice.asp", "youtube-link"],
              "stock categories": ["https://economictimes.indiatimes.com/definition/categories", "youtube-link"],
              "sector": ["https://www.investopedia.com/terms/s/sector-breakdown.asp", "youtube-link"],
              "bear market": ["https://www.investopedia.com/terms/b/bearmarket.asp", "youtube-link"],
              "bonds": ["https://www.investopedia.com/terms/b/bond.asp", "youtube-link"],
              "bull market": ["https://www.investopedia.com/terms/b/bullmarket.asp", "youtube-link"],
              "business day": ["https://www.investopedia.com/terms/b/business-day.asp", "youtube-link"],
              "capital": ["https://www.investopedia.com/terms/c/capital.asp", "youtube-link"],
              "certificate": ["https://www.investopedia.com/terms/s/stockcertificate.asp", "youtube-link"],
              "equities": ["https://www.investopedia.com/terms/e/equity.asp", "youtube-link"],
              "frequency": ["https://www.moneycontrol.com/glossary/stocks/frequency_3404.html", "youtube-link"],
              "growth stock": ["https://www.fool.com/investing/how-to-find-a-growth-stock.aspx", "youtube-link"],
              "index": ["https://www.investopedia.com/terms/i/index.asp", "youtube-link"],
              "inflation": ["https://www.investopedia.com/terms/i/inflation.asp", "youtube-link"],
              "liquidity": ["https://www.investopedia.com/terms/l/liquidity.asp", "youtube-link"],
              "mutual fund": ["https://www.investopedia.com/terms/m/mutualfund.asp", "youtube-link"],
              "option": ["https://www.investopedia.com/terms/o/option.asp", "youtube-link"],
              "penny stock": ["https://www.investopedia.com/terms/p/pennystock.asp", "youtube-link"],
              "portfolio": ["https://www.investopedia.com/terms/p/portfolio.asp", "youtube-link"],
              "preferred stock": ["https://www.investopedia.com/terms/p/preferredstock.asp", "youtube-link"],
              "profit": ["https://www.investopedia.com/terms/p/profit.asp", "youtube-link"],
              "risk": ["https://www.investopedia.com/terms/r/risk.asp", "youtube-link"],
              "securities": ["https://www.investopedia.com/terms/s/security.asp", "youtube-link"],
              "transactions": ["https://www.investopedia.com/terms/t/transaction.asp", "youtube-link"],
              "volatility": ["https://www.investopedia.com/terms/v/volatility.asp", "youtube-link"],
              "venture capital": ["https://www.investopedia.com/terms/v/venturecapital.asp.", "youtube-link"]
              }

        try:
            self.definition.setText(topics_dict[topic[0]])
        except:
            self.definition.setText("The term " + topic + " was not found.")
