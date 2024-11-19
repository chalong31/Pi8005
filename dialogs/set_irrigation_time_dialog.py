from PyQt5.QtWidgets import QDialog
from ui.set_irrigation_time import Ui_Set_irrigation_time

class SetIrrigationTimeDialog(QDialog, Ui_Set_irrigation_time):

    clicked_num = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 초기화

    def click_cancel(self):
        print("click_cancel")
        self.reject()

    def get_value(self):
        return self.clicked_num

    def click_num(self):
        print("click_num")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        self.clicked_num = clicked_button.text()  # 버튼의 text 가져오기
        self.accept()