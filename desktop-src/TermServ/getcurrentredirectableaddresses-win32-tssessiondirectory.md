---
title: GetCurrentRedirectableAddresses method of the Win32_TSSessionDirectory class
description: Obtains the currently configured list of DNS eligible addresses that can be used for redirection.
ms.assetid: 79f35d8f-b5f9-4b0f-bb7d-0d1ee3f02346
ms.tgt_platform: multiple
keywords:
- GetCurrentRedirectableAddresses method Remote Desktop Services
- GetCurrentRedirectableAddresses method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , GetCurrentRedirectableAddresses method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.GetCurrentRedirectableAddresses
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetCurrentRedirectableAddresses method of the Win32\_TSSessionDirectory class

Obtains the currently configured list of DNS eligible addresses that can be used for redirection.

## Syntax


```mof
uint32 GetCurrentRedirectableAddresses(
  [out] uint32 fTokenRedirection,
  [out] string IPAddresses[]
);
```



## Parameters

<dl> <dt>

*fTokenRedirection* \[out\]
</dt> <dd>

Type: **uint32**

A flag that indicates whether token redirection should be used.

</dd> <dt>

*IPAddresses* \[out\]
</dt> <dd>

Type: **string\[\]**

An array of the currently configured DNS eligible IP addresses that can be used for redirection.

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

 

