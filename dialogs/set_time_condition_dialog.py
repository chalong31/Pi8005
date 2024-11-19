import re

from PyQt5.QtWidgets import QDialog
from ui.set_time_condition import Ui_Set_time_condition
from dialogs.set_indiviual_time_dialog import SetIndiviualTimeDialog
from dialogs.set_certain_time_dialog import SetCertainTimeDialog
from dialogs.set_number_dialog import SetNumberDialog

class SetTimeConditionDialog(QDialog, Ui_Set_time_condition):

    new_time_condition_set = ""
    time_map = {}

    def __init__(self, p_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        self.p_no = p_no
        self.btn_mon.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_tue.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_wen.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_thu.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_fri.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_sat.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_sun.setStyleSheet("background-color: rgb(85, 255, 255);")

    def set_cancel(self):
        self.reject()

    def send_text(self):
        return self.new_time_condition_set

    def send_map(self):
        return self.time_map

    def set_time_con_indvd(self):
        print("set_time_con_indvd")
        self.new_time_condition_set = "개별시간"
        dialog = SetIndiviualTimeDialog(self.p_no)
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_time():
                self.time_map = dialog.send_time()
            self.accept()

    def set_time_con_certain(self):
        print("set_time_con_certain")
        self.new_time_condition_set = "일정시간"
        dialog = SetCertainTimeDialog(self.p_no)
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_time():
                self.time_map = dialog.send_time()
        self.accept()

    def set_time_con_light(self):
        print("set_time_con_light")
        self.new_time_condition_set = "광량"+"\n"+self.btn_set_irrigation_time_8.text()
        self.accept()

    def set_time_con_j(self):
        print("set_time_con_j")
        dialog = SetNumberDialog(self.p_no, "set_j", "", "")
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num():
                self.btn_set_irrigation_time_8.setText(dialog.send_num() + "J/cm2")

    def set_time_con_humid(self):
        print("set_time_con_humid")
        self.new_time_condition_set = "지습"+"\n"+self.btn_set_irrigation_time_7.text()
        self.accept()

    def set_time_con_h_per(self):
        print("set_Time_con_h_per")
        dialog = SetNumberDialog(self.p_no, "set_h", "", "")
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num():
                self.btn_set_irrigation_time_7.setText(dialog.send_num() + "%")

    def click_day_of_week(self):
        print("click_day_of_week")

        def get_background_color(style_sheet):
            # 16진수 색상 코드 또는 rgb() 형식을 모두 탐지하는 정규식
            match = re.search(r'background-color:\s*(#[0-9a-fA-F]{6}|rgb\(\d{1,3},\s*\d{1,3},\s*\d{1,3}\));',
                              style_sheet)
            if match:
                return match.group(1)  # 색상 코드 반환
            return "No color found"

        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        if get_background_color(clicked_button.styleSheet()) == "rgb(85, 255, 255)":
            clicked_button.setStyleSheet("background-color: #e1e1e1;  /* 버튼 배경색 */")
        else:
            clicked_button.setStyleSheet("background-color: rgb(85, 255, 255);  /* 버튼 배경색 */")
