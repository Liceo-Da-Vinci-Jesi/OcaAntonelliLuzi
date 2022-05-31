import wx

import time
import random

import caselle
from domanda import Domanda
import ElencoDomande
import domanda



class Tabellone(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco dei paesaggi di Giacomo")
        panel = wx.Panel(self)
        
        self.listaGiocatori = []
        self.turno = 0
        
        ElencoDomande.load()
        
        self.punteggio1=wx.StaticText(self,label="",size=(150,160),pos=(180,400))
        self.punteggio1.SetBackgroundColour("#53c653")
        self.punteggio2=wx.StaticText(self,label="",size=(150,160),pos=(330,400))
        self.punteggio2.SetBackgroundColour("#53c653")
        self.punteggio3=wx.StaticText(self,label="",size=(150,160),pos=(480,400))
        self.punteggio3.SetBackgroundColour("#53c653")
        self.punteggio4=wx.StaticText(self,label="",size=(150,160),pos=(630,400))
        self.punteggio4.SetBackgroundColour("#53c653")
        
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
                    self.punteggi()
                self.controllo()
                self.punteggi()
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
                    self.punteggi()
                self.controllo()
                self.punteggi()
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
                    self.punteggi()
                self.controllo()
                self.punteggi()
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
                    self.punteggi()
                self.controllo()
                self.punteggi()
                return
    
    def controllo(self):
        self.domanda=Domanda()
        c=self.giocatore.casella
        if c in caselle.listaBiografia:
            if c==1:
                m=len(ElencoDomande.domandeRecanati)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeRecanati[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeRecanati.remove(self.domandaEstratta)
                return
            if c==8:
                m=len(ElencoDomande.domandeRoma)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeRoma[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeRoma.remove(self.domandaEstratta)
                return
            if c==14:
                m=len(ElencoDomande.domandeMilano)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeMilano[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeMilano.remove(self.domandaEstratta)
                return
            if c==21:
                m=len(ElencoDomande.domandeBologna)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeBologna[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeBologna.remove(self.domandaEstratta)
                return
            if c==27:
                m=len(ElencoDomande.domandeFirenze)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeFirenze[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeFirenze.remove(self.domandaEstratta)
                return
            if c==33:
                m=len(ElencoDomande.domandePisa)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandePisa[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandePisa.remove(self.domandaEstratta)
                return
            if c==39:
                m=len(ElencoDomande.domandeNapoli)
                n=random.randint(0,m-1)
                self.domandaEstratta=ElencoDomande.domandeNapoli[n]
                self.domanda.Show()
                self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
                self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
                self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
                self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
                self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
                ElencoDomande.domandeNapoli.remove(self.domandaEstratta)
                return
        if c in caselle.listaInfinito:
            self.giocatore.punteggio+=50
            return
        if c in caselle.listaCanti:
            m=len(ElencoDomande.domandeCanti)
            n=random.randint(0,m-1)
            self.domandaEstratta=ElencoDomande.domandeCanti[n]
            self.domanda.Show()
            self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeCanti.remove(self.domandaEstratta)
            return
        if c in caselle.listaOperette:
            m=len(ElencoDomande.domandeOperette)
            n=random.randint(0,m-1)
            self.domandaEstratta=ElencoDomande.domandeOperette[n]
            self.domanda.Show()
            self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeOperette.remove(self.domandaEstratta)
            return
        if c in caselle.listaZibaldone:
            m=len(ElencoDomande.domandeZibaldone)
            n=random.randint(0,m-1)
            self.domandaEstratta=ElencoDomande.domandeZibaldone[n]
            self.domanda.Show()
            self.domanda.d.SetValue(self.domandaEstratta["Domanda"])
            self.domanda.risposta1.SetLabel(self.domandaEstratta["Risposta a"])
            self.domanda.risposta2.SetLabel(self.domandaEstratta["Risposta b"])
            self.domanda.risposta3.SetLabel(self.domandaEstratta["Risposta c"])
            self.domanda.giusta.SetLabel(self.domandaEstratta["Risposta giusta"])
            ElencoDomande.domandeZibaldone.remove(self.domandaEstratta)
            return
        if c in caselle.listaSiepe:
            if self.giocatore.punteggio < 50:
                ElencoDomande.g=""
                self.giocatore.punteggio = 0
            else:
                self.giocatore.punteggio-=50
                ElencoDomande.g=""
            return
        else:
            ElencoDomande.g=""
            return
        
    def punteggi(self):
        if len(self.listaGiocatori) == 2:
            g1=self.listaGiocatori[0]
            n1=g1.nome
            p1=g1.punteggio
            c1=g1.casella
            stringa=n1 + "\n\nPunteggio:" + str(p1) + "\n\nCasella:" + str(c1)
            self.punteggio1.SetLabel(stringa)
            g2=self.listaGiocatori[1]
            n2=g2.nome
            p2=g2.punteggio
            c2=g2.casella
            stringa=n2 + "\n\nPunteggio:" + str(p2) + "\n\nCasella:" + str(c2)
            self.punteggio2.SetLabel(stringa)
        if len(self.listaGiocatori) == 3:
            g1=self.listaGiocatori[0]
            n1=g1.nome
            p1=g1.punteggio
            c1=g1.casella
            stringa=n1 + "\n\nPunteggio:" + str(p1) + "\n\nCasella:" + str(c1)
            self.punteggio1.SetLabel(stringa)
            g2=self.listaGiocatori[1]
            n2=g2.nome
            p2=g2.punteggio
            c2=g2.casella
            stringa=n2 + "\n\nPunteggio:" + str(p2) + "\n\nCasella:" + str(c2)
            self.punteggio2.SetLabel(stringa)
            g3=self.listaGiocatori[2]
            n3=g3.nome
            p3=g3.punteggio
            c3=g3.casella
            stringa=n3 + "\n\nPunteggio:" + str(p3) + "\n\nCasella:" + str(c3)
            self.punteggio3.SetLabel(stringa)
        if len(self.listaGiocatori) == 4:
            g1=self.listaGiocatori[0]
            n1=g1.nome
            p1=g1.punteggio
            c1=g1.casella
            stringa=n1 + "\n\nPunteggio:" + str(p1) + "\n\nCasella:" + str(c1)
            self.punteggio1.SetLabel(stringa)
            g2=self.listaGiocatori[1]
            n2=g2.nome
            p2=g2.punteggio
            c2=g2.casella
            stringa=n2 + "\n\nPunteggio:" + str(p2) + "\n\nCasella:" + str(c2)
            self.punteggio2.SetLabel(stringa)
            g3=self.listaGiocatori[2]
            n3=g3.nome
            p3=g3.punteggio
            c3=g3.casella
            stringa=n3 + "\n\nPunteggio:" + str(p3) + "\n\nCasella:" + str(c3)
            self.punteggio3.SetLabel(stringa)
            g4=self.listaGiocatori[3]
            n4=g4.nome
            p4=g4.punteggio
            c4=g4.casella
            stringa=n4 + "\n\nPunteggio:" + str(p4) + "\n\nCasella:" + str(c4)
            self.punteggio4.SetLabel(stringa)
        
        
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()
