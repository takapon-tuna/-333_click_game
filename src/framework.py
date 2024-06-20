import tkinter as tk  # tkinterモジュールをインポート

# ゲームのモデルクラス


class GameModel:
    def __init__(self):
        self.score = 0  # スコアの初期値
        self.click_point = 1  # クリックごとのスコア増加量

    def increment_score(self):
        self.score += self.click_point  # スコアを増加させるメソッド


# ゲームのビュークラス（tkinterのTkクラスを継承）
class GameView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # コントローラーの参照を保持
        self.title("クリッカーゲーム")  # ウィンドウのタイトル
        self.geometry("640x360")  # ウィンドウのサイズ
        self.create_widgets()  # ウィジェットの作成

    def create_widgets(self):
        # スコア表示用のラベル
        self.score_label = tk.Label(
            self, text=f"スコア: {self.controller.model.score}", font=('Helvetica', 16))
        self.score_label.pack(pady=20)  # ラベルをウィンドウに配置

        # クリックボタン
        self.click_button = tk.Button(self, text="クリック！", command=self.controller.increment_score, font=(
            'Helvetica', 20), bg='blue', fg='white')
        self.click_button.pack(pady=20)  # ボタンをウィンドウに配置

    def update_score(self):
        self.score_label.config(
            text=f"スコア: {self.controller.model.score}")  # スコアラベルを更新


# ゲームのコントローラークラス
class GameController:
    def __init__(self, model, view):
        self.model = model  # モデルの参照を保持
        self.view = view  # ビューの参照を保持

    def increment_score(self):
        self.model.increment_score()  # モデルのスコアを増加
        self.view.update_score()  # ビューのスコア表示を更新


def main():
    model = GameModel()  # モデルオブジェクトの作成
    controller = GameController(model, None)  # 一時的にviewをNoneで初期化
    view = GameView(controller=controller)  # GameViewにcontrollerを設定
    controller.view = view  # GameControllerにviewを設定
    view.mainloop()  # イベントループの開始


if __name__ == "__main__":
    main()  # メイン関数の呼び出し
