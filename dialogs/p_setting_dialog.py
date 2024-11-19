from PyQt5.QtWidgets import QDialog
from ui.p_setting import Ui_P_setting
from dialogs.set_flow_dialog import SetFlowDialog
from dialogs.set_time_condition_dialog import SetTimeConditionDialog
from dialogs.set_number_dialog import SetNumberDialog

class PSettingDialog(QDialog, Ui_P_setting):
    def __init__(self, p_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        # UI 초기 숨김
        self.frame_set_flow_1.hide()
        self.frame_set_flow_2.hide()
        self.frame_set_time_1.hide()
        self.frame_set_time_2.hide()

        self.p_no = p_no

        # 타이틀 표시
        self.lable_p_set_main.setText(p_no + "번 프로그램 설정")

    def set_cancel(self):
        self.close()

    def view_yang_set(self):
        print("view_yang_set")
        self.frame_set_yang_1.show()
        self.frame_set_yang_2.show()
        self.frame_set_flow_1.hide()
        self.frame_set_flow_2.hide()
        self.frame_set_time_1.hide()
        self.frame_set_time_2.hide()

    def view_flow_set(self):
        print("view_flow_set")
        self.frame_set_yang_1.hide()
        self.frame_set_yang_2.hide()
        self.frame_set_flow_1.show()
        self.frame_set_flow_2.show()
        self.frame_set_time_1.hide()
        self.frame_set_time_2.hide()

    def view_time_set(self):
        print("view_time_set")
        self.frame_set_yang_1.hide()
        self.frame_set_yang_2.hide()
        self.frame_set_flow_1.hide()
        self.frame_set_flow_2.hide()
        self.frame_set_time_1.show()
        self.frame_set_time_2.show()

    def set_ec(self, p_no):
        print("set_ec")
        dialog = SetNumberDialog(p_no,"set_ec","","EC")
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num() and dialog.send_num() != "":
                self.btn_set_ec.setText(dialog.send_num())

    def set_ph(self):
        print("set_ph")
        dialog = SetNumberDialog(self.p_no,"set_ph","","pH")
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num() and dialog.send_num() != "":
                self.btn_set_ph.setText(dialog.send_num())

    def set_valve(self):
        print("set_valve")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        btn_valve = clicked_button.objectName()[-1]  # 버튼의 objectName 가져오기
        dialog = SetNumberDialog(self.p_no, "set_valve", "", btn_valve)
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num() and dialog.send_num() != "":
                # 버튼 객체들을 딕셔너리에 매핑
                button_map = {
                    'a': self.btn_set_valve_a,
                    'b': self.btn_set_valve_b,
                    'c': self.btn_set_valve_c,
                    'd': self.btn_set_valve_d,
                    'p': self.btn_set_valve_p
                }
                # 해당 버튼 객체에 접근하여 텍스트 설정
                if btn_valve in button_map:
                    button_map[btn_valve].setText(dialog.send_num() + "%")

    def set_flow(self):
        print("set_flow")
        dialog = SetFlowDialog(self.p_no)
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_text():
                self.btn_set_irrigation.setText(dialog.send_text())

    def set_time_condition(self):
        print("set_time_condition")
        dialog = SetTimeConditionDialog(self.p_no)
        time_dic = {
            1: self.label_time_1,
            2: self.label_time_2,
            3: self.label_time_3,
            4: self.label_time_4,
            5: self.label_time_5,
            6: self.label_time_6,
            7: self.label_time_7,
            8: self.label_time_8,
            9: self.label_time_9,
            10: self.label_time_10,
            11: self.label_time_11,
            12: self.label_time_12,
            13: self.label_time_13,
            14: self.label_time_14,
            15: self.label_time_15,
        }
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_text() == "개별시간" or dialog.send_text() == "일정시간":
                self.btn_set_time_condition.setText(dialog.send_text())
                for i in dialog.send_map():
                    if dialog.send_map()[i] != "_ _ : _ _":
                        time_dic[i].setText(dialog.send_map()[i])
                    else:
                        time_dic[i].setText("")
            elif dialog.send_text():
                for i in range(len(time_dic)):
                    time_dic[i+1].setText("")
                self.btn_set_time_condition.setText(dialog.send_text())

    def set_flow_zone(self, p_no):
        print("set_flow_zone")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        btn_flow_zone = clicked_button.objectName().split("_")[-1]  # 버튼의 objectName 가져오기
        irrigation_method = self.btn_set_irrigation.text()
        dialog = SetNumberDialog(p_no, "set_flow_zone", irrigation_method, btn_flow_zone)
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num() and dialog.send_num() != "":
                # 버튼 객체들을 딕셔너리에 매핑
                button_map = {
                    "1": self.btn_set_flow_zone_1,
                    "2": self.btn_set_flow_zone_2,
                    "3": self.btn_set_flow_zone_3,
                    "4": self.btn_set_flow_zone_4,
                    "5": self.btn_set_flow_zone_5,
                    "6": self.btn_set_flow_zone_6,
                    "7": self.btn_set_flow_zone_7,
                    "8": self.btn_set_flow_zone_8,
                    "9": self.btn_set_flow_zone_9,
                    "10": self.btn_set_flow_zone_10,
                    "11": self.btn_set_flow_zone_11,
                    "12": self.btn_set_flow_zone_12,
                    "13": self.btn_set_flow_zone_13,
                    "14": self.btn_set_flow_zone_14,
                    "15": self.btn_set_flow_zone_15,
                    "16": self.btn_set_flow_zone_16,
                }
                # 해당 버튼 객체에 접근하여 텍스트 설정
                if btn_flow_zone in button_map:
                    button_map[btn_flow_zone].setText(dialog.send_num())