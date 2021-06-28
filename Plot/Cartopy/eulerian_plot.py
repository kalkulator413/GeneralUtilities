import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np


class BaseCartopy():
    def __init__(self,lat_grid,lon_grid,ax=False):
        assert max(lat_grid)<=90
        assert min(lat_grid)>=-90
        assert max(lon_grid)<=180
        assert min(lon_grid)>=-180

        self.lat_grid = lat_grid
        self.lon_grid = lon_grid

        if not ax:
            fig = plt.figure()
            self.ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        else:
            self.ax = ax

    def meshgrid(self):
        return np.meshgrid(self.lon_grid,self.lat_grid)

    def finish_map(self):
        self.ax.add_feature(cfeature.LAND)
        self.ax.add_feature(cfeature.COASTLINE)
        self.ax.set_aspect('auto')
        gl = self.ax.gridlines(draw_labels=True)
        gl.xlabels_top = False
        gl.ylabels_right = False

    def get_map(self):
        XX,YY = self.meshgrid()
        return (XX,YY,self.ax)

class SOSECartopy(BaseCartopy):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('I am plotting antarctic region')
        llcrnrlon=-180.
        llcrnrlat=-80.
        urcrnrlon=180.
        urcrnrlat=-25
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map()

class CreteCartopy(BaseCartopy):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('I am plotting Crete')
        llcrnrlon=20.
        llcrnrlat=30
        urcrnrlon=30
        urcrnrlat=40
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map()

class MobyCartopy(BaseCartopy):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('I am plotting Moby')
        center_lat = 20.8
        center_lon = -157.2
        llcrnrlon=(center_lon-3)
        llcrnrlat=(center_lat-3)
        urcrnrlon=(center_lon+3)
        urcrnrlat=(center_lat+3)
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.ax.scatter(center_lon,center_lat,500,marker='*',color='Red',zorder=10)
        self.finish_map()

class GomCartopy(BaseCartopy):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('I am plotting GOM')
        llcrnrlon=-100.
        llcrnrlat=20.5
        urcrnrlon=-81.5
        urcrnrlat=30.5
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())        
        self.finish_map()

class GlobalCartopy(BaseCartopy):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)      
        print('I am plotting global region')
        llcrnrlon=-180.
        llcrnrlat=-80.
        urcrnrlon=180.
        urcrnrlat=80
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map()

class HypernavCartopy(BaseCartopy):
    def __init__(self,nc,float_pos_dict,*args,pad=1,**kwargs):
        super().__init__(*args,**kwargs)     
        try:
            urlat = nc['lat'][:].max()
            lllat = nc['lat'][:].min()
            urlon = nc['lon'][:].max()
            lllon = nc['lon'][:].min()
        except TypeError:
            urlat = max(nc.lats)
            lllat = min(nc.lats)
            urlon = max(nc.lons)
            lllon = min(nc.lons)        
        llcrnrlon=(lllon-pad)
        llcrnrlat=(lllat-pad)
        urcrnrlon=(urlon+pad)
        urcrnrlat=(urlat+pad)
        self.ax.scatter(float_pos_dict['lon'],float_pos_dict['lat'],c='pink',linewidths=5,marker='x',s=80,zorder=10)
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map()

class PointCartopy(BaseCartopy):
    def __init__(self,geopy_point,*args,pad=1,**kwargs):
        super().__init__(*args,**kwargs)          
        llcrnrlon=(geopy_point.longitude-pad)
        llcrnrlat=(geopy_point.latitude-pad)
        urcrnrlon=(geopy_point.longitude+pad)
        urcrnrlat=(geopy_point.latitude+pad)
        self.ax.set_extent([llcrnrlon,urcrnrlon,llcrnrlat,urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map()