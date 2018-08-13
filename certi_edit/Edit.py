from PIL import Image,ImageDraw,ImageFont
import pandas as pd
def func():
	df = pd.read_excel(io="Info.xlsx",sheet_name="Sheet1")
	font_type1=ImageFont.truetype("Coval-Black.ttf", 80)
	font_type2=ImageFont.truetype("Coval-Black.ttf", 40)
	for i in range(len(df["NAME"])):
		image = Image.open("sample.jpg")
		draw = ImageDraw.Draw(image)
		draw.text(xy=(800,690),text=df.NAME[i],fill=(0,0,0),font=font_type1)
		draw.text(xy=(580,1350),text=df.CODE[i],fill=(0,0,0),font=font_type2)
		draw.text(xy=(500,1440),text=str(df.ISSUE_DATE[i]),fill=(0,0,0),font=font_type2)
		draw.text(xy=(1000,1200),text=str(df.START_DATE[i]),fill=(0,0,0),font=font_type2)
		draw.text(xy=(1300,1200),text=str(df.END_DATE[i]),fill=(0,0,0),font=font_type2)
		image.show()