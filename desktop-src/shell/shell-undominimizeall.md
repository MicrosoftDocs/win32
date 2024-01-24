---
description: Restores all desktop windows to the same state they were in before the last MinimizeAll command.
ms.assetid: dcedfa18-6dde-4fb8-9679-4d6ff80249e4
title: Shell.UndoMinimizeALL method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.UndoMinimizeALL
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.UndoMinimizeALL method

Restores all desktop windows to the same state they were in before the last [**MinimizeAll**](shell-minimizeall.md) command. This method has the same effect as right-clicking the taskbar and selecting **Undo Minimize All Windows** on older systems or a second clicking of the **Show Desktop** icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.

## Syntax


```JScript
iRetVal = Shell.UndoMinimizeALL()
```


```VB

Shell.UndoMinimizeALL() As Integer
```





## Parameters

This method has no parameters.

## Examples

The following example shows **UndoMinimizeALL** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellUndoMinimizeALLJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.UndoMinimizeALL();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellUndoMinimizeALLVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.UndoMinimizeALL

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellUndoMinimizeAllVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objShell.UndoMinimizeALL

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



 

 




