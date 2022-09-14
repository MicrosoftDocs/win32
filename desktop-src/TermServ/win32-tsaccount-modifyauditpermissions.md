---
title: ModifyAuditPermissions method of the Win32_TSAccount class
description: Prepares to set a more granular set of audit permissions to the specified account.
ms.assetid: 7df44a37-257d-49c6-8193-f1e1c5ebbb57
ms.tgt_platform: multiple
keywords:
- ModifyAuditPermissions method Remote Desktop Services
- ModifyAuditPermissions method Remote Desktop Services , Win32_TSAccount class
- Win32_TSAccount class Remote Desktop Services , ModifyAuditPermissions method
topic_type:
- apiref
api_name:
- Win32_TSAccount.ModifyAuditPermissions
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ModifyAuditPermissions method of the Win32\_TSAccount class

The **ModifyAuditPermissions** method prepares to set a more granular set of audit permissions to the specified account.

## Syntax


```mof
uint32 ModifyAuditPermissions(
  [in] uint32  PermissionMask,
  [in] boolean Success
);
```



## Parameters

<dl> <dt>

*PermissionMask* \[in\]
</dt> <dd>

The set of [Remote Desktop Session Host Permissions](terminal-services-permissions.md) to associate with the specified account. The value of this parameter is a bitmap, and any or all of the following values may be selected.

<dt>

<span id="WINSTATION_QUERY"></span><span id="winstation_query"></span>

<span id="WINSTATION_QUERY"></span><span id="winstation_query"></span>**WINSTATION\_QUERY** (0)


</dt> <dd>

Permission to query information about a session.

</dd> <dt>

<span id="WINSTATION_SET"></span><span id="winstation_set"></span>

<span id="WINSTATION_SET"></span><span id="winstation_set"></span>**WINSTATION\_SET** (1)


</dt> <dd>

Permission to modify connection parameters.

</dd> <dt>

<span id="WINSTATION_RESET"></span><span id="winstation_reset"></span>

<span id="WINSTATION_RESET"></span><span id="winstation_reset"></span>**WINSTATION\_RESET** (6)


</dt> <dd>

Permission to reset or end a session or connection.

</dd> <dt>

<span id="WINSTATION_VIRTUAL___STANDARD_RIGHTS_REQUIRED"></span><span id="winstation_virtual___standard_rights_required"></span>

<span id="WINSTATION_VIRTUAL___STANDARD_RIGHTS_REQUIRED"></span><span id="winstation_virtual___standard_rights_required"></span>**WINSTATION\_VIRTUAL \| STANDARD\_RIGHTS\_REQUIRED** (3)


</dt> <dd>

Permission to use virtual channels. Virtual channels provide access from a server program to client devices.

</dd> <dt>

<span id="WINSTATION_SHADOW"></span><span id="winstation_shadow"></span>

<span id="WINSTATION_SHADOW"></span><span id="winstation_shadow"></span>**WINSTATION\_SHADOW** (4)


</dt> <dd>

Permission to shadow or remotely control another user's session.

</dd> <dt>

<span id="WINSTATION_LOGON"></span><span id="winstation_logon"></span>

<span id="WINSTATION_LOGON"></span><span id="winstation_logon"></span>**WINSTATION\_LOGON** (5)


</dt> <dd>

Permission to log on to a session on the server.

</dd> <dt>

<span id="WINSTATION_LOGOFF"></span><span id="winstation_logoff"></span>

<span id="WINSTATION_LOGOFF"></span><span id="winstation_logoff"></span>**WINSTATION\_LOGOFF** (2)


</dt> <dd>

Permission to log off a user from a session.

</dd> <dt>

<span id="WINSTATION_MSG"></span><span id="winstation_msg"></span>

<span id="WINSTATION_MSG"></span><span id="winstation_msg"></span>**WINSTATION\_MSG** (7)


</dt> <dd>

Permission to send a message to another user's session.

</dd> <dt>

<span id="WINSTATION_CONNECT"></span><span id="winstation_connect"></span>

<span id="WINSTATION_CONNECT"></span><span id="winstation_connect"></span>**WINSTATION\_CONNECT** (8)


</dt> <dd>

Permission to connect to another session.

</dd> <dt>

<span id="WINSTATION_DISCONNECT"></span><span id="winstation_disconnect"></span>

<span id="WINSTATION_DISCONNECT"></span><span id="winstation_disconnect"></span>**WINSTATION\_DISCONNECT** (9)


</dt> <dd>

Permission to disconnect a session.

</dd> </dl> </dd> <dt>

*Success* \[in\]
</dt> <dd>

Specifies if the permission set specified by the value of the *PermissionMask* parameter is allowed or denied.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

The specified permission set is allowed.

</dd> <dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

The specified permission set is denied.

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
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSAccount**](win32-tsaccount.md)
</dt> </dl>

 

