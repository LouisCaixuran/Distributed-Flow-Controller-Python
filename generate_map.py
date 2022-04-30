from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook


def draw_map(file="./friendMap.png",friends_address={"alice":(43.07167832752132, -89.40666590224633),"bob":(42.35087234171386, -71.10510942329232),"john":(40.952173148593396, -76.88535528597656)}):
    fig = plt.figure(num=None, figsize=(12, 8) ) 
    m = Basemap(width=6000000,height=4500000,resolution='c',projection='aea',lat_1=35.,lat_2=45.,lon_0=-100,lat_0=40)
    m.drawcoastlines(linewidth=0.5)
    m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
    m.drawmeridians(np.arange(-180.,181.,15.),labels=[False,False,False,True],dashes=[2,2])
    m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
    m.drawstates(linewidth=0.5, linestyle='solid', color='k')
    m.shadedrelief()
    for i in friends_address.keys():
        x,y=m(friends_address[i][1],friends_address[i][0])
        plt.plot(x,y,'ro', markersize=5)
        plt.text(x,y,i,fontsize="large")
       
    plt.savefig(file)
    plt.show()
    return 

draw_map()
