---
title: CreatePartnership method of the MSFT\_WvrAdminTasks class
description: Creates a replication partnership between two existing replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '12ec1356-6bc8-4918-9ea3-a071e3e0f908'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreatePartnership method", "CreatePartnership method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, CreatePartnership method"]
---

# CreatePartnership method of the MSFT\_WvrAdminTasks class

Creates a replication partnership between two existing replication groups.

## Syntax


```mof
uint32 CreatePartnership(
  [in]  string                         SourceComputerName,
  [in]  string                         SourceRGName,
  [in]  string                         DestinationComputerName,
  [in]  string                         DestinationRGName,
  [in]  uint32                         ReplicationMode,
  [in]  boolean                        PreventReplication,
  [in]  boolean                        Seeded,
  [in]  uint32                         AsyncRPO,
  [in]  boolean                        EnableEncryption,
  [out] MSFT_WvrReplicationPartnership Output[]
);
```



## Parameters

<dl> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the source computer.

</dd> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*ReplicationMode* \[in\]
</dt> <dd>

Whether the replication is performed synchronously or asynchronously.

The possible values are.

<dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (1)


</dt> <dd></dd> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*PreventReplication* \[in\]
</dt> <dd>

**true** to prevent replication.

</dd> <dt>

*Seeded* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AsyncRPO* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*EnableEncryption* \[in\]
</dt> <dd>

**true** to enable encryption; otherwise, **false**.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the resulting [**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md) embedded instance.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| Header<br/>                   | <dl> <dt>Wmp.h</dt> </dl>          |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





