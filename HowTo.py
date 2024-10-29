By TMP4
Open root/intrologin.py
Search for:
##########################

import uiScriptLocale

add after:
##########################

# INTERACTIVE_LOGIN
import background
import grp
INTERACTIVE_LOGIN = 1 # ENABLE 1 DISABLE 0
# INTERACTIVE_LOGIN END

Search for: 
##########################

app.ShowCursor()

add before:
##########################

		if INTERACTIVE_LOGIN == 1: # INTERACTIVE_LOGIN
			self.LoadMap()

Search for:
##########################

def Close(self):

add before:
##########################

	# INTERACTIVE_LOGIN
	def LoadMap(self):
		environments = [
			{'x' : 469600,'y': 953500, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 105.0, 'height' : 40.0, 'snow' : 0 },	#a1
			{'x' : 360800,'y': 877600, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 255.0, 'height' : 40.0, 'snow' : 0 },	#a3
			{'x' : 62400,'y': 167900, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 10.0, 'height' : 40.0, 'snow' : 0 },		#b1
			{'x' : 143000,'y': 237700, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 110.0, 'height' : 40.0, 'snow' : 0 },	#b3
			{'x' : 958600,'y': 263700, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 155.0, 'height' : 40.0, 'snow' : 0 },	#c1
			{'x' : 861200,'y': 243800, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 125.0, 'height' : 40.0, 'snow' : 0 },	#c3
			{'x' : 896400,'y': 21500, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 225.0, 'height' : 40.0, 'snow' : 0 },	#ox
			{'x' : 232600,'y': 521200, 'dis' : 2500.0, 'pit' : 10.0, 'rot' : 30.0, 'height' : 40.0, 'snow' : 0 },	#desert
			{'x' : 1106200,'y': 53600, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 90.0, 'height' : 40.0, 'snow' : 0 },	#trent2
			{'x' : 338900,'y': 754100, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 310.0, 'height' : 40.0, 'snow' : 0 },	#ork
			{'x' : 433800,'y': 170700, 'dis' : 2500.0, 'pit' : 10.0, 'rot' : 343.0, 'height' : 40.0, 'snow' : 1 },	#snow
			{'x' : 601700,'y': 707300, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 90.0, 'height' : 40.0, 'snow' : 0 },	#flame
			{'x' : 1104800,'y': 1783900, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 175.0, 'height' : 40.0, 'snow' : 0 },	#cape
			{'x' : 1057200,'y': 1622100, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 12.0, 'height' : 40.0, 'snow' : 0 },	#bay
			{'x' : 1175900,'y': 1584300, 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 360.0, 'height' : 40.0, 'snow' : 0 },	#thunder
			{'x' : 1277800,'y': 1741300, 'dis' : 2500.0, 'pit' : -15.0, 'rot' : 1.0, 'height' : 40.0, 'snow' : 0 },	#dawn
			{'x' : 885440 ,'y': 102400 , 'dis' : 2500.0, 'pit' : 5.0, 'rot' : 300.0, 'height' : 40.0, 'snow' : 0 },	#monkeyboss
		]
		map_random = environments[app.GetRandom(0,len(environments)-1)]
		app.SetCamera(map_random['dis'], map_random['pit'], map_random['rot'], map_random['height'])
		net.Warp(map_random['x'], map_random['y']);
		
		background.SetViewDistanceSet(background.DISTANCE0, 25600)
		"""
		background.SetViewDistanceSet(background.DISTANCE1, 19200)
		background.SetViewDistanceSet(background.DISTANCE2, 12800)
		background.SetViewDistanceSet(background.DISTANCE3, 9600)
		background.SetViewDistanceSet(background.DISTANCE4, 6400)
		"""
		background.SelectViewDistanceNum(background.DISTANCE0)
		
		if map_random['snow'] == 1:
			background.EnableSnow(1)
		
		# From 21:00 to 5:59 the environment will set to night. Remove this part if you don't need it.
		h = time.localtime()[3]
		if h <= 5 or h >= 21: 
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT) 
			background.SetEnvironmentData(1)
		else:
			background.SetEnvironmentData(0)
		
		self.GetChild("bg1").Hide()
		self.GetChild("bg2").Hide()
		
	def OnRender(self):
		if INTERACTIVE_LOGIN == 1:
			app.RenderGame()
			grp.PopState()
			grp.SetInterfaceRenderState()
		
	# INTERACTIVE_LOGIN END

Search for:
##########################

ServerStateChecker.Update()

add after:
##########################

		if INTERACTIVE_LOGIN == 1: # INTERACTIVE_LOGIN
			app.UpdateGame()

Search for:
##########################

app.HideCursor()

add afer:
##########################

		if INTERACTIVE_LOGIN == 1: # INTERACTIVE_LOGIN
			background.Destroy()