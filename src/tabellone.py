import wx

import time
import random

import caselle
from domanda import Domanda
import ElencoDomande



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
        self.SetMaxSize((1280,780))
        self.SetMinSize((1280,780))
    
    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
        self.pedine()
        ElencoDomande.load()
                
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
                self.giocatore=self.listaGiocatori[0]
                c=self.giocatore.casella
                p=self.viewer1
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos1[x+1])
                    time.sleep(1)
                    (self.giocatore.casella)+=1
                self.controllo()
                return
            if self.turno==1:
                self.giocatore=self.listaGiocatori[1]
                c=self.giocatore.casella
                p=self.viewer2
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos2[x+1])
                    time.sleep(1)
                    (self.giocatore.casella)+=1
                self.controllo()
                return
            if self.turno==2:
                self.giocatore=self.listaGiocatori[2]
                c=self.giocatore.casella
                p=self.viewer3
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos3[x+1])
                    time.sleep(1)
                    (self.giocatore.casella)+=1
                self.controllo()
                return
            if self.turno==3:
                self.giocatore=self.listaGiocatori[3]
                c=self.giocatore.casella
                p=self.viewer4
                self.turno+=1
                for x in range(c,c+d):
                    p.SetPosition(caselle.pos4[x+1])
                    time.sleep(1)
                    (self.giocatore.casella)+=1
                self.controllo()
                return
    
    def controllo(self):
        self.domanda=Domanda()
        c=self.giocatore.casella
        if c in caselle.listaBiografia:
            if c==1:
                m=len(ElencoDomande.domandeRecanati)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeRecanati[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeRecanati.remove(domandaEstratta)
                return
            if c==8:
                m=len(ElencoDomande.domandeRoma)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeRoma[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeRoma.remove(domandaEstratta)
                return
            if c==14:
                m=len(ElencoDomande.domandeMilano)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeMilano[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeMilano.remove(domandaEstratta)
                return
            if c==21:
                m=len(ElencoDomande.domandeBologna)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeBologna[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeBologna.remove(domandaEstratta)
                return
            if c==27:
                m=len(ElencoDomande.domandeFirenze)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeFirenze[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeFirenze.remove(domandaEstratta)
                return
            if c==33:
                m=len(ElencoDomande.domandePisa)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandePisa[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandePisa.remove(domandaEstratta)
                return
            if c==39:
                m=len(ElencoDomande.domandeNapoli)
                n=random.randint(1,m)
                domandaEstratta=ElencoDomande.domandeNapoli[n]
                self.domanda.Show()
                self.domanda.d.SetValue(domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeNapoli.remove(domandaEstratta)
                return
        if c in caselle.listaInfinito:
            self.giocatore.punteggio+=50
            return
        if c in caselle.listaCanti:
            m=len(ElencoDomande.domandeCanti)
            n=random.randint(1,m)
            domandaEstratta=ElencoDomande.domandeCanti[n]
            self.domanda.Show()
            self.domanda.d.SetValue(domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeCanti.remove(domandaEstratta)
            return
        if c in caselle.listaOperette:
            m=len(ElencoDomande.domandeOperette)
            n=random.randint(1,m)
            domandaEstratta=ElencoDomande.domandeOperette[n]
            self.domanda.Show()
            self.domanda.d.SetValue(domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeOperette.remove(domandaEstratta)
            return
        if c in caselle.listaZibaldone:
            m=len(ElencoDomande.domandeZibaldone)
            n=random.randint(1,m)
            domandaEstratta=ElencoDomande.domandeZibaldone[n]
            self.domanda.Show()
            self.domanda.d.SetValue(domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeZibaldone.remove(domandaEstratta)
            return
        if c in caselle.listaSiepe:
            if self.giocatore.punteggio < 50:
                self.giocatore.punteggio = 0
            else:
                self.giocatore.punteggio-=50
            return
        else:
            return
            
        
        
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()
