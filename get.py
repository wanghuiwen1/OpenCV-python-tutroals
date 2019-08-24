import urllib.request
import PIL.Image as Image
import io

lever = 1



to_image = Image.new('RGB', (4*512, 4*512))

path = "/home/wanghuiwen/Downloads/img/map.jpg"
baseurl = "https://satellite.nsmc.org.cn/mongoTile_DSS/NOM/TileServer.php?layer=PRODUCT&PRODUCT=FY4A-_AGRI--_N_DISK_1047E_L1C_MTCC_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.JPG&DATE=20190824&TIME=0100&&ENDTIME=&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fjpeg&TRANSPARENT=true&LAYERS=satellite&NOTILE=BLACK&TILED=true&WIDTH=256&HEIGHT=256&SRS=EPSG%3A11111&STYLES=&BBOX="
x = -5500
y = 5500
urls = []
index = 0


for a in range(16):
    x1 = x + ((index % 4) * 2750)
    y1 = 5500 - int((index / 4 + 1)) * 2750
    y2 = 5500 - int(index / 4) * 2750
    x2 = x + (((index % 4)+1) * 2750)
    index += 1

    urls.append(str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2))

index = 0
for url in urls:
    try:
        with urllib.request.urlopen(baseurl+url) as response:
            tile = Image.open(io.BytesIO(response.read()))
            print((index % 4)*512, int(index / 4)*512)
            to_image.paste(tile, ((index % 4)*512, int(index / 4)*512))
    except Exception as e:
        print(e)
        exception = e
        print("[{}/3] Retrying to download '{}'...")
    # urllib.request.urlretrieve(baseurl+urls[index],filename=str(index)+".jpg")
    index += 1

to_image.save(path)
