---
description: Displays the Date and Time dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting Adjust date/time.
ms.assetid: D4B949F6-5508-4624-9706-491184703DC6
title: IShellDispatch.SetTime method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.SetTime
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.SetTime method

Displays the **Date and Time** dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting **Adjust date/time**.

## Syntax


```JScript
IShellDispatch.SetTime()
```


```VB

IShellDispatch.SetTime()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Remarks

This method is implemented and accessed through the [**Shell.SetTime**](shell-settime.md) method.

## Examples

The following examples show the use of **SetTime** in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellSetTimeJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objshell.SetTime();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellSetTimeVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objshell.SetTime
 
        set objShell = nothing
    end function
```



Visual Basic:


```VB
Private Sub fnShellSetTimeVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objshell.SetTime
 
    Set objShell = Nothing
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




