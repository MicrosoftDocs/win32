---
title: GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatistics class
description: This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN historical connections for a specified time duration.
audience: developer
ms.assetid: f91eab49-e009-49b3-a3ac-69486b990ba7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAccountingStatistics method
- GetByAccountingStatistics method, PS_RemoteAccessConnectionStatistics class
- PS_RemoteAccessConnectionStatistics class, GetByAccountingStatistics method
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatistics.GetByAccountingStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatistics class

This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN historical connections for a specified time duration.

## Syntax


```mof
uint32 GetByAccountingStatistics(
  [in]  string                           ComputerName,
  [in]  datetime                         StartDateTime,
  [in]  datetime                         EndDateTime,
  [out] RemoteAccessAccountingConnection cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When a ComputerName is specified the statistics on that Remote Access server are retrieved

</dd> <dt>

*StartDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the statistics of historical connections is to be retrieved and indicates the start date. If a date is not specified then the time stamp of the first record in the accounting database is used by default

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the statistics of historical connections is to be retrieved and indicates the end date. If a date is not specified then the time stamp of the last record in the accounting database is used by default

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

 

 





