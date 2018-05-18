---
title: GetServerEventDetailEx method of the MSFT\_ServerManagerTasks class
description: Retrieves the details of events generated in an event log by a particular source.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5af8da79-fbfb-4057-827e-4eb72505ecf8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetServerEventDetailEx method", "GetServerEventDetailEx method, MSFT_ServerManagerTasks class", "MSFT_ServerManagerTasks class, GetServerEventDetailEx method"]
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerEventDetailEx
api_location:
- MgmtProvider.dll
api_type:
- COM
---

# GetServerEventDetailEx method of the MSFT\_ServerManagerTasks class

Retrieves the details of events generated in an event log by a particular source.

**Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.

## Syntax


```mof
uint32 GetServerEventDetailEx(
  [in]  string                 FilterXml,
  [in]  uint64                 Skip,
  [in]  uint64                 Top,
  [in]  boolean                ReverseDirection,
  [in]  uint32                 BatchSize,
  [out] MSFT_ServerEventDetail cmdletOutput[]
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

The number of events to return from query's result set after skipping the count of events specified by *Skip* parameter.

</dd> <dt>

*ReverseDirection* \[in\]
</dt> <dd>

The condition of query direction, reverse direction if set to **True**.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to use for streaming data back to the client.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded [**MSFT\_ServerEventDetail**](msft-servereventdetail.md) instances that represent the list of selected events that match the query.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerEventDetail**](msft-servereventdetail.md)
</dt> </dl>

 

 





