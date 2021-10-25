import sys
import requests
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore


class Destination:
    name = '서울'
    longitude = 37.5714
    latitude = 126.9658

    def __init__(self, name, latitude, longitude):
        self.name = name

        if not isinstance(latitude, float):
            raise ValueError(f'latitude of {name} is not decimal.')

        self.latitude = latitude

        if not isinstance(longitude, float):
            raise ValueError(f'longitude of {name} is not decimal');

        self.longitude = longitude


cred = credentials.Certificate(sys.argv[1])
firebase_admin.initialize_app(cred, {
    'projectId': sys.argv[2],
})
db = firestore.client()

destinationList = [
    Destination('서울', 37.5714, 126.9658),
    Destination('백령도', 37.9661, 124.6305),
    Destination('동두천', 37.9019, 127.0607),
    Destination('파주', 37.8859, 126.7665),
    Destination('인천', 37.4776, 126.6244),
    Destination('수원', 37.2723, 126.9853),
    Destination('강화', 37.7074, 126.4463),
    Destination('양평', 37.4886, 127.4945),
    Destination('이천', 37.264, 127.4842),
    Destination('북춘천', 37.9475, 127.7547),
    Destination('철원', 38.1479, 127.3042),
    Destination('춘천', 37.9026, 127.7357),
    Destination('원주', 37.3376, 127.9466),
    Destination('영월', 37.1813, 128.4574),
    Destination('인제', 38.0599, 128.1671),
    Destination('홍천', 37.6836, 127.8804),
    Destination('북강릉', 37.8046, 128.8554),
    Destination('울릉도', 37.4813, 130.8986),
    Destination('강릉', 37.7515, 128.891),
    Destination('속초', 38.2509, 128.5647),
    Destination('대관령', 37.6771, 128.7183),
    Destination('동해', 37.5071, 129.1243),
    Destination('태백', 37.1703, 128.9893),
    Destination('정선군', 37.3814, 128.6459),
    Destination('청주', 36.6392, 127.4407),
    Destination('충주', 36.9704, 127.9527),
    Destination('추풍령', 36.2202, 127.9946),
    Destination('제천', 37.1593, 128.1943),
    Destination('보은', 36.4876, 127.7341),
    Destination('홍성', 36.5926, 126.6444),
    Destination('대전', 36.372, 127.3721),
    Destination('서산', 36.7766, 126.4939),
    Destination('천안', 36.7624, 127.2927),
    Destination('보령', 36.3272, 126.5574),
    Destination('부여', 36.2724, 126.9208),
    Destination('금산', 36.1056, 127.4818),
    Destination('전주', 35.8408, 127.1186),
    Destination('군산', 36.0053, 126.7614),
    Destination('부안', 35.7295, 126.7166),
    Destination('임실', 35.6123, 127.2856),
    Destination('정읍', 35.5631, 126.8392),
    Destination('남원', 35.4054, 127.333),
    Destination('장수', 35.657, 127.5203),
    Destination('순창', 35.3714, 127.1286),
    Destination('고창', 35.3489, 126.599),
    Destination('광주', 35.1729, 126.8916),
    Destination('목포', 34.8169, 126.3812),
    Destination('흑산도', 34.6872, 125.451),
    Destination('여수', 34.7393, 127.7406),
    Destination('완도', 34.3959, 126.7018),
    Destination('진도(첨찰산)', 34.4721, 126.3238),
    Destination('진도군', 34.4731, 126.2585),
    Destination('영광', 35.2837, 126.4778),
    Destination('순천', 35.0204, 127.3694),
    Destination('장흥', 34.6888, 126.9195),
    Destination('해남', 34.5536, 126.569),
    Destination('고흥', 34.6182, 127.2757),
    Destination('강진군', 34.6261, 126.7689),
    Destination('보성군', 34.7633, 127.2123),
    Destination('광양', 34.943, 127.691),
    Destination('안동', 36.5729, 128.7073),
    Destination('포항', 36.0326, 129.3796),
    Destination('대구', 35.8282, 128.6522),
    Destination('울진', 36.9918, 129.4128),
    Destination('상주', 36.4084, 128.1574),
    Destination('봉화', 36.9436, 128.9145),
    Destination('영주', 36.8719, 128.517),
    Destination('문경', 36.6273, 128.1488),
    Destination('영덕', 36.5333, 129.4094),
    Destination('의성', 36.3561, 128.6886),
    Destination('구미', 36.1306, 128.3205),
    Destination('영천', 35.9774, 128.9514),
    Destination('청송군', 36.4321, 129.0423),
    Destination('경주', 35.8175, 129.2009),
    Destination('부산', 35.1047, 129.032),
    Destination('울산', 35.5825, 129.3347),
    Destination('창원', 35.1702, 128.5729),
    Destination('북창원', 35.2264, 128.6275),
    Destination('통영', 34.8455, 128.4356),
    Destination('진주', 35.1638, 128.04),
    Destination('거창', 35.6674, 127.909),
    Destination('합천', 35.565, 128.1699),
    Destination('밀양', 35.4915, 128.7441),
    Destination('산청', 35.413, 127.8791),
    Destination('거제', 34.8882, 128.6045),
    Destination('남해', 34.8166, 127.9264),
    Destination('김해시', 35.2267, 128.893),
    Destination('양산', 35.3072, 129.02),
    Destination('의령군', 35.3226, 128.2881),
    Destination('함양군', 35.5114, 127.7454),
    Destination('제주', 33.5141, 126.5297),
    Destination('고산', 33.2938, 126.1628),
    Destination('서귀포', 33.2461, 126.5653),
    Destination('성산', 33.3868, 126.8802)
]

for destination in destinationList:
    res = requests.get(
        f'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily?lat={destination.latitude}&lon={destination.longitude}',
        headers={'x_rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': sys.argv[3]})
    data = res.json()['data']

    for daily in data:
        date = datetime.strptime(daily['valid_date'], '%Y-%m-%d')
        dailyDict = {
            'date': date.strftime('%m%d'),
            'averageTemperature': daily['temp'],
            'maximumTemperature': daily['max_temp'],
            'minimumTemperature': daily['min_temp'],
            'cloudAmount': daily['clouds'] / 10.0,
            'humidity': daily['rh'],
            'windSpeed': daily['wind_spd'],
            'precipitationPercentage': daily['pop'],
        }

        weather = daily['weather']['description'].lower()

        if 'snow' in weather:
            dailyDict['rainFall'] = daily['snow']
            dailyDict['snowFall'] = daily['snow_depth']
        elif 'rain' in weather:
            dailyDict['rainFall'] = daily['precip']

        docName = date.strftime('%Y%m%d')

        docRef = db.collection(destination.name).document(docName)
        docRef.set(dailyDict)

        print(f'{destination.name} {docName}')
