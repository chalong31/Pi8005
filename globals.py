# 프로그램 선택 변수

pro_sel = 0 # 선택 프로그램
#select_pro = 0 # ?

pro_onoff = [] # 프로그램 O,X
pro_flag = []  # 프로그램 플래그
flag_working_num = 0 # 0:정지, 1:개별시간, 2:일시정지, 3:광량, 4:지습, 5:수동작동

set_lgt_num = [] # 광량 설정
set_ph_num = [] # pH set 숫자
set_ec_num = [] # EC set 숫자
set_soil_num = [] # 지습 센서 설정
sel_ph_p = [] # pH 밸브 %
sel_yang_p = [[]] # 양액 밸브 선택 %
use_soil_sensor = []

day_set = [[]] # 요일 설정

wk_tms = [[]] # 작동하는 시간(시*60+분) - 시작, 종료, 간격
#wk_tms_m = [[]] # 작동하는 시간 - 분 (일정시간)
wk_tmi_no = [[]] # 일정시간 횟수
wk_tmi = [[]] # 작동하는 시간 - 시간 (개별시간)
#wk_timi_m = [[]] # 작동하는
#wk_tmi = [] # 개별 혼합에서 모두 사용
#wk_tmi_pro = [] # 혼합에서 시간과 함께 프로그램 번호 기억

f_light_start_time = [] # 광량 선택시 시작시간 적용 여부(기본적으로 적용됨) = 1
f_lgt_least_working = [] # 최소광량 작동 선택 여부 = 0
lgt_least_working = [] # 최대광량 시간 설정 = 0

sum_cur_lgt = [] # 현재 적산광량
start_sum_lgt = [] # 적산광량 시작
total_sum_lgt = []
cur_soil_humi = [] # 현재 지습

kws_sel = [] # 관수밸브 선택
kws_tm_l = [[]] # 관수밸브 작동 시간-분
sel_valb_g = [] # 밸브그룹선택

# 전체 시간 배열
tol_list_time = [] # 작업 시간 리스트
tol_pro_sel = [] # 프로그램 선택 num
tol_worked = [] # 작업여부 1:앞으로 할 작업, 0:이미 한 작업
tol_kwan_num = 0 # 전체 관수 횟수

set_auto_run = 1 # 0:자동실행 정지, 1:자동실행

cur_chk_time = 0

chk_lgt_step_time = [] # 광량설정시 시간간격 작동을 위한 변수

# dynamic 광량 설정 변수
flag_sel_var_time = [[]]
set_var_LGT_time = [[]]
set_var_LGT_value = [[]]
set_var_watering_rate = [[]]
set_var_time_step = [[]]
set_var_time_min = [[]]

# 릴레이 동작 체크
f_chk_wonsu = 0 # 원수
f_chk_kwansu = 0 # 관수
f_chk_warn = 0 # 경고
f_chk_ph = 0 # ph벨브
f_chk_yang = [] # ec 벨브
f_chk_valb = [] # 전자벨브
f_chk_clean = 0 # ?
f_chk_filter = 0 # ?

# 양액조정변수
ph_dev = 0.0 # ph 편차
ec_dev = 0.0 # ec 편차
soil_dev = 0.0 # 지습 편차
ec_low = 0.0 # 
lgt_dev = 0 # 광량 편차
mul_litt = 0 # 유량조정
ph_con = 0 # 산 or 염
cont_ecv = 0.0 # 양액 조정
cont_phv = 0.0 # 산 조정

stir_sel = 0 # 교반 선택
stir_time = 0 # 교반 시간
stir_sec = 0 # 교반 초

# 경고 관련
wnl_ph = 0.0 # ph 경고 하한
wnh_ph = 0.0 # ph 경고 상한
wnl_ec = 0.0 # ec 경고 하한
wnh_ec = 0.0 # ec 경고 상한
wn_dly_sec = 0 # 경고 지연 시간
wn_dly_num = 0 # 경고 지연 횟수
ph_onoff = 0 # 산 강제 조정(산 사용하지 않을 때)

# 센서 보정
cor_ph1 = 0 # ph 보정 - 4
cor_ph2 = 0 # ph 보정 - 7
cor_ec1 = 0 # ec 보정
cor_ec2 = 0 # ec 보정
cor_soil1 = 0 # 지습 보정
cor_soil2 = 0 # 지습 보정
cor_lgt1 = 0 # 광량보정
cor_lgt2 = 0 # 광량보정
cor_lgt3 = 0 # 광량보정
cor_lgt4 = 0 # 광량보정

sensor_sens_ec = 2.0
sensor_sens_lgt = 2.0
cor_used_ec = 3.3
cor_used_ph = 1.0
cor_used_ph1 = 5.3
cor_used_ph2 = 7.3
cor_used_ec1 = 0.7
cor_used_ec2 = 3.5

# 총배액량 / 총공급량 비율 계산
tol_Supply = 0.0 # 총공급량
tol_Drain = 0.0 # 총배액량

workCond = ["메뉴", "대기중", "작동중", "작동중", "정지_"]
warnMsg = ["", "양액농도", "산 농도", "최대 유량 초과(L)", "최대 시간 초과(S)", "강제종료(EC.pH)", "양액 조정중"]

flag_ADIn = 0

# 현재 센서들 데이터
curr_lgt = 0
curr_ec = 0
curr_ph = 0
curr_temp = 0
curr_humi = 0
curr_soil = 0
curr_soil_humi = 0
curr_soil_temp = 0

#  EC, pH 평균 관련
dDayAvgECSum = 0.0 # EC 시간 누적값
dDayAvgPHSum = 0.0 # pH 시간 누적값
dDayAvgUsedECSum = 0.0 # EC(폐액) 시간 누적값
dDayAvgUsedPHSum = 0.0 # PH(페액) 시간 누적값
iPre_Hour = 0 # 현재시간과 비교하기위한 시간
iStart_Hour = 0 # 최초 시작시간
dUsedEC = 0.0
dUsedPH = 0.0
unit_water = 2000

# 환경값 분당 저장 변수
count_lgt = 0
day_time = []
day_temp = []
day_humi = []
day_dlgt = []
day_ec = []
day_ph = []
day_soil_temp = []
day_soil_humi = []

sel_old_day = ""

