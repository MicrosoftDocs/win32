---
title: RemoveStretchPartnership method of the MSFT\_WvrAdminTasks class
description: Removes an existing replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b71f6e88-2c31-40ba-a449-6f8950eee07c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveStretchPartnership method", "RemoveStretchPartnership method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, RemoveStretchPartnership method"]
---

# RemoveStretchPartnership method of the MSFT\_WvrAdminTasks class

Removes an existing replication partnership.

## Syntax


```mof
uint32 RemoveStretchPartnership(
  [in] string ClusterName,
  [in] string SourceRGName,
  [in] string DestinationRGName
);
```



## Parameters

<dl> <dt>

*ClusterName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





