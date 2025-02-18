import pandas as pd
import numpy as np
from datetime import date #, datetime

censo = pd.read_excel('./utils_ucm/data/censo.xlsx')

permf2000c = pd.read_csv('./utils_ucm/data/permf2000c.csv',sep=';',decimal=',')
permf2020_col_1ord = pd.read_csv('./utils_ucm/data/per2020_col_1ord.csv',sep=';',decimal=',')
permf2020_col_2ord = pd.read_csv('./utils_ucm/data/per2020_col_2ord.csv',sep=';',decimal=',')
permf2012c = permf2020_col_1ord


lx_unisex = pd.read_csv('./utils_ucm/data/PASEM2020_Decesos_2ord_Unisex.csv')


pasem2020 = pd.read_csv('./utils_ucm/data/pasem2020.csv',sep=';',decimal=',')
PASEM2020_Gen_F_2ord = pasem2020['PASEM2020_General_F_2ord'][:-10].tolist()
PASEM2020_Gen_M_2ord = pasem2020['PASEM2020_General_M_2ord'][:-10].tolist()
PASEM2020_Rel_F_1ord = pasem2020['PASEM2020_Rel_F_1ord'][:-11].tolist()
PASEM2020_Rel_M_1ord = pasem2020['PASEM2020_Rel_M_1ord'][:-11].tolist()

def per2000c(sex,anno_nac,edad_w):
	edad_w = min(edad_w, 113)
	t = anno_nac + edad_w
	if sex == 'M':
		b = np.exp(-permf2000c['fac_m'][edad_w]*(t-2000))
		return permf2000c['qx_m'][edad_w] * b / 1000
	else:
		b = np.exp(-permf2000c['fac_f'][edad_w]*(t-2000))
		return permf2000c['qx_f'][edad_w] * b / 1000

def per2012c(sex,anno_nac,edad_w):
	edad_w = min(edad_w, 120)
	t = anno_nac + edad_w
	if sex == 'M':
		b = np.exp(-permf2012c['fac_m'][edad_w]*(t-2012))
		return permf2012c['qx_m'][edad_w] * b / 1000
	else:
		b = np.exp(-permf2012c['fac_f'][edad_w]*(t-2012))
		return permf2012c['qx_f'][edad_w] * b / 1000

def per2020_col_2ord(sex,anno_nac,edad_w):
	edad_w = min(edad_w, 120)
	t = anno_nac + edad_w
	if sex == 'M':
		b = np.exp(-permf2020_col_2ord['fac_m'][edad_w]*(t-2012))
		return permf2020_col_2ord['qx_m'][edad_w] * b / 1000
	else:
		b = np.exp(-permf2020_col_2ord['fac_f'][edad_w]*(t-2012))
		return permf2020_col_2ord['qx_f'][edad_w] * b / 1000

def per2020_col_1ord(sex,anno_nac,edad_w):
	edad_w = min(edad_w, 120)
	t = anno_nac + edad_w
	if sex == 'M':
		b = np.exp(-permf2020_col_1ord['fac_m'][edad_w]*(t-2012))
		return permf2020_col_1ord['qx_m'][edad_w] * b / 1000
	else:
		b = np.exp(-permf2020_col_1ord['fac_f'][edad_w]*(t-2012))
		return permf2020_col_1ord['qx_f'][edad_w] * b / 1000


lx_decesos_m = [100000, 99679.39508, 99656.39126, 99637.18915, 99621.40135, 99608.4211, 99597.42232, 99587.66883, 99578.53506, 99569.6968, 99560.83167, 99551.39849, 99540.75059, 99527.86038, 99511.59828, 99490.72637, 99464.05327, 99430.97252, 99391.56342, 99352.17629, 99312.00072, 99270.85121, 99228.66385, 99185.26806, 99140.77455, 99095.29074, 99049.07831, 99002.67851, 98956.59904, 98911.30897, 98867.1731, 98824.00097, 98781.49674, 98739.02346, 98695.54314, 98649.67524, 98599.97507, 98545.543, 98485.79773, 98420.47241, 98349.28745, 98271.57306, 98186.29181, 98087.6053, 97971.79553, 97835.31441, 97674.85347, 97486.72483, 97266.32335, 97009.81939, 96712.87427, 96371.78194, 95995.34313, 95581.66597, 95128.98482, 94635.45815, 94099.03297, 93517.34564, 92887.80251, 92207.70226, 91474.3459, 90685.15701, 89837.66431, 88929.2445, 87956.91438, 86917.10178, 85805.47514, 84616.86306, 83345.1117, 81983.02994, 80522.44106, 78954.12772, 77267.83708, 75452.35462, 73495.92626, 71386.75634, 69113.65897, 66666.64185, 64037.39602, 61220.06607, 58212.01767, 55014.79784, 51632.11612, 48073.78527, 44357.03208, 40507.62461, 36560.93843, 32562.59432, 28568.12887, 24641.72127, 20853.70949, 17276.39576, 13978.55926, 11018.89668, 8440.014238, 6263.95513, 4490.473961, 3098.523765, 2049.967134, 1294.786887, 777.0463661, 427.6558169, 211.0514587, 90.2159918, 31.95488136, 8.842214465, 1.755665635, 0.216936185, 0.012025021, 0]