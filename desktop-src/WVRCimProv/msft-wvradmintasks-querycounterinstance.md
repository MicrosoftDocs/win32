---
title: QueryCounterInstance method of the MSFT\_WvrAdminTasks class
description: Queries partition related performance counter information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1fbaeb93-a934-43d5-8870-b66608b6ff8f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["QueryCounterInstance method", "QueryCounterInstance method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, QueryCounterInstance method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.QueryCounterInstance
api_location:
- wvrcimprov.dll
api_type:
- COM
---

# QueryCounterInstance method of the MSFT\_WvrAdminTasks class

Queries partition related performance counter information.

## Syntax


```mof
uint32 QueryCounterInstance(
  [in]  string PartitionId,
  [out] string DataPartitionCounter,
  [out] string LogPartitionCounter,
  [out] string NetworkCounter
);
```



## Parameters

<dl> <dt>

*PartitionId* \[in\]
</dt> <dd>

The partition ID.

</dd> <dt>

*DataPartitionCounter* \[out\]
</dt> <dd>

On success, returns the data partition counter.

</dd> <dt>

*LogPartitionCounter* \[out\]
</dt> <dd>

On success, returns the log partition counter.

</dd> <dt>

*NetworkCounter* \[out\]
</dt> <dd>

On success, returns the network counter.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





