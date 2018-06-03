---
title: GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatistics class
description: This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN historical connections for a specified time duration.
audience: developer
ms.assetid: 91db914f-aa69-4f36-b7e3-27a5e465b941
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByActiveStatistics method
- GetByActiveStatistics method, PS_RemoteAccessConnectionStatistics class
- PS_RemoteAccessConnectionStatistics class, GetByActiveStatistics method
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatistics.GetByActiveStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatistics class

This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN historical connections for a specified time duration.

## Syntax


```mof
uint32 GetByActiveStatistics(
  [in]  string                           ComputerName,
  [in]  string                           ResourceName,
  [in]  string                           RoutingDomain,
  [out] RemoteAccessMonitoringConnection cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When a ComputerName is specified the statistics on that Remote Access server are retrieved

</dd> <dt>

*ResourceName* \[in\]
</dt> <dd>

This parameter enables a user to filter the statistics of active connections based on the server (resource) that the end-user is accessing. It indicates the IP address or hostname of the server (resource) that a user is accessing

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

**Windows Server 2012:** This parameter is unavailable prior to Windows Server 2012 R2.

The name of the routing domain for which to retrieve statistics.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Based on the input specified, the current (real-time) connection statistics or accounting statistics for the specified time duration

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConnectionStatistics**](ps-remoteaccessconnectionstatistics.md)
</dt> </dl>

 

 





