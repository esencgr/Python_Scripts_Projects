import requests
# url = 'https://www2.census.gov/geo/tiger/GENZ2017/shp/cb_2017_02_tract_500k.zip'
# target_path = 'alaska.zip'

# response = requests.get(url, stream=True)
# handle = open(target_path, "wb")
# for chunk in response.iter_content(chunk_size=512):
#     if chunk:  # filter out keep-alive new chunks
#         handle.write(chunk)
# handle.close()

request = requests.get('https://drive.google.com/file/d/1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB/view?usp=sharing')

# with open('survey2020.zip','wb') as file:
with open("stack.csv","wb") as file:

    file.write(request.content)

# import zipfile
# with zipfile.ZipFile('alaska.zip') as zip:
#     zip.extract('alaska')

# import shutil,os

# shutil.move('survey2020/survey_results_public.csv','mysurvey.csv')
# shutil.rmtree('survey2020')
# os.remove('survey2020.zip')
