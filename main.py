import urllib.request, urllib.error
import pandas as pd

df = pd.read_excel('input.xlsx')
#print the column names
#print(df.columns)
statuses = []
urls = []
#get the values for a given column
values = df['Website Url'].values
for url in values : 
	print(url)
	try:
		conn = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
		# Return code error (e.g. 404, 501, ...)
		print('HTTPError: {}'.format(e.code))
		status = e.code
	except urllib.error.URLError as e:
		# Not an HTTP-specific error (e.g. connection refused)
		print('URLError: {}'.format(e.reason))
		status = e.reason
	else:
		# 200
		status=conn.getcode()
	print(status)
	urls.append(url)
	statuses.append(status)
print(statuses)


columns=['Website Url','Status']
df = pd.DataFrame([urls,statuses], columns=columns)
writer = pd.ExcelWriter('output/file.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()