import wx

class CheckBoxApplication(wx.Frame):

	def __init__(self,parent,title):
		super(CheckBoxApplication,self).__init__(parent,title=title,size=(350,300))
		self.initUI()

	def initUI(self):

		panel01 = wx.Panel(self)

		self.Apple 	= wx.CheckBox(panel01,label='Apple',pos=(10,10))
		self.Orange	= wx.CheckBox(panel01,label='Orange',pos=(20,20))
		self.Bananna= wx.CheckBox(panel01,label='Bananna',pos=(30,30))

		self.Bind(wx.EVT_CHECKBOX,self.onChecked)
		self.Centre()

	def onChecked(self,e):
		cb = e.GetEventObject()
		print (cb.GetLabel(),'is Clicked',cb.GetValue())


def main():
	application = wx.App()
	obj = CheckBoxApplication(None,title='Check Box')
	obj.Show()
	application.MainLoop()

if __name__ == '__main__':
	main()
