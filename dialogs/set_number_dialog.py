from PyQt5.QtWidgets import QDialog
from ui.set_number import Ui_Set_number

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