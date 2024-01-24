---
title: CheckStatus method of the Win32_TSGatewayConnection class
description: Checks the status of a Remote Desktop Gateway (RD Gateway) server connection to another computer, and determines whether the target computer is configured for load balancing.
ms.assetid: e8ee3d40-76eb-401f-b255-bccd7ba8c058
ms.tgt_platform: multiple
keywords:
- CheckStatus method Remote Desktop Services
- CheckStatus method Remote Desktop Services , Win32_TSGatewayConnection class
- Win32_TSGatewayConnection class Remote Desktop Services , CheckStatus method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnection.CheckStatus
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CheckStatus method of the Win32\_TSGatewayConnection class

Checks the status of a Remote Desktop Gateway (RD Gateway) server connection to another computer, and determines whether the target computer is configured for load balancing.

## Syntax


```mof
uint32 CheckStatus(
  [in] string ServerName,
  [in] string EndPointName
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

The name of the source RD Gateway server from which the connection is checked.

</dd> <dt>

*EndPointName* \[in\]
</dt> <dd>

The name of the target server (the endpoint) to which access is checked from the source server.

</dd> </dl>

## Return value

This method returns the following possible return values.

<dl> <dt>


</dt> <dd>

0

The connection status is OK. The endpoint is reachable and is configured for load balancing.

</dd> <dt>


</dt> <dd>

1

The connection status is unknown. Most likely, an exception occurred.

</dd> <dt>


</dt> <dd>

0x80075c34

The endpoint is either not reachable, or it is not configured for load balancing.

</dd> <dt>


</dt> <dd>

0x80075c32

A status error occurred. The endpoint is reachable, but the RPC/HTTP Load Balancing Service (RPCHTTPLBS) service is not started on the target computer.

</dd> </dl>

## Remarks

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

 

