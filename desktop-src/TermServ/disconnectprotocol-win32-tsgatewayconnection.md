---
title: DisconnectProtocol method of the Win32_TSGatewayConnection class
description: Disconnects all connections of the specified protocol from the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 0ca3f478-dfdc-404e-ac17-43b6873b7256
ms.tgt_platform: multiple
keywords:
- DisconnectProtocol method Remote Desktop Services
- DisconnectProtocol method Remote Desktop Services , Win32_TSGatewayConnection class
- Win32_TSGatewayConnection class Remote Desktop Services , DisconnectProtocol method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnection.DisconnectProtocol
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DisconnectProtocol method of the Win32\_TSGatewayConnection class

Disconnects all connections of the specified protocol from the Remote Desktop Gateway (RD Gateway) server.

## Syntax


```mof
uint32 DisconnectProtocol(
  [in] string ProtocolName
);
```



## Parameters

<dl> <dt>

*ProtocolName* \[in\]
</dt> <dd>

The protocol name for a specific connection. This can be retrieved from the **ProtocolName** property of the **Win32\_TSGatewayConnection** class.

<dt>

"TS"
</dt> <dd>

The protocol for the RD Gateway server.

</dd> </dl> </dd> </dl>

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

[**Win32\_TSGatewayConnection**](win32-tsgatewayconnection.md)
</dt> </dl>

 

