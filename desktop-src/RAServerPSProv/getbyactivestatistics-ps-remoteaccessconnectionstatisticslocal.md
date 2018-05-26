---
title: GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatisticsLocal class
description: This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data.
audience: developer
ms.assetid: e07fb91c-e27a-451f-a075-26d22b7722c7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByActiveStatistics method
- GetByActiveStatistics method, PS_RemoteAccessConnectionStatisticsLocal class
- PS_RemoteAccessConnectionStatisticsLocal class, GetByActiveStatistics method
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsLocal.GetByActiveStatistics
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByActiveStatistics method of the PS\_RemoteAccessConnectionStatisticsLocal class

This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data.

## Syntax


```mof
uint32 GetByActiveStatistics(
  [in]  string                                ResourceName,
  [out] RemoteAccessMonitoringConnectionLocal cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ResourceName* \[in\]
</dt> <dd>

Resource name to filter by.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains an array of [**RemoteAccessMonitoringConnectionLocal**](remoteaccessmonitoringconnectionlocal.md) objects that describe the Remote Access connection objects from Monitoring data.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConnectionStatisticsLocal**](ps-remoteaccessconnectionstatisticslocal.md)
</dt> </dl>

 

 





