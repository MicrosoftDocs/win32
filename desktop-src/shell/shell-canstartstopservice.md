---
Description: Determines if the current user can start and stop the named service.
ms.assetid: 1428F529-61F6-4113-A553-2C0D617FD859
title: Shell.CanStartStopService method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell.CanStartStopService method

Determines if the current user can start and stop the named service.

## Syntax


```JScript
retVal = Shell.CanStartStopService(
  sServiceName
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
<td><pre><code>Shell.CanStartStopService( _
  ByVal sServiceName As String _
) As Variant</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*sServiceName* \[in\]
</dt> <dd>

Type: **String**

A **String** that contains the name of the service.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if the user can start and stop the service; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if the user can start and stop the service; otherwise, **false**.

## Remarks

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the usage of **CanStartStopService** for JScript and VBScript.

JScript:


```JScript
<script language="JScript">
    function fnCanStartStopServiceJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var bReturn;

        bReturn = objShell.CanStartStopService("service name");
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnCanStartStopServiceVB()
        dim objShell
        dim bReturn

        set objShell = CreateObject("shell.application")

        bReturn = objShell.CanStartStopService("service name")

        set objShell = nothing
    end function
</script>
```



## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




