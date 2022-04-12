#4 AS
#Gioco dell'oca

import wx

class Finestra(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco del paesaggio di Leopardi")
        panel = wx.Panel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
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
    window = Finestra()
    window.Show()
    app.MainLoop() 