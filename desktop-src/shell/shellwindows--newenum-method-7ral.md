---
description: Creates and returns a new ShellWindows object that is a copy of this ShellWindows object.
title: ShellWindows._NewEnum method (Exdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellWindows._NewEnum
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 85e84c13-62aa-4502-b642-ca55273a800d
api_name: 
 - ShellWindows._NewEnum
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# ShellWindows.\_NewEnum method

Creates and returns a new [**ShellWindows**](shellwindows.md) object that is a copy of this **ShellWindows** object.

## Syntax


```JScript
retVal = ShellWindows._NewEnum()
```



## Parameters

This method has no parameters.

## Return value

Type: **[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)\*\***

An object reference to the [**ShellWindows**](shellwindows.md) object copy.

## Examples

The following example shows **\_NewEnum** in use. Proper usage is shown for VBScript and Visual Basic. This method cannot be used with JScript.

VBScript:


```VB
<script language="VBScript">
    function fnShellWindowsNewEnumVB()
        dim objShell
        dim objShellWindows
        
        set objShell = CreateObject("shell.application")
        set objShellWindows = objshell.Shell_Windows

        if (not objShellWindows is nothing) then
            dim objEnumItems
            
            for each objEnumItems in objShellWindows
                alert(objEnumItems.Type)
            next
        end if

        set objShellWindows = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellWindowsNewEnumVB()
    Dim objShell        As Shell
    Dim objShellWindows As ShellWindows
    
    Set objShell = New Shell
    Set objShellWindows = objshell.Shell_Windows

    If (Not objShellWindows Is Nothing) Then
        Dim vEnumItem As Variant
        
        For Each vEnumItem In objShellWindows
            Debug.Print vEnumItem.Type
        Next vEnumItem
    End If

    Set objShellWindows = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
