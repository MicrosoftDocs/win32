---
title: GetEventRecords method of the MSFT\_MTEventChannel class
description: Retrieves the details of events generated in an event log by a particular source.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cc9cb29d-f781-4d8f-8037-3db889080f36
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetEventRecords method
- GetEventRecords method, MSFT_MTEventChannel class
- MSFT_MTEventChannel class, GetEventRecords method
topic_type:
- apiref
api_name:
- MSFT_MTEventChannel.GetEventRecords
api_location:
- MtTmProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetEventRecords method of the MSFT\_MTEventChannel class

Retrieves the details of events generated in an event log by a particular source.

## Syntax


```mof
uint32 GetEventRecords(
  [in]  string             FilterXml,
  [in]  uint64             Skip,
  [in]  uint64             Top,
  [in]  boolean            ReverseDirection,
  [in]  uint32             BatchSize,
  [out] MSFT_MTEventRecord Result[]
);
```



## Parameters

<dl> <dt>

*FilterXml* \[in\]
</dt> <dd>

The xml string of event filter query.

</dd> <dt>

*Skip* \[in\]
</dt> <dd>

The number of event records to skip from the query's result set.

</dd> <dt>

*Top* \[in\]
</dt> <dd>

The number of events to return from query's result set after skipping the count of events specified by Skip parameter.

</dd> <dt>

*ReverseDirection* \[in\]
</dt> <dd>

The condition of query direction, reverses direction if set to true.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to use for streaming data back to the client.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

Embedded [**MSFT\_MTEventRecord**](msft-mteventrecord.md) instances representing the events that match the query.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTEventChannel**](msft-mteventchannel.md)
</dt> </dl>

 

 





