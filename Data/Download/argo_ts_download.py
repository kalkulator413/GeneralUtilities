from GeneralUtilities.Data.Filepath.instance import get_data_folder
import os
import subprocess
data_folder = os.path.join(get_data_folder(),'Raw/Argo/temp-sal')

def download():
    subprocess.call(['mkdir', data_folder])
    url = 'https://sio-argo.ucsd.edu/pub/www-argo/RG/RG_ArgoClim_Temperature_2019.nc.gz'
    subprocess.call(["wget", url, "-P" , data_folder])
    url = 'https://sio-argo.ucsd.edu/pub/www-argo/RG/RG_ArgoClim_Salinity_2019.nc.gz'
    subprocess.call(["wget", url, "-P" , data_folder])

    subprocess.call(['cd', data_folder])
    tarred_file = os.path.join(data_folder, 'RG_ArgoClim_Temperature_2019.nc.gz')
    subprocess.call(["gzip", "-d", tarred_file])
    tarred_file = os.path.join(data_folder, 'RG_ArgoClim_Salinity_2019.nc.gz')
    subprocess.call(["gzip", "-d", tarred_file])

    for year in range(2019, 2024):
        for month in range(1, 13):
            
            if year == 2023 and month > 6:
                break

            if month < 10:
                name = f'RG_ArgoClim_{year}0{month}_2019.nc'
            else:
                name = f'RG_ArgoClim_{year}{month}_2019.nc'
            subprocess.call(['wget', 'https://sio-argo.ucsd.edu/pub/www-argo/RG/' + name + '.gz', '-P', data_folder])
            subprocess.call(['gzip', '-d', os.path.join(data_folder, name)])
    
    subprocess.call(['rm', data_folder + '/*.gz.*'])
