---
title: RemoveUserGroupNames method of the Win32_TSGatewayResourceAuthorizationPolicy class
description: Removes the specified user group names from the existing user groups in the UserGroupNames property.
ms.assetid: 8538e41a-b9ae-43ce-b19a-40a40f9a12f5
ms.tgt_platform: multiple
keywords:
- RemoveUserGroupNames method Remote Desktop Services
- RemoveUserGroupNames method Remote Desktop Services , Win32_TSGatewayResourceAuthorizationPolicy class
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , RemoveUserGroupNames method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy.RemoveUserGroupNames
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveUserGroupNames method of the Win32\_TSGatewayResourceAuthorizationPolicy class

Removes the specified user group names from the existing user groups in the **UserGroupNames** property.

## Syntax


```mof
uint32 RemoveUserGroupNames(
  [in] string UserGroupNames
);
```



## Parameters

<dl> <dt>

*UserGroupNames* \[in\]
</dt> <dd>

Semicolon-separated list of user group names.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

If multiple user group names are in the *UserGroupNames* parameter and one of the names cannot be processed, none of the names will be processed.

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> </dl>

 

