---
description: IShellDispatch2.GetSystemInformation method - Retrieves system information.
ms.assetid: 57c066e3-080f-4ecc-b56e-877f0569e901
title: IShellDispatch2.GetSystemInformation method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch2.GetSystemInformation
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch2.GetSystemInformation method

Retrieves system information.

## Syntax


```JScript
retVal = IShellDispatch2.GetSystemInformation(
  sName
)
```


```VB

IShellDispatch2.GetSystemInformation( _
  ByVal sName As BSTR _
) As Variant
```





## Parameters

<dl> <dt>

*sName* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that specifies the system information that is being requested.

</dd> </dl>

## Return value

### JScript

Type: **Variant**

Returns the value of the requested system information. The return type depends on which system information is requested. See the Remarks section for details.

### VB

Type: **Variant**

Returns the value of the requested system information. The return type depends on which system information is requested. See the Remarks section for details.

## Remarks

This method is implemented and accessed through the [**Shell.GetSystemInformation**](./shell-getsysteminformation.md) method.

This method can be used to request many system information values. The following table gives the *sName* value that is used to request the information and the associated type of the returned value.



*sName*

Return type

Description

DirectoryServiceAvailable

**Boolean**

Set to **true** if the directory service is available; otherwise, **false**.

DoubleClickTime

**Integer**

The double-click time, in milliseconds.

ProcessorLevel

**Integer**

**Windows Vista and later**. The processor level. Returns 3, 4, or 5, for x386, x486, and Pentium-level processors, respectively.

ProcessorSpeed

**Integer**

The processor speed, in megahertz (MHz).

ProcessorArchitecture

**Integer**

The processor architecture. For details, see the discussion of the **wProcessorArchitecture** member of the [**SYSTEM\_INFO**](/windows/win32/api/sysinfoapi/ns-sysinfoapi-system_info) structure.

PhysicalMemoryInstalled

**Integer**

The amount of physical memory installed, in bytes.

The following are valid only on Windows XP.

IsOS\_Professional

**Boolean**

Set to **true** if the operating system is Windows XP Professional Edition; otherwise, **false**.

IsOS\_Personal

**Boolean**

Set to **true** if the operating system is Windows XP Home Edition; otherwise, **false**.

The following is valid only on Windows XP and later.

IsOS\_DomainMember

**Boolean**

Set to **true** if the computer is a member of a domain; otherwise, **false**.



 

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **GetSystemInformation** for JScript and VBScript.

JScript:


```JScript
<script language="JavaScript">
    function fnGetSystemInformationJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var vReturn;

        vReturn = objShell.GetSystemInformation("ProcessorLevel");
        document.write(vReturn);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnGetSystemInformationVB()
        dim objShell
        dim vReturn

        set objShell = CreateObject("shell.application")

        vReturn = objShell.GetSystemInformation("ProcessorLevel")
        document.write(vReturn)

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



 

 
