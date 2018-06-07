---
Description: Runs the specified Control Panel (\*.cpl) application.
title: Shell.ControlPanelItem method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell.ControlPanelItem method

Runs the specified Control Panel (\*.cpl) application. If the application is already open, it will activate the running instance.

> [!Note]  
> As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:
>
> ``` syntax
> control.exe /name Microsoft.Personalization
> ```

 

## Syntax


```JScript
Shell.ControlPanelItem(
  bstrDir
)
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
<td><pre><code>Shell.ControlPanelItem( _
  ByVal bstrDir As BSTR _
)</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*bstrDir* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/windows/desktop/1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

The Control Panel application's file name. All Control Panel applications have the .cpl extension.

</dd> </dl>

## Return value

### JScript

This method does not return a value.

### VB

This method does not return a value.

## Examples

The following example uses **ControlPanelItem** to run the Control Panel's **Display Properties** item. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellControlPanelItemJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.ControlPanelItem("desk.cpl");
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellControlPanelItemVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        objShell.ControlPanelItem("desk.cpl")
       
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellControlPanelItemVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
    objShell.ControlPanelItem ("desk.cpl")
    
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



 

 




