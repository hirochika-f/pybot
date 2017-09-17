# _*_coding: utf-8_*_

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from plugins.scripts.confirm_weather import ConfirmWeather

@respond_to('(.雨*)')
def confirm_weather(message, something):
  weather_class = ConfirmWeather()
  weather_class.return_rainfall(message)
