---
title: AddAccount method of the Win32_TSPermissionsSetting class (Faxcomex.h)
description: The AddAccount method prepares to add an account to the terminal with the specified permission set. You can add users, groups, or computers.
ms.assetid: da4d8f5b-7aa2-4b55-bf0f-b3e98b70a06b
ms.tgt_platform: multiple
keywords:
- AddAccount method Remote Desktop Services
- AddAccount method Remote Desktop Services , Win32_TSPermissionsSetting class
- Win32_TSPermissionsSetting class Remote Desktop Services , AddAccount method
topic_type:
- apiref
api_name:
- Win32_TSPermissionsSetting.AddAccount
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AddAccount method of the Win32\_TSPermissionsSetting class

The **AddAccount** method prepares to add an account to the terminal with the specified permission set. You can add users, groups, or computers.

## Syntax


```mof
uint32 AddAccount(
  [in] string AccountName,
  [in] uint32 PermissionPreSet
);
```



## Parameters

<dl> <dt>

*AccountName* \[in\]
</dt> <dd>

The name of the account to add to the terminal.

</dd> <dt>

*PermissionPreSet* \[in\]
</dt> <dd>

The set of permissions to associate with the specified account. This parameter can be any or all of the following values. For more information, see [Remote Desktop Services Permissions](terminal-services-permissions.md).

<dt>

<span id="WINSTATION_GUEST_ACCESS"></span><span id="winstation_guest_access"></span>

<span id="WINSTATION_GUEST_ACCESS"></span><span id="winstation_guest_access"></span>**WINSTATION\_GUEST\_ACCESS** (0)


</dt> <dd>

The account has Logon permission.

</dd> <dt>

<span id="WINSTATION_USER_ACCESS"></span><span id="winstation_user_access"></span>

<span id="WINSTATION_USER_ACCESS"></span><span id="winstation_user_access"></span>**WINSTATION\_USER\_ACCESS** (1)


</dt> <dd>

The account has the following permissions: Logon, Query Information, Send Message, and Connect.

</dd> <dt>

<span id="WINSTATION_ALL_ACCESS"></span><span id="winstation_all_access"></span>

<span id="WINSTATION_ALL_ACCESS"></span><span id="winstation_all_access"></span>**WINSTATION\_ALL\_ACCESS** (2)


</dt> <dd>

The account has all Remote Desktop Services Permissions.

</dd> </dl> </dd> </dl>

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
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSPermissionsSetting**](win32-tspermissionssetting.md)
</dt> </dl>

 

