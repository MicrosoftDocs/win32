---
title: Extending ADSI
description: With the ADSI extension model, you can associate a directory class with your own COM object.
ms.assetid: bf9a324d-14eb-4eb9-a80d-b0431db3af26
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Extending ADSI

With the ADSI extension model, you can associate a directory class with your own COM object. From an ADSI programmer or script writer's perspective, the extension becomes an integral part of ADSI. For example, when a new employee joins Fabrikam, the Windows NT administrator will create a user object in the directory and the payroll administrator will need to set up some entries in the human resource systems for this user. With an ADSI extension, this process can be streamlined into one single script.


```VB
Dim usr
Dim sUserName

On Error Resume Next

sUserName = InputBox ("Enter the name of the user to add:")

Set usr = ou.Create("user", "CN=" & sUserName)

If Err.Number <> 0 Then
    WScript.Echo "An error has occurred. " & Err.Number
    Exit Sub 
End If

// Insert code to set some attributes

usr.SetInfo

If Err.Number <> 0 Then
    WScript.Echo "An error has occurred. " & Err.Number
    Exit Sub 
End If

usr.AddToPayroll  'this is a custom method from an ADSI Extension

If Err.Number <> 0 Then
    WScript.Echo "An error has occurred. " & Err.Number
    Exit Sub 
End If

Debug.Print "User: " & usr.Name & "has been created"
```



For more information, see [ADSI Extensions](adsi-extensions.md).

 

 




