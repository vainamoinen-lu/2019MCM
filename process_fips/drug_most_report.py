import pandas as pd
import matplotlib.pyplot as plt
nflis_path="../MCM_NFLIS_Data.xlsx"
nflis_frame=pd.read_excel(nflis_path,sheet_name="Data")

tmp_frame=nflis_frame[['DrugReports','SubstanceName']]
tmp_frame=tmp_frame.rename(columns={'DrugReports':'tmp_cnt','SubstanceName':'substance_name'})


drug_cnt=tmp_frame.groupby(tmp_frame['substance_name'])['tmp_cnt'].sum().to_frame().reset_index()

drug_cnt.columns=['substance_name','cnt']

drug_cnt=drug_cnt.sort_values(by='cnt',ascending=False)
drug_cnt=drug_cnt[0:10]



# drug_cnt.plot(kind='bar')
# substance_name=drug_cnt['substance_name']
# cnt=drug_cnt['cnt']
# plt.bar(substance_name,cnt)
drug_cnt=drug_cnt.set_index('substance_name')
drug_cnt.plot(kind='bar')

plt.title("10 most reported drugs")
plt.tight_layout()
plt.savefig("most_reported_drug_cnt.png",figsize=(100,100))


# print(drug_cnt.columns)
# print(drug_cnt)
# grouped_mean.plot(kind='bar')
# plt.title("drug reported most")
# plt.savefig("drug_cnt.png")