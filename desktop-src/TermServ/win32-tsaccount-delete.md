---
title: Delete method of the Win32_TSAccount class
description: The Delete method deletes the specified user, group, or computer account.
ms.assetid: d0bb06d6-781c-4711-a59d-9ff233dd2a4c
ms.tgt_platform: multiple
keywords:
- Delete method Remote Desktop Services
- Delete method Remote Desktop Services , Win32_TSAccount class
- Win32_TSAccount class Remote Desktop Services , Delete method
topic_type:
- apiref
api_name:
- Win32_TSAccount.Delete
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Delete method of the Win32\_TSAccount class

The **Delete** method deletes the specified user, group, or computer account.

## Syntax


```mof
uint32 Delete();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSAccount**](win32-tsaccount.md)
</dt> </dl>

 

