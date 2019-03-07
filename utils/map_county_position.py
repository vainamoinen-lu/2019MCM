# to get new file map a place to a position on map

import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 
nflis_path="../MCM_NFLIS_Data.xlsx"
nflis_df=pd.read_excel(nflis_path,sheet_name="Data")

zipcode_path='../zipcode.csv'
zipcode_df=pd.read_csv(zipcode_path)

zipcode_df=zipcode_df.rename(columns={'city':'county','state':'state','latitude':'latitude',\
'longitude':'longitude'})


#further process nflis

nflis_df=nflis_df.rename(columns={'COUNTY':'county','State':'state','FIPS_County':'fips_county',\
'FIPS_State':'fips_state','TotalDrugReportsCounty':'county_report'})
tmp_year=2017
nflis_df=nflis_df.loc[nflis_df['YYYY']==tmp_year]


nflis_df=nflis_df[['county','state','county_report']]



nflis_df=nflis_df.groupby(['county','state']).mean().reset_index()

#convert to upper
zipcode_county=zipcode_df['county']
zipcode_county=zipcode_county.str.upper()

zipcode_df['county']=zipcode_county

# print(zipcode_df)

map_df=pd.merge(nflis_df,zipcode_df,how='left',on=['county','state'])
map_df=map_df.drop_duplicates(subset=['county','state'],keep='first')
map_df=map_df.dropna(axis=0,how='any')
map_df=map_df[['county','state','latitude','longitude','county_report']]

# map_df.to_csv('county2position.csv')

longitude_list=map_df['longitude'].tolist()

longitude_list=np.array(longitude_list)
# print(longitude_list)
max_longitude=longitude_list.max()
min_longitude=longitude_list.min()

horizon_start=0
horizon_end=99
k_longitude=(horizon_end-horizon_start)/(max_longitude-min_longitude)
b_longitude=horizon_start-k_longitude*min_longitude
# print(k_longitude)

latitude_list=map_df['latitude'].tolist()

latitude_list=np.array(latitude_list)
# print(longitude_list)
max_latitude=latitude_list.max()
min_latitude=latitude_list.min()

vertical_start=0
vertical_end=99
k_latitude=(vertical_end-vertical_start)/(max_latitude-min_latitude)
b_latitude=vertical_start-k_latitude*min_latitude


img_arr=np.zeros((100,100))
for row in map_df.iterrows():
    row=row[1]
   

    tmp_longitude=row['longitude']
    tmp_latitude=row['latitude']
    tmp_county_report=row['county_report']
    tmp_horizon=k_longitude*tmp_longitude+b_longitude
    tmp_vertical=k_latitude*tmp_latitude+b_latitude
    tmp_vertical=int(tmp_vertical+0.1)
    tmp_horizon=int(tmp_horizon+0.1)
    img_arr[tmp_horizon][tmp_vertical]=tmp_county_report


img = Image.fromarray(img_arr)
img=img.convert('L')
img.show()
img.save(str(tmp_year)+'_img.jpg')





# print(map_df)

