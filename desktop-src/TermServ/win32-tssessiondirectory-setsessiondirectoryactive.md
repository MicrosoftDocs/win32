---
title: SetSessionDirectoryActive method of the Win32_TSSessionDirectory class
description: The SetSessionDirectoryActive method sets the SessionDirectoryActive property.
ms.assetid: b2175d1a-b62f-4bdf-9122-76e85233fba4
ms.tgt_platform: multiple
keywords:
- SetSessionDirectoryActive method Remote Desktop Services
- SetSessionDirectoryActive method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetSessionDirectoryActive method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetSessionDirectoryActive
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSessionDirectoryActive method of the Win32\_TSSessionDirectory class

The **SetSessionDirectoryActive** method sets the **SessionDirectoryActive** property.

## Syntax


```mof
uint32 SetSessionDirectoryActive(
  [in] uint32 SessionDirectoryActive
);
```



## Parameters

<dl> <dt>

*SessionDirectoryActive* \[in\]
</dt> <dd>

Type: **uint32**

Flag disabling or enabling the Session Directory service.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Disable the Session Directory service.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Enable the Session Directory service.

</dd> </dl> </dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

