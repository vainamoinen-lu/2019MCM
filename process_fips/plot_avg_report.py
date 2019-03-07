
import pandas as pd
import matplotlib.pyplot as plt
nflis_path="../MCM_NFLIS_Data.xlsx"
nflis_frame=pd.read_excel(nflis_path,sheet_name="Data")

tmp_frame=nflis_frame[['State','TotalDrugReportsCounty']]
tmp_frame=tmp_frame.rename(columns={'State':'state','TotalDrugReportsCounty':'county_report'})


grouped_mean=tmp_frame.groupby(tmp_frame['state'])['county_report'].mean()

print(grouped_mean)
grouped_mean.plot(kind='bar')
plt.title("average drug reports in one county of each state")
plt.savefig("avg_report.png")
