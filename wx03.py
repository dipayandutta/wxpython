import wx

class ThirdExample(wx.Frame):

    def __init__(self,parent,title):
        super(ThirdExample,self).__init__(parent,title=title,size=(350,250))



def main():
    app = wx.App()
    Example = ThirdExample(None,title='Third Example')
    Example.Show()
    app.MainLoop()    

if __name__ == '__main__':
    main()
