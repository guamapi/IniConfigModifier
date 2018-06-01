class IniConfigModifier:
	def __init__(self,file_path):
		self.setting_list=[]
		self.file_path=file_path

		f=open(self.file_path,"r")
		fl=f.readlines()
		line_count=0
		'''
		for e in setting_list
		e[0] is setting field
		e[1] is setting line number
		e[2] is setting value
		'''
		for l in fl:
			if "=" in l:
				line_count+=1
				key=l.split("=")[0]
				value=l[len(key)+1:len(l)-1]
				self.setting_list.append([key,line_count,value])
			else:
				line_count+=1
				self.setting_list.append([l,line_count,"not_setting"])

	def set_fullscreen(self,value=0):
		v=str(value)
		self.replace("fullscreenmode",v)
		self.replace("preferredfullscreenmode",v)

	def set_resolution(self,axis_x=1280,axis_y=720):
		x=str(axis_x)
		y=str(axis_y)
		self.replace("resolutionsizex",x)
		self.replace("resolutionsizey",y)

	def set_graphics_quality(self,quality="Epic"):
		'''
		Epic: 3
		High: 2
		Med: 1
		LOW: 0
		'''
		n=""
		if str(quality).lower()=="epic":
			n="3"
		elif str(quality).lower()=="high":
			n="2"
		elif str(quality).lower()=="med":
			n="1"
		elif str(quality).lower()=="low":
			n="0"

		self.replace("sg.ViewDistanceQuality",n)
		self.replace("sg.AntiAliasingQuality",n)
		self.replace("sg.ShadowQuality",n)
		self.replace("sg.PostProcessQuality",n)
		self.replace("sg.TextureQuality",n)
		self.replace("sg.EffectsQuality",n)
		self.replace("sg.FoliageQuality",n)

	def replace(self,IN,value):

		a=self.setting_list
		#replace by line number 
		if IN.isdigit():
			if self.out_of_range(IN):
				print ("Line number not exist")
			else:
				for l in a:
					if str(l[1])==IN:
						l[2]=value
		#replace by setting
		else:
			if self.not_exist(IN):
				print ("Setting not exist")
			else:
				for l in a:
					if l[0].lower()==IN.lower():
						l[2]=value

		f=open(self.file_path,"w")
		for l in a:
			if l[2]=="not_setting":
				s=l[0]
			else:
				s=l[0]+"="+l[2]+"\r\n"
			f.write(s)
	
	#true if input value not exist
	def not_exist(self,IN):
		exist=False
		for l in self.setting_list:
			if l[0].lower()==IN.lower():
				exist=True
				break
		return not exist

	#true if input number out of range
	def out_of_range(self,IN):
		outofrange=True
		if int(IN)<=len(self.setting_list):
			outofrange=False
		return outofrange


l=GameSettingConfig("test.ini")

#l.replace("test","2")

#l.set_graphics_quality("low")
#l.set_resolution(156,283)
#l.set_fullscreen(2)
