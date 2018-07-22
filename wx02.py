import wx

class Frame(wx.Frame):
    pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame(parent=None,title='Second Example')
        self.frame.Show()
        
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
        
