import pandas as pd
import xarray as xr
from data.traces import build_trace_library_production

dataFolder = '/Users/an1009/Ecommons/HFC/PyMC/Data/Processed/'

# ------------------------------------------------------------
# Load Atmospheric Concentration calculated from AGAGE
# ------------------------------------------------------------
observations_file = 'AGAGE_AnnualMean_concentration.parquet'
atmosConc = pd.read_parquet(f"{dataFolder}{observations_file}")
gases = atmosConc.columns.values

# ------------------------------------------------------------
# Load Lifetimes data
# ------------------------------------------------------------
lt_file = 'mean_lifetimes.parquet'
lifeTimes = pd.read_parquet(f"{dataFolder}{lt_file}")

# ------------------------------------------------------------
# Reported Production data
# ------------------------------------------------------------
trace_library_prod = build_trace_library_production()
prod = {}
for c in gases:
   gn = c.replace("-","")
   file = f"{dataFolder}priors_{gn}.parquet"
   prod[c] = pd.read_parquet(file).loc[1956:2023]
   if 'shortProd1' in prod[c].columns:
      prod[c]['shortProd'] =  prod[c]['shortProd1'] + prod[c]['shortProd2']
      prod[c] = prod[c].drop(['shortProd1','shortProd2'],axis=1)
   file = f"{dataFolder}posterior_{gn}.zarr"
   if gn in ['cfc11','cfc12','cfc113','cfc114','cfc115']:
      eprod = xr.open_zarr(file)
      prod_vars = set(trace_library_prod.keys()) & set(eprod.data_vars)
      for v in prod_vars:
         prod[c][v] = eprod[v].sel(metric='median')
         prod[c][v+'_std'] = eprod[v].sel(metric='stddev')
   prod[c].attrs['title'] = 'Reported & Estimted Production'
   prod[c].attrs['units'] = 'Gg'
   prod[c].attrs['long_name'] = 'Production'


