---
description: Shell.ServiceStop method - Stops a named service.
ms.assetid: AC22C91E-BBC6-4a2e-8D39-F9D7C0AC0947
title: Shell.ServiceStop method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.ServiceStop
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.ServiceStop method

Stops a named service.

## Syntax


```JScript
retVal = Shell.ServiceStop(
  sServiceName,
  vPersistent
)
```


```VB

Shell.ServiceStop( _
  ByVal sServiceName As BSTR, _
  ByVal vPersistent As Variant _
) As Variant
```





## Parameters

<dl> <dt>

*sServiceName* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the name of the service.

</dd> <dt>

*vPersistent* \[in\]
</dt> <dd>

Type: **Variant**

Set to **true** to have the service started by the service control manager when [**ServiceStart**](./shell-servicestart.md) is called. To leave the service configuration unchanged, set *vPersistent* to **false**.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

## Remarks

The method returns **false** if the service has already been stopped. Before calling this method, you can call [**Shell.IsServiceRunning**](./shell-isservicerunning.md) to ascertain the status of the service.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
