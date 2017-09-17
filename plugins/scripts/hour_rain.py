import urllib.request
import json

class HourRain():

  def __init__(self):

    # YahooAPI の URL
    base_url = "https://map.yahooapis.jp/weather/V1/place?"
    # 調べたい場所の経度緯度
    coordinates_shinyoko = "139.620759, 35.511117"
    # ClientID
    client_id = "dj00aiZpPW9rVEtPN3NOUHFHTSZzPWNvbnN1bWVyc2VjcmV0Jng9NWQ-"
    self.url = "%scoordinates=%s&appid=%s&output=json" % (base_url, coordinates_shinyoko, client_id)

  def return_rainfall(self, message):
    # urllib を使って対象 URL の内容をロード
    response = urllib.request.urlopen(self.url).read()
    # ロードした JSON
    data_json = json.loads(response.decode("utf-8"))
    weather_info = data_json['Feature'][0]['Property']['WeatherList']['Weather']
    base_minutes = 10

    for index, var in enumrate(weather_info):
        info = self.return_rain_level(var["Rainfall"])
        if index == 0:
          before_words = "今、"
          if var['Rainfall'] == 0.0:
            after_words = "っていない"
          else:
            after_words = "っている"

        else:
          before_words = '%s分後、' % (base_minutes)
          if var['Rainfall'] == 0.0:
            after_words = "らないだろう"
          else:
            after_words = "るだろう"
          base_minutes += 10

        message.send(before_words + info + after_words)


  def retrun_rain_level(self, rainfall):
    if (rainfall == 0.0):
      rain_level = "雨は降"
    elif (rainfall < 20.0):
      rain_level = "やや強い雨、ザーザーと降"
    elif (rainfall < 30.0):
      rain_level = "土砂降りで、傘をさしていてもぬれる雨が降"
    elif (rainfall < 50.0):
      rain_level = "傘持ってるか?バケツをひっくり返したように雨が降"
    elif (rainfall < 80.0):
      rain_level = "滝のように非常に激しい雨が降"
    elif (rainfall >= 80.0):
      rain_level = "すぐ帰れ!!息苦しくなるような圧迫感がある猛烈な雨が降"
    return rain_level