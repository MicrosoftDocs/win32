---
Description: Displays the Shut Down Windows dialog box. This is the same as clicking the Start menu and selecting Shut Down.
ms.assetid: 6fa8e2e0-a58f-4837-89f5-898cece2d80a
title: Shell.ShutdownWindows method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell.ShutdownWindows method

Displays the **Shut Down Windows** dialog box. This is the same as clicking the **Start** menu and selecting **Shut Down**.

## Syntax


```JScript
iRetVal = Shell.ShutdownWindows()
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Shell.ShutdownWindows() As Integer</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Examples

The following example shows **ShutdownWindows** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellShutdownWindowsJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.ShutdownWindows();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellShutdownWindowsVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.ShutdownWindows

        set objShell = nothing
    end function
```



Visual Basic:


```VB
Private Sub fnShellShutdownWindowsVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objShell.ShutdownWindows

    Set objShell = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




