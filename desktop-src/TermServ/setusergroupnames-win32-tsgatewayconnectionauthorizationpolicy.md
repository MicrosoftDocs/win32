---
title: SetUserGroupNames method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Sets the UserGroupNames property for this Remote Desktop connection authorization policy (RD \ 160;CAP).
ms.assetid: 03c9b2c5-8769-46f2-941f-302d798dd3a1
ms.tgt_platform: multiple
keywords:
- SetUserGroupNames method Remote Desktop Services
- SetUserGroupNames method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , SetUserGroupNames method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.SetUserGroupNames
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetUserGroupNames method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Sets the **UserGroupNames** property for this Remote Desktop connection authorization policy (RD CAP).

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

List of semicolon-separated user group names. The names are of the format *Domain\\UserGroupName*. If the user belongs to any of these user groups, the user will be permitted access to the RD Gateway server.

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

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> </dl>

 

