#4 AS
#Gioco dell'oca

import wx

# class Giocatori(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title="Gioco del paesaggio di Leopardi")
#         panel = wx.Panel(self)
#         
#         vbox=wx.BoxSizer(wx.VERTICAL)
#         
#         hbox1=wx.BoxSizer(wx.HORIZONTAL)
#         
#         header=wx.StaticText(self,label="Scegli la tua pedina", style=wx.ALIGN_CENTER,size=(1280,85))
#         font = wx.Font(48, wx.ROMAN, wx.BOLD, wx.NORMAL)
#         header.SetFont(font)
#         header.SetBackgroundColour("#53c653")
#         hbox1.Add(header)
#         
#         vbox.Add(hbox1)
#         
#         bag=wx.GridBagSizer(4,4)
#         icona1=wx.ToggleButton(self,label="Icona 1")
#         bag.Add(icona1,pos=(0,0),span=(1,0),flag=wx.EXPAND,border=10)
#         icona2=wx.ToggleButton(self,label="Icona 2")
#         bag.Add(icona2,pos=(0,1),span=(1,1))
#         icona3=wx.ToggleButton(self,label="Icona 3")
#         bag.Add(icona3,pos=(0,2),span=(1,2))
#         icona4=wx.ToggleButton(self,label="Icona 4")
#         bag.Add(icona4,pos=(0,3),span=(1,4))
# 
#         vbox.Add(bag,flag=wx.EXPAND,border=10)
#         
#         self.Centre()
#         self.SetSizer(vbox)
#         self.SetMaxSize((1280,720))
#         self.SetMinSize((1280,720))
        

class Tabellone(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco del paesaggio di Leopardi")
        panel = wx.Panel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        header=wx.StaticText(self,label="", size=(1280,20),pos=(0,0))
        header.SetBackgroundColour("#53c653")
        
        header2=wx.StaticText(self,label="", size=(1280,25),pos=(0,720))
        header2.SetBackgroundColour("#53c653")
        
        header3=wx.StaticText(self,label="", size=(20,780),pos=(0,0))
        header3.SetBackgroundColour("#53c653")
        
        header4=wx.StaticText(self,label="", size=(20,780),pos=(1245,0))
        header4.SetBackgroundColour("#53c653")

        self.SetSizer(sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Centre()
        self.SetMaxSize((1280,780))
        self.SetMinSize((1280,780))
    
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
#     app = wx.App()
#     window = Giocatori()
#     window.Show()
#     app.MainLoop()
    
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop() 