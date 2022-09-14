---
title: SetUserGroupNames method of the Win32_TSGatewayResourceAuthorizationPolicy class
description: Sets the UserGroupNames property for the Remote Desktop resource authorization policy (RD \ 160;RAP).
ms.assetid: 91b77cd6-779e-460a-88a3-eda7a6fe99e5
ms.tgt_platform: multiple
keywords:
- SetUserGroupNames method Remote Desktop Services
- SetUserGroupNames method Remote Desktop Services , Win32_TSGatewayResourceAuthorizationPolicy class
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , SetUserGroupNames method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy.SetUserGroupNames
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetUserGroupNames method of the Win32\_TSGatewayResourceAuthorizationPolicy class

Sets the **UserGroupNames** property for the Remote Desktop resource authorization policy (RD RAP).

## Syntax


```mof
uint32 SetUserGroupNames(
  [in] string UserGroupNames
);
```



## Parameters

<dl> <dt>

*UserGroupNames* \[in\]
</dt> <dd>

Semicolon-separated list of user group names. The names are of the format *Domain\\UserGroupName*. If the user belongs to any of these user groups, access will be permitted.

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

 

