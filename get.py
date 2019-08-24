import urllib.request
path = "/home/wanghuiwen/Downloads/img/"
baseurl = "https://satellite.nsmc.org.cn/mongoTile_DSS/NOM/TileServer.php?layer=PRODUCT&PRODUCT=FY4A-_AGRI--_N_DISK_1047E_L1C_MTCC_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.JPG&DATE=20190824&TIME=0100&&ENDTIME=&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fjpeg&TRANSPARENT=true&LAYERS=satellite&NOTILE=BLACK&TILED=true&WIDTH=256&HEIGHT=256&SRS=EPSG%3A11111&STYLES=&BBOX="
x=-5500
y=5500

index = 0
for a in range(4):
    x1=x+(index*2750)
    y1 = 2750
    index+=1
    y2=5500
    x2=x+(index*2750)

    print(x1,y1,x2,y2)
# urls=[
# "-5500,2750,-2750,5500",
# "-2750,2750,0,5500",
# "0,2750,2750,5500",
# "2750,2750,5500,5500",
# ]
# index=0
# for url in urls:
#     print(urls[index])
#     urllib.request.urlretrieve(baseurl+urls[index],filename=str(index)+".jpg")
#     index+=1

