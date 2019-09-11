from netCDF4 import Dataset
import numpy as N
def lawr(jobid,nyrs):
        file=Dataset('/scratch/dcw32/netscratch/um/'+jobid+'/'+jobid+'_cloud_diags.nc')
	oh=file.variables['cloud_cond_nuc'][:]
	ohj=N.empty([nyrs,85,145,192])
	for i in range (0,nyrs):
		q=12*i
		ohi=oh[q:q+12,:,:,:]
		ohj[i,:,:,:]=N.mean(ohi,axis=0)
	ohstd=N.std(ohj,axis=0)
	oh=N.mean(oh,axis=0)
	file.close()
	return (ohd)
