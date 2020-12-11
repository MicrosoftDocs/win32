---
title: RestoreDefaults method of the Win32_TSPermissionsSetting class (Netfw.h)
description: Restores the default permission set values for the terminal.
ms.assetid: bdd01290-7c7c-4355-85dc-ade51b2abd94
ms.tgt_platform: multiple
keywords:
- RestoreDefaults method Remote Desktop Services
- RestoreDefaults method Remote Desktop Services , Win32_TSPermissionsSetting class
- Win32_TSPermissionsSetting class Remote Desktop Services , RestoreDefaults method
topic_type:
- apiref
api_name:
- Win32_TSPermissionsSetting.RestoreDefaults
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RestoreDefaults method of the Win32\_TSPermissionsSetting class

The **RestoreDefaults** method restores the default permission set values for the terminal.

## Syntax


```mof
uint32 RestoreDefaults();
```



## Parameters

This method has no parameters.

## Return value

Returns Success on success, otherwise Failure.

## Remarks

Default permissions are the following:

-   The Administrators, System, and Remote Desktop Help Assistant accounts have all [Remote Desktop Services Permissions](terminal-services-permissions.md).
-   The Remote Desktop Users account has Logon, Connect, Query Information, and Send Message permission.
-   The Local Service and Network Service accounts have Query Information, and Send Message permission.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| Header<br/>                   | <dl> <dt>Netfw.h</dt> </dl>      |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSPermissionsSetting**](win32-tspermissionssetting.md)
</dt> </dl>

 

