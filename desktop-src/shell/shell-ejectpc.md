---
description: Shell.EjectPC method - Ejects the computer from its docking station. This is the same as clicking the Start menu and selecting Eject PC, if your computer supports this command.
ms.assetid: eaba3dce-8fea-453f-90c2-4a9b5cb05ecc
title: Shell.EjectPC method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.EjectPC
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.EjectPC method

Ejects the computer from its docking station. This is the same as clicking the **Start** menu and selecting **Eject PC**, if your computer supports this command.

## Syntax


```JScript
Shell.EjectPC()
```


```VB

Shell.EjectPC()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example shows **EjectPC** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellEjectPCJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.EjectPC();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellEjectPCVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.EjectPC

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellEjectPCVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objShell.EjectPC

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



 

 




