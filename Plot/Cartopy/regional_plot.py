from GeneralUtilities.Plot.Cartopy.eulerian_plot import BaseCartopy
# import cartopy.crs as ccrs
class ccrs():
    pass
    def PlateCarree(central_longitude=0):
        return None

class RegionalBase(BaseCartopy):
# need to add class method to generate ax with center lon
    central_longitude=0
    def __init__(self,*args,adjustable=False,**kwargs):
        super().__init__(*args,**kwargs)
        self.ax.set_extent([self.llcrnrlon,self.urcrnrlon,self.llcrnrlat,self.urcrnrlat], crs=ccrs.PlateCarree())
        self.finish_map(adjustable=adjustable)


class GOMCartopy(RegionalBase):
    llcrnrlon=-87
    llcrnrlat=23
    urcrnrlon=-84
    urcrnrlat=25
    def __init__(self,*args,**kwargs):
        print('I am plotting GOM')
        super().__init__(*args,**kwargs)

class SOSECartopy(RegionalBase):
    llcrnrlon=-180.
    llcrnrlat=-80.
    urcrnrlon=180.
    urcrnrlat=-25
    def __init__(self,*args,**kwargs):
        print('I am plotting antarctic region')
        super().__init__(*args,**kwargs)

class CreteCartopy(RegionalBase):
    llcrnrlon=22.5
    llcrnrlat=33
    urcrnrlon=28.5
    urcrnrlat=38
    def __init__(self,*args,**kwargs):
        print('I am plotting Crete')
        super().__init__(*args,**kwargs)

class KonaCartopy(RegionalBase):
    llcrnrlon=-157
    llcrnrlat=18.8
    urcrnrlon=-155.6
    urcrnrlat=20.35
    def __init__(self,*args,**kwargs):
        print('I am plotting Kona')
        super().__init__(*args,**kwargs)

class PuertoRicoCartopy(RegionalBase):
    llcrnrlon=-68.5 
    llcrnrlat=16
    urcrnrlon=-65
    urcrnrlat=22.5
    def __init__(self,*args,**kwargs):
        print('I am plotting Puerto Rico')
        super().__init__(*args,**kwargs)

class MobyCartopy(RegionalBase):
    def __init__(self,*args,**kwargs):
        print('I am plotting Moby')
        center_lat = 20.8
        center_lon = -157.2
        self.llcrnrlon=(center_lon-3)
        self.llcrnrlat=(center_lat-3)
        self.urcrnrlon=(center_lon+3)
        self.urcrnrlat=(center_lat+3)
        super().__init__(*args,**kwargs)
        self.ax.scatter(center_lon,center_lat,500,marker='*',color='Red',zorder=10)

class GOMCartopy(RegionalBase):
    llcrnrlon=-100.
    llcrnrlat=20.5
    urcrnrlon=-81.5
    urcrnrlat=30.5
    def __init__(self,*args,**kwargs):
        print('I am plotting GOM')
        super().__init__(*args,**kwargs)

class CCSCartopy(RegionalBase):
    llcrnrlon=-135.
    llcrnrlat=20
    urcrnrlon=-110
    urcrnrlat=55
    def __init__(self,*args,**kwargs):
        print('I am plotting CCS')
        super().__init__(*args,**kwargs)

class DrakePassageCartopy(RegionalBase):
    llcrnrlon=-120.
    llcrnrlat=-65.
    urcrnrlon=-40.
    urcrnrlat=-50.
    def __init__(self,*args,**kwargs):
        print('I am plotting Drake Passage')
        super().__init__(*args,**kwargs)


class WeddellSeaCartopy(RegionalBase):
    llcrnrlon=-65.
    llcrnrlat=-75.
    urcrnrlon=40.
    urcrnrlat=-50.
    def __init__(self,*args,**kwargs):
        print('I am plotting Weddell Sea')
        super().__init__(*args,**kwargs)

class TahitiCartopy(RegionalBase):
    llcrnrlon=-152
    llcrnrlat=-19
    urcrnrlon=-148
    urcrnrlat=-16
    def __init__(self,*args,**kwargs):
        print('I am plotting Tahiti')
        super().__init__(*args,**kwargs)

class NAtlanticCartopy(RegionalBase):
    llcrnrlon=-90.
    llcrnrlat=15.
    urcrnrlon=5.
    urcrnrlat=85.
    def __init__(self,*args,**kwargs):
        print('I am plotting N Atlantic')
        super().__init__(*args,**kwargs)

class NPacificCartopy(RegionalBase):
    llcrnrlon=120.
    llcrnrlat=0.
    urcrnrlon=260.
    urcrnrlat=80.
    def __init__(self,*args,**kwargs):
        print('I am plotting N Pacific')
        super().__init__(*args,**kwargs)

class SAtlanticCartopy(RegionalBase):
    llcrnrlon=-80.
    llcrnrlat=-60.
    urcrnrlon=30.
    urcrnrlat=0.
    def __init__(self,*args,**kwargs):
        print('I am plotting S Atlantic')
        super().__init__(*args,**kwargs)


class SPacificCartopy(RegionalBase):
    llcrnrlon=120.
    llcrnrlat=-60.
    urcrnrlon=280.
    urcrnrlat=0.
    def __init__(self,*args,**kwargs):
        print('I am plotting S Pacific')
        super().__init__(*args,**kwargs)

class PacificCartopy(RegionalBase):
    llcrnrlon=130.
    llcrnrlat=-20.
    urcrnrlon=270.
    urcrnrlat=45.
    projection=ccrs.PlateCarree(central_longitude=180)
    def __init__(self,*args,**kwargs):
        print('I am plotting Pacific')
        super().__init__(*args,**kwargs)

class AtlanticCartopy(RegionalBase):
    llcrnrlon=-80.
    llcrnrlat=-40.
    urcrnrlon=20.
    urcrnrlat=80.
    def __init__(self,*args,**kwargs):
        print('I am plotting Atlantic')
        super().__init__(*args,**kwargs)

class SouthernOceanCartopy(RegionalBase):
    llcrnrlon=-180.
    llcrnrlat=-90.
    urcrnrlon=180.
    urcrnrlat=-30.
    def __init__(self,*args,**kwargs):
        print('I am plotting Southern Ocean')
        super().__init__(*args,**kwargs)