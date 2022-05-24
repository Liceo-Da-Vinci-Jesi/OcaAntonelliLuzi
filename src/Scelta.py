import wx
import Gioco as g


class Scelta(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Gioco dei paesaggi di Giacomo")
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#b3ffb3")
        
        self.conta=0
        
        header=wx.StaticText(panel,label="Scegli la tua pedina", style=wx.ALIGN_CENTER,pos=(0,0),size=(1280,85))
        font1 = wx.Font(48, wx.ROMAN, wx.BOLD, wx.NORMAL)
        header.SetFont(font1)
        header.SetBackgroundColour("#53c653")
        
        bmp1 = wx.Bitmap("images/Pedina 1.png", wx.BITMAP_TYPE_PNG)
        bmp2 = wx.Bitmap("images/Pedina 2.png", wx.BITMAP_TYPE_PNG)
        bmp3 = wx.Bitmap("images/Pedina 3.png", wx.BITMAP_TYPE_PNG)
        bmp4 = wx.Bitmap("images/Pedina 4.png", wx.BITMAP_TYPE_PNG)
        
        self.icona1=wx.BitmapToggleButton(panel,-1,bmp1,pos=(30,120),size=(250,250))
        self.icona1.Bind(wx.EVT_TOGGLEBUTTON,self.inseriscinome1)

        self.icona2=wx.BitmapToggleButton(panel,-1,bmp2 ,pos=(350,120),size=(250,250))
        self.icona2.Bind(wx.EVT_TOGGLEBUTTON,self.inseriscinome2)
        
        self.icona3=wx.BitmapToggleButton(panel,-1, bmp3,pos=(670,120),size=(250,250))
        self.icona3.Bind(wx.EVT_TOGGLEBUTTON,self.inseriscinome3)
        
        self.icona4=wx.BitmapToggleButton(panel,-1,bmp4,pos=(990,120),size=(250,250))
        self.icona4.Bind(wx.EVT_TOGGLEBUTTON,self.inseriscinome4)
        
        self.nome1=wx.TextCtrl(panel,pos=(30,380),size=(200,40))
        self.nome1.Hide()
        self.nome2=wx.TextCtrl(panel,pos=(350,380),size=(200,40))
        self.nome2.Hide()
        self.nome3=wx.TextCtrl(panel,pos=(670,380),size=(200,40))
        self.nome3.Hide()
        self.nome4=wx.TextCtrl(panel,pos=(990,380),size=(200,40))
        self.nome4.Hide()
        
        self.pulsante1=wx.Button(panel,label="✔",pos=(240,380),size=(40,40))
        self.pulsante1.Hide()
        self.pulsante1.Bind(wx.EVT_BUTTON,self.persona1)
        self.pulsante2=wx.Button(panel,label="✔",pos=(560,380),size=(40,40))
        self.pulsante2.Hide()
        self.pulsante2.Bind(wx.EVT_BUTTON,self.persona2)
        self.pulsante3=wx.Button(panel,label="✔",pos=(880,380),size=(40,40))
        self.pulsante3.Hide()
        self.pulsante3.Bind(wx.EVT_BUTTON,self.persona3)
        self.pulsante4=wx.Button(panel,label="✔",pos=(1200,380),size=(40,40))
        self.pulsante4.Hide()
        self.pulsante4.Bind(wx.EVT_BUTTON,self.persona4)
        
        self.pulsantestart=wx.Button(panel,label="Start",pos=(335,500),size=(600,100))
        self.pulsantestart.SetFont(font1)
        self.pulsantestart.SetBackgroundColour("#53c653")
        self.pulsantestart.Hide()
        self.pulsantestart.Bind(wx.EVT_BUTTON,self.start)
        
        self.text=wx.StaticText(panel,label="",pos=(480,430),size=(200,40))
        
        font2=wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        
        self.nome1.SetFont(font2)
        self.nome2.SetFont(font2)
        self.nome3.SetFont(font2)
        self.nome4.SetFont(font2)
        self.text.SetFont(font2)
        
        self.Centre()
        self.SetMaxSize((1280,720))
        self.SetMinSize((1280,720))
        
    def inseriscinome1(self,evt):
        v=self.icona1.GetValue()
        self.icona2.SetValue(False)
        self.icona3.SetValue(False)
        self.icona4.SetValue(False)
        self.nome2.SetLabel("")
        self.nome3.SetLabel("")
        self.nome4.SetLabel("")
        self.nome2.Hide()
        self.nome3.Hide()
        self.nome4.Hide()
        self.pulsante2.Hide()
        self.pulsante3.Hide()
        self.pulsante4.Hide()
        self.text.SetLabel("")
        if v == True:
            self.nome1.Show()
            self.pulsante1.Show()
        else:
            self.nome1.Hide()
            self.pulsante1.Hide()
            
    def persona1(self,evt):
        v=self.nome1.GetValue()
        if v != "":
            nome=v
            icona=""
            p1=g.Giocatore(nome,icona)
            s=p1.__str__()
            self.text.SetLabel(s)
            self.icona1.Disable()
            self.nome1.Disable()
            self.pulsante1.Disable()
            self.conta+=1
            if self.conta >= 2:
                self.pulsantestart.Show()
        else:
            self.text.SetLabel("Non hai inserito il nome!")
        
            
    def inseriscinome2(self,evt):
        v=self.icona2.GetValue()
        self.icona1.SetValue(False)
        self.icona3.SetValue(False)
        self.icona4.SetValue(False)
        self.nome1.SetLabel("")
        self.nome3.SetLabel("")
        self.nome4.SetLabel("")
        self.nome1.Hide()
        self.nome3.Hide()
        self.nome4.Hide()
        self.pulsante1.Hide()
        self.pulsante3.Hide()
        self.pulsante4.Hide()
        self.text.SetLabel("")
        if v == True:
            self.nome2.Show()
            self.pulsante2.Show()
        else:
            self.nome2.Hide()
            self.pulsante2.Hide()
            
    def persona2(self,evt):
        v=self.nome2.GetValue()
        if v != "":
            nome=v
            icona=""
            p2=g.Giocatore(nome,icona)
            s=p2.__str__()
            self.text.SetLabel(s)
            self.icona2.Disable()
            self.nome2.Disable()
            self.pulsante2.Disable()
            self.conta+=1
            if self.conta >= 2:
                self.pulsantestart.Show()
        else:
            self.text.SetLabel("Non hai inserito il nome!")
            
    def inseriscinome3(self,evt):
        v=self.icona3.GetValue()
        self.icona1.SetValue(False)
        self.icona2.SetValue(False)
        self.icona4.SetValue(False)
        self.nome1.SetLabel("")
        self.nome2.SetLabel("")
        self.nome4.SetLabel("")
        self.nome1.Hide()
        self.nome2.Hide()
        self.nome4.Hide()
        self.pulsante1.Hide()
        self.pulsante2.Hide()
        self.pulsante4.Hide()
        self.text.SetLabel("")
        if v == True:
            self.nome3.Show()
            self.pulsante3.Show()
        else:
            self.nome3.Hide()
            self.pulsante3.Hide()
            
    def persona3(self,evt):
        v=self.nome3.GetValue()
        if v != "":
            nome=v
            icona=""
            p3=g.Giocatore(nome,icona)
            s=p3.__str__()
            self.text.SetLabel(s)
            self.icona3.Disable()
            self.nome3.Disable()
            self.pulsante3.Disable()
            self.conta+=1
            if self.conta >= 2:
                self.pulsantestart.Show()
        else:
            self.text.SetLabel("Non hai inserito il nome!")
            
    def inseriscinome4(self,evt):
        v=self.icona4.GetValue()
        self.icona1.SetValue(False)
        self.icona2.SetValue(False)
        self.icona3.SetValue(False)
        self.nome1.SetLabel("")
        self.nome2.SetLabel("")
        self.nome3.SetLabel("")
        self.nome1.Hide()
        self.nome2.Hide()
        self.nome3.Hide()
        self.pulsante1.Hide()
        self.pulsante2.Hide()
        self.pulsante3.Hide()
        self.text.SetLabel("")
        if v == True:
            self.nome4.Show()
            self.pulsante4.Show()
        else:
            self.nome4.Hide()
            self.pulsante4.Hide()
            
    def persona4(self,evt):
        v=self.nome4.GetValue()
        if v != "":
            nome=v
            icona=""
            p4=g.Giocatore(nome,icona)
            s=p4.__str__()
            self.text.SetLabel(s)
            self.icona4.Disable()
            self.nome4.Disable()
            self.pulsante4.Disable()
            self.conta+=1
            if self.conta >= 2:
                self.pulsantestart.Show()
        else:
            self.text.SetLabel("Non hai inserito il nome!")
            
    def start(self,evt):
        self.Close()
        window = Tabellone()
        window.Show()
        

if __name__ == "__main__":
    app = wx.App()
    window = Scelta()
    window.Show()
    app.MainLoop()