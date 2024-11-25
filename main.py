from Upscayl import MainPage
import time


app = MainPage()

app.start_upscayl('00025-image.jpg')
time.sleep(8)
app.close_upscayl('отключить upscayl')
