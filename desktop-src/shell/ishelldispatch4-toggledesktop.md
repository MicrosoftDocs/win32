---
Description: Displays or hides the desktop.
title: IShellDispatch4.ToggleDesktop method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IShellDispatch4.ToggleDesktop method

Displays or hides the desktop.

## Syntax


```JScript
IShellDispatch4.ToggleDesktop()
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
<td><pre><code>IShellDispatch4.ToggleDesktop()</code></pre></td>
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

## Remarks

This method has the same effect as the **Show Desktop** button on the taskbar. It either hides all open windows to show the desktop or it hides the desktop by showing all open windows. The **ToggleDesktop** method does not display a user interface, it just invokes the toggle action.

## Examples

The following examples show the proper use of **ToggleDesktop** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnIShellDispatch4ToggleDesktopJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.ToggleDesktop();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnIShellDispatch4ToggleDesktopVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
            objShell.ToggleDesktop
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnIShellDispatch4ToggleDesktopVB()
    Dim objShell As Shell
            
    Set objShell = New Shell
        objShell.ToggleDesktop
    Set objShell = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 




