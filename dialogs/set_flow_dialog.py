from PyQt5.QtWidgets import QDialog
from ui.set_flow import Ui_Set_flow
from dialogs.set_number_dialog import SetNumberDialog

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