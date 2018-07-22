import wx
import os

class LabelExample(wx.Frame):

    def __init__(self,parent,title):
        super(LabelExample,self).__init__(parent,title=title,size=(350,230))
        self.labelShow()
        self.Centre()

    def labelShow(self):
        pwd = os.getcwd()
        #text = wx.StaticText(self,label="Hello World!")
        pwd_text = wx.StaticText(self,label="Current Working Directory"+pwd)

def main():
    app = wx.App(redirect=False)
    frame = LabelExample(None,title="Label Example")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
