import wx

class CentreWindow(wx.Frame):

    def __init__(self,parent,title):
        super(CentreWindow,self).__init__(parent,title=title,size=(350,230))
        self.Centre()


def main():

    app = wx.App()
    obj = CentreWindow(None,title='Centre Window')
    obj.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
