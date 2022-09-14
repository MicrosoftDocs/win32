---
title: DisconnectUser method of the Win32_TSGatewayConnection class (Tsgauthenticationengine.h)
description: Disconnects all connections of the specified user from the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 3c5d66b6-c1f0-4a91-bf93-be886d8e2391
ms.tgt_platform: multiple
keywords:
- DisconnectUser method Remote Desktop Services
- DisconnectUser method Remote Desktop Services , Win32_TSGatewayConnection class
- Win32_TSGatewayConnection class Remote Desktop Services , DisconnectUser method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnection.DisconnectUser
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DisconnectUser method of the Win32\_TSGatewayConnection class

Disconnects all connections of the specified user from the Remote Desktop Gateway (RD Gateway) server.

## Syntax


```mof
uint32 DisconnectUser(
  [in] string UserName
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The user name, in *Domain***\\***UserName* format, whose connections are to be disconnected.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                             |
| Header<br/>                   | <dl> <dt>Tsgauthenticationengine.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl>             |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnection**](win32-tsgatewayconnection.md)
</dt> </dl>

 

