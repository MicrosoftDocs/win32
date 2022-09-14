---
description: Displays the Windows Help and Support Center. This method has the same effect as clicking the Start menu and selecting Help and Support.
ms.assetid: fc13fef8-dac8-4c59-936d-8da0e63e06d4
title: Shell.Help method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.Help
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.Help method

Displays the Windows Help and Support Center. This method has the same effect as clicking the **Start** menu and selecting **Help and Support**.

## Syntax


```JScript
Shell.Help()
```


```VB

Shell.Help()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example shows **Help** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellHelpJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.Help();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellHelpVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.Help

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellHelpVB()
    Dim objShell As Shell

    Set objShell = New Shell
    objShell.Help

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



 

 




