from GeneralUtilities.Data.Filepath.instance import get_data_folder
from GeneralUtilities.Data.Download.download_utilities import execute_download
import os
data_folder = os.path.join(get_data_folder(),'Raw/Aviso/')

def download():
        for year in range(2017, 2024):
                for month in range(1, 13):

			# skip downloading all incomplete months
			if year == 2017 and month <= 2:
				continue
			elif year == 2021 and month == 12:
				continue
			elif year = 2022 and month == 1:
				continue
			elif year == 2023 and month > 6:
				continue
			
                        url = f"https://coastwatch.noaa.gov/erddap/griddap/noaacwBLENDEDsshDaily.nc?sla%5B({year}-{month}-01):1:({year}-{month}-31T00:00:00Z)%5D%5B(-89.875):1:(89.875)%5D%5B(-179.875):1:(179.875)%5D"
                        filename = str(month) + ".nc"
                        folder = os.path.join(data_folder, str(year))
                        execute_download(url,filename,folder)

