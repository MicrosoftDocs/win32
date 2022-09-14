---
description: Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting Show windows side by side.
ms.assetid: 63CB7E20-48E6-4cfe-B0BA-0D28A7B151BD
title: IShellDispatch.TileVertically method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.TileVertically
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.TileVertically method

Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting **Show windows side by side**.

## Syntax


```JScript
IShellDispatch.TileVertically()
```


```VB

IShellDispatch.TileVertically()
```





## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Remarks

This method is implemented and accessed through the [**Shell.TileVertically**](shell-tilevertically.md) method.

## Examples

The following examples show the use of **TileVertically** in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellTileVerticallyJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objshell.TileVertically();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellTileVerticallyVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objshell.TileVertically

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellTileVerticallyVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objshell.TileVertically

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



 

 




