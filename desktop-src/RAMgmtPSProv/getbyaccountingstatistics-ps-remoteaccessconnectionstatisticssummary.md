---
title: GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatisticsSummary class
description: This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration.
audience: developer
ms.assetid: aa6ff523-7951-4b02-a9f5-eadd872c7289
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAccountingStatistics method
- GetByAccountingStatistics method, PS_RemoteAccessConnectionStatisticsSummary class
- PS_RemoteAccessConnectionStatisticsSummary class, GetByAccountingStatistics method
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsSummary.GetByAccountingStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatisticsSummary class

This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration.

## Syntax


```mof
uint32 GetByAccountingStatistics(
  [in]  datetime                      StartDateTime,
  [in]  datetime                      EndDateTime,
  [in]  string                        ComputerName,
  [out] RemoteAccessAccountingSummary cmdletOutput
);
```



## Parameters

<dl> <dt>

*StartDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the statistics summary of historical connections is to be retrieved and indicates the start date. If a date is not specified then the time stamp of the first record in the accounting database is used by default

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the statistics summary of historical connections is to be retrieved and indicates the end date. If a date is not specified then the time stamp of the last record in the accounting database is used by default

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When a ComputerName is specified the statistics summary on that Remote Access server is retrieved

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Based on the input specified this cmdlet displays the summary of the current (real-time) connection statistics or summary of the accounting statistics for the specified time duration

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

[**PS\_RemoteAccessConnectionStatisticsSummary**](ps-remoteaccessconnectionstatisticssummary.md)
</dt> </dl>

 

 





