#4 AS
#Gioco dell'oca

import wx

class Giocatori(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco del paesaggio di Leopardi")
        panel = wx.Panel(self)
        

class Tabellone(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco del paesaggio di Leopardi")
        panel = wx.Panel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        header=wx.StaticText(self,label="Il gioco del paesaggio di Leopardi", style=wx.ALIGN_CENTER, size=(2170,100),pos=(0,0))
        font = wx.Font(60, wx.ROMAN, wx.BOLD, wx.NORMAL)
        header.SetFont(font)
        header.SetBackgroundColour("#53c653")
        sizer.Add(header)

        self.SetSizer(sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Centre()        
    
    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("tabellone.png")
        dc.DrawBitmap(bmp, 0, 0)

        
# ----------------------------------------

if __name__ == "__main__":
    app = wx.App()
    window = Gioco()
    window.Show()
    app.MainLoop()
    
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop() 