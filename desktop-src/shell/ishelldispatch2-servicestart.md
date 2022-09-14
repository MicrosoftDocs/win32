---
description: IShellDispatch2.ServiceStart method - Starts a named service.
ms.assetid: 3af57cdc-f449-433d-a9e1-119038045e4c
title: IShellDispatch2.ServiceStart method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch2.ServiceStart
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch2.ServiceStart method

Starts a named service.

## Syntax


```JScript
retVal = IShellDispatch2.ServiceStart(
  sServiceName,
  vPersistent
)
```


```VB

IShellDispatch2.ServiceStart( _
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

Set to **true** to have the service started automatically by the service control manager during system startup. Set to **false** to leave the service configuration unchanged.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

## Remarks

This method is implemented and accessed through the [**Shell.ServiceStart**](./shell-servicestart.md) method.

The method returns **false** if the service has already been started. Before calling this method, you can call [**Shell.IsServiceRunning**](./shell-isservicerunning.md) to ascertain the status of the service.

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **ServiceStart** to start the Messenger service. Usage is shown for JScript and VBScript.

JScript:


```JScript
<script language="JScript">
    function fnServiceStartJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var bReturn;
        
        bReturn = objShell.ServiceStart("Messenger", true);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnServiceStartVB()
        dim objShell
        dim bReturn

        set objShell = CreateObject("shell.application")

        bReturn = objShell.ServiceStart("Messenger", true)

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



 

 
