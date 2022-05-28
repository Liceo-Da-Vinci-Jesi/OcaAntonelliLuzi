#Gioco dell'oca classi
import wx

from scelta import Scelta
from tabellone import Tabellone
from giocatore import Giocatore


class Gioco:
    def __init__(self):
        
        self.listaGiocatori = []
        
        self.schermataIniziale = Scelta()
        self.schermataIniziale.pulsante1.Bind(wx.EVT_BUTTON,self.persona1)
        self.schermataIniziale.pulsante2.Bind(wx.EVT_BUTTON,self.persona2)
        self.schermataIniziale.pulsante3.Bind(wx.EVT_BUTTON,self.persona3)
        self.schermataIniziale.pulsante4.Bind(wx.EVT_BUTTON,self.persona4)
        self.schermataIniziale.pulsantestart.Bind(wx.EVT_BUTTON,self.start)

        self.tabellone = Tabellone()
        
        self.schermataIniziale.Show()

    def persona1(self,evt):
        v = self.schermataIniziale.nome1.GetValue()
        if v != "":
            nome=v
            icona=self.schermataIniziale.bmp1
            pos=(100,95)
            giocatore1 = Giocatore(nome,icona,pos)
            self.listaGiocatori.append(giocatore1)
            
            self.schermataIniziale.text.SetLabel("Benvenuto " + nome)
            self.schermataIniziale.icona1.Disable()
            self.schermataIniziale.nome1.Disable()
            self.schermataIniziale.pulsante1.Disable()
            self.schermataIniziale.conta += 1
            if self.schermataIniziale.conta >= 2:
                self.schermataIniziale.pulsantestart.Show()
        else:
            self.schermataIniziale.text.SetLabel("Non hai inserito il nome!")

    def persona2(self,evt):
        v = self.schermataIniziale.nome2.GetValue()
        if v != "":
            nome=v
            icona=self.schermataIniziale.bmp2
            pos=(130,95)
            giocatore2 = Giocatore(nome,icona,pos)
            self.listaGiocatori.append(giocatore2)
            
            self.schermataIniziale.text.SetLabel("Benvenuto " + nome)
            self.schermataIniziale.icona2.Disable()
            self.schermataIniziale.nome2.Disable()
            self.schermataIniziale.pulsante2.Disable()
            self.schermataIniziale.conta += 1
            if self.schermataIniziale.conta >= 2:
                self.schermataIniziale.pulsantestart.Show()
        else:
            self.schermataIniziale.text.SetLabel("Non hai inserito il nome!")
            
    def persona3(self,evt):
        v = self.schermataIniziale.nome3.GetValue()
        if v != "":
            nome=v
            icona=self.schermataIniziale.bmp3
            pos=(100,140)
            giocatore3 = Giocatore(nome,icona,pos)
            self.listaGiocatori.append(giocatore3)
            
            self.schermataIniziale.text.SetLabel("Benvenuto " + nome)
            self.schermataIniziale.icona3.Disable()
            self.schermataIniziale.nome3.Disable()
            self.schermataIniziale.pulsante3.Disable()
            self.schermataIniziale.conta += 1
            if self.schermataIniziale.conta >= 2:
                self.schermataIniziale.pulsantestart.Show()
        else:
            self.schermataIniziale.text.SetLabel("Non hai inserito il nome!")
            
    def persona4(self,evt):
        v = self.schermataIniziale.nome4.GetValue()
        if v != "":
            nome=v
            icona=self.schermataIniziale.bmp4
            pos=(130,140)
            giocatore4 = Giocatore(nome,icona,pos)
            self.listaGiocatori.append(giocatore4)
            
            self.schermataIniziale.text.SetLabel("Benvenuto " + nome)
            self.schermataIniziale.icona4.Disable()
            self.schermataIniziale.nome4.Disable()
            self.schermataIniziale.pulsante4.Disable()
            self.schermataIniziale.conta += 1
            if self.schermataIniziale.conta >= 2:
                self.schermataIniziale.pulsantestart.Show()
        else:
            self.schermataIniziale.text.SetLabel("Non hai inserito il nome!")


    def start(self,evt):
        self.schermataIniziale.Close()
        self.tabellone.listaGiocatori = self.listaGiocatori
        self.tabellone.Show()


if __name__ == "__main__":
    app = wx.App()
    g = Gioco()
    app.MainLoop()
