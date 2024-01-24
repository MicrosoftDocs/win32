---
description: Shell.ToggleDesktop method - Displays or hides the desktop.
title: Shell.ToggleDesktop method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.ToggleDesktop
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: BD07F7F2-A588-4189-95F4-3A8E2905E8F5

---

# Shell.ToggleDesktop method

Displays or hides the desktop.

## Syntax


```JScript
Shell.ToggleDesktop()
```


```VB

Shell.ToggleDesktop()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Remarks

This method has the same effect as the **Show Desktop** button on the taskbar. It either hides all open windows to show the desktop or it hides the desktop by showing all open windows. The **ToggleDesktop** method does not display a user interface, it just invokes the toggle action.

## Examples

The following examples show the proper use of **ToggleDesktop** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnIShellDispatch4ToggleDesktopJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.ToggleDesktop();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnIShellDispatch4ToggleDesktopVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
            objShell.ToggleDesktop
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnIShellDispatch4ToggleDesktopVB()
    Dim objShell As Shell
            
    Set objShell = New Shell
        objShell.ToggleDesktop
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 




