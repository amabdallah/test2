"""Subclass of msg_somethigWrong, which is generated by wxFormBuilder."""

import wx
import Validations

# Implementing msg_somethigWrong
class msg_somethigWrong( Validations.msg_somethigWrong ):
	def __init__( self, parent ):
		Validations.msg_somethigWrong.__init__( self, parent )
	
	# Handlers for msg_somethigWrong events.
	def btn_okOnButtonClick( self, event ):
		self.Destroy()
	
	
