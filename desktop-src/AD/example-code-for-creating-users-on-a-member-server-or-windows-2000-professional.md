---
title: Example Code for Creating Users on a Member Server or Windows 2000 Professional
description: The following Visual Basic code example creates a user on a member server or Windows 2000 Professional.
ms.assetid: 0a0800d6-eb2c-4d88-b9d4-91640206fe7b
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating users on a member server or Windows 2000 Professional
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Example Code for Creating Users on a Member Server or Windows 2000 Professional

The following Visual Basic code example creates a user on a member server or Windows 2000 Professional.


```VB
' Example: Creating a user on a member server or workstation
 
Dim cont As IADsContainer
Dim oUser As IADsUser
Dim v As Variant

On Error GoTo Cleanup

''''''''''''''''''''
' Parse the arguments
''''''''''''''''''''
 
sComputer = 
  InputBox("This script creates a user on a member " _
           & "server or workstation." _
           & vbCrLf & vbCrLf _
           & "Specify the computer name:")
If sComputer = "" Then
    Exit Sub
End If

sUser = InputBox("Specify the user name:")
If sUser = "" Then
    Exit Sub
End If
 
''''''''''''''''''''
' Bind to the computer.
''''''''''''''''''''
Set cont = GetObject("WinNT://" & sComputer & ",computer")
 
''''''''''''''''''''
' Create the user.
''''''''''''''''''''
Set oUser = cont.Create("user", sUser)
 
'''''''''''''''''''''''''''
' Write the user to the computer's security database.
'''''''''''''''''''''''''''
oUser.SetInfo

strText = "The user " & sUser & " was successfully added."
strText = strText & vbCrLf _
          & "The user has the following properties:"

'''''''''''''''''''''
' Read the user that was just created
' and display its name and its properties.
'''''''''''''''''''''
oUser.GetInfo

strText = strText & "Number of properties: " & Count
For cprop = 1 To Count
  Set v = oUser.Next()
  If IsNull(v) Then
    Exit For
  End If
  strText = strText & vbCrLf & cprop & ") " & v.Name _
            & " (" & v.ADsType & ") "
Next

MsgBox strText, vbInformation, "Create user on " & sComputer

Cleanup:
   If (Err.Number<>0) Then
      MsgBox ("An error has occurred. " & Err.Number)
   Set cont = Nothing
   Set oUser = Nothing
   Set v = Nothing


```



 

 




