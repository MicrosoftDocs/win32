---
title: SetSessionTimeout method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Sets the SessionTimeout and SessionTimeoutAction properties.
ms.assetid: 11491c97-3ef8-46c1-9504-696c613e374e
ms.tgt_platform: multiple
keywords:
- SetSessionTimeout method Remote Desktop Services
- SetSessionTimeout method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , SetSessionTimeout method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.SetSessionTimeout
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSessionTimeout method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Sets the **SessionTimeout** and **SessionTimeoutAction** properties.

## Syntax


```mof
uint32 SetSessionTimeout(
  [in] uint32 SessionTimeout,
  [in] uint32 SessionTimeoutAction
);
```



## Parameters

<dl> <dt>

*SessionTimeout* \[in\]
</dt> <dd>

Type: **uint32**

The new timeout value, in minutes. A value of 0 means there is no timeout.

</dd> <dt>

*SessionTimeoutAction* \[in\]
</dt> <dd>

Type: **uint32**

Specifies the action to be taken in case of a session timeout. This can be one of the following values.

<dt>

0
</dt> <dd>

Disconnect the session.

</dd> <dt>

1
</dt> <dd>

Attempt to re-authorize the session.

</dd> </dl> </dd> </dl>

## Return value

Type: **uint32**

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> </dl>

 

