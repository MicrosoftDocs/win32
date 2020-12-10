---
title: SetPasswordAllowed method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Sets the PasswordAllowed property, which enables or disables support for using a password to connect to the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 2d2dfc45-ac2c-41dc-b2c1-4c8eab42c442
ms.tgt_platform: multiple
keywords:
- SetPasswordAllowed method Remote Desktop Services
- SetPasswordAllowed method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , SetPasswordAllowed method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.SetPasswordAllowed
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetPasswordAllowed method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Sets the **PasswordAllowed** property, which enables or disables support for using a password to connect to the Remote Desktop Gateway (RD Gateway) server.

## Syntax


```mof
uint32 SetPasswordAllowed(
  [in] boolean Allowed
);
```



## Parameters

<dl> <dt>

*Allowed* \[in\]
</dt> <dd>

New **PasswordAllowed** value.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

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

 

