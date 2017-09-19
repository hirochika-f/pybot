# _*_coding: utf-8_*_

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from plugins.scripts.hour_rain import HourRainS
from plugins.scripts.hour_rain import HourRainE

@respond_to('(^雨海老名$)')
def confirm_weather(message, something):
  weather_class = HourRainE()
  weather_class.return_rainfall(message)

@respond_to('(^雨$)')
def confirm_weather(message, something):
  weather_class = HourRainS()
  weather_class.return_rainfall(message)
