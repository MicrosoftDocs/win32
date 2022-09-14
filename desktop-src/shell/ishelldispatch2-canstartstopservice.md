---
description: IShellDispatch2.CanStartStopService method - Determines if the current user can start and stop the named service.
ms.assetid: cbb54ae9-02e6-4243-a782-e9f125c21c0d
title: IShellDispatch2.CanStartStopService method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch2.CanStartStopService
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch2.CanStartStopService method

Determines if the current user can start and stop the named service.

## Syntax


```JScript
retVal = IShellDispatch2.CanStartStopService(
  sServiceName
)
```


```VB

IShellDispatch2.CanStartStopService( _
  ByVal sServiceName As String _
) As Variant
```





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

This method is implemented and accessed through the [**Shell.CanStartStopService**](./shell-canstartstopservice.md) method.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
