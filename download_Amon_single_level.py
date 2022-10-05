# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # ERA5 monthly averaged data on single levels from 1985 to 2014
# ERA5 form: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=form
#
# ERA5 variables: https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation

import cdsapi
import glob

# path = '/home/franzihe/nird_franzihe/data/ERA5/'
# path = '/home/franzihe/nird_ERA5/'
path = "/scratch/franzihe/input/ERA5/monthly_means/0.25deg/"

form = "netcdf"  # 'grib'

available_month = {
    "01_12": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
}

available_years = {
    "85-89": ["1985", "1986", "1987", "1988", "1989",],
    "90-99": [
        "1990",
        "1991",
        "1992",
        "1993",
        "1994",
        "1995",
        "1996",
        "1997",
        "1998",
        "1999",
    ],
    "00-09": [
        "2000",
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
    ],
    "10-14": ["2010", "2011", "2012", "2013", "2014",],
}

variable = {
    # '2t':   '2m_temperature',
    # 'msr'  :'mean_snowfall_rate',
    # 'sf'   :'snowfall',
    # 'tclw' : 'total_column_cloud_liquid_water',
    # 'tciw' : 'Total column cloud ice water'
    "tp": "total_precipitation"
}

counter = 0
for keys, var in variable.items():
    for years in available_years:
        for months in available_month:
            #   print(var, available_years[years], available_month[months])

            if form == "netcdf":
                _ff = "nc"
            elif form == "grib":
                _ff = "grib"

            filename = "{keys}_Amon_ERA5_{starty}{startm}_{endy}{endm}.{format}".format(
                keys=keys,
                starty=available_years[years][0],
                startm=available_month[months][0],
                endy=available_years[years][-1],
                endm=available_month[months][-1],
                format=_ff,
            )
            #            print(filename)

            files = glob.glob(path + filename)
            if path + filename in files:
                print(path + filename + " is downloaded")
                counter += 1
                print("Have downloaded in total : " + str(counter) + " files")
            else:
                c = cdsapi.Client()
                c.retrieve(
                    "reanalysis-era5-single-levels-monthly-means",
                    {
                        "product_type": "monthly_averaged_reanalysis",
                        "variable": var,
                        "year": available_years[years],
                        "month": available_month[months],
                        "time": "00:00",
                        #                    'grid': '0.25/0.25',        # Regrid from the default grid to a regular lat/lon with specified resolution. The first number is east-west resolution (longitude) and the second is north-south (latitude).
                        "format": form,
                        "stream": "moda",
                    },
                    path + filename,
                )
            print("File saved: {}".format(path + filename))
