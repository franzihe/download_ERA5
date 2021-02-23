# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Plot the seasonal mean of the variable _snowfall_

# +
# supress warnings
import warnings
warnings.filterwarnings('ignore') # don't output warnings

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from glob import glob

### Create dask cluster to work parallel in large datasets

from dask.distributed import Client
client = Client(n_workers=2, 
                threads_per_worker=2, 
                memory_limit='4GB',
                processes=False)
client
chunks={'time' : 10,}
client
# -

_path = '/home/franzihe/nird_NS9600K/franzihe/data/ERA5/3_hourly/'
_path = '/home/franzihe/astra_franzihe/Data/ERA5/1deg/'
var = 'sf'
#var = 'tp'

xr.open_dataset('/home/franzihe/astra_franzihe/Data/ERA5/1deg/sf_Amon_ERA5_1deg_199001_199012.nc').time

# +
fn_list = [ff for ff in glob(_path + var + '_3hourly_*.nc') if (int(ff[-9:-5])>= 2008)]
fn_list.sort()

if len(fn_list) > 0:

    fn = xr.open_mfdataset(fn_list, chunks = chunks, 
                           parallel = True, 
                           use_cftime = False,
                          ) 
#    fn['time'] = fn.indexes['time'].to_datetimeindex()
# -

_path + var 

f,axsm = plt.subplots(2,2, figsize = [10,7], subplot_kw={'projection' : ccrs.PlateCarree()})
axs = axsm.flatten()
for sea, ax in zip(fn.tp.groupby('time.season').sum('time').season, axs.flatten()):
    im = fn.tp.sel(time = (fn.tp['time.season'] == sea),).mean('time', keep_attrs = True).plot.pcolormesh(ax = ax,
                                                                                                          transform = ccrs.PlateCarree(),
                                                                                                          robust = True,
                                                                                                          add_colorbar = False)
    ax.coastlines()
f.subplots_adjust(right = 0.8, top = 1.0)
f.suptitle('Mean {starty} - {endy}'.format(starty = np.asarray(fn['time.year'][0]),  endy = np.asarray(fn['time.year'][-1])), fontweight = 'bold')
cbar_ax = f.add_axes([0.85, 0.15, 0.025, 0.7])
f.colorbar(im, 
               cax=cbar_ax, 
               extend = 'both',
               format='%.0e').ax.set_ylabel(fn.tp.attrs['long_name'] + ' [' + fn.tp.attrs['units'] + ']')
plt.tight_layout()


