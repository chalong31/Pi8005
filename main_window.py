from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from datetime import datetime
from ui.Pi8005_menu import Ui_MainWindow
from dialogs.p_setting_dialog import PSettingDialog


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