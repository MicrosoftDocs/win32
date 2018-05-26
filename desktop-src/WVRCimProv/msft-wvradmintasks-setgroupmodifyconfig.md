---
title: SetGroupModifyConfig method of the MSFT\_WvrAdminTasks class
description: Modifies settings on an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17634cb5-8e41-496c-afe1-b80df6ff47ea
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetGroupModifyConfig method
- SetGroupModifyConfig method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetGroupModifyConfig method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SetGroupModifyConfig
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetGroupModifyConfig method of the MSFT\_WvrAdminTasks class

Modifies settings on an existing replication group.

## Syntax


```mof
uint32 SetGroupModifyConfig(
  [in] string  ComputerName,
  [in] string  Name,
  [in] string  Description,
  [in] uint64  LogSizeInBytes,
  [in] uint32  ReplicationMode,
  [in] boolean Encryption,
  [in] boolean AllowVolumeResize
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description of the replication group.

</dd> <dt>

*LogSizeInBytes* \[in\]
</dt> <dd>

Size of log in Bytes.

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

*Encryption* \[in\]
</dt> <dd>

Whether this replication group uses an encrypted channel for communication.

**true** if this replication group uses an encrypted channel for communication; otherwise, **false**.

</dd> <dt>

*AllowVolumeResize* \[in\]
</dt> <dd>

**true** if the replicas in this replication group are allowed to be resized; otherwise, **false**.

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

 

 





