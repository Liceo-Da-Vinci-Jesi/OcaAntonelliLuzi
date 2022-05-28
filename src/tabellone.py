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
        self.pedina3=wx.Bitmap("images/pedina ridimensionata 3.png", wx.BITMAP_TYPE_PNG)
        self.viewer3 = wx.StaticBitmap(self, bitmap=self.pedina3,pos=(100,140))
        self.pedina4=wx.Bitmap("images/pedina ridimensionata 4.png", wx.BITMAP_TYPE_PNG)
        self.viewer4 = wx.StaticBitmap(self, bitmap=self.pedina4,pos=(145,140))
        
        self.pulsante=wx.Button(self,label="Tira dado",size=(100,100),pos=(800,400))
        self.pulsante.Bind(wx.EVT_BUTTON,self.posizione)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Centre()
        self.pedine()
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
    
    def pedine(self):
        self.numeroGiocatori=len(self.listaGiocatori)
        if self.numeroGiocatori == 2:
            self.viewer3.Hide()
            self.viewer4.Hide()
        if self.numeroGiocatori == 3:
            self.viewer4.Hide()
    
    def posizione(self,evt):
        if self.turno >= self.numeroGiocatori:
            self.turno=0
        d=random.randint(1,6)
        self.pulsante.SetLabel(str(d))
        self.numeroGiocatori=len(self.listaGiocatori)
        if self.turno < self.numeroGiocatori:
            if self.turno==0:
                giocatore=self.listaGiocatori[0]
                c=giocatore.casella
                p=self.viewer1
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos1[x+1])
                    time.sleep(1)
                    (giocatore.casella)+=1
                return
            if self.turno==1:
                giocatore=self.listaGiocatori[1]
                c=giocatore.casella
                p=self.viewer2
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos2[x+1])
                    time.sleep(1)
                    (giocatore.casella)+=1
                return
            if self.turno==2:
                giocatore=self.listaGiocatori[2]
                c=giocatore.casella
                p=self.viewer3
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos3[x+1])
                    time.sleep(1)
                    (giocatore.casella)+=1
                return
            if self.turno==3:
                giocatore=self.listaGiocatori[3]
                c=giocatore.casella
                p=self.viewer4
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos4[x+1])
                    time.sleep(1)
                    (giocatore.casella)+=1
                return
        
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()
