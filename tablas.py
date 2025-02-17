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
