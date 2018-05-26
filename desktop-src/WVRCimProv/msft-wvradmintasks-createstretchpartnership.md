---
title: CreateStretchPartnership method of the MSFT\_WvrAdminTasks class
description: Creates a replication partnership between two existing replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44d0ce55-36bf-4551-95fc-7a57794bfcbe
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateStretchPartnership method
- CreateStretchPartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, CreateStretchPartnership method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateStretchPartnership method of the MSFT\_WvrAdminTasks class

Creates a replication partnership between two existing replication groups.

## Syntax


```mof
uint32 CreateStretchPartnership(
  [in]  string                         ClusterName,
  [in]  string                         SourceRGName,
  [in]  string                         DestinationRGName,
  [in]  boolean                        PreventReplication,
  [in]  boolean                        Seeded,
  [out] MSFT_WvrReplicationPartnership Output[]
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

</dd> <dt>

*PreventReplication* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Seeded* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the resulting [**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md) embedded instance.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





