---
Description: 'Displays the Find: All Files dialog box. This is the same as clicking the Start menu and then selecting Search (or its equivalent under systems earlier than Windows XP.'
ms.assetid: cccdd3ea-b52a-4fbe-b4c5-1efc1dd6d770
title: Shell.FindFiles method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell.FindFiles method

Displays the **Find: All Files** dialog box. This is the same as clicking the **Start** menu and then selecting **Search** (or its equivalent under systems earlier than Windows XP.

## Syntax


```JScript
Shell.FindFiles()
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
<td><pre><code>Shell.FindFiles()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example shows **FindFiles** in use. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellFindFilesJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.Shell_FindFiles();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellFindFilesVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.FindFiles

        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellFindFilesVB()
    Dim objShell As Shell

    Set objShell = New Shell
    objShell.FindFiles

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



 

 




