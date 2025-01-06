import numpy as np
import pandas as pd
from datetime import datetime, date

def EdAct(fechanac, fval):
	if isinstance(fechanac, datetime):
		pass
	else:
		fechanac = pd.to_datetime(str(fechanac))
	if isinstance(fval, datetime):
		pass
	else:
		fval = pd.to_datetime(str(fval))
	
	return np.rint((fval - fechanac).days / 365.25).astype(int) #cactus divide por 365.25

def EdReal(fechanac, fval):
	if isinstance(fechanac, datetime):
		pass
	else:
		fechanac = pd.to_datetime(str(fechanac))
	if isinstance(fval, datetime):
		pass
	else:
		fval = pd.to_datetime(str(fval))

	edad = fval.year - fechanac.year - ((fval.month, fval.day) < (fechanac.month, fechanac.day))
	return np.maximum(edad, 0)

def DiaJub(fechanac):
	fechanac = pd.to_datetime(str(fechanac))
	try:
		return date(fechanac.year + 65, fechanac.month, fechanac.day)
	except:
		return date(fechanac.year + 65, fechanac.month, fechanac.day - 1)


#print(EdAct('1973-06-30','2017-12-31'))
#print(EdReal('1973-06-30','2017-12-31'))
#print(DiaJub('1973-06-30'))
