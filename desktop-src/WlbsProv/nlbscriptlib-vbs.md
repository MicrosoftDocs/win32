---
title: NlbScriptLib.vbs
description: NLBScriptLib.vbs serves as a common library of functions for the jobs in Nlb.wsf. It is mainly used to provide a standard mechanism for connecting to the Network Load Balancing provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '45194f75-f5f8-4955-ad2b-047e3f49b1be'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# NlbScriptLib.vbs

NLBScriptLib.vbs serves as a common library of functions for the jobs in Nlb.wsf. It is mainly used to provide a standard mechanism for connecting to the Network Load Balancing provider.


```VB
'''''''''''''''''''''''''''''''''''
' NlbScriptLib.vbs
'
' Contains functions and constants used by Nlb.wsf
'
'''''''''''''''''''''''''''''''''''

Public Const DEBUG_MODE = False

' The NLB provider namespace
Public Const NLB_NAMESPACE = "root\MicrosoftNLB"

' Global objects
Public g_objLocator     'SWbemLocator object
Public g_objService     'SWbemService object
Public g_objArgs        'Arguments object
Public g_objNode        'MicrosoftNLB_Node object

'Global strings
Public g_strCIP         'Cluster IP
Public g_strDIP         'Dedicated IP
Public g_strHostID      'Host priority
Public g_strPort        'Port number
Public g_strNameKey     'Used to specify the Name property

Public Function ConnectNLB()
' 
' Sets all global objects and establishes a connection to a 
' Network Load Balancing host via its dedicated IP address (DIP).  
'
' Every job in NLB.WSF calls ConnectNLB.
'
' ConnectNLB expects the following command-line arguments:
' 1) The user ID of the caller.
' 2) The password of the caller.
'
  Dim strUsername, strPassword
  Dim xmlDoc, ElementList, objNode, objNodes

  'Parse the XML document
  Set XMLDoc = CreateObject("Microsoft.xmlDOM")
  xmlDoc.Async = False
  xmlDoc.Load("Nlb.xml")
  Set ElementList = xmlDoc.getElementsByTagName("clusterIP")
  g_strCIP = ElementList.item(0).text
  Set ElementList = xmlDoc.getElementsByTagName("dedicatedIP")
  g_strDIP = ElementList.item(0).text
  Set ElementList = xmlDoc.getElementsByTagName("hostID")
  g_strHostID = ElementList.item(0).text
  Set ElementList = xmlDoc.getElementsByTagName("portnumber")
  g_strPort = ElementList.item(0).text
  Set ElementList = Nothing
  Set XMLDoc = Nothing    

  'Parse command-line arguments
  Set g_objArgs = WScript.Arguments
  If g_objArgs.Count < 2 Then
    ShowSyntax
    WScript.Quit
  End If

  'Connect to NLB
  Set g_objLocator = CreateObject("WbemScripting.SWbemLocator")
  Set g_objService = g_objLocator.ConnectServer(g_strDIP,      _
                                                NLB_Namespace, _
                                                strUserName,   _
                                                strPassword)
  g_objLocator.Security_.ImpersonationLevel = 3

  'Get a MicrosoftNLB_Node object
  Set objNodes = g_objService.InstancesOf ("MicrosoftNLB_Node")
  For Each objNode in objNodes
    Exit For
  Next
  Set g_objNode = objNode
  g_strNameKey = g_strCIP & ":" & g_strHostID

End Function

Public Function QuitWithMessage(strMessage)
  WScript.Echo strMessage
  DisconnectNLB
  WScript.Quit
End Function

Public Function EnumProperties(obj)
  Dim oProps, oProp
  Set oProps = obj.Properties_
  On Error Resume Next
  For Each oProp in oProps
    WScript.Echo oProp.Name & " : " & CStr(oProp.Value)
    If Err.Number = 94 Then 
      'Error 94 = Invalid Use of Null
      Err.Clear
      WScript.Echo oProp.Name & " : (null)"
    End If
  Next
  Set oProp = Nothing
  Set oProps = Nothing
End Function

Public Function DisconnectNLB
  Set g_objNodes = Nothing
  Set g_objArgs = Nothing
  Set g_objService = Nothing
  Set g_objLocator = Nothing
End Function

Public Function ShowSyntax()
  WScript.Echo vbCrLf
  WScript.Echo String(70,"=")
  WScript.Echo "NLB.WSF SYNTAX GUIDE:" & vbCrLf
  WScript.Echo "Run NLB.WSF on the command line using the following basic syntax:"
  WScript.Echo "    cscript //Job:<JobID> nlb.wsf <arglist>" & vbCrLf
  WScript.Echo "For <JobID>, specify the name of the job you want to run."
  WScript.Echo "Job names are defined in NLB.WSF." & vbCrLf
  WScript.Echo "For <arglist>, specify:"
  WScript.Echo "    1. Your network user name."
  WScript.Echo "    2. Your network password."
  WScript.Echo "Example: Running the Test job"
  WScript.Echo "    cscript //Job:" & Chr(34) & "Test" & Chr(34) & " " & _
               "nlb.wsf " & Chr(34) & "Administrator" & Chr(34) & " " &  _
               Chr(34) & Chr(34) & vbCrLf
  WScript.Echo String(70,"=")
End Function
```



 

 




