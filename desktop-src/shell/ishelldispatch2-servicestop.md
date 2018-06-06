---
Description: Stops a named service.
ms.assetid: f4cd0e2c-4ecc-4e9f-a0b5-d2a8a739f0e2
title: IShellDispatch2.ServiceStop method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IShellDispatch2.ServiceStop method

Stops a named service.

## Syntax


```JScript
retVal = IShellDispatch2.ServiceStop(
  sServiceName,
  vPersistent
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
<td><pre><code>IShellDispatch2.ServiceStop( _
  ByVal sServiceName As BSTR, _
  ByVal vPersistent As Variant _
) As Variant</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*sServiceName* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/windows/desktop/1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** that contains the name of the service.

</dd> <dt>

*vPersistent* \[in\]
</dt> <dd>

Type: **Variant**

Set to **true** to have the service started by the service control manager when [**ServiceStart**](ishelldispatch2-servicestart.md) is called. To leave the service configuration unchanged, set *vPersistent* to **false**.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

## Remarks

This method is implemented and accessed through the [**Shell.ServiceStop**](https://msdn.microsoft.com/AC22C91E-BBC6-4a2e-8D39-F9D7C0AC0947) method.

The method returns **false** if the service has already been stopped. Before calling this method, you can call [**Shell.IsServiceRunning**](https://msdn.microsoft.com/FDC41C2D-7462-458f-BBE6-D97260C26B6C) to ascertain the status of the service.

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **ServiceStop** to stop the Messenger service. Usage is shown for JScript and VBScript.

JScript:


```JScript
<script language="JScript">
    function fnServiceStopJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var bReturn;
        
        bReturn = objShell.ServiceStop("Messenger", true);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnServiceStopVB()
        dim objShell
        dim bReturn

        set objShell = CreateObject("shell.application")

        bReturn = objShell.ServiceStop("Messenger", true)

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



 

 




