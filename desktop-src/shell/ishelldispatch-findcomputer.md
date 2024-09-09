---
description: IShellDispatch.FindComputer method Displays the Search Results Computers dialog box. The dialog box shows the result of the search for a specified computer.
ms.assetid: 9B687A8A-BB29-49a0-8AE3-11A75FAF3257
title: IShellDispatch.FindComputer method (Shldisp.h)
ms.topic: reference
ms.date: 04/07/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.FindComputer
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.FindComputer method

Displays the **Search Results: Computers** dialog box. The dialog box shows the result of the search for a specified computer.

## Syntax


```JScript
IShellDispatch.FindComputer()
```


```VB

IShellDispatch.FindComputer()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Remarks

This method is implemented and accessed through the [**Shell.FindComputer**](shell-findcomputer.md) method.

## Examples

The following examples show the use of **FindComputer** in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellFindComputerJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objshell.FindComputer();
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
        objshell.FindComputer

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellFindComputerVB()
    Dim objShell As Shell

    Set objShell = New Shell
    objshell.FindComputer

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



 

 




