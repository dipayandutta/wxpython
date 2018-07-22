import wx

class Position(wx.Frame):

	def __init__(self,parent,title):
		super(Position,self).__init__(parent,title=title,size=(350,230))
		self.initUI()


	def initUI(self):

		self.panel = wx.Panel(self)

		self.panel.SetBackgroundColour("gray")
		self.LoadImage()
		self.Centre()

		self.chick.SetPosition((20,20))
		self.kitten.SetPosition((40,160))
		self.DOg.SetPosition((170,50))

	def LoadImage(self):
		self.chick = wx.StaticBitmap(self.panel,wx.ID_ANY,wx.Bitmap("chick.jpg",wx.BITMAP_TYPE_ANY))
		self.kitten = wx.StaticBitmap(self.panel,wx.ID_ANY,wx.Bitmap("kitten.jpg",wx.BITMAP_TYPE_ANY))
		self.DOg = wx.StaticBitmap(self.panel,wx.ID_ANY,wx.Bitmap("DOg.jpg",wx.BITMAP_TYPE_ANY))


def main():
	application = wx.App()
	object = Position(None,title='Layout Example')
	object.Show()
	application.MainLoop()


if __name__ == '__main__':
	main()