---
title: SetCurrentRedirectableAddresses method of the Win32_TSSessionDirectory class
description: Sets the configured list of DNS eligible addresses that can be used for redirection.
ms.assetid: cad6a8a8-fdf1-406e-abeb-37acb396ac16
ms.tgt_platform: multiple
keywords:
- SetCurrentRedirectableAddresses method Remote Desktop Services
- SetCurrentRedirectableAddresses method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetCurrentRedirectableAddresses method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetCurrentRedirectableAddresses
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetCurrentRedirectableAddresses method of the Win32\_TSSessionDirectory class

The **SetCurrentRedirectableAddresses** method sets the configured list of DNS eligible addresses that can be used for redirection.

## Syntax


```mof
uint32 SetCurrentRedirectableAddresses(
  [in] uint32 fTokenRedirection,
  [in] string IPAddresses[]
);
```



## Parameters

<dl> <dt>

*fTokenRedirection* \[in\]
</dt> <dd>

Type: **uint32**

A flag that indicates whether token redirection should be used.

</dd> <dt>

*IPAddresses* \[in\]
</dt> <dd>

Type: **string\[\]**

An array of strings that represents the list of DNS eligible IP addresses that can be used for redirection.

</dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success; otherwise, returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

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

 

