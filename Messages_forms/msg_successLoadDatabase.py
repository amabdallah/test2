"""Subclass of msg_successLoadDatabase, which is generated by wxFormBuilder."""

import wx
import Validations

# Implementing msg_successLoadDatabase
class msg_successLoadDatabase( Validations.msg_successLoadDatabase ):
	def __init__( self, parent ):
		Validations.msg_successLoadDatabase.__init__( self, parent )
	
	# Handlers for msg_successLoadDatabase events.
	def btn_okOnButtonClick( self, event ):
		self.Destroy()
	
