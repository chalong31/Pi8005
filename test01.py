import sys
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
# from setuptools.extern import names

from ui.Pi8005_menu import Ui_MainWindow  # 변환된 파일에서 UI 클래스 가져오기
from ui.p_setting import Ui_P_setting
from ui.set_flow import Ui_Set_flow
from ui.set_time_condition import Ui_Set_time_condition
from ui.set_certain_time import Ui_Set_certain_time
from ui.set_indiviual_time import Ui_Set_indiviual_time
from ui.set_number import Ui_Set_number
from ui.set_clock import Ui_Set_clock
from ui.set_irrigation_time import Ui_Set_irrigation_time

from PyQt5.QtCore import QTimer
from datetime import datetime




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        # 여기서 추가적인 초기화 작업을 수행할 수 있습니다.
        # 예를 들어, 버튼 클릭 시 액션을 설정할 수 있습니다.
        #self.pushButton.clicked.connect(self.on_button_click)

        # QTimer 설정: 1초마다 update_time 메서드 호출
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000밀리초(1초) 간격으로 실행

        # 처음 실행 시 즉시 시간 업데이트
        self.update_time()

    def p_setting_open(self):
        # 프로그램 설정창 열기
        print("open p")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        button_name = clicked_button.objectName()  # 버튼의 objectName 가져오기
        # 특정 문자열 위치를 뒤에서부터 찾기
        index = button_name.rfind("_")
        p_no = button_name[index+1:len(button_name)].strip()
        dialog = PSettingDialog(p_no)
        dialog.exec_()  # 다이얼로그 창 실행 (모달 모드)

    def update_time(self):
        # 현재 날짜와 시간 가져오기 및 포맷팅
        current_date = datetime.now().strftime("%Y년%m월%d일")
        current_time = datetime.now().strftime("%H시%M분%S초")

        # 라벨에 날짜와 시간 설정
        self.lblDispDate.setText(current_date)
        self.lblDIspTime.setText(current_time)

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

class SetFlowDialog(QDialog, Ui_Set_flow):

    new_flow_set = ""

    def __init__(self, p_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        self.p_no = p_no

    def set_cancel(self):
        self.reject()

    def send_text(self):
        return self.new_flow_set

    def set_flow_time(self):
        print("set_flow_time")
        self.new_flow_set = "시간(S)"
        self.accept()

    def set_flow_liter(self):
        print("set_flow_liter")
        self.new_flow_set = "유량(L)"
        self.accept()

    def set_flow_dripper(self):
        print("set_flow_dripper")
        self.new_flow_set = "드립퍼"+"\n["+self.btn_set_irrigation_unit_3.text()+"]"
        self.accept()

    def set_flow_unit(self):
        print("set_flow_unit")
        dialog = SetNumberDialog(self.p_no, "set_unit", "", "")
        if dialog.exec_() == QDialog.Accepted:
            if dialog.send_num():
                self.btn_set_irrigation_unit_3.setText(dialog.send_num())

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

class SetNumberDialog(QDialog, Ui_Set_number):

    num_text = ""

    def __init__(self, p_no, target, method, z_no):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        self.p_no = p_no
        self.target = target
        self.method = method
        self.z_no = z_no
        SetNumberDialog.num_text = ""
        self.btn_dot.hide()
        if target == "set_ec":
            self.btn_dot.show()
            self.label_number_zone.setText(z_no)
        elif target == "set_ph":
            self.btn_dot.show()
            self.label_number_zone.setText(z_no)
        elif target =="set_valve":
            self.label_number_unit.setText("%")
            self.label_number_zone.setText(z_no.upper()+"액")
        elif target == "set_flow_zone":
            self.label_number_zone.setText(z_no + "구역")
            if method == "시간(S)":
                self.label_number_unit.setText("초")
            elif method == "유량(L)":
                self.label_number_unit.setText("L")
            elif method == "드립퍼":
                self.label_number_unit.setText("cc")
        elif target == "set_unit":
            self.label_number_unit.setText("개")
        elif target == "set_j":
            self.label_number_zone.setText("광량")
            #self.label_number_unit.setText("J/cm2")
        elif target == "set_h":
            self.label_number_zone.setText("지습")
            self.label_number_unit.setText("%")
        elif target == "set_irrigation_time":
            self.label_number_unit.setText("번")

    def set_cancel(self):
        self.reject()

    def set_num_save(self):
        print("set_num_save")
        if SetNumberDialog.num_text != "":
            self.accept()
        else:
            self.reject()

    def send_num(self):
        if self.target == "set_ec" or self.target == "set_ph": # ec ph 설정시
            if SetNumberDialog.num_text[-1] != ".":
                send_text = str(float(SetNumberDialog.num_text))
                return send_text
            else:
                return None
        elif self.target == "set_valve" or self.target == "set_h": # 밸브 설정시
            if int(SetNumberDialog.num_text) >= 100:
                return "100"
            else:
                send_text = str(int(SetNumberDialog.num_text))
                return send_text
        else:
            return str(int(SetNumberDialog.num_text))


    def click_num_back(self):
        print("click_num_back")
        newtext = SetNumberDialog.num_text[:-1]
        SetNumberDialog.num_text = newtext
        self.label_number.setText(SetNumberDialog.num_text)

    def click_num_clear(self):
        print("click_num_clear")
        SetNumberDialog.num_text = ""
        self.label_number.setText(SetNumberDialog.num_text)

    def click_num(self):
        print("click_num")
        clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
        button_text = clicked_button.text()  # 버튼의 objectName 가져오기
        if self.target == "set_ec" or self.target == "set_ph":
            index = SetNumberDialog.num_text.find(".")
            if len(SetNumberDialog.num_text) < 2 : # 십의자리 초과하는 숫자 못쓰게
                SetNumberDialog.num_text += button_text
                self.label_number.setText(SetNumberDialog.num_text)
            elif "." in SetNumberDialog.num_text and len(SetNumberDialog.num_text[index+1:]) < 2:
                #소수점 둘째 자리까지 가져오기
                SetNumberDialog.num_text += button_text
                self.label_number.setText(SetNumberDialog.num_text)
        elif self.target == "set_irrigation_time":
            if len(SetNumberDialog.num_text) < 2 : # 십의자리 초과하는 숫자 못쓰게
                SetNumberDialog.num_text += button_text
                self.label_number.setText(SetNumberDialog.num_text)
        elif self.target == "set_valve" or self.target == "set_h":
            if len(SetNumberDialog.num_text) < 3 : # 백의자리 초과하는 숫자 못쓰게
                SetNumberDialog.num_text += button_text
                self.label_number.setText(SetNumberDialog.num_text)
        else :
            if len(SetNumberDialog.num_text) < 4:  # 천의자리 초과하는 숫자 못쓰게
                SetNumberDialog.num_text += button_text
                self.label_number.setText(SetNumberDialog.num_text)

    def click_dot(self):
        print("click_dot")
        if SetNumberDialog.num_text == "" or SetNumberDialog.num_text[-1] == "." or "." in SetNumberDialog.num_text:
            return
        else:
            clicked_button = self.sender()  # 클릭된 버튼 객체 가져오기
            button_text = clicked_button.text()  # 버튼의 objectName 가져오기
            SetNumberDialog.num_text += button_text
            self.label_number.setText(SetNumberDialog.num_text)

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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

