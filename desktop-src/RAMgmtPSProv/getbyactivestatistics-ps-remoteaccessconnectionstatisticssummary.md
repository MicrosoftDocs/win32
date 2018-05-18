---
title: GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatisticsSummary class
description: This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration.
audience: developer
ms.assetid: '08d29c0d-4bae-4a08-a3a0-e63b196ab1db'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByActiveStatistics method", "GetByActiveStatistics method, PS_RemoteAccessConnectionStatisticsSummary class", "PS_RemoteAccessConnectionStatisticsSummary class, GetByActiveStatistics method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsSummary.GetByActiveStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatisticsSummary class

This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration.

## Syntax


```mof
uint32 GetByActiveStatistics(
  [in]  string                        ComputerName,
  [out] RemoteAccessMonitoringSummary cmdletOutput
);
```



## Parameters

<dl> <dt>

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConnectionStatisticsSummary**](ps-remoteaccessconnectionstatisticssummary.md)
</dt> </dl>

 

 





