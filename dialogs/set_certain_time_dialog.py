from PyQt5.QtWidgets import QDialog
from ui.set_certain_time import Ui_Set_certain_time
from dialogs.set_clock_dialog import SetClockDialog
from dialogs.set_irrigation_time_dialog import SetIrrigationTimeDialog

class SetCertainTimeDialog(QDialog, Ui_Set_certain_time):

    def make_time(self, min):  # 분 -> 시간
        hours, minutes = divmod(min, 60)  # 시간과 분으로 나눔
        str_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"  # 00:00 형식으로 변환

        return str_time

    def make_min(self, time):  # 시간 -> 분
        hours, minutes = map(int, time.split(":"))  # 시와 분을 정수로 변환
        total_minutes = hours * 60 + minutes  # 전체 분 계산

        return total_minutes

    def __init__(self, p_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화

    def set_cancel(self):
        self.reject()

    def send_time(self):
        print("send_time")
        time_map = {}
        for i in range(15):
            time_map[i+1] = "_ _ : _ _"

        #print(self.btn_set_irrigation_3.text())
        start_time = self.make_min(self.btn_set_irrigation_3.text())
        end_time = self.make_min(self.btn_set_irrigation_5.text())
        if self.label_time_interval.text() == "_ _ : _ _":
            time_map[1] = self.make_time(start_time)
        else:
            if start_time != end_time:
                time_interval = int((end_time - start_time)/(int(self.btn_set_irrigation_6.text())-1))
            else:
                time_interval = 100000
            next_time = start_time
            for i in range(15):
                if next_time <= end_time:
                    time_map[i + 1] = self.make_time(next_time)
                else:
                    time_map[i + 1] = "_ _ : _ _"
                next_time = next_time + time_interval

        return time_map


    def set_certain_save(self):
        print("set_certain_save")
        if self.btn_set_irrigation_3.text() == "_ _ : _ _" or self.btn_set_irrigation_5.text() == "_ _ : _ _" or self.btn_set_irrigation_6.text() == "0":
            pass
        else:
            self.accept()

    def display_time_interval(self):
        if self.btn_set_irrigation_3.text() != "_ _ : _ _" and self.btn_set_irrigation_5.text() != "_ _ : _ _" and self.btn_set_irrigation_6.text() != "0":
            start_time = self.make_min(self.btn_set_irrigation_3.text())
            end_time = self.make_min(self.btn_set_irrigation_5.text())
            if self.btn_set_irrigation_6.text() != "1" and self.btn_set_irrigation_6.text() != "0":
                time_interval = int((end_time - start_time) / (int(self.btn_set_irrigation_6.text()) - 1))
                self.label_time_interval.setText(self.make_time(time_interval))
        else:
            self.label_time_interval.setText("_ _ : _ _")

    def time_change(self):
        if self.btn_set_irrigation_3.text() != "_ _ : _ _" and self.btn_set_irrigation_5.text() != "_ _ : _ _":
            if self.make_min(self.btn_set_irrigation_3.text()) > self.make_min(self.btn_set_irrigation_5.text()):
                prev_time = self.btn_set_irrigation_3.text()
                self.btn_set_irrigation_3.setText(self.btn_set_irrigation_5.text())
                self.btn_set_irrigation_5.setText(prev_time)

    def set_time_start(self):
        print("set_time_start")
        dialog = SetClockDialog()
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_time():
                self.btn_set_irrigation_3.setText(dialog.send_time())
            self.time_change()
            self.display_time_interval()

    def set_time_end(self):
        print("set_time_end")
        dialog = SetClockDialog()
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_time():
                self.btn_set_irrigation_5.setText(dialog.send_time())
            self.time_change()
            self.display_time_interval()

    def set_irrigation_time(self):
        print("set_irrigation_time")
        dialog = SetIrrigationTimeDialog()
        if dialog.exec_() == QDialog.Accepted:
            if dialog.get_value():
                self.btn_set_irrigation_6.setText(dialog.get_value())
            self.display_time_interval()