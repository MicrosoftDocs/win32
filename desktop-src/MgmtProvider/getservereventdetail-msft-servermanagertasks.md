---
title: GetServerEventDetail method of the MSFT\_ServerManagerTasks class
description: Retrieves the details of events generated in an event log by a particular source.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13aecf45-9ea0-4583-9824-738d64fb9fb0
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetServerEventDetail method
- GetServerEventDetail method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetServerEventDetail method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerEventDetail
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetServerEventDetail method of the MSFT\_ServerManagerTasks class

Retrieves the details of events generated in an event log by a particular source.

## Syntax


```mof
uint32 GetServerEventDetail(
  [in]  string                 Logs[],
  [in]  uint8                  Levels[],
  [in]  uint64                 StartTimes[],
  [in]  uint64                 EndTimes[],
  [in]  uint32                 BatchSize,
  [in]  string                 QueryFiles[],
  [in]  sint32                 QueryFileIds[],
  [out] uint64                 LatestEventTimestamp,
  [out] MSFT_ServerEventDetail cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Logs* \[in\]
</dt> <dd>

The list of logs to query when collecting events.

</dd> <dt>

*Levels* \[in\]
</dt> <dd>

An array of bitmasks that specify the level of events to query. Valid values are 0 through 4.

</dd> <dt>

*StartTimes* \[in\]
</dt> <dd>

The list of start times used to filter the events based on the log time.

</dd> <dt>

*EndTimes* \[in\]
</dt> <dd>

The list of end times used to filter the events based on the logged time.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to use for streaming data back to the client.

</dd> <dt>

*QueryFiles* \[in\]
</dt> <dd>

The list of query files to use when for collecting feature events.

</dd> <dt>

*QueryFileIds* \[in\]
</dt> <dd>

The list of query file ids to return as the query file identifier in the event details object. If this is null or empty, the index of the file in the QueryFiles paramerter is returned. If present the number of elements should exactly match the number of elements in the QueryFiles parameter.

</dd> <dt>

*LatestEventTimestamp* \[out\]
</dt> <dd>

The log time of the latest event returned by the function.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded instances of the [**MSFT\_ServerEventDetail**](msft-servereventdetail.md) class that represent the list of selected events that match the specified criteria.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerEventDetail**](msft-servereventdetail.md)
</dt> </dl>

 

 





