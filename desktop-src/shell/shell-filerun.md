---
description: Displays the Run dialog to the user. This method has the same effect as clicking the Start menu and selecting Run.
ms.assetid: bb984777-e09f-41e6-8359-51c5291654f7
title: Shell.FileRun method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.FileRun
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.FileRun method

Displays the **Run** dialog to the user. This method has the same effect as clicking the **Start** menu and selecting **Run**.

## Syntax


```JScript
Shell.FileRun()
```


```VB

Shell.FileRun()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example shows **FileRun** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellFileRunJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.FileRun();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellFileRunVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.FileRun

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellFileRunVB()
    Dim objShell As Shell

    Set objShell = New Shell
    objShell.FileRun

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



 

 




