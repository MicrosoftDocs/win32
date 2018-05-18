---
Description: 'Returns a value that indicates whether a particular service is running.'
ms.assetid: 'FDC41C2D-7462-458f-BBE6-D97260C26B6C'
title: 'Shell.IsServiceRunning method'
---

# Shell.IsServiceRunning method

Returns a value that indicates whether a particular service is running.

## Syntax


```JScript
retVal = Shell.IsServiceRunning(
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
<td><pre><code>Shell.IsServiceRunning( _
  ByVal sServiceName As BSTR _
) As Variant</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*sServiceName* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** that contains the name of the service.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if the service specified by *sServiceName* is running; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if the service specified by *sServiceName* is running; otherwise, **false**.

## Remarks

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **IsServiceRunning** to determine whether the Themes service is running for an application. Usage is shown for JScript and VBScript.

JScript:


```JScript
function fnIsServiceRunningJ()
{
    var objShell = new ActiveXObject("shell.application");
    var bReturn;

    bReturn = objShell.IsServiceRunning("Themes");
}
```



VBScript:


```VB
function fnIsServiceRunningVB()
    dim objShell
    dim bReturn

    set objShell = CreateObject("shell.application")

    bReturn = objShell.IsServiceRunning("Themes")

    set objShell = nothing
end function
```



## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




