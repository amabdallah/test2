"""Subclass of msg_dependencyViolation, which is generated by wxFormBuilder."""

import wx
import Validations

# Implementing msg_dependencyViolation
class msg_dependencyViolation( Validations.msg_dependencyViolation ):
	def __init__( self, parent ):
		Validations.msg_dependencyViolation.__init__( self, parent )
	
	# Handlers for msg_dependencyViolation events.
	def btn_okOnButtonClick( self, event ):
		self.Destroy()
	
