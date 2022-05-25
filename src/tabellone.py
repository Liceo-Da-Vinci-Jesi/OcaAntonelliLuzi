import wx

import time
import random

import caselle



class Tabellone(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco dei paesaggi di Giacomo")
        panel = wx.Panel(self)
        
        self.listaGiocatori = []
        self.turno = 0
        
        header=wx.StaticText(self,label="", size=(1280,20),pos=(0,0))
        header.SetBackgroundColour("#53c653")
        
        header2=wx.StaticText(self,label="", size=(1280,25),pos=(0,720))
        header2.SetBackgroundColour("#53c653")
        
        header3=wx.StaticText(self,label="", size=(20,780),pos=(0,0))
        header3.SetBackgroundColour("#53c653")
        
        header4=wx.StaticText(self,label="", size=(20,780),pos=(1245,0))
        header4.SetBackgroundColour("#53c653")
        
        self.pedina1=wx.Bitmap("images/pedina ridimensionata 1.png", wx.BITMAP_TYPE_PNG)
        self.viewer1 = wx.StaticBitmap(self, bitmap=self.pedina1,pos=(100,95))
        self.pedina2=wx.Bitmap("images/pedina ridimensionata 2.png", wx.BITMAP_TYPE_PNG)
        self.viewer2 = wx.StaticBitmap(self, bitmap=self.pedina2,pos=(145,95))
        
        
        self.pulsante=wx.Button(self,label="Tira dado",size=(100,100),pos=(800,400))
        self.pulsante.Bind(wx.EVT_BUTTON,self.posizione)

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
        bmp = wx.Bitmap("images/tabellone.png")
        dc.DrawBitmap(bmp, 0, 0)
        
    def posizione(self,evt):
        d=random.randint(1,6)
        
        # PROF: qui c'è da sistemare... servono le liste di questi oggetti. Oppure quattro funzioni che chiamate a seconda del turno
        p=self.viewer1
        giocatore=self.listaGiocatori[self.turno]
        c=giocatore.casella
        self.pulsante.SetLabel(str(d))
        for x in range(c,c+d):
            p.SetPosition(caselle.pos1[x+1])
            time.sleep(1)
        self.turno = (self.turno + 1) % len(self.listaGiocatori)
        
        
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()
