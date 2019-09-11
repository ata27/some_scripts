from netCDF4 import Dataset
import numpy as N
def lawr(jobid):
        file=Dataset('/scratch/dcw32/netscratch/um/'+jobid+'/'+jobid+'_oh.nc')
	oh=file.variables['mass_fraction_of_hydroxyl_radical_in_air'][:]
	oh=N.mean(oh,axis=0)
	file.close()
	file=Dataset('/scratch/dcw32/netscratch/um/'+jobid+'/'+jobid+'_P-theta.nc')
	P=file.variables['air_pressure'][:]
	P=N.mean(P,axis=0)
	file.close()
	file=Dataset('/scratch/dcw32/netscratch/um/'+jobid+'/'+jobid+'_airmass.nc')
	airmass=file.variables['air_mass_atm'][:]
	airmass=N.mean(airmass,axis=0)
	return (oh,P,airmass)
