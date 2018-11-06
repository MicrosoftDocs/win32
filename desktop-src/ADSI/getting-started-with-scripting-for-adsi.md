---
title: Getting Started with Scripting for ADSI
description: Scripting is useful for system administrators who want to create batch scripts for frequently used tasks.
ms.assetid: ae479d6b-75cf-4659-8a91-c2cbdcf56091
ms.tgt_platform: multiple
keywords:
- Getting Started with Scripting for ADSI ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with Scripting for ADSI

Scripting is useful for system administrators who want to create batch scripts for frequently used tasks.

To start scripting with ADSI, you must have a computer that runs Windows or be logged on to a domain that contains data for computer accounts in the directory.

## A Simple Scripting Sample: Finding Names and Locations of Computer Accounts

Create a new text file using a text editor. The following code example shows how to find names and locations of computer accounts.


```VB
'---------------------------------------------------------------
' Returns the name and location for all the computer accounts in 
' Active Directory.
'--------------------------------------------------------------- 
Const ADS_SCOPE_SUBTREE = 2
Set objConnection = CreateObject("ADODB.Connection")
Set objCommand =   CreateObject("ADODB.Command")
objConnection.Provider = "ADsDSOObject"
objConnection.Open "Active Directory Provider"
Set objCommand.ActiveConnection = objConnection
objCommand.CommandText = "Select Name, Location from 'LDAP://DC=fabrikam,DC=com' " & "where objectClass='computer'"  
objCommand.Properties("Page Size") = 1000
objCommand.Properties("Timeout") = 30 
objCommand.Properties("Searchscope") = ADS_SCOPE_SUBTREE 
objCommand.Properties("Cache Results") = False 
Set objRecordSet = objCommand.Execute
objRecordSet.MoveFirst
Do Until objRecordSet.EOF
    Wscript.Echo "Computer Name: " & objRecordSet.Fields("Name").Value
    Wscript.Echo "Location: " & objRecordSet.Fields("Location").Value
    objRecordSet.MoveNext
Loop
```



Save the file as First.vbs. Modify the line that begins with "objCommand.CommandText" to change the path to your domain. At the command prompt, type **cscript First.vbs** for a command line or First.vbs for Windows scripting. The results should be returned in the command prompt.

For more information about scripting for ADSI, see [Active Directory Service Interfaces Scripting](adsi-scripting-tutorial.md).

 

 




