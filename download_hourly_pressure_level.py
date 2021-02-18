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

# # ERA5 monthly averaged data on pressure levels from 1985 to 2014
#
# ERA5 form: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=form
#
# ERA5 variables: https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation

import cdsapi
import glob

path = '/home/franzihe/nird_NS9600K/franzihe/data/ERA5/3_hourly/'

form = 'netcdf' # 'grib'

available_month = {
                   '01':['01'],
                   '02':['02'],
                   '03':['03'],
                   '04':['04'], 
                   '05':['05'], 
                   '06':['06'], 
                   '07':['07'],
                   '08':['08'], 
                   '09':['09'], 
                   '10':['10'], 
                   '11':['11'], 
                   '12':['12']
                  }

available_years = {
                   "08": ['2008',],
                    }


variable = {'t'   :'temperature',
            'crwc':'specific_rain_water_content',
            'cswc':'specific_snow_water_content',
             'clwc':'specific_cloud_liquid_water_content',
            'ciwc':'specific_cloud_ice_water_content'
           }

counter = 0
for keys, var in variable.items(): 
    for years in (available_years):
        for months in available_month:
            
            if form == 'netcdf':
                _ff = 'nc'
            elif form == 'grib':
                _ff = 'grib'


            filename = '{keys}_3hourly_ERA5_{starty}{startm}.{format}'.format(keys = keys,
                                                                                   starty = available_years[years][0],
                                                                                   startm = available_month[months][0], 
                                                                                      format = _ff)
            files = glob.glob(path+filename)
            if path + filename in files:
                print(path + filename + ' is downloaded')
                counter += 1
                print("Have downloaded in total : " + str(counter) + " files")
            else:
                c = cdsapi.Client()

                c.retrieve(
                    'reanalysis-era5-pressure-levels',
                    {
                        'product_type': 'reanalysis',
                        'format': form,
                        'pressure_level': [
                            '1', '2', '3',
                            '5', '7', '10',
                            '20', '30', '50',
                            '70', '100', '125',
                            '150', '175', '200',
                            '225', '250', '300',
                            '350', '400', '450',
                            '500', '550', '600',
                            '650', '700', '750',
                            '775', '800', '825',
                            '850', '875', '900',
                            '925', '950', '975',
                            '1000',
                        ],
                        'variable': var,
                        'year': available_years[years],
                        'month': available_month[months],
                        'day': [
                            '01', '02', '03',
                            '04', '05', '06',
                            '07', '08', '09',
                            '10', '11', '12',
                            '13', '14', '15',
                            '16', '17', '18',
                            '19', '20', '21',
                            '22', '23', '24',
                            '25', '26', '27',
                            '28', '29', '30',
                            '31',
                        ],
                        'time': [
                            '00:00', '03:00', '06:00',
                            '09:00', '12:00', '15:00',
                            '18:00', '21:00',
                        ],
                    },
                    path + filename)
                print('File saved: {}'.format(path + filename))


