---
title: CreateStretchTopology method of the MSFT\_WvrAdminTasks class
description: Creates a replication partnership between two new or existing replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ad29f2be-b73d-4a80-b6ea-426d22086b62
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateStretchTopology method
- CreateStretchTopology method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, CreateStretchTopology method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateStretchTopology method of the MSFT\_WvrAdminTasks class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a replication partnership between two new or existing replication groups.

## Syntax


```mof
uint32 CreateStretchTopology(
  [in]  string                   ClusterName,
  [in]  string                   SourceRGName,
  [in]  string                   SourceRGDescription,
  [in]  string                   SourceVolumeName[],
  [in]  string                   SourceLogVolumeName,
  [in]  string                   DestinationRGName,
  [in]  string                   DestinationRGDescription,
  [in]  string                   DestinationVolumeName[],
  [in]  string                   DestinationLogVolumeName,
  [in]  uint64                   LogSizeInBytes,
  [in]  boolean                  PreventReplication,
  [in]  boolean                  Seeded,
  [out] MSFT_WvrReplicationGroup Output[]
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

*SourceRGDescription* \[in\]
</dt> <dd>

The description of the source replication group.

</dd> <dt>

*SourceVolumeName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*SourceLogVolumeName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*DestinationRGDescription* \[in\]
</dt> <dd>

The description of the destination replication group.

</dd> <dt>

*DestinationVolumeName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationLogVolumeName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*LogSizeInBytes* \[in\]
</dt> <dd>

The size of the log file in Bytes.

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

Returns the resulting [**MSFT\_WvrReplicationGroup**](msft-wvrreplicationgroup.md) embedded instance.

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

 

 





