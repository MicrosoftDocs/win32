---
description: "Shell.FindComputer method - 'Displays the Search Results: Computers dialog box. The dialog box shows the result of the search for a specified computer.'"
ms.assetid: 0304b955-afde-4de4-824a-9ec9c9530360
title: Shell.FindComputer method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.FindComputer
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.FindComputer method

Displays the **Search Results: Computers** dialog box. The dialog box shows the result of the search for a specified computer.

## Syntax


```JScript
Shell.FindComputer()
```


```VB

Shell.FindComputer()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example shows **FindComputer** in use. The result of this code is the same as pressing the **Start** button, clicking **Search**, clicking the **Printers, computers, or people** option, then clicking **A computer on the network**. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellFindComputerJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.FindComputer();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellFindComputerVB()
        dim objShell
        dim ssfWINDOWS
        ssfWINDOWS = 36

        set objShell = CreateObject("shell.application")
        objShell.FindComputer

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellFindComputerVB()
    Dim objShell As Shell

    Set objShell = New Shell
    objShell.FindComputer

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



 

 




