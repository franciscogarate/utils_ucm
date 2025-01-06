from datetime import datetime, date

def FecRenv(fechanac, fechavenc):
	fecharenv = pd.to_datetime(date(fechavenc.year - 1, fechavenc.month, fechavenc.day))
	if fecharenv < fechanac:
		return fechanac
	else:
		return fecharenv

def antiguedad(falta, fval):
	return int(fval.year - falta.year) + ((fval.month, fval.day) > (falta.month, falta.day)) - 1