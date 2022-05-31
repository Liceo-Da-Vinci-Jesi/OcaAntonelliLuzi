import wx
import csv

import random

class Domanda(wx.Frame):
    def __init__(self,giocatore):
        super().__init__(None,title="Domanda")
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#b3ffb3")
        
        self.giocatore=giocatore
        self.punteggio=0
        
        linea1 = wx.StaticLine(panel, pos=(276,0), size=(5,450))
        linea2 = wx.StaticLine(panel, pos=(282,0), size=(5,450))
        linea1.SetBackgroundColour("#85e085")
        self.d=wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.TE_READONLY,pos=(310,50), size=(300,50))
        immagine = wx.Bitmap("images/casaLeopardi.jpeg")
        viewer = wx.StaticBitmap(panel, bitmap=immagine)
        
        self.risposta1 = wx.CheckBox(panel, label="", pos=(320,125), size=(250,40))
        self.risposta1.Bind(wx.EVT_CHECKBOX, self.Risposta1)
        
        self.risposta2 = wx.CheckBox(panel, label="", pos=(320,170),size=(250,40))
        self.risposta2.Bind(wx.EVT_CHECKBOX, self.Risposta2)
        
        self.risposta3 = wx.CheckBox(panel, label="", pos=(320,215),size=(250,40))
        self.risposta3.Bind(wx.EVT_CHECKBOX, self.Risposta3)
        
        self.conferma=wx.Button(panel,label="Conferma",pos=(550,375),size=(80,20))
        self.conferma.Hide()
        self.conferma.Bind(wx.EVT_BUTTON,self.risposta)
        
        self.giusta=wx.StaticText(panel,label="")
        self.giusta.Hide()
         
        font3=wx.Font(10, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        font4=wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
         
        self.d.SetFont(font3)
        self.risposta1.SetFont(font4)
        self.risposta2.SetFont(font4)
        self.risposta3.SetFont(font4)
        
        self.Centre()
        self.SetMaxSize((650,447))
        self.SetMinSize((650,447))
        
    def Risposta1(self,evt):
        v=self.risposta1.GetValue()
        self.risposta2.SetValue(False)
        self.risposta3.SetValue(False)
        if v == True:
            self.conferma.Show()
        else:
            self.conferma.Hide()
        return
        
    def Risposta2(self,evt):
        v=self.risposta2.GetValue()
        self.risposta1.SetValue(False)
        self.risposta3.SetValue(False)
        if v == True:
            self.conferma.Show()
        else:
            self.conferma.Hide()
        return
    
    def Risposta3(self,evt):
        v=self.risposta3.GetValue()
        self.risposta2.SetValue(False)
        self.risposta1.SetValue(False)
        if v == True:
            self.conferma.Show()
        else:
            self.conferma.Hide()
        return
    
    def risposta(self,evt):
        risp=""
        if self.risposta1.GetValue() == True:
            risp=self.risposta1.GetLabel()
        if self.risposta2.GetValue() == True:
            risp=self.risposta2.GetLabel()
        if self.risposta3.GetValue() == True:
            risp=self.risposta3.GetLabel()
        if risp != self.giusta.GetLabel():
            dial = wx.MessageDialog(None, "Risposta errata!", "Errore", wx.OK | wx.ICON_ERROR)
            r = dial.ShowModal()
            self.Close()
            return
        
        dial = wx.MessageDialog(None, "Risposta giusta!", "Non errore", wx.OK)
        dial.ShowModal()
        self.giocatore.punteggio += self.punteggio
        self.Close()
        return




