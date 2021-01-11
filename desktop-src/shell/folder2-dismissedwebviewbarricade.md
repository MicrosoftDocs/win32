---
description: Called in response to the web view barricade being dismissed by the user.
ms.assetid: 170893b6-c947-45b1-b717-a93a0b083bda
title: Folder2.DismissedWebViewBarricade method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder2.DismissedWebViewBarricade
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Folder2.DismissedWebViewBarricade method

Called in response to the web view barricade being dismissed by the user.

## Syntax


```JScript
Folder2.DismissedWebViewBarricade()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

An application calls this method after the user dismisses the web view barricade.

## Examples

The following example uses **DismissedWebViewBarricade** to specify that the web view barricade for the C:\\Windows folder has been dismissed. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolder2ObjectDismissedWebViewBarricadeJ()
    {
        var objShell  = new ActiveXObject("shell.application");
        var objFolder2 = new Object;
        
        objFolder2 = objShell.NameSpace("C:\\WINDOWS");
        if (objFolder2 != null)
        {
            objFolder2.DismissedWebViewBarricade();
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnFolder2ObjectDismissedWebViewBarricadeVB()
        dim objShell
        dim objFolder2

        set objShell = CreateObject("shell.application")
        set objFolder2 = objShell.NameSpace("C:\WINDOWS")

        if (not objFolder2 is nothing) then
            objFolder2.DismissedWebViewBarricade()
        end if

        set objFolder2 = nothing
        set objShell = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub btnDismissedWebViewBarricade_Click()
    Dim objShell   As Shell
    Dim objFolder2 As Folder2

    Set objShell = New Shell
    Set objFolder2 = objShell.NameSpace("C:\WINDOWS")

    If (Not objFolder2 Is Nothing) Then
        objFolder2.DismissedWebViewBarricade
    End If

    Set objFolder2 = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**Folder2**](folder2-object.md)
</dt> <dt>

[**Folder**](folder.md)
</dt> </dl>

 

 




