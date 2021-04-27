---
description: Shell.IsServiceRunning method - Returns a value that indicates whether a particular service is running.
ms.assetid: FDC41C2D-7462-458f-BBE6-D97260C26B6C
title: Shell.IsServiceRunning method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.IsServiceRunning
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.IsServiceRunning method

Returns a value that indicates whether a particular service is running.

## Syntax


```JScript
retVal = Shell.IsServiceRunning(
  sServiceName
)
```


```VB

Shell.IsServiceRunning( _
  ByVal sServiceName As BSTR _
) As Variant
```





## Parameters

<dl> <dt>

*sServiceName* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
