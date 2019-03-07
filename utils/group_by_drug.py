import pandas as pd
nflis_path="../MCM_NFLIS_Data.xlsx"
nflis_frame=pd.read_excel(nflis_path,sheet_name="Data")
# print(nflis_frame.head(3))
grouped_df=nflis_frame.groupby(nflis_frame['SubstanceName'])
# print(grouped_df.count())
drug_and_cnt=grouped_df.count()
drug_and_cnt.to_csv("count_group_by_drug.csv",index=1)
