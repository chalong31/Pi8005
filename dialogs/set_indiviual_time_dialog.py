from PyQt5.QtWidgets import QDialog
from ui.set_indiviual_time import Ui_Set_indiviual_time
from dialogs.set_clock_dialog import SetClockDialog

class SetIndiviualTimeDialog(QDialog, Ui_Set_indiviual_time):

    def __init__(self, p_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화

    def set_cancel(self):
        self.reject()

    def send_time(self):
        time_map = {
            1: self.btn_set_indvd_time_1.text(),
            2: self.btn_set_indvd_time_2.text(),
            3: self.btn_set_indvd_time_3.text(),
            4: self.btn_set_indvd_time_4.text(),
            5: self.btn_set_indvd_time_5.text(),
            6: self.btn_set_indvd_time_6.text(),
            7: self.btn_set_indvd_time_7.text(),
            8: self.btn_set_indvd_time_8.text(),
            9: self.btn_set_indvd_time_9.text(),
            10: self.btn_set_indvd_time_10.text(),
            11: self.btn_set_indvd_time_11.text(),
            12: self.btn_set_indvd_time_12.text(),
            13: self.btn_set_indvd_time_13.text(),
            14: self.btn_set_indvd_time_14.text(),
            15: self.btn_set_indvd_time_15.text()
        }
        return time_map

    def set_indvd_save(self):
        print("set_indvd_save")

        self.accept()

    def set_indvd_time_part(self):
        print("set_indvd_time_part")

        def make_time(min): # 분 -> 시간
            hours, minutes = divmod(min, 60)  # 시간과 분으로 나눔
            str_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"  # 00:00 형식으로 변환

            return str_time

        def make_min(time): # 시간 -> 분
            hours, minutes = map(int, time.split(":"))  # 시와 분을 정수로 변환
            total_minutes = hours * 60 + minutes  # 전체 분 계산

            return total_minutes

        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        btn_time_zone = clicked_button.objectName().split("_")[-1]  # 버튼의 objectName 가져오기
        time_arr = [] #개별시간 배열
        # 버튼 객체들을 딕셔너리에 매핑
        button_map = {
            1 : self.btn_set_indvd_time_1,
            2 : self.btn_set_indvd_time_2,
            3 : self.btn_set_indvd_time_3,
            4 : self.btn_set_indvd_time_4,
            5 : self.btn_set_indvd_time_5,
            6 : self.btn_set_indvd_time_6,
            7 : self.btn_set_indvd_time_7,
            8 : self.btn_set_indvd_time_8,
            9 : self.btn_set_indvd_time_9,
            10 : self.btn_set_indvd_time_10,
            11 : self.btn_set_indvd_time_11,
            12 : self.btn_set_indvd_time_12,
            13 : self.btn_set_indvd_time_13,
            14 : self.btn_set_indvd_time_14,
            15 : self.btn_set_indvd_time_15,
        }

        # 버튼 텍스트를 배열에 집어 넣기
        for key, value in button_map.items():
            if value.text() != "_ _ : _ _":
                t_minutes = make_min(value.text())
                time_arr.append(t_minutes)

        # 시간입력기에서 입력한 값을 배열에 추가하기
        dialog = SetClockDialog()
        if dialog.exec_() == QDialog.Accepted:
            if button_map[int(btn_time_zone)].text() == "_ _ : _ _":
                if dialog.send_time() != "_ _ : _ _":
                    t_minutes = make_min(dialog.send_time())
                    time_arr.append(t_minutes)
            else:
                #print("제거전:" + str(time_arr))
                t_minutes = make_min(button_map[int(btn_time_zone)].text())
                time_arr.remove(t_minutes)
                #print("제거후:" + str(time_arr))
                if dialog.send_time() != "_ _ : _ _":
                    t_minutes = make_min(dialog.send_time())
                    time_arr.append(t_minutes)
                    #print("추가후:" + str(time_arr))

        # 시간 배열 중복제거 후 정렬
        time_arr = sorted(set(time_arr))
        #print("중복제거:" + str(time_arr))

        # 화면 초기화
        for i in range(len(button_map)):
            button_map[i + 1].setText("_ _ : _ _")

        # 화면에 표시하기
        for i in range(len(time_arr)):
            str_time = make_time(time_arr[i])
            button_map[i+1].setText(str_time)