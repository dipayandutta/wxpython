# Example of creation of menus and toolbars

import wx

class MenuExample(wx.Frame):

    def __init__(self,parent,title):
        super(MenuExample,self).__init__(parent,title=title,size=(350,230))
        self.initUI()


    def initUI(self):

        menubar = wx.MenuBar()
        fileMenu  = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT,'Quit','Quit Application')
        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
        self.Centre()

    def OnQuit(self,e):
        self.Close()


def main():
    app = wx.App(redirect=False)
    frame = MenuExample(None,title="Menu Example")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
        
