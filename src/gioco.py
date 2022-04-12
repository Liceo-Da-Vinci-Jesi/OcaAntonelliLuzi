#4 AS
#Gioco dell'oca

import wx

class Finestra(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco dell'oca")
        panel = wx.Panel(self)
        bmp = wx.Bitmap("tabellone.jpg")
        panel.SetBackgroundImage(bmp)
        
        self.Centre()
        
# ----------------------------------------

if __name__ == "__main__":
    app = wx.App()
    window = Finestra()
    window.Show()
    app.MainLoop() 