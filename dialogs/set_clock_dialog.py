from PyQt5.QtWidgets import QDialog
from ui.set_clock import Ui_Set_clock

class SetClockDialog(QDialog, Ui_Set_clock):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 초기화

    def set_cancel(self):
        self.reject()

    def click_time_save(self):
        print("set_num_save")
        if self.label_time_1.text() == '_' and self.label_time_2.text() == '_' and self.label_time_3.text() == '_' and self.label_time_4.text() == '_':
            self.accept()
        elif self.label_time_1.text() == '_' or self.label_time_2.text() == '_' or self.label_time_3.text() == '_' or self.label_time_4.text() == '_':
            pass
        else:
            self.accept()

    def send_time(self):
        send_text = self.label_time_1.text() + self.label_time_2.text() + ":" + self.label_time_3.text() + self.label_time_4.text()
        if self.label_time_1.text() == '_' and self.label_time_2.text() == '_' and self.label_time_3.text() == '_' and self.label_time_4.text() == '_':
            return "_ _ : _ _"
        else:
            return send_text

    def click_time_back(self):
        print("click_num_back")
        if self.label_time_4.text() != "_":
            self.label_time_4.setText("_")
        elif self.label_time_3.text() != "_":
            self.label_time_3.setText("_")
        elif self.label_time_2.text() != "_":
            self.label_time_2.setText("_")
        elif self.label_time_1.text() != "_":
            self.label_time_1.setText("_")

    def click_time_clear(self):
        print("click_num_clear")
        self.label_time_1.setText("_")
        self.label_time_2.setText("_")
        self.label_time_3.setText("_")
        self.label_time_4.setText("_")

    def click_time(self):
        print("click_num")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        button_text = clicked_button.text()  # 버튼의 objectName 가져오기
        if self.label_time_1.text() == "_":
            if button_text == "0" or button_text == "1" or button_text == "2":
                self.label_time_1.setText(button_text)
        elif self.label_time_2.text() == "_":
            if self.label_time_1.text() == "2":
                if button_text == "0" or button_text == "1" or button_text == "2" or button_text == "3":
                    self.label_time_2.setText(button_text)
            else:
                self.label_time_2.setText(button_text)
        elif self.label_time_3.text() == "_":
            if button_text != "6" and button_text != "7" and button_text != "8" and button_text != "9":
                self.label_time_3.setText(button_text)
        elif self.label_time_4.text() == "_":
            self.label_time_4.setText(button_text)