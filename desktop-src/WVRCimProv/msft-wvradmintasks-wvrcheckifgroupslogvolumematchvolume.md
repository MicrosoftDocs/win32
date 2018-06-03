---
title: WvrCheckIfGroupsLogVolumeMatchVolume method of the MSFT\_WvrAdminTasks class
description: Perform a remote cim call to check whether given replication group log volume matches with the volume which is to be removed from a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 748ec363-370b-4cf3-a1f8-0d7d9b18d025
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrCheckIfGroupsLogVolumeMatchVolume method
- WvrCheckIfGroupsLogVolumeMatchVolume method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrCheckIfGroupsLogVolumeMatchVolume method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrCheckIfGroupsLogVolumeMatchVolume method of the MSFT\_WvrAdminTasks class

Perform a remote cim call to check whether given replication group log volume matches with the volume which is to be removed from a group

## Syntax


```mof
uint32 WvrCheckIfGroupsLogVolumeMatchVolume(
  [in] string ReplicationGroupName,
  [in] string VolumeName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*VolumeName* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





