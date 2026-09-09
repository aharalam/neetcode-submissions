class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # Remove any forward history
        self.history = self.history[:self.current + 1]

        # Add the new page
        self.history.append(url)

        # Move current position to the new page
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back, but don't go before the homepage
        self.current = max(0, self.current - steps)

        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward, but don't go past the latest page
        self.current = min(len(self.history) - 1, self.current + steps)

        return self.history[self.current]