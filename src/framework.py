import tkinter as tk


class ClickerGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("クリッカーゲーム")
        self.geometry("400x200")  # ウィンドウのサイズを400x200に設定
        self.score = 0
        self.score_label = tk.Label(
            self, text=f"スコア: {self.score}", font=('Helvetica', 14))
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(
            self, text="クリック！", command=self.increment_score, font=('Helvetica', 14))
        self.click_button.pack(pady=20)

    def increment_score(self):
        self.score += 1
        self.score_label.config(text=f"スコア: {self.score}")


def main():
    app = ClickerGame()
    app.mainloop()


if __name__ == "__main__":
    main()
