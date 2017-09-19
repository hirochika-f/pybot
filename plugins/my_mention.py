# _*_coding: utf-8_*_

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from plugins.scripts.hour_rain import HourRain

#@respond_to('(雨海老名)')
#def confirm_weather_e(message, something):
#  weather_class = HourRain(mode="e")
#  weather_class.return_rainfall(message)

@respond_to('(^雨$)')
def confirm_weather(message, something):
  weather_class = HourRain()
  weather_class.return_rainfall(message)
