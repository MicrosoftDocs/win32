---
description: IShellDispatch.ShutdownWindows method - Displays the Shut Down Windows dialog box. This is the same as clicking the Start menu and selecting Shut Down.
ms.assetid: 3C4F6579-6398-4af4-8911-FE22555B0ABC
title: IShellDispatch.ShutdownWindows method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.ShutdownWindows
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.ShutdownWindows method

Displays the **Shut Down Windows** dialog box. This is the same as clicking the **Start** menu and selecting **Shut Down**.

## Syntax


```JScript
IShellDispatch.ShutdownWindows()
```


```VB

IShellDispatch.ShutdownWindows()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Remarks

This method is implemented and accessed through the [**Shell.ShutdownWindows**](shell-shutdownwindows.md) method.

## Examples

The following example shows the use of **ShutdownWindows** in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellShutdownWindowsJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objshell.ShutdownWindows();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellShutdownWindowsVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objshell.ShutdownWindows

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellShutdownWindowsVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objshell.ShutdownWindows

    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




