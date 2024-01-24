---
title: GetRedirectableAddresses method of the Win32_TSSessionDirectory class
description: Obtains the entire list of DNS eligible addresses.
ms.assetid: 828079e7-472c-4428-97a0-2d5dedcdae91
ms.tgt_platform: multiple
keywords:
- GetRedirectableAddresses method Remote Desktop Services
- GetRedirectableAddresses method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , GetRedirectableAddresses method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.GetRedirectableAddresses
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetRedirectableAddresses method of the Win32\_TSSessionDirectory class

Obtains the entire list of DNS eligible addresses.

## Syntax


```mof
uint32 GetRedirectableAddresses(
  [in]  uint32 fTokenRedirection,
  [out] string IPAddresses[],
  [out] string AdapterNames[],
  [out] string NetConName[]
);
```



## Parameters

<dl> <dt>

*fTokenRedirection* \[in\]
</dt> <dd>

Type: **uint32**

A flag that indicates whether token redirection should be used.

</dd> <dt>

*IPAddresses* \[out\]
</dt> <dd>

Type: **string\[\]**

The entire list of IP addresses that are available for redirection.

</dd> <dt>

*AdapterNames* \[out\]
</dt> <dd>

Type: **string\[\]**

The list of network adapter names that are associated with the addresses that are available for redirection.

</dd> <dt>

*NetConName* \[out\]
</dt> <dd>

Type: **string\[\]**

The list of network connection names that are associated with the addresses that are available for redirection.

</dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

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

 

