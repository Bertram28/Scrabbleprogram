import wx
import gui

class ScrabbleFrame(gui.MainFrame):
	def __init__(self,parent):
		gui.MainFrame.__init__(self,parent)

	def close_func( self, event ):
		self.Close()

	def afslut(self, event ):
		self.Close()

app = wx.App(False)
frame = ScrabbleFrame(None)
frame.Show(True)
app.MainLoop()
