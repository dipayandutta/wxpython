import wx

class Example08(wx.Frame):
	def __init__(self,parent,title):
		super(Example08,self).__init__(parent,title=title,size=(350,230))
		self.initUI()

	def initUI(self):

		menubar = wx.MenuBar()

		fileMenu = wx.Menu()
		fileMenu.Append(wx.ID_NEW,'&MEW')
		fileMenu.Append(wx.ID_OPEN,'&Open')
		fileMenu.Append(wx.ID_SAVE,'&Save')
		fileMenu.AppendSeparator()

		imp = wx.Menu()
		imp.Append(wx.ID_ANY,'Import News Fedd ...')
		imp.Append(wx.ID_ANY,'Import bookmarks...')
		imp.Append(wx.ID_ANY,'Import mail ...')

		fileMenu.AppendMenu(wx.ID_ANY,'I&mport',imp)

		quit = wx.MenuItem(fileMenu,wx.ID_EXIT,'&Quit')
		fileMenu.AppendItem(quit)


		self.Bind(wx.EVT_MENU,self.OnQuit,quit)

		menubar.Append(fileMenu,'&File')
		self.SetMenuBar(menubar)


		TestMenu = wx.Menu() # Creating a New Menu 
		# Creating two menu Items
		TestMenu.Append(wx.ID_ANY,'Menu1')
		TestMenu.Append(wx.ID_ANY,'Menu2')
		# Creating a Menu Item with an action 

		print_msg = wx.MenuItem(TestMenu,wx.ID_ANY,'&Print')
		TestMenu.Append(print_msg)

		#Bind the Menu Item Action
		self.Bind(wx.EVT_MENU,self.OnClick,print_msg)

		menubar.Append(TestMenu,'&TEST') # Displaying the new menu in the MenuBar



		self.SetSize((350,230))
		self.Centre()

	def OnQuit(self,e):
		self.Close()

	# Method to perform the print function 
	def OnClick(self,e):
		print("Item Clicked...")

def main():
	application = wx.App(redirect=False)
	obj = Example08(None,title='MenuBar Example')
	obj.Show()
	application.MainLoop()


if __name__ == '__main__':
	main()