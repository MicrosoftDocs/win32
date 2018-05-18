---
title: NewSrGroup method of the MSFT\_WvrAdminTasks class
description: Creates a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7d493024-964f-4e64-8bb3-9585c0f698c6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewSrGroup method", "NewSrGroup method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, NewSrGroup method"]
---

# NewSrGroup method of the MSFT\_WvrAdminTasks class

Creates a replication group.

## Syntax


```mof
uint32 NewSrGroup(
  [in]  string                   ComputerName,
  [in]  string                   Description,
  [in]  uint64                   LogSizeInBytes,
  [in]  string                   LogVolumeName,
  [in]  string                   Name,
  [in]  string                   VolumeName[],
  [in]  boolean                  EnableConsistencyGroups,
  [in]  boolean                  EnableEncryption,
  [in]  uint32                   MinimumPartnersInSync,
  [out] MSFT_WvrReplicationGroup Output[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer on which to create the replication group.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A textual description of the new group.

</dd> <dt>

*LogSizeInBytes* \[in\]
</dt> <dd>

The size of the log file in Bytes.

</dd> <dt>

*LogVolumeName* \[in\]
</dt> <dd>

Full path of the log container.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The friendly name of the group.

</dd> <dt>

*VolumeName* \[in\]
</dt> <dd>

A collection of volume names.

</dd> <dt>

*EnableConsistencyGroups* \[in\]
</dt> <dd>

Set **true** to enable consistency groups.

</dd> <dt>

*EnableEncryption* \[in\]
</dt> <dd>

**true** to enable encryption; otherwise, **false**.

</dd> <dt>

*MinimumPartnersInSync* \[in\]
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





