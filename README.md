# Download ERA5 reanalysis
Scripts to download montly means from ERA5 in pressure and single levels. 
Inspired by ECMWFs _How to download ERA5_ 

https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5

## Variables
...can be chosen from a list 

https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation 

For my study:
- In pressure levels:
  - _t   : temperature_
  - _clwc : specific_cloud_liquid_water_content_
  - _ciwc : specific_cloud_ice_water_content_
  - _cswc : specific_snow_water_content_
- In single levels:
  - _2t   : 2m_temperature_
  - _msr  : mean_snowfall_rate_
  - _sf   : snowfall_

## Forms
ERA5 monthly averaged data on pressure levels from 1979 to present: 

https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels-monthly-means?tab=form

ERA5 monthly averaged data on single levels from 1979 to present: 

https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=form

## Necessary Python 3.7 packages
- jupyter 
- jupyterlab
- cdsapi
- glob
- dask
- xarray
- matplotlib
- cartopy
- numpy

## How to cite
Hellmuth, Franziska, (2020), Download ERA5, University of Oslo, Oslo, Norway. Contact: franziska.hellmuth@geo.uio.no
