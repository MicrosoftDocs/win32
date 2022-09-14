---
title: Update method of the Win32_TSGatewayRADIUSServer class
description: Updates the current Remote Authentication Dial-In User Service (RADIUS) server.
ms.assetid: 38a15768-66eb-40d6-a079-16555f2bf96a
ms.tgt_platform: multiple
keywords:
- Update method Remote Desktop Services
- Update method Remote Desktop Services , Win32_TSGatewayRADIUSServer class
- Win32_TSGatewayRADIUSServer class Remote Desktop Services , Update method
topic_type:
- apiref
api_name:
- Win32_TSGatewayRADIUSServer.Update
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Update method of the Win32\_TSGatewayRADIUSServer class

Updates the current Remote Authentication Dial-In User Service (RADIUS) server.

## Syntax


```mof
uint32 Update(
  [in] string Name,
  [in] string SharedSecret
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

RADIUS server name.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret for the RADIUS server.

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

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> </dl>

 

