---
title: SetSharedSecret method of the Win32_TSGatewayRADIUSServer class
description: Sets the SharedSecret property for this Remote Authentication Dial-In User Service (RADIUS) server.
ms.assetid: b4f7afb7-862f-4c30-b60a-aa6a8dbbe3e9
ms.tgt_platform: multiple
keywords:
- SetSharedSecret method Remote Desktop Services
- SetSharedSecret method Remote Desktop Services , Win32_TSGatewayRADIUSServer class
- Win32_TSGatewayRADIUSServer class Remote Desktop Services , SetSharedSecret method
topic_type:
- apiref
api_name:
- Win32_TSGatewayRADIUSServer.SetSharedSecret
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSharedSecret method of the Win32\_TSGatewayRADIUSServer class

Sets the **SharedSecret** property for this Remote Authentication Dial-In User Service (RADIUS) server.

## Syntax


```mof
uint32 SetSharedSecret(
  [in] string SharedSecret
);
```



## Parameters

<dl> <dt>

*SharedSecret* \[in\]
</dt> <dd>

New shared secret.

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

 

