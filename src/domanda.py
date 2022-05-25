import wx
import Gioco as g


class Domanda(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Domanda")
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#b3ffb3")
        
        
        
        linea1 = wx.StaticLine(panel, pos=(276,0), size=(5,450))
        linea2 = wx.StaticLine(panel, pos=(282,0), size=(5,450))
        linea1.SetBackgroundColour("#85e085")
        self.domanda=wx.StaticText(panel,label="- Qual è l'ultima opera che Leopardi compone prima\n   di lasciare Recanati per sempre?",pos=(310,50), size=(300,50))
        immagine = wx.Bitmap("images/casaLeopardi.jpeg")
        viewer = wx.StaticBitmap(panel, bitmap=immagine)
        
        self.risposta1 = wx.CheckBox(panel, label="Operette morali", pos=(340,125))
        self.risposta1.Bind(wx.EVT_CHECKBOX, self.Risposta)
        
        self.risposta2 = wx.CheckBox(panel, label="Grandi idilli", pos=(340,150))
        self.risposta2.Bind(wx.EVT_CHECKBOX, self.Risposta)
        
        self.risposta3 = wx.CheckBox(panel, label="Zibaldone", pos=(340,175))
        self.risposta3.Bind(wx.EVT_CHECKBOX, self.Risposta)
        
         
        font3=wx.Font(10, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        font4=wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
         
        self.domanda.SetFont(font3)
        self.risposta1.SetFont(font4)
        self.risposta2.SetFont(font4)
        self.risposta3.SetFont(font4)
        
        self.Centre()
        self.SetMaxSize((650,447))
        self.SetMinSize((650,447))
        
    def Risposta(self,evt):
        if self.risposta1.GetValue():
            self.risposta2.SetValue(False)
            self.risposta3.SetValue(False)
        if self.risposta2.GetValue():
            self.risposta1.SetValue(False)
            self.risposta3.SetValue(False)
        if self.risposta3.GetValue():
            self.risposta2.SetValue(False)
            self.risposta1.SetValue(False)
        
            
            
            return

if __name__ == "__main__":
    app = wx.App()
    window = Scelta() #qui ci va messo "Scelta" o "Domanda"
    window.Show()
    app.MainLoop()