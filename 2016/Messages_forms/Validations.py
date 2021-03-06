# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class msg_connSQLiteSuccs
###########################################################################

class msg_connSQLiteSuccs ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1000, title = u"Successful Connection to the WaMDaM database", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\n\nYou are successfully connected to the WaMDaM SQLite database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1001, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_connSQLiteInvalid
###########################################################################

class msg_connSQLiteInvalid ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1002, title = u"Error: Invalid WaMDaM SQLite Database File", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\nThe SQLite database file you selected is invalid. Make sure to select a WaMDaM database file. You can download a blank SQLite WaMDaM file from GitHub @ https://github.com/amabdallah/WaM-DaM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1003, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_selectDatabaseFirst
###########################################################################

class msg_selectDatabaseFirst ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1004, title = u"Error: Select a WaMDaM SQLite database first", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\nSelect a WaMDaM SQLite database before you click Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1005, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_workbookInvalid
###########################################################################

class msg_workbookInvalid ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1006, title = u"Error: Invalid WaMDaM workbook", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\nThe selected file does not match the WaMDaM workbook. The original template has either been changed or you selected a different file.\n\nMake sure that the sheet names and the column headers are not changed and are identical to the original templates.\nYou can download a blank template from GitHub at https://github.com/amabdallah/WaM-DaM\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1007, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_selectWorkbokFirst
###########################################################################

class msg_selectWorkbokFirst ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1008, title = u"Error: Select a WaMDaM workbook first", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\nYou need to select a WaM-DaM workbook first", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1009, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_emptyRequiredField
###########################################################################

class msg_emptyRequiredField ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1010, title = u"Error: Empty required field", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\nYou have a empty entry in required field in the --xyz table--", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1011, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_duplicateEnties
###########################################################################

class msg_duplicateEnties ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1012, title = u"Error: Duplicate entries for a unique field", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\nYou entered duplicate values in the field name x and table name y” entries for this field and table should be unique. Delete the duplicated value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1013, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_dependencyViolation
###########################################################################

class msg_dependencyViolation ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1014, title = u"Error: dependency on other tables", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\n\n\nYou entered a value that is dependent on other table but does \nnot exist in the other table", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1015, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_registerCVs
###########################################################################

class msg_registerCVs ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1016, title = u"Register your data with controlled vocabulary ", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\nIt seems that you did not register your data terms with controlled\nvocabulary in the xyz tables (s), you may choose to proceed and\nload your data to the database. However, it is recommend that \nyou register your terms against the available controlled\nvocabulary or you create additional controlled vocabulary of your\nchoice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.btn_continue = wx.Button( self, 1017, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_continue, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.btn_cancel = wx.Button( self, 1018, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_cancel, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_continue.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	
	

###########################################################################
## Class msg_somethigWrong
###########################################################################

class msg_somethigWrong ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1019, title = u"Sorry: something went wrong ", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\nsomething went wrong while loading data into SQLite, \nplease check your input data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1020, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class msg_successLoadDatabase
###########################################################################

class msg_successLoadDatabase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = 1021, title = u"Successfully loaded data into the database", pos = wx.DefaultPosition, size = wx.Size( 458,212 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\nYou successfully loaded the selected data into the database. \nYou can view the data by using: SQLite Manager: Add-ons for\nFirefox web browser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.btn_ok = wx.Button( self, 1022, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

